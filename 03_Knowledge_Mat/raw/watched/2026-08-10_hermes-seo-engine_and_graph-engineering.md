---
title: Watched & Scrubbed — Hermes 24/7 Traffic Engine + Graph Engineering (Julian Goldie)
type: video_notes
status: active
date: 2026-08-10
sources:
  - "The Hermes 24/7 Traffic Engine — https://www.youtube.com/watch?v=QOivt0EGrpQ (~13 min)"
  - "Graph Engineering / Agent Assembly Line — https://youtu.be/3Km65xyDh3A (~15 min)"
captured_by: claude-watch pipeline (captions -> scrubbed to M7 branding)
note: Sales-pitch/community-plug content stripped. Kept the mechanics + how they apply to the M7 playbook.
---

# 🎬 Video 1 — The Hermes 24/7 Traffic Engine (SEO on autopilot)

**Thesis:** one Hermes agent runs the full SEO loop — finds keywords, writes content, builds links, and reviews its own work — around the clock. Proof shown: several small sites (DR ~20) taken from 0 → 34–325 organic clicks/day, beating DR-50 sites.

## The 4 parts of the engine
1. **Keywords — from your own GSC data.** Plug Hermes into **Google Search Console API** and pull the keywords where you get **impressions but no clicks**. That's Google saying *"I'd rank you higher if you gave me a proper page."* No guessing, no research — the gaps are already in your data.
2. **Content — one keyword + one REAL case study → 5 articles.** The case study matters most: every fact comes from your real jobs/results/numbers = **"information gain"** Google rewards (vs generic fluff it now ignores). Output: 5 unique articles (different titles/angles/FAQs) across sites, **indexed within the hour** by pinging an indexing API (Indexional). AI never invents — it pulls from your source of truth.
3. **Backlinks — the part nobody automates.** Hunter API (find blogs + emails) + Google Workspace (send). Hermes finds niche blogs, personalizes outreach, sends, and manages the replies/follow-ups. Only **editorial, manually-placed** links count (not directories) — they're an exclusive moat competitors can't copy. Bonus: those brand mentions **train the AI** to recommend you in AI Overviews.
4. **The self-upgrade loop.** End-of-batch check: it reviews what worked, proposes edits to its **own instructions**, and (with cross-session memory) gets sharper each cycle. Compounds: more content → more rankings → more GSC data → more keywords → repeat.

**Honest timeline:** 3–6 months, with a flat "sandbox" period first (flat, flat, flat → up). AI content ranks *if* built on real case studies; Google punishes empty fluff, not AI.

## 🍍 How this maps to the M7 playbook (you already have the inputs)
| Engine part | You already have | Action |
|---|---|---|
| Keywords (impressions-no-clicks) | **GSC is connected** (OpenSEO Striking-Distance 100: grapevine roofing company, roof replacement southlake…) | Feed the striking-distance list to the `seo` engine |
| Real case study | **39GB media + real jobs + 430 5-star reviews** | Use a real Frisco/Southlake job as the case study per page |
| 5 articles / multi-site | roofingllc.com + contractors.com + restorations.com | One striking-distance keyword → a city page + supporting posts |
| Backlink outreach | Hermes `leads`/outreach engine | Niche outreach — but every send stays **PAUSED (Outbox Shield)** |
| Self-upgrade loop | Hermes memory + Goal Mode | Nightly review goal already in Master SOP |
> Brand law still governs every page: **CPPA** (never "free"), **IKO**, RCAT #03-0637, Navy/Gold/Cyan, PAUSED to Outbox.

---

# 🎬 Video 2 — Graph Engineering (the Agent Assembly Line)

**Thesis:** stop using *one* agent for a whole task (a "loop" that suffers **context rot** — the desk gets buried, quality drops). Instead run a **team of one-job agents in parallel** — a graph / assembly line. Nodes = agents, edges = handoffs.

## The mechanics that matter
- **3 wins:** speed (4 agents at once beat 1 doing 4 jobs), quality (clean context per agent), and **debuggability** (you see exactly which station broke).
- **Cost reality:** multi-agent uses ~**15× the tokens** of a chat. Two levers cut it: **prompt caching** (shared instructions cached → a ~$10 run drops to ~$1) and **model-per-agent** (cheap/fast models for simple stations, your best model only where brains are needed).
- **2 gotchas:** (1) **concurrency ceiling** ~16 parallel agents in Claude Code (tied to CPU cores) — the rest queue; (2) **pacing** — fire in small groups (~6 at a time) or you trip provider rate limits and the whole batch dies.
- **You don't write the workflow** — Claude Code generates it ("dynamic workflows" is Anthropic's own term; it's in Claude Code now). You describe the goal + what "good" looks like.
- **The one station where cheap wrecks everything = the CHECKER.** Two rules: (1) the agent that *built* the work must **never** check it — use a **fresh agent with zero memory** (clean eyes); (2) put your **best model** on the checker. Anthropic stacks checkers (code-review + simplify + verify + design = 4 angles). A clean report from a weak checker proves nothing.
- **When to build a graph (3 signals):** context is bloating + quality slipping · the work is high-stakes/client-facing · speed matters (daily job). Otherwise a simple loop is fine.
- **First move (10 min):** draw a process as boxes; for each arrow ask *"does the next step need the last step's output?"* No → they run in **parallel**. Hand the drawing to Claude Code.

## 🍍 How this maps to the M7 playbook
- **Your Agent Kanban IS this** — dispatcher → worker → reviewer is the assembly line. The SEO research suite you already have (keyword-map / technical-audit / performance / geo) was exactly a 4-station parallel run.
- **Adopt the CHECKER rule:** a *separate, fresh* reviewer agent must brand-check every draft (against CPPA/IKO/zero-green) before it lands in the Outbox — never the agent that wrote it. That's your Outbox Shield done right.
- **Pace + cache:** run Kanban jobs in small waves (~6), use free/cheap models (Hermes gpt-5.6-sol, Groq, Cerebras) for the grunt stations and a strong model only on the final brand/quality checker.


<!-- M7-FIREWALL-EXEMPT: governance-reference (internal SEO notes; "free" = free/organic traffic concept, not marketing copy) -->
