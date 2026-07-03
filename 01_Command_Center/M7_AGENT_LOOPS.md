---
type: agent_loops_map
title: M7 Agent Loops — the control panel for every automation
status: active
last_updated: 2026-06-22
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🔁 M7 AGENT LOOPS — WHAT RUNS WITHOUT YOU PROMPTING

## What an "agent loop" is (plain English)
A normal prompt = you ask, the AI answers, done. You have to ask again next time.
An **agent loop** = a job that **fires on its own trigger** (a clock, or a change in your data),
does the work, and leaves the result waiting for you. **You stop being the trigger.**

A loop has three parts:
1. **Trigger** — what starts it (a time like "Monday 7am", or an event like "lead marked Denied").
2. **The job** — the steps it runs (read files → draft → firewall-check → save).
3. **The landing spot** — where the result goes. For us that's almost always
   `01_Command_Center/Outbox_Drafts/` as a **PAUSED draft** (Outbox Shield — you publish, not the bot).

**Why this is the whole point of M7:** your rules (CPPA, IKO, no green, phone, the avatars) live in
`GROUNDING.md` + the playbooks. Every loop reads those first. So the loop already knows your brand —
you never re-explain it. That's how you "don't have to prompt all the agents."

---

## TWO ENGINES RUN YOUR LOOPS
| Engine | What it is | When it runs | Needs |
|--------|-----------|--------------|-------|
| **Cowork Scheduled Tasks** (this Claude app) | jobs in `Scheduled/` that I run | when the **Claude desktop app is open** (catches up on next launch) | the app open |
| **Hermes skills** (`04_Tech_Lab/hermes_skills/`) | YAML jobs Hermes runs locally | when the **Hermes daemon is running** | Hermes + Ollama on |

Same idea, two runners. Cowork loops are great for anything touching Meta/Google/web.
Hermes loops are great for local file work and run even when this app is closed.

---

## YOUR LOOPS RIGHT NOW (live inventory)

### A. Cowork scheduled tasks (in `Scheduled/`)
| Loop | Trigger | What it does | Status |
|------|---------|--------------|--------|
| **weekly-social-captions** ⭐new | Mon 7:00 AM | Drafts 8 brand-compliant captions (3 pillars) → PAUSED to Outbox | ✅ ON |
| **pineapple-gbp-monday-draft** | Mon 8:00 AM | Drafts a Google Business Profile post, alerts you to paste it | ✅ ON |
| **pineapple-deal-resurrector** | 1st & 15th, 8 AM | Revives dead leads (Closed Lost) using storm + roof-age data → drafts | ✅ ON |
| pineapple-daily-performance-brief | Daily 6:00 AM | Ad spend + lead count vs 7-day avg, from new CRM | ✅ ON |
| pineapple-morning-handshake | Daily 7:30 AM | New-lead scan + storm weather brief, from new CRM | ✅ ON |
| pineapple-lead-enrichment | Daily 7:35 AM | Enriches new CRM leads (avatar + job-value band) | ✅ ON |
| pineapple-review-sweep | Daily 5:00 PM | Flags signed jobs to ask for reviews; queues testimonials | ✅ ON |
| pineapple-denial-sniper-monitor | 9 AM & 4 PM | Watches CRM for "Claim Denied" → drafts a Denial Sniper reply | ✅ ON |

### B. Hermes skills (in `04_Tech_Lab/hermes_skills/`)
| Loop | Trigger | What it does |
|------|---------|--------------|
| **review_request_loop** | Daily 18:00 | Drafts PAUSED review-request texts for the day's finished jobs |
| **weekly_review** | Mon 08:00 | "Track & double down" — which source signed jobs, 1% Kill / 1.5% Scale brief |
| **social_content_batch** | on call | Batch-drafts social content, firewall-checked, PAUSED |
| **generate_cppa_proposal** | on call | Drafts a CPPA proposal ($18K+ floor), PAUSED |
| **brand_compliance_check** | on call | Runs the firewall, returns PASS/FAIL |

### C. Always-on background loops (not scheduled — event-driven)
- **Brand Firewall `--watch`** — live-watches the 4-Fala rooms; any green or banned term fails instantly.
- **Campaign Factory pipeline** (`05_Campaign_Factory`): a 3-stage loop with `CONTEXT.md` gates —
  `10_Research_Stage → 20_Copy_Drafting → 30_Compliance_Audit`. Each artifact is wrapped in the
  Cross-Agent JSON envelope (see `CROSS_AGENT_PROTOCOL.md`) so Claude Code, Hermes, and NotebookLM
  hand work to each other **without you in the middle** — and nothing advances unless the firewall passes.
- **Daily Drive sync** (`M7_DAILY_SYNC.bat`, registered once) — keeps the vault settled.

---

## ✅ AIRTABLE RETIRED — all loops now read the new CRM
As of 2026-06-22, **Airtable is decommissioned.** All 5 previously-stale loops were **rewired to the
new M7 CRM** (`02_Workspaces/Pineapple_Mana_Master_CRM_M7.xlsx` — tabs: Google_LSA_Leads,
Master_Lead_Tracker, Attribution, Meta_Ads, Assets) and **turned back on**. Every one is draft-only and
lands in `Outbox_Drafts` — nothing publishes or edits the CRM without you. The denial monitor was also
dialed back from hourly to twice daily (9 AM / 4 PM) to cut noise.

> **First-run tip:** any loop that touches a live connector (e.g. Meta Ads, weather) may pause on a
> permission prompt the first time. Open the **Scheduled** panel → **Run now** on each once to pre-approve
> its tools; after that they run untouched. Loops that only read the CRM file need no approval.

---

## WHERE CLAUDE & CLAUDE CODE FIT (do they loop?)
- **Claude (this app)** — runs the **Cowork scheduled loops** above on a clock. This is your hands-free layer.
- **Claude Code** — the **builder**, not a clock-loop. It runs when you (or Hermes via `delegate_task`)
  hand it a job — big builds, vault audits, multi-file refactors. Its "loop" is the Campaign Factory
  pipeline: it picks up a stage, does research/drafting, writes the JSON envelope, passes it on.
- **Hermes** — the **orchestrator**. It runs its own scheduled skills AND can dispatch Claude Code,
  Ollama, etc. If you want one brain to route everything, Hermes is it.

**So: you do NOT prompt each agent every time.** You set the loop once (or I do), the agent reads your
grounding files, and it produces PAUSED drafts on schedule. Your only standing jobs stay human:
**answer leads in 5 min, approve/post the drafts, authorize ad spend.**

---

## THE BENEFIT (why loops beat prompting)
- **Consistency** — the content/reviews/briefs happen even on your busy days. No willpower required.
- **No re-explaining** — brand rules are read from files every run; the firewall guarantees compliance.
- **Speed** — Monday morning you already have captions, a GBP post, and a decision brief waiting.
- **Safety** — every loop lands PAUSED. Nothing publishes or spends without you. (Outbox Shield.)
- **Leverage** — this is how one person runs the marketing of a team.

## HOW TO ADD A NEW LOOP (just tell me)
Say: *"Make a loop that every [when] does [what], saved to Outbox."* I'll wire it, firewall it, and
it shows up in your `Scheduled/` panel. You review the first run and approve its tools once.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
