---
INTENT: THE single router for the whole Pineapple M7 system. One front door. Every tab, agent, and SELF tab reads its workflow from here. Copy-paste ready.
type: router
status: CANONICAL — this is the ONE file. If it's not here, it doesn't run.
owner: JR. Moeakiola (Saia)
updated: 2026-07-02
---

# 🍍 PINEAPPLE M7 — COMMAND CENTER OS (The One Brain)

> **ADHD rule: you only ever open THIS file.** It tells you where to go and gives you the exact words to paste. Everything else is a library you never have to dig through.

## 🧭 The 3 files that run everything
1. **[AGENT_READ_ME_FIRST.md](AGENT_READ_ME_FIRST.md)** — the LAWS (brand, CPPA, IKO, zero green, Outbox Shield). Never breaks.
2. **[SHARED_MEMORY.md](SHARED_MEMORY.md)** — the LIVE BRAIN (what's done, what's next). Updated every day by the loop.
3. **THIS FILE (COMMAND_CENTER_OS.md)** — the ROUTER (where to go + what to paste).

Plus the **[DAILY_LOOP.md](DAILY_LOOP.md)** — the 3-minute ritual so nothing gets forgotten.

---

## 🔁 THE NON-STOP LOOP (how nothing gets forgotten)
Every agent, every session, every tab follows the same 4 beats:
1. **READ** → AGENT_READ_ME_FIRST + SHARED_MEMORY (know the laws + the state).
2. **DO** → the workflow for the tab you're in (below).
3. **STAGE** → output lands PAUSED in `01_Command_Center/Outbox_Drafts/`.
4. **LOG** → one line to `03_Knowledge_Mat/log.md` + update SHARED_MEMORY "Current State."
> Same 4 beats everywhere. That's the loop. Read → Do → Stage → Log.

---

## 📋 THE ROUTER — every tab & agent, with copy-paste

### 🖥️ WORKSPACE tabs
| Tab | What it's for | 📋 Paste this to start | Source SOP |
|-----|---------------|------------------------|-----------|
| **Mission Control** | Home / status | "Give me today's Pineapple status: what's in the Outbox, what's next, any blockers." | M7_MASTER_SOP.md |
| **Paperclip** | Your AI company (org chart, tasks) | "Open the Pineapple company. Show the org chart and any tasks waiting on me." | 2026-06-18_SOP_Paperclip_Hermes_Empire.md |
| **AI Agent Mastermind** | Multi-agent debate on a decision | "Run a Research·Writer·Editor·Judge pass on: [my question]. Stay in Pineapple brand." | M7_AGENT_LOOPS.md |
| **Agent Kanban** | The 5-lane board | "Show my Kanban. Move nothing without my GO. Flag anything stuck." | M7_Agent_Kanban.md |
| **Memory** | Search all notes | "Search my vault for [topic] and summarise the latest, ignore old duplicates." | SHARED_MEMORY.md |

### ⚙️ SELF tabs
| Tab | What it's for | 📋 Paste this to start | Source SOP |
|-----|---------------|------------------------|-----------|
| **SEO** | Roofing/Restoration blog drafts | "Run the SEO skill for keyword: [keyword]. Draft to Outbox, PAUSED. Pineapple voice, author JR. Moeakiola." | .claude/skills/blog-post.md |
| **Loop** | Auto Builder→Judge quality loop | "Loop on [task] until a Judge scores it 90+. Show me each round." | M7_AGENT_LOOPS.md |
| **Video** | Video/reel scripts | "Script a 50-sec reel on [topic]. Hook in first 0.5s. Navy/Gold, zero green, CPPA CTA. Draft only." | M7_CONTENT_FACTORY.md |
| **Thumbnails** | Thumbnail concepts | "3 thumbnail concepts for [topic]. Navy #1A365D + Gold #FBC02D only. No green." | M7_CONTENT_FACTORY.md |
| **Music** | Background tracks | "Instrumental for a roofing testimonial reel, ~30s, confident, no lyrics." | M7_CONTENT_FACTORY.md |
| **Notebook** | Deep research (NotebookLM) | "Research [topic] in NotebookLM, pull the 5 key facts, cite sources." | 2026-06-18_SOP_Gemini_NotebookLM_SOURCE.md |
| **Kanban** | Task board (SELF) | "Add [task] to the right lane. Nothing ships without my GO." | M7_Agent_Kanban.md |

### 🤖 AGENT tabs
| Agent | When to use | 📋 Paste this to start | Source |
|-------|-------------|------------------------|--------|
| **Claude** | Building, coding, writing | "Read AGENT_READ_ME_FIRST + SHARED_MEMORY, then: [task]. Stage output PAUSED, log it." | CLAUDE.md |
| **Hermes** | Multi-step jobs w/ tools | `hermes chat --profile roofing` → "[task]. Follow M7 rules. Draft only." | M7_HERMES_START_HERE.md |
| **OpenClaw** | Browser tasks | "Open [site], pull [data], report back. Never publish/send." | ARCHITECTURE_MCP_MAP.md |

### 🏢 PAPERCLIP agents (standing orders)
| Agent | Standing order |
|-------|----------------|
| **M7 CEO** | Route work to CMO/CTO/COO. Nothing publishes without Saia GO. |
| **CMO → Marketing / SEO** | Draft roofing content to Outbox. CPPA, IKO, zero green. |
| **COO → Lead Engine / Ops** | Speed-to-lead 5 min. Brand-firewall every output. |
| **CTO** | Keep dashboard, Paperclip, Hermes, SEO pipeline running. |

---

## 🗃️ THE LIBRARY (you never open this — the router points to the right one)
- **Laws:** AGENT_READ_ME_FIRST.md · CLAUDE.md (constitution)
- **Money/Brand:** MASTER_PLAYBOOK.md · M7_HOW_WE_MAKE_MONEY.md · M7_LEAD_ENGINE.md
- **Content:** M7_CONTENT_FACTORY.md · M7_INTEGRATED_CAMPAIGN.md
- **Ops:** M7_MASTER_SOP.md · SOP_DAILY_LAUNCH.md · M7_OPERATING_RHYTHM.md
- **Everything else:** 65+ files in 01_Command_Center + 1,157 in 00_Atlas — **mostly daily duplicates. Flagged for cleanup (see below).**

> ⚠️ **Cleanup pending your GO:** 00_Atlas has ~1,157 files that are the same SOPs re-saved daily. I can archive the old dated copies to `_Archive/` and keep one canonical each — cutting the mess ~80% without deleting anything. Say "clean the Atlas" and I'll do it.

---

*Ko e hala 'o e fononga ko e faka'apa'apa — the path of the journey is respect.* 🌺
