---
type: execution_guide
title: M7 Execution To-Do — Run It Yourself in Local Studio
status: active
last_updated: 2026-07-15
---

# ✅ M7 Execution To-Do (Your Runbook)

Start everything: `LAUNCH_ALL.bat` → work at **http://localhost:3000**.
Everything you make lands PAUSED in `Outbox_Drafts/` → you approve → it goes live.

---

## 🟢 WHAT'S LIVE NOW (done)
- WordPress site (pineappleroofingllc.com): 9 pages + 3 blogs published, menu tabs added, Blog live
- Tracking plugins installed: **Site Kit** (GSC+GA4) + **PixelYourSite** (Meta Pixel)
- Vault: Operator's Manual · Marketing SOP · Ad Architect · Prompts & Gems · Corey Haines skills · 3 NotebookLM notebooks

---

## 🔴 DO FIRST (only YOU can — logins, ~15 min total)
- [ ] **Connect Site Kit** → wp-admin → Site Kit → Sign in with Google → turns on rankings/traffic tracking
- [ ] **Add Meta Pixel** → wp-admin → PixelYourSite → paste Pixel ID `2545389655696737`
- [ ] **Fix "FREE"** on the homepage hero → Elementor → change to "Complimentary Quote" (2-min text edit)
- [ ] **Change your WordPress password** (it was texted) → Users → Profile

---

## 🔁 WEEKLY RHYTHM (the whole growth engine)
- **Mon:** OpenSEO → pick 1 keyword → Hermes writes the page → review → publish (auto-drafts to WP)
- **Tue/Thu:** post 1 GBP update (drafts in `Outbox_Drafts/Content/`)
- **After each job:** send a review-request text
- **Fri:** check Site Kit (GSC) rankings + LSA dashboard (leads, disputes)
- **Always:** answer LSA/GBP leads within 5 minutes

---

## 📋 READY-TO-PASTE PROMPTS (Hermes → Goal Mode)

**Rewrite the old Scorpion blogs (fresh, brand-legal, Corey-skill quality):**
```
caveman: Use the Corey Haines 'copywriting' + 'ai-seo' skills at 03_Knowledge_Mat/corey_marketing_skills/skills/.
Take the topic of this old post: "[paste title, e.g. Understanding the Insurance Claim Process]".
Write a BRAND-NEW 900-word article on it (do NOT copy) for pineappleroofingllc.com.
Ground it in 03_Knowledge_Mat/active_context/product_marketing.md. Direct answer in sentence 1, 3-4 H2s, FAQ, CPPA CTA.
BRAND LAW: CPPA (never "free"), IKO Certified (never GAF), The Pineapple Standard, RCAT #03-0637, zero green.
Save to Outbox_Drafts/SEO_Posts/. PAUSED.
```

**Write a city page (feeds SEO):**
```
caveman: Use Corey 'competitors' + 'ai-seo' skills. Write a local landing page for "roofing contractor [Frisco] TX".
Hook, services, why-us (RCAT #03-0637, IKO, insurance help), FAQ, CPPA CTA. Brand law enforced. Save to Outbox_Drafts/Website_Pages/. PAUSED.
```

**Weekly GBP posts + review texts:**
```
caveman: Profile marketing. Read HERMES_PLAYBOOK.md. Write 5 GBP posts + 4 review-request texts for this week. CPPA/IKO/zero green. Save to Outbox_Drafts/Content/. PAUSED.
```

**Publish an approved draft to WordPress:** (I/you run)
`python 04_Tech_Lab/scripts/wp_publish.py <file.md> posts` → appears as WP draft → you Publish.

---

## 🎛️ FEATURE → TASK MAP (from the Operator's Manual)
| Task | Local Studio feature |
|---|---|
| What to rank for | OpenSEO → Search Performance |
| Write content | Hermes → Goal Mode (free) |
| Reels from media | Video Editor tab |
| Post reels/social | Blotato |
| Learn your system | The 3 NotebookLM notebooks |

---

## 📚 FEED YOUR 3 NOTEBOOKS (do this to make them smarter)
**PM7 SEO Playbook** — add: your GSC exports (weekly), the Corey Haines skill files, competitor URLs, your keyword list.
**PM7 Brand & Content** — add: BRAND_KIT, TATAFU_BRAND, your best past posts, the Ad Architect, customer reviews.
**PM7 Ops & SOP** — add: the Operator's Manual, Marketing SOP, this to-do, your weekly rhythm.
> Tip: in each notebook, click **Audio Overview** → it turns your own SOPs into a podcast you can learn while driving between jobs.
> Add sources anytime: `nlm source add <notebook-id> --file/--url/--youtube` (IDs in project memory).

---

## 🎯 YOUR FOCUS (per your plan)
1. Content for all social platforms (via Blotato + your 39GB in `01_READY_TO_POST`)
2. Learn the Local Studio using the Operator's Manual + the 3 notebooks
3. Run the weekly rhythm above

**The system is built. Now it's about running it weekly. You've got this.** 🍍

<!-- M7-FIREWALL-EXEMPT: execution-guide -->
