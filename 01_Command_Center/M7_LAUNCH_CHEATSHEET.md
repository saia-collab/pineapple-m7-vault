---
type: launch_cheatsheet
title: M7 LAUNCH CHEAT SHEET — one-click start, free models, Ollama answer
status: active
date: 2026-08-13
note: Internal ops doc. "free" here = free-tier AI models, not customer wording.
---

# 🚀 M7 LAUNCH CHEAT SHEET
**Everything you need to start the studio and free models — no terminal, ever.**

---

## ✅ THE ONE THING TO CLICK EVERY DAY
Double-click **`1 — START Pineapple Studio.bat`** on your Desktop.

That one button starts **all of it**:
| It starts | Port | What it is |
|---|---|---|
| Local Studio | 3737 | your Agentic OS (Hermes, SEO, all tabs) |
| Hermes | 9119 | the agent brain |
| **Free Claude Code** | 8082 | **free models — now works (Groq free tier)** |
| OmniRoute | 20128 | optional free-chat router (see below) |

Wait ~30 seconds. Your browser opens to the Studio automatically. **Done.**

> The old `LAUNCH_ALL.bat` does the exact same thing — I just renamed it `1 — …` so the 3 buttons line up.

---

## 🎛️ THE 3 DESKTOP BUTTONS
| Button | When to click it |
|---|---|
| **1 — START Pineapple Studio.bat** | Every day. Starts everything. This is 95% of the time. |
| **2 — START OmniRoute.bat** | Only if the Studio's *in-app* "Free Claude Code" chat tab says offline **and** you want to use it. Optional. |
| **3 — START Free Claude Code.bat** | If you only want the free-models engine (8082) without restarting the whole Studio. |

**You almost never need 2 or 3 by themselves** — button 1 already starts them. They exist for when you want to restart just that one piece.

---

## 🆓 HOW FREE MODELS WORK NOW (this was the broken part — it's fixed)
- **Free coding = Free Claude Code (:8082) → Groq's free tier** (a cloud model, `llama-3.3-70b`).
- **$0. No login. Uses no computer memory.** This is why it now "just works."
- You had **3 half-connected routers fighting each other** (OmniRoute, 9Router, and this). I turned OFF the two empty ones and pointed everything at the one that has your keys.
- **If it ever says "rate limited":** open `http://127.0.0.1:8082/admin` → Model Config → pick another free model (e.g. `groq/llama-3.1-8b-instant`). That's the only knob you'll ever touch.

### The Studio's in-app "Free Claude Code" TAB (the one that showed OFFLINE)
That specific chat tab is wired to **OmniRoute**, which is empty until you connect one provider **once** (a login + click I can't do for you). **You don't need it** — use the normal **Claude** tab for chat, and free coding runs through button 1's engine. If you *do* want that tab: click button 2, then in the OmniRoute dashboard open **Providers/Discovery** and connect one free provider (e.g. OpenCode "big-pickle"). One time only.

---

## 🧠 "DO I NEED TO LAUNCH OLLAMA?" — **NO.**
- **Ollama is NOT needed for free models anymore.** Free models = cloud Groq (above), which uses zero RAM.
- **Why Ollama kept failing:** it ran out of memory. Your PC has 15 GB RAM but only ~2.4 GB free (Chrome + apps eat the rest). `gemma4` needs ~10 GB → **impossible**, so it crashed with "out-of-memory."
- **Ollama already auto-starts** at boot (it's in your Startup folder) — you never need to launch it by hand.
- **If you ever want a local model anyway** (fully offline, no internet): close Chrome/heavy apps first, then use a SMALL one that fits — `deepseek-coder:latest` (0.7 GB) fits even with low RAM. Skip the big ones (`gemma4`, 7B+) until you have more free memory.
- **Bottom line:** ignore Ollama. It's optional and not part of your daily flow.

---

## 🗺️ WHAT RUNS WHERE (so nothing feels mysterious)
| Port | Thing | Needed? |
|---|---|---|
| 3737 | Local Studio (the OS) | ✅ core |
| 9119 | Hermes agent | ✅ core |
| 8082 | Free Claude Code → Groq free | ✅ free models |
| 11434 | Ollama (local models) | ⬜ optional, auto-starts |
| 20128 | OmniRoute (in-app free chat tab) | ⬜ optional, needs 1 connect |
| 20129 | 9Router | ⬜ ignore |

---

## 🩹 IF SOMETHING LOOKS WRONG
- **Two Studios open / an old one on :3000** → fixed. Button 1 now kills the old :3000 Studio automatically. If you ever see two, just click button 1 again.
- **Free models offline** → click **3 — START Free Claude Code.bat**, wait 5 sec.
- **Studio won't load** → click button 1 again (it's safe to re-click).
- **Full health check** → in Claude Code, run `/m7-doctor` (read-only, changes nothing).

---

## 🔧 WHAT I CHANGED TODAY (2026-08-13)
1. Pointed Free Claude Code (:8082) off the RAM-heavy local model onto **Groq free tier** — verified a real reply came back.
2. Fixed the launcher so :8082 actually starts (it was silently failing).
3. Fixed the "two Studios" — button 1 now kills any old :3000 Studio.
4. Made 3 clean Desktop buttons + this cheat sheet.

<!-- M7-FIREWALL-EXEMPT: governance-reference (launch doc; "free" = free-tier models, not customer wording) -->
