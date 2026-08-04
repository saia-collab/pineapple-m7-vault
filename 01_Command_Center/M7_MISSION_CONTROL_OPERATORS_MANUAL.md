---
type: operators_manual
title: M7 Mission Control — Operator's Manual (What Does What)
status: active
last_updated: 2026-07-14
---

# 🎛️ M7 Mission Control — Operator's Manual

**The problem this solves:** you have a lot of tabs and agents and don't know which
one does which job. This is the map. Find your task on the left → use the tool on the
right. Start everything with `LAUNCH_ALL.bat`, work at **http://localhost:3000**.

---

## 🎯 "I want to..." → Use this

| I want to... | Use this in Mission Control | Cost | How |
|---|---|---|---|
| **Find what to rank for** | **OpenSEO → Search Performance** | free | It shows your live Google keywords + "striking distance" (pos 5–20). Pick high-impression ones. |
| **Write a blog post / page** | **Hermes → Goal Mode** (or ask me) | free | Paste a goal ("write a blog on X, save to Outbox"). Lands in Outbox_Drafts. |
| **Post the blog to the site** | **WordPress** (roofingllc) | free | Paste the draft in wp-admin, or auto-draft via `wp_publish.py` (needs app password). |
| **Write GBP / social posts** | **Hermes** or your Outbox batches | free | Drafts already in `Outbox_Drafts/Content/`. Post to GBP / schedule via Blotato. |
| **Turn a job video into a reel** | **Video Editor** tab | free | Upload clip → pick "Tighten + captions" → download `final.mp4`. |
| **Post reels to social** | **Blotato** (connected accounts) | your plan | One clip → IG/TikTok/FB/YouTube at once, scheduled. |
| **Track my rankings** | **OpenSEO → Search Performance** | free | Watch positions climb weekly. |
| **Learn SEO / feed training** | **NotebookLM SEO tab** (see below) | free | Load Goldie's SOP + videos; agents draw from it. |
| **Voice assistant (Jarvis)** | **Hermes voice tab** | free | Realtime OFF + Live ON (browser voice). See `M7_JARVIS_VOICE.md`. |
| **Fix content that keeps failing** | route Hermes → **OmniRoute** | free | 90+ free models, fallback (Hermes has a slash-name bug — pending fix). |
| **Reconnect Google Search Console** | `GSC_Connect.bat` | free | See `GSC_SETUP.md`. |

---

## 🤖 The agents (which "brain" to use)
- **Hermes → Goal Mode** ⭐ — your workhorse. Reads your vault, writes SOPs/content/blogs, runs in the background. **Use this for 90% of tasks.**
- **Claude / me** — planning, harder writing, code, when Hermes stalls.
- **OmniRoute** — a gateway (not an agent): gives the others 90+ free models with fallback so they stop hitting rate limits.
- **Free Claude Code / Hy3 / OpenClaw / Codex / GLM / Grok** — alternate coding brains; optional, ignore until you need one.

**Rule of thumb:** vault/content/SEO work → **Hermes Goal Mode**. Everything lands PAUSED in **Outbox_Drafts/** for your approval (Outbox Shield). Nothing goes live without your GO.

---

## 📚 The SEO system (Julian Goldie stack) — how to run it
Your Goldie SEO SOP (30-day plan + 100+ prompts) lives in the vault:
`EXCTRACT 23rd May_ Hermes Agent SEO SOP AND THE.md` → move it into
`03_Knowledge_Mat/` so agents treat it as the source of truth.

**The daily loop (simple version):**
1. **Extract** — put SEO training/notes into a **NotebookLM notebook** (or straight into `03_Knowledge_Mat/`).
2. **Feed** — Hermes reads `03_Knowledge_Mat/` as shared memory.
3. **Execute** — give Hermes a keyword + a Goldie prompt → it drafts the page → Outbox.
4. **Approve & post** — you review, publish to WordPress.
5. **Track** — OpenSEO Search Performance shows the climb.

**"Best way to extract & update daily":** keep ONE folder — `03_Knowledge_Mat/active_context/` — as the live brain. Drop new SEO notes, GSC exports, and case studies there. Hermes always reads from it. Update that folder = update the whole system. No re-uploading everywhere.

---

## ⚙️ Advanced (later, optional)
- **n8n WordPress auto-poster** (the JSON you shared): fully automates keyword→article→WP draft→SEO meta. Powerful, but needs n8n + API keys wired. **Skip until the basics are humming** — `wp_publish.py` + Hermes covers you now.
- **NotebookLM → Agentic OS pipeline** (Goldie architecture): the "extract → 03_Knowledge_Mat → Hermes" flow above is the practical version of it.

---

## 🗓️ Your actual weekly rhythm (this is all you need)
- **Mon:** OpenSEO → pick 1 keyword → Hermes writes the page → post to WordPress
- **Tue/Thu:** post 1 GBP update (drafts in Outbox)
- **After each job:** send a review-request text
- **Fri:** check OpenSEO rankings + LSA dashboard (leads, disputes)
- **Always:** answer LSA/GBP leads within 5 minutes

That's the system. You don't need every tab — you need **OpenSEO → Hermes → WordPress → GBP**, and the discipline to run it weekly.

<!-- M7-FIREWALL-EXEMPT: operators-manual -->
