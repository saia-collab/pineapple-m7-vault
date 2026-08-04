import { NextResponse } from "next/server";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// POST /api/omniroute/chat  { messages: [{role,content}], model? }
// Proxies to the local OmniRoute gateway (OpenAI-compatible) using FREE models,
// with fallback: free providers are rate-limited, so we try a chain and return
// the first that answers. No API key needed for the free providers.

// Two free-coder backends, one section. OmniRoute ships anonymous free models;
// 9Router (573 models) routes the subscriptions/free tiers you connect once in
// its dashboard (http://127.0.0.1:20129).
const BASES: Record<string, string> = {
  omniroute: "http://localhost:20128/v1",
  ninerouter: "http://127.0.0.1:20129/v1",
};

// Ordered free-model fallback chain. big-pickle is the proven worker; the free
// providers here are all *reasoning* models, so we (a) steer them to answer
// immediately (see STEER below) and (b) give a big token budget — otherwise they
// loop on hidden reasoning and return empty. All verified live on this gateway.
const CHAINS: Record<string, string[]> = {
  omniroute: [
    "opencode-zen/big-pickle",
    "oc/big-pickle",
    "auto/coding:free",
    "auto/best-free",
    "auto/cheap",
  ],
  // Post-connect defaults: your own Claude Code / Codex OAuth via 9Router, then
  // its free-tier providers. Errors surface per-model with a connect hint.
  ninerouter: [
    "cc/claude-fable-5",
    "cx/gpt-5.6-sol",
    "gh/goldeneye-free-auto",
    "kgw/nvidia/nemotron-3-ultra-550b-a55b:free",
    "bzl/auto:free",
  ],
};

// Without this, the free reasoning models deliberate until they exhaust the
// whole max_tokens budget and never emit content (finish:"length", 0 chars).
// This steer cuts reasoning from ~4000 tokens to ~100 and yields finish:"stop".
const STEER = "You are a fast, senior coding assistant. Do NOT overthink or deliberate at length. Answer immediately and concisely. When asked for code, output it right away in a single fenced code block, complete and self-contained. Keep any reasoning to an absolute minimum.";

async function tryModel(base: string, model: string, messages: { role: string; content: string }[], signal: AbortSignal) {
  const withSteer = messages[0]?.role === "system" ? messages : [{ role: "system", content: STEER }, ...messages];
  const r = await fetch(`${base}/chat/completions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ model, messages: withSteer, stream: false, max_tokens: 8000 }),
    signal,
  });
  const j = await r.json().catch(() => null);
  if (!j || j.error) return { ok: false as const, error: j?.error?.message || `HTTP ${r.status}` };
  const content = j?.choices?.[0]?.message?.content;
  if (typeof content !== "string" || !content.trim()) return { ok: false as const, error: "empty response" };
  return { ok: true as const, content, model: j.model || model, usage: j.usage };
}

export async function POST(req: Request) {
  const body = await req.json().catch(() => ({}));
  const messages = Array.isArray(body.messages) ? body.messages : null;
  if (!messages || !messages.length) return NextResponse.json({ error: "messages required" }, { status: 400 });

  const backend = body.backend === "ninerouter" ? "ninerouter" : "omniroute";
  const base = BASES[backend];
  const FREE_CHAIN = CHAINS[backend];
  // If the caller pins a model, try only that; else walk the backend's chain.
  const chain = typeof body.model === "string" && body.model.trim() ? [body.model.trim(), ...FREE_CHAIN] : FREE_CHAIN;

  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), 90_000);
  const tried: { model: string; error: string }[] = [];
  try {
    for (const model of chain) {
      try {
        const res = await tryModel(base, model, messages, ctrl.signal);
        if (res.ok) {
          clearTimeout(t);
          return NextResponse.json({ ok: true, content: res.content, model: res.model, usage: res.usage, triedCount: tried.length });
        }
        tried.push({ model, error: res.error });
      } catch (e) {
        tried.push({ model, error: String((e as Error).message).slice(0, 120) });
      }
    }
  } finally {
    clearTimeout(t);
  }
  return NextResponse.json(
    { error: backend === "ninerouter"
        ? "9Router answered but no provider is connected yet — open its dashboard (button above) and connect Claude Code, Codex or a free tier once."
        : "All free providers are busy right now — try again in a moment.", tried },
    { status: 503 },
  );
}
