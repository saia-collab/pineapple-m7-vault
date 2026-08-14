---
type: studio_tab_gallery
title: M7 STUDIO TAB GALLERY — which AI tab does what + a wall of DONE tasks (with screenshots)
status: active — living doc. Drop a screenshot under each task as you complete it.
date: 2026-08-14
brand_lock: CPPA · IKO · Navy/Gold/Cyan · zero green · Outbox Shield
---

# 🍍 M7 STUDIO TAB GALLERY
Two jobs: **(A)** tell you *which tab to open* for each task, and **(B)** be your **wall of DONE** — every finished task with the screenshot of the AI feature that made it. Screenshots live in `Agentic OS/_screenshots/`; drop one under each task as you go.

---

## ❓ YOUR QUESTION FIRST: "which Claude chat?"
You have **two things that both run Claude**, and they're for different jobs:

| Tab | What it is | Use it for |
|---|---|---|
| **Claude** (orange) | Direct Claude Code CLI stream, **auto-logs to your Obsidian vault**. Reads your brand law. | **Brand-locked words + building/saving files into the vault** — GBP posts, review replies, SEO page copy, the landing-page copy, "commit and push." **This is your main chat.** |
| **Hermes** (SEO pipeline) | Multi-model agent gateway (profiles like *muse*); powers the green **SEO Content Pipeline** tab. Can *use* Claude as its model. | **Bulk/orchestrated SEO** — keyword → 5 articles → deploy. The assembly line, not the hand-work. |

**Rule of thumb:** anything a customer will read, or anything that must obey brand law → **Claude tab**. A batch of SEO articles from a keyword → **Hermes / SEO Content Pipeline**.

---

## 🎨 FOR THE LANDING PAGES SPECIFICALLY (your Scorpion problem)
The agency built ugly green "FREE" pages. Here's how the studio builds better ones that match your template:

| Step | Tab | What you do |
|---|---|---|
| 1. Get the brand-safe copy | already done | `Outbox_Drafts/Landing_Pages/M7_LANDING_PAGE_BUILD_KIT.md` — scrubbed copy + avatars for all 3 pages |
| 2. **Build the page** | **OpenDesign** (1st choice) | Paste the build prompt from the Kit §3. It outputs one HTML landing page, navy/gold/cyan, no green, no "free." |
| 2-alt | **Antigravity** or **Google AI Studio** | Same paste prompt works in either — pick whichever you like the look of. |
| 3. Polish / brand-lock the words | **Claude tab** | "Read the Kit, check this HTML against brand law, fix any green or 'free' or 'GAF'." |
| 4. Save | **Claude tab** | "Save to Outbox_Drafts/Landing_Pages/ and commit and push." |

> **Why not just let the agency do it?** You saw the result — green hero, "$20,000," "Get My FREE Quote." The Kit + these tabs give you a **brand-perfect** page in minutes, then your brother just publishes it.

**Avatars you're targeting** (full detail in the Kit): Storm/Insurance = Female 35–54 · Roof-Plan/Retail = All 35–44 · Metal/Premium = Owners 40–60 · Metal/Commercial = property managers & HOAs on LinkedIn · (optional) Emergency = active-leak, all ages.

---

## 🗺️ THE FULL TAB MAP — what each studio feature is for
| Tab | Best task | Output lands in |
|---|---|---|
| **Claude** | Brand-locked copy, page building, vault edits, commit | vault / Outbox |
| **Hermes → SEO Content Pipeline** | Keyword → 5 SEO articles → deploy | `Outbox_Drafts/SEO/` |
| **OpenDesign** | Landing pages, graphics, designed HTML | `Outbox_Drafts/Landing_Pages/` |
| **Antigravity** | Multi-agent builds; `/teamwork-preview` drafts a specialist team | vault |
| **Notebook** (NotebookLM) | Study your 100 notebooks, audio overviews, research | reference |
| **Kanban / Agent Kanban** | Drop a task → orchestrator decomposes + assigns to agents | board |
| **Pipeline** ("Inbox → Shipped") | Capture an idea → agents plan → you approve once → built | `Agentic OS/Pipeline/` |
| **Video / OpenMontage / Video Editor** | Repurpose job footage into reels | `Outbox_Drafts/Content/` |
| **Music / Thumbnails / Game Studio / App Lab** | Supporting media + experiments | — |
| **Free Claude Code / Free AI Coder** | Zero-cost drafts (Groq) when you don't need brand-perfect | vault |
| **Memory / Mission Control** | What the agents remember; system status | — |

---

## 🖼️ THE WALL OF DONE — finished tasks + their screenshots
> Add a screenshot: save it to `Agentic OS/_screenshots/` and the `![[...]]` line below will show it in Obsidian. Filenames suggested per row.

### ✅ SEO — 3 city pages drafted (Frisco · Allen · Grapevine)
- **Tab:** Hermes / SEO Content Pipeline → Deploy
- **Output:** `Outbox_Drafts/SEO/2026-08-10_SEO_*` (PAUSED)
- **Screenshot slot:** `![[Agentic OS/_screenshots/done_seo_pipeline_deploy.png]]`

### ✅ Landing Page Build Kit — Scorpion brief scrubbed to brand (3 pages + avatars + build prompt)
- **Tab:** Claude
- **Output:** `Outbox_Drafts/Landing_Pages/M7_LANDING_PAGE_BUILD_KIT.md`
- **Screenshot slot:** `![[Agentic OS/_screenshots/done_landing_page_kit.png]]`

### ✅ Kanban — Collin County roofing cluster (McKinney/Allen/Plano briefs)
- **Tab:** Kanban (DONE column)
- **Screenshot slot:** `![[Agentic OS/_screenshots/done_kanban_collin_cluster.png]]`

### ✅ Pipeline — "Frisco hail-season CPPA push" captured + planned
- **Tab:** Pipeline (Inbox → Shipped)
- **Screenshot slot:** `![[Agentic OS/_screenshots/done_pipeline_cppa_push.png]]`

### ⬜ Landing page HTML built (do this next)
- **Tab:** OpenDesign (paste Kit §3 prompt)
- **When done:** save the HTML to `Outbox_Drafts/Landing_Pages/`, screenshot the rendered page →
- **Screenshot slot:** `![[Agentic OS/_screenshots/done_openDesign_roof_check_lp.png]]`

### ⬜ GBP post from this week's job (The Colony / Plano / metal)
- **Tab:** Claude → `/gbp-post`
- **Screenshot slot:** `![[Agentic OS/_screenshots/done_gbp_post.png]]`

---

## ▶️ ADD A NEW "DONE" IN 3 STEPS
1. Finish a task in any tab → it lands PAUSED in `Outbox_Drafts/`.
2. Screenshot the tab that made it → save to `Agentic OS/_screenshots/`.
3. In the Claude tab: *"Add a DONE row to M7_STUDIO_TAB_GALLERY.md for [task], tab [name], output [path], screenshot [filename]."* → then *"commit and push."*

Your gallery grows itself, and GitHub keeps it forever.

<!-- M7-FIREWALL-EXEMPT: gallery governance-reference (documents banned agency terms to contrast the scrub) -->
