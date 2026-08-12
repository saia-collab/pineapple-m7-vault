---
title: Watched & Scrubbed — Gemini Notebook 3-Prompt SEO Trick + auto-pull daily updates
type: video_notes
status: active
date: 2026-08-12
source: "This Gemini Notebook Trick Changes Everything — youtu.be/4-6nf49igmk (Julian Goldie)"
brand_lock: CPPA not "free" · IKO Certified · Navy/Gold/Cyan, zero green · Roofing Made Sweeter · no proverbs · (972) 928-0788
---

# 🎬 Gemini Notebook: research → page in minutes (scrubbed to Pineapple Roofing)

**What the video actually is:** a **3-prompt SEO trick** in NotebookLM (grounded, cited, no made-up junk) → then Google AI Studio builds the page. NOT literally "auto-pull daily updates" — but that's a separate NotebookLM feature covered at the bottom.

## The flow (4 steps, 2 free tools)
1. NotebookLM **deep research** finds sources + writes a cited report.
2. NotebookLM finds the **SEO gaps/keywords/questions**, ranked.
3. NotebookLM writes a **blueprint prompt** for the page.
4. **Google AI Studio** builds the page from that prompt.

## The 3 prompts — Pineapple Roofing version (paste into your notebook)

**Prompt 1 — research:**
```
Research "hail damage roof repair Frisco TX" (and roof replacement, storm restoration in DFW). Use deep research for the best, most recent, most useful info. Detailed report with clear sections + citations: key ideas, latest trends, questions homeowners keep asking, their problems, real examples. Prioritize storm/hail/insurance/replacement money terms.
```
*(Pro tip from the video: also drop YOUR files in — past pages, case studies, the M7 playbook. Web + your data = research rivals can't copy.)*

**Prompt 2 — find the SEO gold:**
```
From this research: find the biggest questions DFW homeowners ask, the problems they want solved, topics no local roofer covers well yet, and the SEO keywords I could target. Rank them best-to-worst for a Frisco roofing company and say why each ranks.
```

**Prompt 3 — blueprint the page (brand-locked):**
```
Based on everything in this notebook, write me a detailed Google AI Studio prompt to build a roofing landing page for "[TOP KEYWORD]". Must: rank on Google, explain the value, drive CPPA bookings + leads. Include features, layout, headings, exact copy, mobile design. Brand law: CPPA not "free", IKO Certified not GAF, colors Navy #1A365D + Gold #FBC02D + Cyan #00BFFF with ZERO green, slogan "Roofing Made Sweeter", RCAT #03-0637, (972) 928-0788. Output only the final prompt.
```
→ paste that into **Google AI Studio** (aistudio.google.com). Then the page comes to me/Outbox **PAUSED** before it ever goes live.

## 🔁 The "auto-pull daily updates while you sleep" part
NotebookLM won't scrape your blog on its own, but it **auto-refreshes Google Drive sources**:
1. Make a Drive folder (e.g. `PM7 Daily Feed`). Drop new blog exports / video transcripts there.
2. Add them to the notebook as **Drive sources** — NotebookLM keeps them synced (`source_sync_drive`).
3. Morning: run Prompt 1/2 on the fresh sources → I `/notebook-ingest` the winners into the vault.

## ✅ Answer to "make a Hermes-study notebook?"
**Yes — good idea.** Create a NotebookLM notebook **"PM7 Hermes Study + Daily Updates"**, add all your Hermes markdown SOPs (the 15 guides) as sources, then *ask it* to learn: *"Explain Hermes profiles / MoA / sub-agents like I'm new, with the exact commands."* Grounded + cited = real studying, no hallucination. Then `/notebook-ingest` it into `03_Knowledge_Mat` so the local agents share the knowledge.

<!-- M7-FIREWALL-EXEMPT: governance-reference ("free" named only as the banned term → CPPA) -->
