---
title: M7 Quick Card
status: active
last_verified: 2026-08-22
---

# M7 quick card

## Daily buttons

1. `LAUNCH_PM7_STUDIO.bat` — starts Local Studio, Hermes, OmniRoute, and supporting services.
2. `LAUNCH_PM7_FREE.bat` — launches Claude Code through OmniRoute's active context.
3. `LAUNCH_PM7_PAID.bat` — launches Claude Code through the signed-in Claude subscription, with OmniRoute variables cleared for that process.
4. `PM7_REPAIR_AND_VERIFY.bat` — starts the stack, sends three minimal route tests, and writes a PAUSED receipt.
5. `CONFIGURE_PM7_AI_CLIENTS.bat` — regenerates Claude, Codex, OpenCode, and Cursor setup from the live OmniRoute catalog.
6. `CONFIGURE_PM7_GOOGLE_AI.bat` — opens the required Google Gemini/Antigravity provider login with paid-credit overages disabled.
7. `LAUNCH_PM7_GEMINI.bat` — launches an installed Gemini CLI through OmniRoute without writing a key to the vault.

## Current ports

| Service | URL | Required for core Studio |
|---|---|---|
| Local Studio | `http://127.0.0.1:3737/hermes` | yes |
| Hermes | `http://127.0.0.1:9119` | yes |
| OmniRoute | `http://127.0.0.1:20128` | yes |
| OmniRoute OpenAI API | `http://127.0.0.1:20128/v1` | yes |
| Free Claude proxy | `http://127.0.0.1:8082` | optional |
| M7 backend | `http://127.0.0.1:51763` | optional |
| Notebook/Obsidian bridge | `http://127.0.0.1:8643` | optional |
| Ollama | `http://127.0.0.1:11434` | optional |

## Model routes

- Writing/chat: `auto/best-chat`
- Coding: `auto/best-coding`
- Reasoning: `auto/best-reasoning`
- DeepSeek, Kimi, GLM, and MiniMax: select only IDs returned by the live model catalog and backed by a working provider login/key.
- Ollama: optional; use an already-installed lightweight model. Never auto-pull a large model on the 16 GB computer.

## If something fails

Run `PM7_REPAIR_AND_VERIFY.bat`, then open the newest `PM7_LOCAL_VERIFY_*.md` file in `01_Command_Center/Outbox_Drafts/`. Never paste tokens into a receipt or GitHub.

## Safety

All publishing, sending, and ad spend stay PAUSED until Saia gives an explicit GO.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
