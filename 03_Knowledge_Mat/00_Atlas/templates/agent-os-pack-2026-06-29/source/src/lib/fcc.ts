// Free Claude Code (fcc) proxy integration.
//
// fcc-server (https://github.com/Alishahryar1/free-claude-code) is a local
// Python proxy that speaks the Anthropic Messages API but routes traffic to
// OpenRouter / NVIDIA NIM / Kimi / etc — letting us run the Claude CLI against
// free or cheap upstream models instead of paying Anthropic per-token rates.
//
// This module:
//   1. Tells the runner what env vars to inject when spawning `claude`
//   2. Probes /health so the UI can show whether the proxy is alive
//   3. Reads ~/.fcc/.env to surface the active model + provider in the dashboard
//
// Toggle file: ~/.agentic-os/fcc.json — { "enabled": true }
// Default behaviour: enabled iff the proxy is currently listening on :8082.

import { readFile, writeFile, mkdir } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import os from "node:os";
import { omnirouteClaudeEnv, probeOmniRoute, OMNIROUTE_FREE_MODEL } from "@/lib/omniroute";
import { router9ClaudeEnv, probeRouter9, router9ProviderCount, ROUTER9_MODEL,
         type FreeRouter } from "@/lib/router9";
import { readFileSync as _readFileSync } from "node:fs";

const HOME = os.homedir();
const STATE_DIR = path.join(HOME, ".agentic-os");
const STATE_FILE = path.join(STATE_DIR, "fcc.json");
const FCC_ENV_FILE = path.join(HOME, ".fcc", ".env");

export const FCC_PORT = 8082;
export const FCC_BASE = `http://127.0.0.1:${FCC_PORT}`;
export const FCC_TOKEN = "freecc";

export interface FccState {
  enabled: boolean;     // user opt-in (persisted)
  reachable: boolean;   // is the ACTIVE router up?
  model: string | null; // model the active router will use
  provider: string | null; // friendly name of the active router
  router: FreeRouter;   // which free router is selected
  routers: {            // both backends, so the UI can offer the switch
    omniroute: { reachable: boolean; model: string };
    router9: { reachable: boolean; model: string; providers: number | null };
  };
}

async function readState(): Promise<{ enabled: boolean; router: FreeRouter }> {
  try {
    const txt = await readFile(STATE_FILE, "utf8");
    const j = JSON.parse(txt);
    return { enabled: j.enabled !== false, router: j.router === "9router" ? "9router" : "omniroute" };
  } catch { return { enabled: true, router: "omniroute" }; } // default ON, OmniRoute
}

/** Persist which free router Free Claude Code should drive. */
export async function setRouter(router: FreeRouter): Promise<void> {
  if (!existsSync(STATE_DIR)) await mkdir(STATE_DIR, { recursive: true });
  let cur: Record<string, unknown> = {};
  try { cur = JSON.parse(await readFile(STATE_FILE, "utf8")); } catch { /* fresh */ }
  await writeFile(STATE_FILE, JSON.stringify({ ...cur, router }, null, 2));
}

/** Which router is active right now (sync — used by the spawn env). */
export function activeRouterSync(): FreeRouter {
  try {
    const j = JSON.parse(_readFileSync(STATE_FILE, "utf8")) as { router?: string };
    return j.router === "9router" ? "9router" : "omniroute";
  } catch { return "omniroute"; }
}

export async function setEnabled(enabled: boolean): Promise<void> {
  if (!existsSync(STATE_DIR)) await mkdir(STATE_DIR, { recursive: true });
  let cur: Record<string, unknown> = {};
  try { cur = JSON.parse(await readFile(STATE_FILE, "utf8")); } catch { /* fresh */ }
  await writeFile(STATE_FILE, JSON.stringify({ ...cur, enabled }, null, 2));
}

// Free Claude Code now runs on OmniRoute (the fcc-server on :8082 is retired —
// its `fcc` binary isn't even installed). "Reachable" = the OmniRoute gateway
// is up on :20128.
export async function probeReachable(): Promise<boolean> {
  const { router } = await readState();
  return router === "9router" ? probeRouter9() : probeOmniRoute();
}

async function readActiveModel(): Promise<string | null> {
  try {
    const txt = await readFile(FCC_ENV_FILE, "utf8");
    // Find MODEL="..." or MODEL=... — last non-comment occurrence wins
    let model: string | null = null;
    for (const line of txt.split(/\r?\n/)) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith("#")) continue;
      const m = /^MODEL\s*=\s*"?([^"\n]+)"?$/.exec(trimmed);
      if (m) model = m[1].trim();
    }
    return model || null;
  } catch { return null; }
}

function providerNameFromModel(model: string | null): string | null {
  if (!model) return null;
  const head = model.split("/")[0];
  const map: Record<string, string> = {
    "open_router": "OpenRouter",
    "nvidia_nim": "NVIDIA NIM",
    "deepseek": "DeepSeek",
    "kimi": "Kimi",
    "wafer": "Wafer",
    "opencode": "OpenCode Zen",
    "zai": "Z.ai",
    "lmstudio": "LM Studio",
    "llamacpp": "llama.cpp",
    "ollama": "Ollama",
  };
  return map[head] ?? head;
}

export async function getState(): Promise<FccState> {
  const [{ enabled, router }, orUp, r9Up, r9Providers] = await Promise.all([
    readState(), probeOmniRoute(), probeRouter9(), router9ProviderCount(),
  ]);
  const is9 = router === "9router";
  return {
    enabled,
    reachable: is9 ? r9Up : orUp,
    model: is9 ? ROUTER9_MODEL : OMNIROUTE_FREE_MODEL,
    provider: is9 ? "9Router · RTK token saver" : "OmniRoute · free pool",
    router,
    routers: {
      omniroute: { reachable: orUp, model: OMNIROUTE_FREE_MODEL },
      router9: { reachable: r9Up, model: ROUTER9_MODEL, providers: r9Providers },
    },
  };
}
// kept for reference; the old fcc-server model discovery is retired.
void readActiveModel;
void providerNameFromModel;

// Env vars the Free Claude Code agent ALWAYS uses — these point the claude
// CLI at our local fcc-server, which routes to whatever upstream is configured
// in ~/.fcc/.env (OpenRouter Owl Alpha by default in our setup).
//
// CRITICAL: setting ANTHROPIC_API_KEY here is what makes the Claude CLI use
// our proxy token instead of the OAuth credentials saved by `claude login`.
// Without this, OAuth wins and fcc-server returns 401.
export function fccSpawnEnv(): Record<string, string> {
  // Free Claude Code now points the `claude` CLI at the OmniRoute gateway, which
  // routes to 90+ free providers with auto-fallback. (Was the fcc-server on
  // :8082 — retired; its binary isn't installed.)
  const base = activeRouterSync() === "9router" ? router9ClaudeEnv() : omnirouteClaudeEnv();
  return { ...base, CLAUDE_CODE_AUTO_COMPACT_WINDOW: "190000" };
}
