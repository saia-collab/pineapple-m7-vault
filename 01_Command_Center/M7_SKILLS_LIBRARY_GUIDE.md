---
title: M7 Skills & Plugins Library — what's here, how to use, when to access
type: reference
status: active
date: 2026-08-07
note: Cloning = downloading only (safe). INSTALLING/running a third-party skill = review first.
---

# 🧰 M7 Skills & Plugins Library

You now have **three** skill libraries in the vault. This guide says what each thing is, when to reach for it, and — most importantly — **which FREE local tool can do a task so you don't burn Claude tokens.**

| Library | Where | What it is |
|---|---|---|
| **Single Brain skills** | `04_Tech_Lab/vendor/ai-marketing-skills/` | 25 marketing skills (seo-ops, conversion-ops, growth-engine…) — the executable engine behind your Single Brain playbook |
| **Blotato content pack** | `04_Tech_Lab/skills/Blotato_Marketing/` | 7 social-content skills that feed your Blotato scheduler ✅ **new today** |
| **Playbook resources** | `04_Tech_Lab/playbook_resources/` | 10 cloned Claude plugins/tools (memory, routing, design, browser) ✅ **new today** |

---

## 1) 🍍 Blotato content pack (7 skills) — your social engine, ready now
Extracted to `04_Tech_Lab/skills/Blotato_Marketing/blotato-content-pack/`. These are **safe** (they only use Read/Write/Edit — no code execution) and they're the fastest win here.

| Skill | What it does | When to use |
|---|---|---|
| **brand-brief** | Captures your business voice once → `brand-brief.md` every other skill reads | ⭐ **Run this FIRST** — pairs perfectly with Naa Sione's brand doc |
| **post-writer** | Writes platform-native posts from your brief | daily/weekly content |
| **content-coach** | Coaches angles/ideas from your real jobs | when you're stuck for ideas |
| **viral-hooks** | Generates scroll-stopping hooks | every post's first line |
| **post-grader** | Scores a draft before it goes out | QC before Blotato |
| **repurpose** | 1 video/blog → many posts | the 39GB media engine |
| **post-scheduler** | Queues posts to Blotato | after you approve |

> **How to use one:** in the Claude tab (or ask me), say *"Use the Blotato post-writer skill to draft 3 Frisco storm-season posts from brand-brief.md."* It reads the SKILL.md and follows it. Output lands PAUSED.

---

## 2) 🔌 Playbook resources (10 cloned) — power-ups (review before installing)
Cloned to `04_Tech_Lab/playbook_resources/`. **Cloning just downloaded them — nothing is running.** Two are from trusted vendors; the rest are third-party (fine to read/learn from; **review before you INSTALL or run their scripts**).

| Repo | What it is | Trust | When you'd use it |
|---|---|---|---|
| **claude-plugins-official** | Anthropic's official plugin directory | ✅ Anthropic | browse for vetted plugins |
| **playwright-cli** | Microsoft browser-automation CLI | ✅ Microsoft | auto-fill/test/scrape a site |
| **claude-mem** | Persistent memory for Claude Code | ⚠️ 3rd-party | if you want cross-session memory beyond the vault |
| **headroom** | Manages context so you don't hit token limits | ⚠️ 3rd-party | directly relevant to your token question |
| **OmniRoute** | Route across many AI models from one place | ⚠️ 3rd-party | you already have an `omniroute` Hermes profile |
| **obsidian-second-brain** | Connects Claude to an Obsidian vault | ⚠️ 3rd-party | you already run Obsidian — could deepen it |
| **task-observer** | Tracks tasks/progress ("one skill to rule them all") | ⚠️ 3rd-party | oversight of long agent runs |
| **ponytail** | Claude Code plugin (read its README first) | ⚠️ 3rd-party | review to decide |
| **impeccable** | Beautiful-UI design skill (impeccable.style) | ⚠️ 3rd-party | polishing landing pages/tools |
| **skill-ui** | Generate UI components | ⚠️ 3rd-party | building tool front-ends |

**Failed to clone (logged in `clone_errors.txt`):** `code-review-plugin` (it's a subfolder URL, not a repo — **and you already have `/code-review` + `/security-review` built into Claude Code**) and `ui-ux-pro-max` (repo moved/removed).

> 🔒 **Safety rule:** most third-party repos ship `.sh`/hook scripts. Reading them is safe; **running their installers is not automatic** — ask me to review one before you enable it.

---

## 3) 💸 THE TOKEN-SAVER ROUTING — do this when my tokens run low
**Principle: use Claude (me) for judgment, strategy, brand, and orchestration. Offload the mechanical work to the FREE local tools.** Here's who does what:

| The task | Do it with (FREE, no Claude tokens) | Not this |
|---|---|---|
| **Clone GitHub repos / run git** | **opencode Terminal** or your **Antigravity IDE terminal** — it's just git | ~~ask me~~ (today's clone could've run there free) |
| **Build a tool / calculator / UI** | **Hy3 Coder · Muse Code · opencode** (free models) | ~~me~~ |
| **Draft an SEO page** | **Hermes `seo` profile** (free gpt-5.6-sol) | ~~me~~ |
| **Bulk captions / social posts** | **Hermes `content`** + Blotato pack | ~~me~~ |
| **Research / summarize a big doc** | **Notebook (NotebookLM)** tab | ~~me~~ |
| **Multi-step build (research→build→QA)** | **Agent Kanban** (decomposes + assigns) | ~~me~~ |
| **Schedule social posts** | **Blotato** (MCP) | ~~me~~ |
| **Brand QC / firewall a draft** | **Claude tab** + `brand_firewall.py` | — |
| **Strategy · conflicts · what-to-do-next** | ✅ **ME (Claude Code)** — this is my job | free tools |

> **Rule of thumb:** if a task is *"run this command / build this file / draft this page,"* a free local tool can do it. If it's *"decide, verify, or connect the dots,"* that's me. When you see my token warning: **switch execution to opencode/Hy3/Hermes and keep me for the calls that matter.**

---

## 4) "I want to… → open this"
- **…start posting** → Blotato `brand-brief` then `post-writer` → Blotato
- **…clone/install a repo** → opencode Terminal (free) — paste the playbook, it runs git itself
- **…build a free tool** → Hy3 Coder (you already built the roof calculator here)
- **…write city pages** → Hermes `seo` profile
- **…not hit token limits** → review `headroom`; and offload per the table above


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
