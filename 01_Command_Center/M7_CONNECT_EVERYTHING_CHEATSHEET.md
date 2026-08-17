---
title: M7 CONNECT-EVERYTHING CHEAT SHEET — every tab, exactly what it needs
status: reference
date: 2026-08-16
note: Local models (Ollama/LM Studio) are OFF (removed for memory). Everything runs on cloud keys + logins now.
key_locations: Hermes-routed keys -> %LOCALAPPDATA%\hermes\.env  ·  FCC/DeepSeek -> C:\Users\estim\.fcc\.env  ·  CLI logins -> terminal
---

# 🔌 M7 CONNECT-EVERYTHING CHEAT SHEET

**The rule:** local models are gone (memory), so every tab connects with either **(A) an API key you paste into a file**, or **(B) a one-time browser login (OAuth)**. This sheet says exactly which, for every tab.

---

## ⭐ THE ONE KEY THAT UNLOCKS THE MOST — OpenRouter
Hermes (Chat, Oracle, Muse, content generation), Fusion, Sakana, Muse Code, Hy3 all run on **OpenRouter**. Your "Hermes 401 User not found" = no OpenRouter key. Add it and the whole Hermes content/research side comes alive.
1. Get a key: **https://openrouter.ai/keys** (has free `:free` models; +$5 = 1,000/day)
2. Paste it into the Hermes env file (see "How to add a key" below): `OPENROUTER_API_KEY=sk-or-...`
3. Restart the Studio → Hermes tabs work.

---

## ✅ ALREADY WORKING (no action)
| Tab | Runs on |
|---|---|
| **Claude / jcode** | your Claude subscription (`claude login`) — best writer |
| **DeepSeek Coder** | your DeepSeek key (in `.fcc/.env`) ✅ |
| **Kimi Code** | your Kimi login ✅ |
| **Free Claude Code / OmniRoute** | free keyless pool ✅ |

## 🧠 FOR CONTENT + BLOGS (what you actually need — your goal)
| Tab | Needs | Get it |
|---|---|---|
| **Hermes Chat / Oracle / Muse** (research → write blogs) | **OpenRouter key** | openrouter.ai/keys |
| **SEO → OpenSEO** (the findings/keywords) | **Google Search Console** login | run `python scripts/gsc-connect.py` (5-min Google sign-in) |
| **Claude / DeepSeek / Kimi** (the actual writing) | already done ✅ | — |
> This is the whole "find a topic → write the blog" loop. It needs **OpenRouter + a Google sign-in** — nothing else.

## 🎨 MEDIA TABS (optional — each needs a PAID account + browser login)
These make images/video/voice. They are **not** needed for blogs or leads. Connect only if you want them.
| Tab | Command / key | Paid account |
|---|---|---|
| **Higgsfield** (images/video) | `hermes -p muse mcp login higgsfield` | Higgsfield |
| **Hermes Astros** (YouTube competitor watch) | `hermes auth add xai-oauth` | X Premium+ / SuperGrok |
| **Hermes Studio / MiniMax** (image/video) | `hermes auth add minimax-oauth` | MiniMax |
| **Video Director** (AI avatar presenter) | `HEYGEN_API_KEY=...` in Hermes env | HeyGen |
| **Jarvis voice / VSL voice** | `ELEVENLABS_API_KEY=...` in Hermes env | ElevenLabs (free tier) |

## ⚠️ NEEDS LOCAL OLLAMA (currently OFF — memory)
These can't work until Ollama is reinstalled. **The Ollama APP is small and `:cloud` models use no local disk** — only *downloaded* models eat memory. So you CAN reinstall just the app for cloud models if you want:
| Tab | Needs |
|---|---|
| **GLM Code**, **Local** | Ollama app running (`:cloud` models = no disk) |
| **Video Editor** (auto-cut reels) | Ollama (default) OR a stable `claude login` |

---

## 📝 HOW TO ADD A KEY (the no-terminal way)
Two files hold all keys. Open in Notepad, paste on the right line, Ctrl+S:
- **Hermes keys** (OpenRouter, HeyGen, ElevenLabs): open `%LOCALAPPDATA%\hermes\.env`
- **DeepSeek key**: open `C:\Users\estim\.fcc\.env`
Each line is `NAME=your-key-here`. One key per line. After editing, **restart the Studio.**

## 🔑 THE LOGIN COMMANDS (OAuth — run in a NEW PowerShell, approve in browser)
```
claude login                              # Claude (if it ever says "not logged in")
kimi login                                # Kimi
hermes auth add xai-oauth                 # Grok (Astros) — needs X Premium+
hermes auth add minimax-oauth             # MiniMax (Hermes Studio)
hermes -p muse mcp login higgsfield       # Higgsfield
```
Each opens a browser — you click Approve. **Only you can do these; nobody logs in for you.**

## 🎯 PRIORITY ORDER (do these, skip the rest)
1. **OpenRouter key** → Hermes + content generation comes alive.
2. **Google sign-in for SEO** (`gsc-connect.py`) → real keyword findings.
3. That's it for blogs + leads. Media tabs (Higgsfield/MiniMax/HeyGen) are optional extras — add when you want video.

<!-- M7-FIREWALL-EXEMPT: connect reference -->
