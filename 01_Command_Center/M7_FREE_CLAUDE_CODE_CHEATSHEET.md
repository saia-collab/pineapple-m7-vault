---
title: M7 Free Claude Code (FCC) — Study Guide & Cheat Sheet
type: reference
status: active
date: 2026-08-10
panel: http://127.0.0.1:3737/admin  · proxy: fcc-server on :8082 · config file: ~/.fcc/.env
note: FCC lets the Claude/Free-Claude tabs run on FREE models instead of paid. Nothing here publishes anything.
---

# 🆓 Free Claude Code (FCC) — Cheat Sheet

## What it is (30-second version)
FCC is a little **local switchboard** (`fcc-server`) that sits between the Studio's coding tabs and the AI models. Instead of paying Anthropic, it routes your requests to **free** models — either free cloud APIs (OpenRouter, Groq, Gemini…) or a model on your own PC (Ollama). You manage it at **`127.0.0.1:3737/admin`**. All your keys are saved to one file: **`C:\Users\estim\.fcc\.env`**.

- **Admin panel (:3737/admin)** = where you *configure* it. Works even when the proxy is off.
- **fcc-server (:8082)** = the actual proxy that *runs* it. If Mission Control says **"Free Claude Offline · fcc-server down,"** the proxy isn't running — start it (see Fix-it).

---

## The 3 tabs (left sidebar)
| Tab | What it's for |
|---|---|
| **Providers** | Add/manage the AI services (paste API keys, wire local model URLs). The money tab. |
| **Model Config** | Pick *which* model the Claude tabs actually use, and the free-router switch. |
| **Messaging** | Notification/message routing for the server (where status/alerts go). Open it to see its fields; leave default unless you want alerts. |

---

## 🔑 PROVIDERS tab — how to add things
Each card shows a **status badge**:
- **Configured** = key is saved ✅ · **Missing key** = needs a key ⚠️ · **Offline** = local server not running · **Reachable** = local server responding ✅

### Add an API key (cloud provider)
1. Scroll to the **Providers** form (lower half).
2. Find the field (e.g. *Mistral API Key*), **paste your key**.
3. Click **Validate** (checks it works) → **Apply** (saves it to `~/.fcc/.env`).
4. The card flips to **Configured**. Click **Refresh models** to pull that provider's model list.

### Wire a LOCAL model (no key, 100% free/unlimited)
- **Ollama** (recommended, already **Reachable** for you at `:11434`), **LM Studio** (`:1234/v1`), **llama.cpp** (`:8080/v1`).
- Set the URL in its field → click **Test**. Green/**Reachable** = good. **Offline** = that app isn't running (open Ollama / LM Studio first).

> **Validate → Apply** is what saves. Nothing is stored until you click **Apply**. "No changes" at the bottom means nothing's pending.

---

## ⚙️ MODEL CONFIG tab — which model runs
This sets the `MODEL` lines in `~/.fcc/.env`. Point it at a **named free** model:
- **Best free coder:** `open_router/qwen/qwen3-coder:free`
- **Big free general:** `open_router/google/gemma-4-31b-it:free` (256K context)
- **Local unlimited:** `ollama/gemma2` (runs on your PC, no limits, no key)

If you use the advanced Claude-routing lines, point all three at a free model too:
`MODEL_OPUS` = `MODEL_SONNET` = `MODEL_HAIKU` = `open_router/qwen/qwen3-coder:free`

**Router switch (OmniRoute ⇄ 9Router):** two free routing engines. **OmniRoute** (default) = keyless pool of 90+ free providers. **9Router** = adds a token-saver. Flip to whichever is healthy; the panel tells you the command if one is down.

> 🚫 **Never pick a "stealth/alpha" model** (names ending `-alpha`, `owl-alpha`, `sonoma-*`). Labs drop those free for a few weeks then kill them — they suddenly stop working. Always use a **named `:free`** model.

---

## 🖥️ "Add a CLI" — that's a DIFFERENT place (important)
The FCC admin adds **API keys + model URLs**, *not* CLIs. The agent **CLIs** (Claude, Codex, Antigravity, OpenClaw) are installed separately and light up their own left-side tabs:
- **Claude** → run `claude login` once (uses your Claude plan — **no API key needed**).
- **Codex** → OpenAI Codex CLI + `codex login`.
- **Antigravity** (`agy`) → Google's tool (Gemini CLI was retired — use this).
- Each tab works once its program is installed + you're logged in. Don't put an **empty** `ANTHROPIC_API_KEY=` anywhere — it breaks `claude login`.

---

## 📋 Where to get each provider's key (your panel)
| Provider (env var) | Get key at | Free? |
|---|---|---|
| **OpenRouter** `OPENROUTER_API_KEY` | openrouter.ai/keys | ✅ free models (50/day; +$5 → 1000/day) |
| **Groq** `GROQ_API_KEY` | console.groq.com | ✅ free + very fast |
| **Cerebras** `CEREBRAS_API_KEY` | cloud.cerebras.ai | ✅ free tier, fast |
| **Gemini** `GEMINI_API_KEY` | aistudio.google.com/apikey | ✅ free tier |
| **DeepSeek** `DEEPSEEK_API_KEY` | platform.deepseek.com | 💳 cheap |
| **Kimi** `KIMI_API_KEY` | platform.moonshot.ai | 💳 cheap |
| **Z.ai (GLM)** `ZAI_API_KEY` | z.ai | 💳 cheap |
| **NVIDIA NIM** `NVIDIA_NIM_API_KEY` | build.nvidia.com | ✅ free credits |
| **Mistral / Codestral** `MISTRAL_API_KEY` / `CODESTRAL_API_KEY` | console.mistral.ai | ✅ free tier |
| **Fireworks** `FIREWORKS_API_KEY` | fireworks.ai | 💳 |
| **OpenCode Zen/Go** `OPENCODE_API_KEY` | opencode.ai/zen | 💳 (one key, both) |
| **Ollama / LM Studio / llama.cpp** (local) | ollama.com · lmstudio.ai | ✅ free, unlimited |

---

## 🔧 Fix-it
- **"fcc-server down" / Free Claude Offline** → the proxy isn't running. Your **LAUNCH_ALL** / START launcher tries to start it; if it never comes up, `fcc-server` may not be installed yet (optional piece — the rest of the OS works without it).
- **HTTP 402 "requires more credits"** → your free model was retired. Swap the `MODEL` line to a current `:free` model, Apply, restart. (No paid credits needed.)
- **HTTP 429 "free-models-per-day"** → hit OpenRouter's 50/day free limit. Add **$5** to OpenRouter (→1000/day, still free models), OR switch to **Ollama local** (unlimited), OR wait for daily reset.
- **Local model "Offline"** → open the app first (Ollama/LM Studio), then click **Test**.

---

## ✅ Your current state (from your panel, 2026-08-10)
- **Configured:** OpenRouter, Groq, Cerebras, Gemini, DeepSeek, Kimi, Z.ai, NVIDIA NIM, OpenCode (Zen+Go). **Ollama = Reachable** (local, free).
- **Missing key (optional):** Mistral, Codestral, Wafer, Fireworks — add only if you want them.
- **Bottom line:** you already have plenty of free routes wired. For $0 coding, set **Model Config → `open_router/qwen/qwen3-coder:free`** (or `ollama/gemma2` for unlimited local), make sure **fcc-server is running**, and you're set.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference (technical doc; "free" = free AI models/tiers, not marketing copy) -->
