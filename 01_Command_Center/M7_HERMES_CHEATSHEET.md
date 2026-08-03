---
type: hermes_cheatsheet
title: M7 Hermes Cheat Sheet (first-time + ecosystem)
status: active
last_updated: 2026-06-19
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🍍 M7 HERMES CHEAT SHEET

**What Hermes is:** your 24/7 orchestrator. It doesn't replace the other AIs — it *runs* them on
a schedule and keeps memory in your vault. Think: the manager who delegates to the specialists.

**Golden rule:** Hermes can draft, research, schedule, and loop — but **everything it produces
lands PAUSED in `01_Command_Center/Outbox_Drafts/`. You press publish.** (Outbox Shield.)

---

## FIRST-RUN SETUP (one time)
```
hermes memory setup        # point Hermes at the vault: C:\Pineapple Contractors M7
hermes model               # pick model: qwen3.6 or deepseek-v4-flash (64k context)
hermes config set model.context_length 65536   # if it warns about 32k/64k
```
- If using Ollama locally: make sure `ollama serve` is running (port 11434).
- MCP: Hermes reads your Obsidian vault via the Local REST API (http://127.0.0.1:27123).

## THE CORE COMMANDS (from your playbook)
| Command | What it does |
| :--- | :--- |
| `/goal "<objective>"` | Set a standing goal Hermes pursues across turns (autonomous loop) |
| `/goal pause` / `/goal resume` | Stop / restart the loop without losing the goal |
| `/subgoal "<text>"` | Add an acceptance criterion mid-run |
| `/loop 1d "<task>"` | Run a task on a schedule (e.g., daily) |
| `/compact` / `/clear` | Compress or wipe the working context |
| `/vault` | Force-sync the Obsidian memory layer |

---

## ▶ COPY-PASTE M7 GOALS (your actual business)
Paste any of these into Hermes. All respect the Outbox Shield.

**1. Review-request loop (highest ROI — protects your 209 reviews)**
```
/goal "Each day, read 04_Tech_Lab/logs for jobs marked Completed in the CRM. For each, draft the
same-day Google review-request text from 01_Command_Center/M7_LEAD_ENGINE.md, personalize with the
customer name, and save to 01_Command_Center/Outbox_Drafts/ as PAUSED. Do not send. List them for my approval."
```

**2. Daily morning briefing**
```
/goal "Every morning at 8am, parse the CRM Google_LSA_Leads tab + Attribution tab and write a
one-page briefing to 01_Command_Center/Outbox_Drafts/: new leads, leads not yet contacted (flag
any >5 min old), reviews to ask for today, and which avatar is winning. Ground in MASTER_PLAYBOOK.md."
```

**3. Weekly content batch (1-3-12 / 50-5-3)**
```
/goal "Each Monday, take the approved assets in 02_Media_Vault/04_READY_TO_POST and draft a week of
posts (3-4/platform) rotating Sale/Culture/Recruit per the Asset library. Run brand_firewall.py rules.
Save PAUSED to Outbox_Drafts. Never publish live."
```

**4. Lead scoring on new leads**
```
/goal "When a new lead is added to the CRM, run m7_scoring.py to score it, and if score >= 80 alert
me immediately with the speed-to-lead text ready to send."
```

---

## HOW THE ECOSYSTEM FITS (who does what)
| Tool | Role | Hermes uses it for |
| :--- | :--- | :--- |
| **NotebookLM** | Facts / source-grounded research (citations) | research briefs before drafting |
| **Gemini Gems / Notebooks** | Brand-voice style + execution | polished copy in your voice |
| **Ollama (local)** | Private, free local model | offline drafting/scoring, sensitive data |
| **Antigravity** | Gemini agent surface | web sweeps, landing-page formatting |
| **Claude Code** | Builder/coder | edits files/scripts in the vault |
| **Hermes** | Orchestrator (this sheet) | schedules + delegates to all of the above |
| **Dashboard** | Mission Control | see it all at localhost:3939 |

**The flow:** NotebookLM (facts) → Gemini Gem (style) → Hermes (assemble + schedule) →
brand_firewall (compliance) → Outbox_Drafts (PAUSED) → **you publish** → CRM tracks → double down.

---

## FIRST THING TO RUN TODAY
Start with **Goal #1 (review-request loop)** — it compounds your 5.0★ advantage and needs almost no input.
Watch it write a PAUSED draft, approve one, send it. That's your first Hermes win.

## TROUBLESHOOTING (from the playbook)
- "context window below 64k" → `hermes config set model.context_length 65536` or use deepseek-v4-flash.
- Hermes can't see the vault → confirm Obsidian is open + Local REST API on (port 27123) + key matches.
- Nothing should ever publish live — if a goal tries, that's a bug; keep delivery_state PAUSED.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
