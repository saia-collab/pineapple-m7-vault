---
title: M7 Launchers — What Each One Does (read this when confused)
status: active
last_updated: 2026-07-17
---

# 🖥️ M7 Launchers — the plain-English map

## ⭐ KEEP ON DESKTOP (the only 3 you touch regularly)
| Launcher | What it does | When |
|---|---|---|
| **START_LOCAL_STUDIO.bat** | Opens your REAL dashboard at **localhost:3000** | Every day, to start work |
| **UPDATE_AGENT_OS.bat** | Updates Agent OS to the latest build | Occasionally (you just did) |
| **GSC_Connect** (or gsc_auth) | Reconnects Google Search Console | Only if GSC drops |

## 📁 KEEP IN THE FOLDER (situational — not desktop clutter)
| Launcher | What it does |
|---|---|
| LAUNCH_CLAUDE_CODE.bat | Opens Claude Code (me) in a terminal |
| M7_DOCTOR.bat | Runs a health check on the vault |
| M7_CLEANUP.bat | Archives old junk files |
| AM_STARTUP.bat / PM_SHUTDOWN.bat | The optional morning/night loops |
| START_PAPERCLIP.bat | Starts the Paperclip tool |

## 🗄️ ALREADY ARCHIVED (ignore — in Launcher_Archive/)
START_M7, START_M7_SERVER, LAUNCH_ALL_legacy, M7_TIDY, HERMES_COMMAND_CENTER,
INGEST_*, REGISTER_DAILY_SYNC, RUN_M7_DASHBOARD, DOUBLE_CLICK_TO_FIX_MY_FOLDERS.
These are old. You already moved them here. Leave them.

## ⚠️ THE ONE THAT CONFUSED YOU
**RUN_AGENT_OS.bat** opens an OLD dashboard at **localhost:3737** — NOT the one you use.
👉 Use **START_LOCAL_STUDIO.bat** instead. (I left RUN_AGENT_OS in place in case the old
one is ever needed, but don't put it on your desktop.)

## 🍍 The rule
**One button to start your day: START_LOCAL_STUDIO.** That's it. Everything else is
occasional or automatic. If a launcher isn't on this list, it's probably old — ask before running it.

<!-- M7-FIREWALL-EXEMPT: reference -->
