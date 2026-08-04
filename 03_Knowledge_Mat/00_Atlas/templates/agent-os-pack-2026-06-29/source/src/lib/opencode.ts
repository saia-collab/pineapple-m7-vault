// opencode — the open-source terminal coding agent (opencode.ai, 160k★) wired
// into the Agent OS. Runs the locally-installed `opencode` binary headless
// (`opencode run … --format json`) and streams its agentic tool loop into a tab.
//
// Why it's here: opencode is provider-agnostic (75+ providers via models.dev) and
// ships a built-in FREE tier — the `opencode` (Zen) provider serves capable models
// at $0, no API key. So this surface builds real apps for free out of the box, and
// anyone who's run `opencode auth login` can pick their own provider/model too.
import { existsSync } from "node:fs";
import os from "node:os";
import path from "node:path";

export const OPENCODE_BIN =
  process.env.OPENCODE_BIN || path.join(os.homedir(), ".opencode", "bin", "opencode");

export const OPENCODE_ROOT = path.join(os.homedir(), ".agentic-os", "opencode", "builds");

// Built-in free models (opencode Zen provider — no key, cost $0). Verified working
// headless. Users with their own providers configured can pass any provider/model.
export const OPENCODE_MODELS = [
  { id: "opencode/nemotron-3-ultra-free", label: "Nemotron 3 Ultra", sub: "NVIDIA · free · verified" },
  { id: "opencode/big-pickle", label: "Big Pickle", sub: "opencode Zen · free flagship" },
  { id: "opencode/deepseek-v4-flash-free", label: "DeepSeek V4 Flash", sub: "Zen · free · undated build" },
  { id: "deepseek/deepseek-v4-flash", label: "DeepSeek V4 Flash 0731", sub: "official API · agent-tuned · 1M ctx" },
  { id: "openrouter/deepseek/deepseek-v4-flash-0731", label: "DeepSeek V4 Flash 0731 (OR)", sub: "dated id via OpenRouter · 1M ctx" },
  { id: "deepseek/deepseek-v4-pro", label: "DeepSeek V4 Pro", sub: "official API · strong tier · 1M ctx" },
  { id: "opencode/north-mini-code-free", label: "North Mini Code", sub: "Cohere · free · coding" },
  { id: "omniroute/auto/coding", label: "OmniRoute Coding", sub: "free router · verified $0" },
  { id: "omniroute/auto/best-coding", label: "OmniRoute Best-Coding", sub: "free router · strongest" },
  { id: "omniroute/auto/best-fast", label: "OmniRoute Fast", sub: "free router · quick drafts" },
  { id: "tinker/thinkingmachines/Inkling", label: "Inkling", sub: "Tinker · 975B MoE · paid" },
] as const;

export const OPENCODE_DEFAULT_MODEL =
  process.env.OPENCODE_MODEL || "opencode/nemotron-3-ultra-free";

export interface OpenCodeState {
  installed: boolean;
  bin: string;
  ready: boolean;
}

// opencode is a local binary — no daemon to probe. Ready == the binary is present.
export function getOpenCodeState(): OpenCodeState {
  const installed = existsSync(OPENCODE_BIN);
  return { installed, bin: OPENCODE_BIN, ready: installed };
}
