---
title: M7 AGENT OS EXECUTION MASTER — Consolidated (de-duped from 6 Gem outputs)
type: hermes_learnable_sop
status: active
for: Hermes (/learn → run) · Claude · Codex
date: 2026-07-24
note: This REPLACES the six overlapping Gem drafts. Real vault paths only.
---

# 🎛️ M7 AGENT OS EXECUTION MASTER

> One master, de-duplicated from all the Gem/Skool outputs. Everything below uses your **real**
> vault paths. Outbox Shield: all output PAUSED in `01_Command_Center/Outbox_Drafts/`.

## 0. PATH TRANSLATION (the Gems used fantasy folders — here's the real map)
| Gem's made-up path | YOUR real path |
|---|---|
| `01_Fala_Tactical_Outbox/` | `01_Command_Center/Outbox_Drafts/` |
| `02_Fala_Memory_Galaxy/System_Skills/` | `03_Knowledge_Mat/active_context/skills/` |
| `03_Fala_Knowledge_Mat/` | `03_Knowledge_Mat/` |
| `04_Fala_Execution_Engine/` | `04_Tech_Lab/scripts/` |
| `01_READY_TO_POST/` | `02_Media_Vault/` (approved) + Outbox_Drafts (pending) |

## 1. WHAT'S ALREADY DONE (don't rebuild these — they exist)
- **Brand firewall** → `04_Tech_Lab/scripts/brand_firewall.py` ✅
- **Brand law, lexicon, palette, trust bar** → `MASTER_PLAYBOOK.md` ✅
- **Storm response, lead scoring, CARPARK, speed-to-lead** → `MASTER_PLAYBOOK.md` ✅
- **SEO daily routine** → `active_context/M7_SEO_DAILY_SOP.md` ✅
- **Goldie Omnipresence Stack** → `00_Atlas/2026-07-24_SOP_Goldie_Omnipresence_Stack.md` ✅
- **WordPress publish** → `04_Tech_Lab/scripts/wp_publish.py` ✅

## 2. WHAT'S GENUINELY NEW (worth adding — the unique parts of the Gems)
### A. The Hermes `/learn` → skill.md pipeline
Concept: point Hermes at a URL/video/PDF → it distills → writes a reusable `skill.md` →
runs it later without re-explaining. Real command in your build:
```
/learn 03_Knowledge_Mat/active_context/<file>.md
```
Skills land in `03_Knowledge_Mat/active_context/skills/`. (The Gem's dedup Python is optional
polish — not required to start.)

### B. The 3-Lane Agent Routing Matrix (the ONE genuinely useful new framework)
| Lane | Engine | Does | Billing |
|---|---|---|---|
| **BUILD** | Codex / GPT-5.6 (Sol) | code, schema, dashboards, site builds | ChatGPT OAuth (unmetered) |
| **ORCHESTRATE** | Claude Code (me) | brand copy, firewall, strategy, QC | session-paced |
| **BULK** | Hermes Goal Mode | content batches, SEO drafts, GBP posts | free/local models |
Rule: BUILD drafts big → I verify + brand-check → Hermes runs volume → you approve Outbox.

### C. The Kanban Swarm (build a 50-page SEO cluster)
Trigger in the Agentic OS Agent-Kanban: give it a county seed ("Collin County"), the Planner
breaks it into city×service pages, Builder writes each, Reviewer checks, output lands PAUSED.

## 3. THE CONSOLIDATED WEEKLY CADENCE (all 6 Gems agreed on this — merged)
| Day | Action |
|---|---|
| **Mon** | OpenSEO striking-distance pull → pick top 3 keywords |
| **Tue** | Upload real job photos to GBP (toward 100-image rule) |
| **Wed** | Review-request sweep (positive auto-thanks; negative → private draft) |
| **Thu** | 1 GBP post + reply to reviews by neighborhood name |
| **Fri** | Speed-to-lead audit (<5 min) + GSC indexing check |
| **Storm** | Activate 72-hour storm response (already in MASTER_PLAYBOOK) |

## 4. THE PROMPT PACK (7 reusable prompts from the Gems — captured)
Feynman Reteacher · First-Principles CRO Architect · Active-Recall Compliance Coach ·
Spaced-Repetition Scheduler · Knowledge Summarizer · Business Acceleration Roadmap ·
Weakness Diagnostician. → saved full text to `03_Knowledge_Mat/active_context/prompts/` on request.

## 5. HOW TO MAKE IT RUN AUTOMATICALLY (the honest checklist)
1. **Hermes needs its model key** — the OpenRouter key in `~/.hermes/profiles/<active>/.env`. Without it, nothing auto-runs. (This is the standing blocker.)
2. **`/learn` this master** in Hermes so it holds the whole system.
3. **Set ONE daily goal/loop** (the Mon–Fri cadence above) in Hermes Goal Mode.
4. Hermes drafts → Outbox PAUSED → you approve. That's the autonomous loop.

> The Gem scripts (`daily_hermes_runner.py`, `graphify-cli`, Hicksfield MCP) reference tools that
> may not be installed here. Don't run them blind — start with steps 1-4 above, which use what you
> already have. We add the fancy harnesses later, verified, one at a time.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
