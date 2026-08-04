// 9Router integration — the second free-router backend for Free Claude Code,
// alongside OmniRoute (src/lib/omniroute.ts).
//
// 9Router (npm `9router`, 9router.com) is a free AI router + RTK token saver:
//   • RTK compresses tool_result payloads → 20-40% fewer tokens
//   • auto-fallback: your subscription → cheap → free, so you never stall
//   • multi-account round-robin per provider
//   • speaks BOTH protocols: /v1/messages (Anthropic) and /v1/chat/completions
//
// It runs on :20129 (NOT its default 20128 — OmniRoute owns that port):
//   9router -p 20129 -H 127.0.0.1 -n --skip-update
//
// IMPORTANT: unlike OmniRoute's keyless free pool, 9Router routes through
// accounts YOU connect in its dashboard. With zero providerConnections it lists
// a model catalogue but cannot serve a request — hence `providerCount` below, so
// the UI can tell the user to connect one instead of failing cryptically.

import { readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";

export const ROUTER9_BASE = process.env.ROUTER9_BASE_URL || "http://127.0.0.1:20129";
// Default = a model whose provider is actually CONNECTED (E2E-verified 2026-07-30:
// `claude -p` → :20129 → gemini provider → answered). 9Router infers the provider
// from the model name (/^gemini-/ → gemini), so this routes without a combo.
export const ROUTER9_MODEL = process.env.ROUTER9_MODEL || "gemini-3.6-flash";
// 9Router is keyless on localhost, but the Claude CLI demands *a* token.
export const ROUTER9_KEY = process.env.ROUTER9_API_KEY || "free-local";
export const ROUTER9_DASHBOARD = ROUTER9_BASE;

const MODEL_RE = /^[A-Za-z0-9._:/-]+$/;
function safeModel(model?: string | null): string {
  return model && MODEL_RE.test(model) ? model : ROUTER9_MODEL;
}

/** Env that points the `claude` CLI at 9Router instead of Anthropic.
 *  ANTHROPIC_API_KEY must be set or the CLI's saved OAuth wins and we 401. */
export function router9ClaudeEnv(model?: string | null): Record<string, string> {
  const m = safeModel(model);
  return {
    ANTHROPIC_BASE_URL: ROUTER9_BASE,
    ANTHROPIC_AUTH_TOKEN: ROUTER9_KEY,
    ANTHROPIC_API_KEY: ROUTER9_KEY,
    ANTHROPIC_MODEL: m,
    ANTHROPIC_SMALL_FAST_MODEL: m,
    ANTHROPIC_DEFAULT_OPUS_MODEL: m,
    ANTHROPIC_DEFAULT_SONNET_MODEL: m,
    ANTHROPIC_DEFAULT_HAIKU_MODEL: m,
    CLAUDE_CODE_SUBAGENT_MODEL: m,
  };
}

/** Is the gateway up? (/v1/models answers unauthenticated on localhost.) */
export async function probeRouter9(): Promise<boolean> {
  try {
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), 4000);
    const r = await fetch(`${ROUTER9_BASE}/v1/models`, { signal: ctrl.signal, cache: "no-store" });
    clearTimeout(t);
    return r.ok;
  } catch { return false; }
}

/** How many providers are actually connected. 0 ⇒ gateway is up but can't route,
 *  so the UI should say "connect a provider in the 9Router dashboard".
 *  Read straight from 9Router's sqlite (its /api/* is JWT-gated). */
export async function router9ProviderCount(): Promise<number | null> {
  const db = path.join(os.homedir(), ".9router", "db", "data.sqlite");
  try {
    // Avoid a sqlite dependency: count rows via the CLI that ships with macOS.
    const { execFile } = await import("node:child_process");
    return await new Promise<number | null>((resolve) => {
      execFile("sqlite3", [db, "select count(*) from providerConnections;"], { timeout: 4000 },
        (err, stdout) => {
          if (err) return resolve(null);
          const n = parseInt(String(stdout).trim(), 10);
          resolve(Number.isFinite(n) ? n : null);
        });
    });
  } catch { return null; }
}

/** Model catalogue 9Router exposes (for the picker). */
export async function router9Models(limit = 60): Promise<string[]> {
  try {
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), 5000);
    const r = await fetch(`${ROUTER9_BASE}/v1/models`, { signal: ctrl.signal, cache: "no-store" });
    clearTimeout(t);
    if (!r.ok) return [];
    const j = await r.json() as { data?: Array<{ id?: string }> };
    return (j.data ?? []).map((m) => m.id).filter((x): x is string => !!x).slice(0, limit);
  } catch { return []; }
}

/** Same steer OmniRoute needs: free reasoning models deliberate forever
 *  unless told to act immediately. */
export const ROUTER9_STEER =
  "Answer immediately and act. Do NOT overthink or deliberate at length. When the task needs a file written or a command run, use your tools right away, then stop. Keep reasoning to an absolute minimum.";

export function withSteer9(prompt: string): string {
  return `${ROUTER9_STEER}\n\n${prompt}`;
}

/** Human-readable status for the panel. */
export async function router9State(): Promise<{
  reachable: boolean; providers: number | null; model: string; base: string; dashboard: string;
}> {
  const [reachable, providers] = await Promise.all([probeRouter9(), router9ProviderCount()]);
  return { reachable, providers, model: ROUTER9_MODEL, base: ROUTER9_BASE, dashboard: ROUTER9_DASHBOARD };
}

/** Persisted router choice lives in ~/.agentic-os/fcc.json (`router` field). */
export type FreeRouter = "omniroute" | "9router";

export async function readRouterChoice(): Promise<FreeRouter> {
  try {
    const txt = await readFile(path.join(os.homedir(), ".agentic-os", "fcc.json"), "utf8");
    const j = JSON.parse(txt) as { router?: string };
    return j.router === "9router" ? "9router" : "omniroute";
  } catch { return "omniroute"; }
}
