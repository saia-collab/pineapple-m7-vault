---
title: M7 OPERATING MANUAL — How To Actually Run This
status: reference (not outbound content — internal operator guide)
author: Claude Code (acting CEO / VP Onboarding)
date: 2026-07-23
grounds_against: MASTER_PLAYBOOK.md · SOP_Paperclip_Hermes_Empire.md · CLAUDE.md
---

# 🍍 M7 OPERATING MANUAL — How To Actually Run This

You built a whole AI company. This is the manual for **driving** it. No new tools, no
new spend — just *how and when to press each button you already own.*

Read time: 8 minutes. Then you can run the machine.

---

## 0. THE ONE LOOP (memorize this, everything else is detail)

> **Capture → Vault → Orchestrate (Hermes) → Execute (agents) → Firewall → Outbox (PAUSED) → You say GO → Track → Repeat.**

Everything in your system is one of those 7 steps. When you're lost, ask "which step am I on?"

The golden rule that never changes: **nothing goes live until YOU drag it live.** Every
tool below stops at the Outbox. That's the Outbox Shield. It's a feature, not a bug — it
means you can let the agents run hard without fear.

---

## 1. THE THREE BOARDS — what each is, WHEN to open it

Your Agentic OS (localhost:3000) has three "rooms." People get stuck because they look
identical. They are not. Here's the plain difference:

| Board | URL | What it is | Open it WHEN… |
|---|---|---|---|
| **Paperclip** | `localhost:3000/paperclip` | **The HQ / org chart.** Shows your AI company: CEO → CMO/CTO/COO → Marketing, SEO, Lead Engine, Ops. Plus Builds, Issues, Costs. | You want to *see the team*, check what's building, or check what it's costing. This is the "control room," not where you type tasks. |
| **Self-Kanban** | `localhost:3000/kanban` | **The general to-do engine.** Drop ANY goal into TRIAGE; Hermes decomposes it into steps and assigns them. Columns: TRIAGE → TODO → READY → RUNNING → BLOCKED → DONE. | You have *any* task ("write 3 Grapevine posts", "audit my Meta ads"). This is your everyday board. |
| **Agent-Kanban** | `localhost:3000/agent-kanban` | **The SEO article factory.** A Planner → Builder → Reviewer team that writes and **ships SEO articles live to pineapplecontractors.com**. Columns: BACKLOG → BUILDING → REVIEW → DONE. | You specifically want *website/SEO content produced*. It's wired straight to your site. |

### The mental model
- **Paperclip = the office** (who works here, what's on fire, what it costs).
- **Self-Kanban = your inbox/whiteboard** (drop a job, watch it get done).
- **Agent-Kanban = the printing press** (feed a keyword, out comes a published article).

You will live in **Self-Kanban** day to day. You'll open **Agent-Kanban** on SEO days.
You'll glance at **Paperclip** to check health and cost.

---

## 2. HERMES — the brain that already knows your business

**Status: already loaded.** Hermes has memorized the Master Playbook (CPPA, no-green,
RCAT #03-0637, Outbox Shield, the 4-Fala map, the $18k floor, speed-to-lead). You do NOT
need to teach it again. Proof: `03_Knowledge_Mat/HERMES_PLAYBOOK.md` + all 4 profiles.

### How to make Hermes EXECUTE (two modes)
1. **Goal Mode** — you give it an outcome, it plans + does the whole thing.
   - In the Self-Kanban, type a goal into the box and hit Add → it lands in TRIAGE → the
     orchestrator breaks it into cards and runs them.
   - Example goal to paste:
     > "Write 3 brand-compliant social posts for the Grapevine hail keyword, CPPA offer,
     > (972) 928-0788, zero green, land them PAUSED in Outbox_Drafts."
2. **Chat Mode** — you talk to it like a coworker in the Hermes dashboard (localhost:9119)
   for one-off questions or edits.

### Which profile to pick (the dropdown)
- **marketing** → ads, campaigns, offers
- **content** → posts, articles, captions, video scripts
- **roofing** → technical roofing / claim / estimate questions
- **main** → anything general / orchestration

### The one thing to watch
Hermes needs a **model** selected. If it says "Failed to fetch" or "402," switch the model
dropdown to a **local** one (free) — that's the fix we already put in. Cloud models cost
money and rate-limit.

---

## 3. CODEX / CLAUDE CODE / OTHER CLIs — who does what

You asked "codex or other CLI." Here's the honest routing (from your own notes):

| Tool | Best at | Use it for |
|---|---|---|
| **Claude Code** (me) | Building, fixing, file/code work, orchestrating | The heavy lifting — I built your videos, schema, pages. Ask me to *do* things. |
| **Hermes** | 24/7 goal loops, content batches, business memory | Set-and-forget content jobs; the marketing brain. |
| **Codex / GPT (ChatGPT)** | Big one-shot builds when it has quota | It built your 33-page SEO migration package. Good for bulk generation *outside* the vault, then hand the ZIP to me/Hermes to import. |
| **OpenClaw** | Browser automation | When something needs clicking through a website. |

**Rule of thumb:** ChatGPT/Codex *drafts big things*, I *wire them into the vault and verify*,
Hermes *runs them on a loop*, you *approve the Outbox*.

---

## 4. THE CHATGPT SEO/WEBSITE BUILD — what it is and how to ship it

Your screenshot = a **WordPress migration package**: 33 HTML pages (7 core + 13 services +
13 cities), 33 Elementor blocks, 37 verified 301 redirects, a click-by-click Better Search
Replace + Elementor guide. This is a *big deal* — it's your whole site restructure, done.

**It is NOT in your vault yet — it's still in ChatGPT/Drive.** Here's the deploy path:

1. **Download the complete ZIP** from that ChatGPT page to your machine.
2. **Drop it in the vault** at `02_Workspaces/` (I'll import + brand-firewall-scan it — the
   ChatGPT note even says "verified reviews and video reels marked for replacement"; I make
   sure zero green / zero banned terms before anything ships).
3. **Two placeholders stay blank until you fill them** (ChatGPT flagged these correctly):
   the Apps Script `/exec` endpoint and the GA4 Measurement ID. These are yours to paste.
4. **Publish order matters:** publish each page FIRST, *then* import its redirect. The old
   URLs must route through the server where the Redirection plugin lives.
5. I verify every live page (schema + stars + phone + license), same as I did for your 13
   live pages.

> **Say the word and I'll write the exact step-by-step deploy checklist** once the ZIP is in
> the vault. Don't run the redirects blind — that's the one step that can break live URLs.

---

## 5. YOUR FIRST WEEK — concrete, do-this-in-order

Stop reading theory. Here's the actual on-ramp:

**Day 1 — Prove the loop with something safe.**
- Open Self-Kanban → paste ONE goal (e.g. "3 Grapevine posts, PAUSED in Outbox").
- Watch it flow TRIAGE → DONE. Open the Outbox, read the drafts. That's the whole system in
  10 minutes. Now you trust it.

**Day 2 — Ship the two videos.**
- The hail + Allen videos are rendered. Drop them into Blotato with the captions we wrote,
  schedule 12 months out (safety rule), drag one to "Today" when you're ready.

**Day 3 — Fire the SEO factory.**
- Open Agent-Kanban → give it a keyword cluster (e.g. "flat roofing allen tx"). Planner →
  Builder → Reviewer produces the article. Review before it ships.

**Day 4 — Deploy the ChatGPT site build.**
- Download the ZIP → drop in `02_Workspaces/` → I import, scan, and give you the publish
  checklist.

**Day 5 — Set the recurring loop.**
- Give Hermes a `/loop` goal (e.g. "every morning, draft one city post to the Outbox"). Now
  content compounds while you sleep.

**Every day:** open the Outbox each morning, approve or kill. That's your only mandatory job.
The machine does the rest.

---

## 6. CHEAT SHEET (pin this)

**URLs**
- Agentic OS: `localhost:3000` → `/paperclip` (HQ) · `/kanban` (tasks) · `/agent-kanban` (SEO)
- Hermes dashboard: `localhost:9119`

**The rule that governs everything**
- Everything lands PAUSED in `01_Command_Center/Outbox_Drafts/`. Nothing ships without your GO.

**Brand law (baked into every agent already)**
- CPPA (never "free") · IKO Certified (never "GAF") · zero green · Navy #1A365D + Gold #FBC02D
- RCAT #03-0637 · Since 2005 · (972) 928-0788 · $18k+ floor · 5-min speed-to-lead

**If something breaks**
- Hermes "Failed to fetch"/402 → switch to a LOCAL model in the dropdown (free).
- Disk full / render fails → Downloads is 36GB; clear it. npm cache already cleared.
- Not sure who does a task → Section 3 routing table.

**Who to ask**
- Want it *built or fixed*? → me (Claude Code).
- Want it *run on a loop*? → Hermes.
- Want to *see the company/costs*? → Paperclip.

---

---

# PART 2 — EVERY MODULE IN YOUR AGENTIC OS (the full map)

Your OS has ~25 modules. **You do not need most of them yet.** Below is what each one is,
grouped by job, so you stop feeling lost. At the end: the 5 that actually matter this month.

## A. THE BRAIN (memory & research)
| Module | What it is | Use it WHEN |
|---|---|---|
| **Notebook** (`/notebook`) | Your **NotebookLM library** — 100 notebooks (PM7 Ops, Brand, SEO Mastery, Hormozi…), synced to Obsidian. Turns sources into answers, audio overviews, reports. | You want to *research or synthesize* from your own sources before acting. This is where knowledge goes IN. |
| **Memory** (`/memory`) | The **shared memory store** all agents read. What Hermes "knows." | To check or edit what the agents remember about your business. |

## B. THE ORCHESTRATION (who does the work)
| Module | What it is | Use it WHEN |
|---|---|---|
| **Paperclip** | HQ / org chart / costs | See the team & health |
| **Self-Kanban** | Drop a goal → Hermes decomposes | **Daily** — any task |
| **Agent-Kanban** | SEO article factory → ships to site | SEO content days |
| **AI Agent Mastermind** (`/room`) | **Group chat with ALL your models** (Claude, Hermes, Gemini, Codex, OpenClaw, GLM). They read your vault, reply in turn, tag `@claude` for one. | You want *opinions/strategy* — "what should I build next?" A boardroom, not an executor. |
| **Loop** (`/loop`) | **Loop Engineering** — you define "done," a builder acts, a free judge grades it 0–100 adversarially, it repeats until it passes. You stop being the loop. | You want *one thing built to a standard* without babysitting (a landing page, a calculator, a piece of copy). |
| **Pipeline** | Chains steps into an automated flow | Advanced — later |

## C. THE AGENTS (the actual models behind the work)
Claude (build/fix — me) · Hermes (orchestrate + memory) · OpenClaw (browser clicking) ·
Codex (GPT bulk builds) · GLM 5.2 / Kimi / Hy3 (cheaper coders) · **Antigravity** (Gemini
CLI successor, multi-agent harness). You pick these inside the modules; you rarely open them alone.

## D. THE STUDIOS (make media)
| Module | What it makes | Needs |
|---|---|---|
| **Video / The Video Director** | Topic → full video (researches, scripts, HeyGen presenter, b-roll, edits to MP4) | A **HeyGen avatar** selected + HeyGen key |
| **Thumbnails** | Upload one → gpt-image-2 makes better versions, learns your style | image model key |
| **Video Editor / OpenMontage / Music** | Cut, montage, score | — |
| **Open Design / Game Studio / App Lab / Hy3 Coder / GPT 5.6 Code** | Design, games, apps, code, live-preview builds | model keys |

> Note: **HyperFrames** (the tool I used for your 2 hail/flat videos) is *separate* from the
> Video Director module — HyperFrames renders locally with **no key**. That's why your videos
> shipped and the in-app Video Director shows "Avatar failed" (it needs a HeyGen avatar). For
> branded, on-message videos, **keep using HyperFrames via me.** The Director is for
> talking-head/presenter videos later.

## THE CHAIN — "Notebook → Hermes → execute → shared memory → real life"
This is the sentence you asked about. Here's the literal flow:

1. **Notebook / vault** = knowledge goes in (your SOPs, brand, SEO research).
2. **Shared Memory** = Hermes reads that vault through MCP, so it answers *as your business*, not a blank AI.
3. **You give a goal** (Self-Kanban / Loop / a chat).
4. **Hermes orchestrates → agents execute** (Claude builds, OpenClaw clicks, etc.).
5. **Brand Firewall** scans it (no green, no banned words).
6. **Outbox (PAUSED)** — it waits.
7. **You approve → it goes to real life** (Blotato post, live page, sent email).
8. The result is **written back to memory** → the OS gets smarter about your business.

That loop — vault in, approved work out, learnings back in — *is* "shared memory into real life."

## ⚠️ WHAT'S BROKEN RIGHT NOW (from your screenshots) — and the exact fix
All three trace to **one missing key + two uninstalled optional tools.** Facts, no fluff:

| Screen | Error | What it needs |
|---|---|---|
| **AI Agent Mastermind** | "No OpenRouter key in the active Hermes profile" — Claude & Hermes can't reply | An **OpenRouter API key** pasted into the active Hermes profile's `.env` (`~/.hermes/profiles/<active>/.env` → `OPENROUTER_API_KEY=`). *You* paste it (I don't handle your keys). Then the room works. |
| **Antigravity** | "antigravity is not installed or not configured" | The **Antigravity CLI** installed + `AGENTIC_OS_ANTIGRAVITY_BIN` set. Optional — skip unless you want Gemini's multi-agent harness. |
| **Video Director** | "Avatar failed — no avatar selected" | A **HeyGen avatar** picked + HeyGen key. Optional — you already make videos via HyperFrames (me), no key. |

**The only one worth fixing now = the OpenRouter key** (unlocks the Mastermind room). The other
two are optional studios you don't need this month.

## 🎯 THE 80/20 — use THESE 5, ignore the other 20 for now
As your VP, here's where to actually spend attention:
1. **Self-Kanban** — your daily "drop a goal" board.
2. **Agent-Kanban** — ship SEO articles to the site.
3. **Notebook** — research/synthesize from your own sources.
4. **Me (Claude)** — build/fix/deploy (videos, the site migration, schema).
5. **Blotato + the Outbox** — approve & schedule what the machine makes.

Everything else (Loop, Mastermind, Video Director, Game Studio, Hy3, Antigravity…) is a
*nice-to-have you grow into.* Don't let 25 shiny modules stall you. Five is a business.

---

# PART 3 — THE SEO SITE MIGRATION (imported & verified 2026-07-23)
**Location:** `02_Workspaces/2026-07-23_SEO_Site_Migration/pineapple-migration-build/`
**Firewall:** ✅ zero green · zero banned terms · RCAT/phone/CPPA on every page.

**Contents:** 33 pages (7 core, 13 services, 13 cities) + 33 Elementor blocks + redirect CSVs
+ click-by-click WordPress guide. Meta Pixel `2545389655696737` preserved.

### Deploy order (from the build's own README — do NOT reorder step 5/6)
1. **Fill 2 placeholders first:** the Apps Script `/exec` endpoint (form target) and the GA4 ID (`G-XXXXXXX`). *You* provide these.
2. **Replace review/video placeholders** with verified Pineapple sources (build marks them).
3. **Per page:** WordPress → new page → Layout = **Elementor Canvas** → drag one **HTML** widget → paste the matching file from `elementor-blocks/`. (Canvas stops a double header/footer.)
4. **Publish every destination page FIRST.**
5. **Only then** import `redirection-plugin-import.csv` at Tools → Redirection → Import. Format verified: `source,target,regex,http code,type` (correct 5-column).
6. **Test old URLs** → confirm a single `301` hop (never 302 / 404 / homepage catch-all).

### ⚠️ THE ONE THING TO CONFIRM BEFORE REDIRECTS (I won't guess this)
The redirect CSV sends old paths **to `pineappleroofingllc.com`** URLs. Two things must be true
or you'll break live links:
- **Which domain is the real destination** — your Playbook lists the flagship as
  `pineapplecontractors.com`, but the live pages I built are on `pineappleroofingllc.com`. The
  CSV targets `pineappleroofingllc.com`. **Confirm that's the domain you're keeping.**
- **The Redirection plugin must run on the server that actually receives the old-domain traffic.**
  If the old domain is still on Scorpion/another host, a plugin on WordPress alone won't catch it —
  the old host needs the same 301 map, or point the old domain at WordPress first.

Get me a yes on the domain and where the old site is hosted, and I'll finalize the exact redirect
plan. Everything else (pages, blocks, schema) is ready to publish.

---

Ko e hala 'o e fononga ko e faka'apa'apa. *(The path of the journey is respect.)*

<!-- M7-FIREWALL-EXEMPT: internal-operator-guide -->
