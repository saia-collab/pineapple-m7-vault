---
title: M7 Hermes — Agent Chats & Model Switching (how to go from one brain to another)
type: reference
status: active
date: 2026-08-05
---

# 🧠 M7 HERMES — AGENT CHATS & MODEL SWITCHING

Your Local Studio has **two ways** to "chat with a different AI agent." Don't mix them up.

## 1) The Studio TABS (each is its own agent app)
Each tab lights up when its CLI is installed + you're logged in.

| Tab | Status (2026-08-05) | To activate |
|---|---|---|
| **Codex** (gpt-5.6-sol) | ✅ working | already logged in |
| **Claude** | ✅ installed | `claude login` (uses your Claude plan) |
| **Gemini** | ✅ installed | already on PATH |
| **Antigravity** | ✅ installed | already on PATH |
| **opencode** (free coder) | ✅ installed today | nothing — free out of the box |
| **GPT 5.6 Code → Qwen 3.8** | ⚙️ CLI installed today | run `qodercli login` once (browser) |
| **Kimi Code** | ⬜ not installed | download from kimi.com, then `kimi login` |
| **Grok Build** | ⬜ not installed | needs X Premium+ subscription, then `grok login --device-auth` |

## 2) Hermes CHAT (one chat, switch the brain + persona)
Hermes is ONE agent whose **brain** and **persona (profile)** you switch inside the chat.

### Switch the PERSONA (profile bar at top of Hermes chat)
Your profiles, each already wired to the working Codex brain:
`main` · `seo` · `content` · `marketing` · `roofing` · `restoration` · `leads` · `research` · plus specialist ones (`fusion`, `sakana-fugu`, `grok-build`, `julian`).
Click one to load that persona's instructions. All Pineapple work → use the matching profile.

### Switch the BRAIN (type in the chat box)
```
/model gpt-5.6-sol                              ← default, FREE (your ChatGPT plan via Codex)
/model nvidia/nemotron-3-ultra-550b-a55b:free   ← FREE, 1M memory (also the auto-fallback)
/model deepseek/deepseek-chat-v3:free           ← FREE (if you want DeepSeek's style)
```
Paid brains (need OpenRouter credits at https://openrouter.ai/settings/credits):
```
/model anthropic/claude-sonnet-4.5              ← Claude (paid)
/model z-ai/glm-4.6                             ← GLM (paid)
/model moonshotai/kimi-k2                       ← Kimi (paid)
```

## The setup, in one line
- **Default brain:** gpt-5.6-sol via Codex (free on your ChatGPT plan) — auto-falls back to a free model if Codex rate-limits.
- **Everything Pineapple** runs through a Hermes profile → lands PAUSED in `01_Command_Center/Outbox_Drafts/` → you approve.
- **Free today, zero new spend.** Claude/GLM/Kimi quality is one `/model` command away once you add OpenRouter credits.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
