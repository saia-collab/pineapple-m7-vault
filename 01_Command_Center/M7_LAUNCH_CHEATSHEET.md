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

## 🩹 THE ROOT CAUSE OF "TWO STUDIOS" (fixed)
OmniRoute was starting on **port 3737 — the Studio's own port**. It inherited `PORT=3737` from the launcher, so OmniRoute and the Studio fought over 3737: sometimes you got the OS, sometimes OmniRoute's dashboard "as" the Studio. **Fixed:** OmniRoute is now pinned to **20128**, the Studio owns **3737**, and the launcher no longer opens a second browser tab if the Studio is already up.

## 🆓 FREE MODELS — TWO PATHS (one reliable, one bonus)
There are two free systems. Here's the honest truth about each:

**① RELIABLE — Free Claude Code CLI / VS Code → `fcc` (:8082) → Groq free tier.**
- Uses YOUR Groq key. $0, cloud, no RAM. **Verified working.** This is the one to trust for real free coding.
- If it ever rate-limits: `http://127.0.0.1:8082/admin` → Model Config → pick another (e.g. `groq/llama-3.1-8b-instant`).

**② BONUS — the Studio's in-app "Free Claude Code" tab → OmniRoute (:20128) keyless pool.**
- Truly free, no key, 92 models. **But** it's a *keyless* pool — it gets **rate-limited constantly** (429/502 errors) and is NOT dependable for real work. Great when it's up, dead when it's throttled. That's the nature of free-for-nothing pools, not a bug I can fix.
- It now at least *connects* (port fixed, model set to `auto/best-coding`). If it errors, just retry — or use path ① / your **Claude** tab.

**👉 Practical rule:** for real work use your **Claude** / **gpt56** tabs (your subscriptions). For free coding use path ① (fcc/Groq). Treat OmniRoute's in-app tab as a free bonus, not a workhorse.

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
| 20128 | OmniRoute (in-app free tab) | ⬜ optional, keyless pool (often throttled) |
| 20129 | 9Router | ⬜ ignore |

---

## 🩹 IF SOMETHING LOOKS WRONG
- **Two Studios open / an old one on :3000** → fixed. Button 1 now kills the old :3000 Studio automatically. If you ever see two, just click button 1 again.
- **Free models offline** → click **3 — START Free Claude Code.bat**, wait 5 sec.
- **Studio won't load** → click button 1 again (it's safe to re-click).
- **Full health check** → in Claude Code, run `/m7-doctor` (read-only, changes nothing).

---

## 🔧 WHAT I CHANGED (2026-08-13)
1. **Fixed the real "two studios":** OmniRoute was grabbing port **3737** (the Studio's own port, inherited from the launcher) — now pinned to **20128**. This was THE bug.
2. Launcher no longer opens a duplicate browser tab when the Studio is already up; also kills any old :3000 studio.
3. Pointed reliable free coding (`fcc` :8082) to **Groq free tier** — verified a real reply.
4. Wired the Studio's in-app free tab to a model that exists on OmniRoute (`auto/best-coding`) so it connects (the pool's throttling is OmniRoute's, not something I can fix).
5. Fixed the launcher so :8082 (free engine) actually starts. Made 3 Desktop buttons + this cheat sheet.

<!-- M7-FIREWALL-EXEMPT: governance-reference (launch doc; "free" = free-tier models, not customer wording) -->
