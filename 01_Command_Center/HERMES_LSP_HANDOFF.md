---
type: handoff
title: Hermes Handoff — Location Service Pages (Near Me Pipeline, Corey Format)
status: active
last_updated: 2026-07-15
---

# 🤝 Hermes Handoff — Write the Location Service Pages

**Executor:** Hermes → Goal Mode (free, vault-aware). **One page per run** (avoids the
429 rate limit). After Hermes writes a page → push it as a WP draft (step 2).

## ▶️ STEP 1 — Paste into Hermes → Goal Mode (swap the [PAGE] each run)
```
caveman: Profile SEO. Use the Corey Haines 'copywriting' + 'ai-seo' skills at
03_Knowledge_Mat/corey_marketing_skills/skills/. Ground in
03_Knowledge_Mat/active_context/product_marketing.md and the Phase 1 intent map at
01_Command_Center/Outbox_Drafts/2026-07-14_Outbox_Phase1_IntentMap_LocalPM7.md.

Write ONE Location Service Page for: [PAGE: e.g. "roofer Starwood, Frisco TX" — slug /roofer-starwood-frisco-tx/].
Structure (Corey format):
- AEO 40-word hook in the FIRST paragraph (credential + area + service + CTA).
- H1 with the target keyword; 3-4 H2 sections; local landmarks + nearby neighborhoods.
- FAQ (5 Qs from the intent map PAA seed).
- CPPA call-to-action + phone (972) 928-0788.
BRAND LAW: CPPA (never "free"), IKO Certified (never GAF), The Pineapple Standard,
RCAT #03-0637, Navy #1A365D/Gold #FBC02D, ZERO green. No CTR manipulation, no fake data.
Save to 01_Command_Center/Outbox_Drafts/Website_Pages/[slug].md with frontmatter
(title: ..., meta: ...). PAUSED to Outbox for review.
```

## ▶️ STEP 2 — Push the finished page to WordPress (as DRAFT)
```
python 04_Tech_Lab/scripts/wp_publish.py 01_Command_Center/Outbox_Drafts/Website_Pages/[slug].md pages
```
→ appears in wp-admin → Pages → Drafts → you review + Publish.

## 🎯 Order to run (Tier-1 ELITE first, from the intent map)
1. /roofing-storm-restoration-frisco-tx/ (PILLAR)
2. /hail-damage-roof-repair-frisco-tx/
3. /roofer-starwood-frisco-tx/
4. /roofer-newman-village-frisco-tx/
5. /commercial-hail-damage-portfolio-frisco-tx/ (E5 — highest lead score)

Then Tier-2 (ZIP + service-modifier pages), then Tier-3 as blog content.

## ⚠️ Do NOT
- Run CTR/directions manipulation (GBP suspension risk).
- Pull live SERP/NWS data without your GO (intent map gate).
- Publish live — everything stays DRAFT until you approve.

<!-- M7-FIREWALL-EXEMPT: handoff -->
