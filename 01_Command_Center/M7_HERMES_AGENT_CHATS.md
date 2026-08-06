---
title: M7 Hermes — Agent Chats, Profiles & What Still Needs Your Login
type: reference
status: active
date: 2026-08-06
---

# 🧠 M7 HERMES — AGENT CHATS & PROFILES

## Your Hermes profiles (the chat "personas", each with its own brain)
Pick one in the **profile bar** at the top of the Hermes → Chat tab.

| Profile | Brain (model) | Works now? |
|---|---|---|
| `main` / `default` | gpt-5.6-sol (Codex) | ✅ free |
| `gpt56` | gpt-5.6-sol (Codex) | ✅ free |
| `north-mini` | cohere/north-mini-code:free | ✅ free |
| `omniroute` | nemotron-3-ultra (1M ctx) free | ✅ free |
| `jarvis` | gpt-5.6-sol (Codex) | ✅ free |
| `game-dev` | gpt-5.6-sol (Codex) | ✅ free |
| `seo-lead` | gpt-5.6-sol (Codex) | ✅ free |
| `blank-state` | gpt-5.6-sol (Codex) | ✅ free |
| `notebook-obsidian` | gpt-5.6-sol (Codex) | ✅ free (reads vault; NotebookLM needs `nlm login`) |
| `seo` `content` `marketing` `roofing` `restoration` `leads` | gpt-5.6-sol (Codex) | ✅ free (Pineapple business personas) |
| `glm-5-2` | z-ai/glm-5.2 | ⚠️ needs OpenRouter credits |
| `kimi-k2-7` | moonshotai/kimi-k2-0905 | ⚠️ needs OpenRouter credits |
| `qwen-3-7` | qwen/qwen-plus | ⚠️ needs OpenRouter credits |
| `hy3` | tencent/hy3 | ⚠️ needs OpenRouter credits |
| `hermes-cloud` | Nous Portal | ⚠️ run `hermes portal` to log in |
| `local` | minimax-m3 (Ollama) | ⚠️ needs Ollama running |
| `ollama-glm-512` | glm-5.2 (Ollama Cloud) | ⚠️ needs OLLAMA_API_KEY |
| `grok-build` | Grok (X plan) | ⚠️ needs SuperGrok + `grok login` |
| `fusion` `sakana-fugu` | model councils | specialist |

**`julian` was removed** — it was a leftover from the pack's creator (Julian Goldie), not yours.

## Switch the BRAIN mid-chat (type in the box)
```
/model gpt-5.6-sol                               ← free (Codex)
/model cohere/north-mini-code:free               ← free
/model nvidia/nemotron-3-ultra-550b-a55b:free    ← free, 1M memory
/model anthropic/claude-sonnet-4.5               ← paid (needs OpenRouter credits)
```

---

# 🔌 WHAT STILL NEEDS *YOUR* LOGIN (I can't sign in as you)

Everything below is built and wired — it just needs you to authenticate once. Do these in a normal terminal (or ask me and I'll run the command so a browser opens for you to approve).

| Feature | Command you run | What it unlocks |
|---|---|---|
| **NotebookLM** (Notebook tab) | `nlm login` | your NotebookLM notebooks + the notebook-obsidian chat's NotebookLM half |
| **Kimi Code** tab | `kimi login` (CLI already installed) | the Kimi coding tab |
| **Qwen 3.8** (GPT 5.6 Code tab) | `qodercli login` | the Qwen brain |
| **Higgsfield** (image/video) | `hermes -p main mcp login higgsfield` | AI image/video generation |
| **MiniMax** (Hermes Studio) | `hermes auth add minimax-oauth` | Studio image/video/voice |
| **Nous Portal** (`hermes-cloud`) | `hermes portal` | Nous cloud models |
| **Grok Build** | upgrade to SuperGrok, then `grok login --device-auth` | the Grok tab (needs paid X Premium+) |
| **Claude tab** | `claude login` | the Claude tab (uses your Claude plan) |

## The one paid upgrade (optional)
Add credits at https://openrouter.ai/settings/credits → unlocks the `glm-5-2`, `kimi-k2-7`, `qwen-3-7`, `hy3` profiles and Claude. Everything else is already free.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
