---
title: M7 Studio Playground — example prompts per feature + Cowork handoff
type: reference
status: active
date: 2026-08-06
note: Everything lands PAUSED in Outbox_Drafts/. Brand law always on.
---

# 🎮 M7 STUDIO PLAYGROUND — things to try on each tab

Open the tab, paste the example, watch it work. Start with the ⭐ ones.

## Build / code tabs
- ⭐ **opencode / jcode** (free): *"Build a single-page ROI calculator: homeowner enters roof age + sq ft, it estimates replacement urgency. Navy #1A365D + Gold #FBC02D, zero green."*
- **GPT 5.6 Code / Codex**: *"Generate LocalBusiness + RoofingContractor JSON-LD schema for Pineapple Roofing (RCAT #03-0637, IKO Certified, Frisco TX, (972) 928-0788)."*
- **Muse Code**: *"A slick animated 'Storm Damage? Book your CPPA' hero section, single HTML file, Navy/Gold."*
- **Hy3 / DeepSeek / GLM / Kimi**: same prompt on different brains — compare speed/quality.

## SEO tabs
- ⭐ **SEO → Research**: *"Keyword + market map for 'hail damage roof repair Frisco TX' — primary + supporting keywords, competitor pages, fan-out questions."*
- **SEO → Parasite**: pick a keyword you already rank for → get an X thread + a Reel script + a YouTube Short angle.
- **SEO Office** (:3000): click **Add a Site** → paste `https://pineappleroofingllc.com` → it scaffolds a client vault and bootstraps keywords/competitors.
- **Agent Kanban**: type *"Build a 5-page service-area cluster for Collin County roofing"* → watch Planner → Builder → Reviewer (lands PAUSED).

## Media tabs
- ⭐ **Higgsfield** (after `hermes -p main mcp login higgsfield`): *"3 before/after hail-damage roof images, drone angle, Navy/Gold overlay 'Hidden Roof Damage? Book Your CPPA'."* (shows credit cost first — you confirm)
- **Video / OpenMontage**: *"30s 50/5/3 reel: 0–5s hook 'Your roof survived the storm — did it?', credential card at the end (RCAT #03-0637 · IKO · 972-928-0788)."*
- **Thumbnails**: *"6 thumbnail concepts for 'Frisco Hail Roof Inspection', bold Navy/Gold, faceless."*
- **Music / Game Studio**: just play — *"a 10-second upbeat jingle"* / *"a tiny pineapple-catching browser game."*

## Research / memory / councils
- ⭐ **Notebook (NotebookLM)**: open **PM7 SEO Mastery (300 sources)** → Chat → *"Extract the top 10 local-SEO moves for a DFW roofer as a checklist."*
- **Memory**: search *"CPPA"* or *"Hormozi offer"* — pulls from your vault + Omi.
- **Fusion / Sakana Fugu**: *"Should we lead with insurance-deadline or heritage messaging in Frisco? Debate and give a verdict."*
- **Loop**: *"Loop until done: a Frisco storm-restoration landing page that passes the brand firewall (0 green, CPPA, RCAT)."*
- **App Lab**: try **Chat with any Webpage** on a competitor's site.

## Hermes (switch persona in the profile bar)
- ⭐ **`seo` profile**: *"Draft one optimized page for 'flat roofing allen tx' (pos 9). AEO first 40 words, IKO, RCAT #03-0637, PAUSED to Outbox."*
- **`marketing` profile**: *"Build a Grand Slam Offer for our CPPA using the Hormozi framework."*
- **`content` profile**: *"Turn the Metal vs Shingle blog into 5 GBP posts + 3 Reels captions."*
- Switch brains free: `/model gpt-5.6-sol` or `/model cohere/north-mini-code:free`.

---

# ☁️ COWORK HANDOFF — generate the Master SOP in the cloud + push to GitHub

Paste this into **Cowork** (or any cloud Claude with repo access to `pineapple-m7-vault`):

```
You are working in the Pineapple Contractors M7 vault (GitHub repo pineapple-m7-vault).
Read these and consolidate them into ONE master SOP:
  01_Command_Center/M7_MASTER_SOP_STUDIO_DAILY_30DAY.md
  01_Command_Center/M7_MASTER_SOP_Command_Deck.md
  01_Command_Center/M7_HORMOZI_PLAYBOOK.md
  03_Knowledge_Mat/HERMES_PLAYBOOK.md
  01_Command_Center/M7_HERMES_AGENT_CHATS.md
  CLAUDE MOBILE/  (mobile sync + snapshot)

Produce 01_Command_Center/M7_MASTER_SOP_v3.md that:
  1. Maps every Studio tab -> task -> exact paste-in prompt.
  2. Assigns each Hermes profile its job + Goal Mode daily/weekly/nightly.
  3. Consolidates mobile + desktop + local-computer into one flow (Part 7).
  4. Includes the 30-day gameplan.
  5. Enforces M7 brand law: CPPA (never "free"), IKO (never GAF), Full Restoration Coverage
     (never "$0 down"), The Pineapple Standard, RCAT #03-0637, Navy #1A365D + Gold #FBC02D +
     Cyan #00BFFF, ZERO green, Outbox Shield (everything PAUSED).

Do not publish anything. Save the file PAUSED, run brand_firewall.py --check on it,
then git add + commit "Master SOP v3 (cowork)" + git push origin main.
Give me a 5-bullet summary of what you consolidated.
```

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
