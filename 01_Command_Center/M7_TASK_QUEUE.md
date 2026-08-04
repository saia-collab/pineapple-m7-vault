---
type: task_queue
title: M7 TASK QUEUE — the one place you paste work, the agents execute it
status: active
last_updated: 2026-07-05
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🗂️ M7 TASK QUEUE — paste a task here, an agent runs it (no human error)

> **How this works (the reliable rail):** you keep ONE list. An agent reads this file top-to-bottom,
> runs the next unchecked task **grounded on the Playbook**, writes the result **PAUSED to Outbox**,
> ticks the box, and logs it. You review in the dashboard and approve. Nothing publishes on its own.
>
> **Three ways to fire it — pick ONE and stick to it:**
> 1. **🌙 Hermes Goal Mode (best for overnight batches)** — dashboard → Hermes → **Goal Mode**, paste the
>    STANDING FIRE PROMPT below, walk away. It works the queue and drops drafts in Outbox.
> 2. **📋 Agent Kanban → "Dispatch now" (best for one-off copy-paste)** — dashboard → Kanban, drop ONE
>    task line into the New-task box, hit **Dispatch now**; the orchestrator decomposes + assigns agents.
> 3. **⌨️ Claude Code / Cowork** — paste the STANDING FIRE PROMPT into any agent chat.
>
> **The golden rule stays:** agents DRAFT to Outbox_Drafts; **only Saia publishes.**

---

## ▶️ STANDING FIRE PROMPT  (copy this once — it runs the whole queue)
```
Read 01_Command_Center/M7_TASK_QUEUE.md, 03_Knowledge_Mat/HERMES_PLAYBOOK.md, and
01_Command_Center/GROUNDING.md. Execute the NEXT unchecked task in the queue, following the Playbook
exactly: CPPA (never "free"), IKO (never "GAF"), Navy #1A365D + Gold #FBC02D + Cyan #00BFFF (zero green),
RCAT #03-0637, 972-928-0788. Self-critique the output to 9.5/10 vs the Elite Compliance rules, then run
python 04_Tech_Lab/scripts/brand_firewall.py --check on it. Write the result PAUSED to the Outbox path
named in the task. Tick the task's checkbox in this file, append one line to m7_execution_manifest.md and
03_Knowledge_Mat/log.md, then STOP (do not publish, do not spend, do not touch the next task unless I say
"continue"). If any required fact or variable is missing, ask me instead of inventing it.
```
> Add **"continue"** at the end if you want it to work several tasks in a row unattended (overnight).

---

## 📌 THIS MONTH'S QUEUE  (July 2026 — ordered by leverage; check off as done)

### FREE stack (Hermes / FCC / Grok — $0)
- [x] **SEO city pages — batch 1** → 6 AEO pages (Frisco, Lewisville, McKinney, Plano, Allen, The Colony) in `Outbox_Drafts/SEO_Posts/`. *(done 2026-07-05)*
- [x] **SEO city pages — batch 2** *(done 2026-07-05 — 7 pages: Prosper, Little Elm, Castle Hills, ZIPs 75033/75034/75035, Frisco hail-damage)* — `Draft AEO city pages for Prosper, Little Elm, Castle Hills + ZIP pages 75033/75034/75035 + a Frisco hail-damage page (roofing). Same AEO rules (40-word answer, RCAT+IKO, LocalBusiness+FAQ JSON-LD, CPPA CTA, proverb, zero green, never "free"). PAUSED to Outbox_Drafts/SEO_Posts/.`
- [x] **Weekly branded content** *(done 2026-07-06)* — `Read M7_EXECUTE.md. Draft this week: 8–12 branded captions (Authority/Proof/Heritage) + 6 repurposed video cuts + 2 GBP posts + 3 testimonial money-quotes. PAUSED to Outbox_Drafts/Content/. Firewall-checked.`
- [x] **1-3-12 Meta campaign brief** *(done 2026-07-06)* — `Read M7_INTEGRATED_CAMPAIGN.md. Draft the 1-3-12 brief: 3 ad sets (Local Fan · Culture Seeker · Founder's Circle) × 12 PACT creatives, $250/wk CBO, 1% Kill / 1.5% Scale rules. PAUSED to Outbox_Drafts/Campaigns/ — Saia launches in Meta.`
- [x] **Video + call scripts** *(done 2026-07-06)* — `From M7_CONTENT_FACTORY.md, write 5 50/5/3 video scripts + CARPARK call scripts + Lead Bridge SMS sequences. PAUSED to Outbox_Drafts/Scripts/.`
- [x] **Review-request texts** *(done 2026-07-06)* — `Read M7_LEAD_ENGINE.md. Draft this week's review-request texts for finished jobs. PAUSED to Outbox_Drafts/Reviews/.`

### HERO builds (Claude Fable 5 — 1 day, minimal spend — see M7_THIS_MONTH.md)
- [x] **Rebuild roofing website** *(done 2026-07-06 — 7 pages + CSS)* → `Outbox_Drafts/Website_Roofing/` (Fable Task 1)
- [x] **CPPA offer landing page** *(done 2026-07-06)* → `Outbox_Drafts/Landing_CPPA.html` (Fable Task 2)
- [x] **Restorations homepage** (dual-brand, never mix vocab) → `Outbox_Drafts/Website_Restorations/` (Fable Task 4)

> Each task above is already Playbook-grounded and Outbox-safe. To run one on the Kanban, paste just its
> back-tick prompt into the New-task box and hit **Dispatch now**.

---

## ➕ ADD A TASK (your format — keep it this simple)
```
- [ ] **Short name** — `Exact instruction. Where it saves (Outbox_Drafts/...). Any brand notes.`
```
That's it. Add the line, fire the STANDING FIRE PROMPT, done.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
