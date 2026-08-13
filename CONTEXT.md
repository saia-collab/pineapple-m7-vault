# CONTEXT.md — M7 Root Router (ICM Layer 1)
**"Where do I go?"** This file routes any AI agent to the right room. It stores almost nothing — it points. Read `CLAUDE.md` first (identity + brand law), then this, then the target folder's own `CONTEXT.md`.

> Full method: `01_Command_Center/M7_ICM_FOLDER_SOP.md`. Brand law is absolute (CPPA not "free", IKO not GAF, Navy/Gold/Cyan + zero green, no proverbs, The Pineapple Standard). Everything ships PAUSED to `Outbox_Drafts/`.

## Pick the room by the job
| If the job is… | Go to | Then read |
|---|---|---|
| Strategy, playbooks, brand rules, offers | **`01_Command_Center/`** | its `CONTEXT.md` + `Brand_DNA/` |
| Find a photo / video / drone shot / proof asset | **`02_Media_Vault/`** (read-only) | its `CONTEXT.md` (naming: `YEAR_MONTH_CAMPAIGN`) |
| Research → notes → JSON contracts → script drafts (Obsidian brain) | **`03_Knowledge_Mat/`** | its `CONTEXT.md` + the Map-of-Content index |
| Run a script (video render, scrape, Meta upload), configs, `.env` | **`04_Tech_Lab/`** | its `CONTEXT.md` (mechanical — no AI writing here) |
| Campaign builds / content factory | **`05_Campaign_Factory/`** | its files |
| Any finished draft to review | **`01_Command_Center/Outbox_Drafts/`** (PAUSED) | — |
| Prompts + which AI tab to use | **`01_Command_Center/M7_PROMPT_CONTROL_PANEL.md`** | — |
| Launchers / how to change models / log in | **`01_Command_Center/M7_MOBILE_HOWTO_AND_STATUS.md`** | — |

## Persistent state (read to resume without re-explaining)
- **`_memory/task_plan.md`** — current goals / blitz objectives
- **`_memory/progress.md`** — real-time state (where we left off)
- **`_memory/findings.md`** — intelligence log (scrapes, GSC, competitor gaps)
- **`_memory/decisions.md`** — strategic pivots + why

## The rule
Load only the room you're in. Don't read `02_Media_Vault` (39 GB) or `04_Tech_Lab` code just to write a caption in `01_Command_Center`. One agent, one room, the right file. Output of one room becomes input to the next via that room's `output/` or `Outbox_Drafts/`.

<!-- M7-FIREWALL-EXEMPT: governance-reference (ICM L1 router) -->
