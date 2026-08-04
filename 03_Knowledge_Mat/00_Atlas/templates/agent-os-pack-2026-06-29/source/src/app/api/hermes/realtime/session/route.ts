import { NextResponse } from "next/server";
import { readFileSync } from "node:fs";
import path from "node:path";
import os from "node:os";
import { readHermesEnv } from "@/lib/hermesPhone";
import { config } from "@/lib/config";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// POST /api/hermes/realtime/session  { voice? } → { value, model, expires_at }
// Mints a short-lived OpenAI Realtime client secret the browser uses for a direct
// WebRTC speech-to-speech link (gpt-realtime). The persona + the user's own context
// are baked into the session server-side; the API key never reaches the browser.

function openaiKey(): string | null {
  try { const m = readFileSync(path.join(os.homedir(), ".claude", "skills", "youtube-thumbnails", ".env"), "utf8").match(/^OPENAI_API_KEY=(.+)$/m); if (m) return m[1].trim().replace(/^["']|["']$/g, ""); } catch { /* next */ }
  try { const k = readHermesEnv().OPENAI_API_KEY; if (k && k.trim()) return k.trim(); } catch { /* ignore */ }
  return process.env.OPENAI_API_KEY?.trim() || null;
}

// Who APOLLO is talking to — pulled live from the user's OWN vault so it knows them.
// Add an "About Me.md" note to your vault to give APOLLO your profile.
function userContext(): string {
  const root = config.vaultRoot;
  if (root) {
    for (const rel of ["About Me.md", path.join("04 Resources", "About Me.md")]) {
      try {
        let t = readFileSync(path.join(root, rel), "utf8");
        t = t.replace(/\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g, "$1").replace(/[#*`>]/g, "").replace(/\n{3,}/g, "\n\n").trim();
        if (t) return t.slice(0, 2000);
      } catch { /* try next candidate */ }
    }
  }
  return `${config.userName !== "You" ? config.userName : "The user"} — (no profile note found; add an "About Me.md" to your vault so APOLLO knows who you are.)`;
}

const PERSONA =
  "You are APOLLO — a refined English butler AI. " +
  "Crisp Received Pronunciation, calm and unflappable, warm but precise, with a touch of dry wit. " +
  "Address the user politely (\"sir\", or by name if you know it). This is a live SPOKEN conversation, so keep replies short and natural — " +
  "usually one or two sentences; never monologue. You know the user (context below) — use it to be " +
  "specific and personal, but never read the context aloud. When they ask you to open, launch, go to, or pull " +
  "up a website or an app (e.g. \"open Google\", \"pull up YouTube\", \"launch Notes\"), CALL the open_app_or_site " +
  "function to actually do it, then confirm briefly in character (e.g. \"Opening Google now.\"). " +
  "For anything that is a WEBSITE or an online service — YouTube, Gmail, an analytics dashboard, a company, a search — pass a full " +
  "https:// URL (e.g. \"https://youtube.com\", \"https://analytics.google.com\"), NOT a bare word; only use a plain app name for real " +
  "installed Mac apps like Notes or Safari. Never ask the user to clarify a reasonable request first — just take your best shot and open it. " +
  "The function returns a mode: if mode is \"search\" it means no app matched so it opened a web search — in that case say you've pulled up a search for it, don't claim you opened an app. " +
  "When they ask you to build, make, create, code, generate, whip up, or design an app, game, page, or visual " +
  "(e.g. \"build a snake game\", \"make me a neon landing page\", \"create a particle galaxy\"), CALL the build_app " +
  "function with a clear, specific prompt describing what to build, and say something brief like \"Building that now, sir.\" " +
  "The build previews live in the panel within a minute or so. Don't claim you've opened or built " +
  "something unless you actually called the matching function.";

// Model ladder — newest first. gpt-realtime-2.1 is OpenAI's latest API speech-to-speech
// generation (same full-duplex direction as GPT-Live, which is ChatGPT-only for now).
// When the GPT-Live API ships, set APOLLO_REALTIME_MODEL=gpt-live-1 and nothing else changes.
const REALTIME_MODELS = [
  process.env.APOLLO_REALTIME_MODEL || "gpt-realtime-2.1",
  "gpt-realtime", // stable fallback if the newer model rejects the session
];

// ── Voice providers ─────────────────────────────────────────────────────────
// APOLLO_VOICE_PROVIDER=xai flips Apollo onto Grok Voice Think Fast 2.0
// (xAI's realtime S2S — #1 Tau Voice agentic, $0.08/min). Requires XAI_API_KEY
// from console.x.ai (the Grok-subscription OAuth used by grok-4-5/Grok Build
// does NOT cover the developer API). xAI's API is OpenAI-compatible; if the
// realtime session shape drifts, adjust here and nothing else changes.
function xaiKey(): string | null {
  try { const k = readHermesEnv().XAI_API_KEY; if (k && k.trim()) return k.trim(); } catch { /* ignore */ }
  return process.env.XAI_API_KEY?.trim() || null;
}
const VOICE_PROVIDERS = {
  openai: {
    secretsUrl: "https://api.openai.com/v1/realtime/client_secrets",
    models: REALTIME_MODELS,
    key: openaiKey,
    missingKeyMsg: "OpenAI key not found — set OPENAI_API_KEY (as an env var or in your Hermes profile .env)",
  },
  xai: {
    secretsUrl: "https://api.x.ai/v1/realtime/client_secrets",
    models: [process.env.APOLLO_XAI_VOICE_MODEL || "grok-voice-think-fast-2", "grok-voice"],
    key: xaiKey,
    missingKeyMsg: "Grok Voice needs an xAI API key — create one at console.x.ai and set XAI_API_KEY (env or Hermes profile .env). Your Grok OAuth login doesn't cover the developer API.",
  },
} as const;
const VOICE_PROVIDER = (process.env.APOLLO_VOICE_PROVIDER === "xai" ? "xai" : "openai") as keyof typeof VOICE_PROVIDERS;

export async function POST(req: Request) {
  const provider = VOICE_PROVIDERS[VOICE_PROVIDER];
  const key = provider.key();
  if (!key) return NextResponse.json({ error: provider.missingKeyMsg }, { status: 400 });
  const body = await req.json().catch(() => ({}));
  // cedar/marin are the new-generation natural voices; cedar suits the butler. ash kept for continuity.
  const voice = /^(alloy|ash|ballad|coral|echo|sage|shimmer|verse|marin|cedar)$/.test(body?.voice) ? body.voice : "cedar";
  const instructions = `${PERSONA}\n\n# Who you're talking to\n${userContext()}`;

  let lastErr: unknown = null;
  for (const model of provider.models) {
  try {
    const r = await fetch(provider.secretsUrl, {
      method: "POST",
      headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        session: {
          type: "realtime",
          model,
          instructions,
          audio: {
            input: {
              // Tight VAD → it starts replying ~as soon as you stop talking.
              // silence_duration_ms is the main latency lever (default 500); 280 is snappy
              // without chopping you off mid-pause.
              turn_detection: { type: "server_vad", threshold: 0.5, prefix_padding_ms: 200, silence_duration_ms: 280 },
              transcription: { model: "gpt-4o-mini-transcribe" },
            },
            output: { voice },
          },
          // Lets the butler actually act on the user's Mac (handled client-side).
          tools: [
            {
              type: "function",
              name: "open_app_or_site",
              description: "Open a website or a macOS application on the user's Mac. Call this whenever they ask to open, launch, go to, or pull up something.",
              parameters: {
                type: "object",
                properties: { target: { type: "string", description: "A full https:// URL for a website (e.g. 'https://google.com'), or a macOS app name (e.g. 'Notes', 'Safari')." } },
                required: ["target"],
              },
            },
            {
              type: "function",
              name: "build_app",
              description: "Build a single self-contained HTML app, game, page, or visual on the user's Mac and preview it live in the panel. Call this whenever they ask to build, make, create, code, generate, whip up, or design something (e.g. 'build a snake game', 'make a neon landing page', 'create a particle galaxy'). The build runs on-device and takes up to ~90 seconds.",
              parameters: {
                type: "object",
                properties: { prompt: { type: "string", description: "A clear, specific description of what to build, e.g. 'a playable neon snake game with a score counter and increasing speed'." } },
                required: ["prompt"],
              },
            },
          ],
          tool_choice: "auto",
        },
      }),
    });
    const j = await r.json();
    if (r.ok && j?.value) return NextResponse.json({ value: j.value, model, expires_at: j.expires_at });
    lastErr = j?.error?.message || `realtime session failed (${model})`;
    // fall through to the next model in the ladder
  } catch (e) {
    lastErr = String(e);
  }
  }
  return NextResponse.json({ error: String(lastErr || "realtime session failed") }, { status: 502 });
}
