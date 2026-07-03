---
type: master_study_guide
title: M7 OS — Big Study Guide (print me)
status: active
last_updated: 2026-06-18
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🍍 PINEAPPLE CONTRACTORS M7 — BIG STUDY GUIDE

**Motto: Plan → Push → Play → Profit (the Pineapple Standard).**
Read this top to bottom once. Print it. It is the single map for the whole system.

---

## 0. WHAT THIS SYSTEM IS (one breath)
A local "AI operating system" living in `C:\Pineapple Contractors M7`. It turns your roofing
knowledge into marketing — research → write → compliance-check → PAUSED draft → you publish.
AI agents do the work; **you press publish.** That's the whole idea. It's already built.

---

## 1. THE OBSIDIAN FIX (this was your blocker — now solved)
Your two plugins were mismatched. I corrected the configs to your real settings:
- **Local REST API** runs on HTTP **port 27123**, key starts `1f8aa92...`
- MCP-Tools + the client configs now point there (were wrongly on 27124 + an old key).

**To finish the connection (one time):**
1. Open Obsidian → keep it OPEN (the API only answers while the app runs).
2. Settings → Community plugins → confirm **Local REST API** is ENABLED, "Enable non-encrypted (HTTP) server" is ON.
3. In a terminal, re-point Claude Code to the right door:
   ```
   claude mcp remove obsidian
   claude mcp add --transport http obsidian http://127.0.0.1:27123/mcp/ --header "Authorization: Bearer 1f8aa9201f4d4769ec53b2eb57dc1333c5a6b6e6b379294e71229a584d17cd8d"
   ```
4. Restart Claude Code. "Could not attach" will be gone.

> You do NOT need GitHub for Obsidian. You do NOT need to clone the estim/EMAI vault to fix this —
> your vault is already more complete. The only issue was the port/key mismatch, now fixed.

---

## 2. THE FOLDER MAP (what each room is for, plain English)
| Folder | Think of it as | What lives here |
| :--- | :--- | :--- |
| `01_Command_Center` | The brain / front desk | Playbooks, dashboard, GROUNDING rules, Outbox drafts |
| `02_Workspaces` | The work table | Active campaign staging |
| `02_Media_Vault` | The photo/video closet | Drone shots, reels |
| `03_Knowledge_Mat` | The library | Research, `raw/` intake, `00_Atlas/` index + templates |
| `04_Tech_Lab` | The engine room | All scripts, server.js, configs, logs, skills, skills_inbox |
| `05_Campaign_Factory` | The assembly line | Research → Copy → Compliance stages |

**Rule:** nothing loose in the root except `MEMORY.md`, `USER.md`, `GROUNDING.md`, and the
`.bat` launchers. (Run `M7_TIDY.bat` to auto-clean stray files — see section 6.)

---

## 3. THE LAUNCHERS (your only buttons — double-click these)
| File | What it does | When |
| :--- | :--- | :--- |
| `RUN_M7_DASHBOARD.bat` | Starts engine + dashboard at localhost:3000 | Every work session |
| `HERMES_COMMAND_CENTER.bat` | Starts Hermes + engine + firewall together | When using Hermes |
| `INGEST_AND_INDEX.bat` | Files new skills/templates + rebuilds catalog | After dropping files in `skills_inbox` |
| `REGISTER_DAILY_SYNC.bat` | Schedules daily 9 AM auto-update | ONCE |
| `M7_DAILY_SYNC.bat` | The daily self-update (runs itself once scheduled) | Automatic |
| `M7_TIDY.bat` | Cleans loose root files into the right rooms | When the root looks messy |

---

## 4. WHAT'S DONE vs WHAT'S LEFT
**✅ DONE (verified):** 4-Fala folders · GROUNDING constitution · brand_firewall (green=0) ·
scoring engine · campaign factory · skill intake (9 skills, 351 templates) · server.js engine ·
dashboard with model fleet + telemetry + sparklines · Hermes skills + daemon · MCP registered ·
daily auto-sync · first campaign drafted (PAUSED in Outbox).

**🟡 LEFT FOR YOU (~20 min, one time):**
1. Do the Obsidian fix in section 1 (open app + re-add MCP).
2. Double-click `REGISTER_DAILY_SYNC.bat`.
3. Put real keys in `04_Tech_Lab\config\.env` (OpenRouter, ElevenLabs; Meta only when advertising).
4. Drag the `EMAI Starter Vault` folder into `03_Knowledge_Mat\`, then run `INGEST_AND_INDEX.bat`.
5. Review the campaign in `Outbox_Drafts\` and launch the Local Fan ad set ($250/week).

---

## 5. THE AI AGENTS (who does what)
| Agent | Job | You use it for |
| :--- | :--- | :--- |
| **Claude Code** | Builder/executor in the vault | "Do X to my files/scripts" (autonomous) |
| **Hermes** | 24/7 planner/orchestrator | Standing goals, scheduled loops |
| **Ollama** | Local private model | Offline drafting/scoring, no cloud |
| **NotebookLM** | Source-grounded research | Fact-checked research with citations |
| **Antigravity** | Gemini agent surface | Web sweeps, landing pages |
| **Paperclip** | Content multiplier | Turn 1 idea into many posts |

All of them obey `GROUNDING.md` and the **Outbox Shield** (drafts only; you publish).

---

## 6. CLEAN-UP PLAN (local + Google Drive)
- Run `M7_TIDY.bat` (section 3) to sweep loose root files into the right rooms.
- Google Drive mirrors the vault automatically — once local is tidy, Drive matches within minutes.
- Don't manually reorganize folders in Drive; always tidy locally and let it sync down.

---

## 7. THE DAILY RITUAL (Plan-Push-Play-Profit)
1. **Plan** — open dashboard (`RUN_M7_DASHBOARD.bat` → localhost:3000). Check telemetry + tasks.
2. **Push** — generate/refresh a campaign; it lands PAUSED in `Outbox_Drafts`.
3. **Play** — review, then YOU launch one ad set in Meta ($250/week cap).
4. **Profit** — track which avatar books CPPAs; double down on the winner (see `SPEND_CONTROL.md`).

---

## 8. THE NORTH STAR (read this when overwhelmed)
You have built the factory. The factory doesn't pay you — the roofs it books do. There will be a
new AI tool every week forever; you do NOT need them. **Freeze v1.0. Ship the campaign. Book CPPAs.**
Everything in this guide exists to serve that one outcome.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
