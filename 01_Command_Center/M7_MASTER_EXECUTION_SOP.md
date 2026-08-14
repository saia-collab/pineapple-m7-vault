---
type: master_execution_sop
title: M7 MASTER EXECUTION SOP — one plan to launch the machine (strategy → draft → launch → track)
status: active
date: 2026-08-13
supersedes_index: M7_DAILY_LEAD_SOP · M7_VA_TASK_HANDOFF · CODEX WordPress AI Bridge SOP · M7_SEO_DIGITAL_MASTER_PLAN
brand_lock: CPPA (never "free") · IKO (never GAF) · Navy #1A365D + Gold #FBC02D + Cyan #00BFFF · zero green · RCAT #03-0637 · (972) 928-0788 · Outbox Shield
---

# 🍍 M7 MASTER EXECUTION SOP
**Read this ONE doc to know what to run.** Your studio already drafted a mountain of work. The job now is **launch it, in order**, and keep a simple daily loop. ADHD rule: **one phase at a time — don't jump ahead.**

---

## 0) THE STRATEGY (your CEO audit, in 4 lines)
1. **Keep the old site** (`pineapplecontractors.com`, ~235 pages of Google authority). **Fix** the new one (`pineappleroofingllc.com`). **Migrate** authority page-by-page.
2. Money follows intent: **LSA 30% · Google Search 25% · SEO/GBP 15%** · Meta 10% · rest small tests.
3. **The flywheel:** Google/LSA/Yelp → City+Service page → **CPPA** call/text → CRM 60-sec response → signed job → reviews+photos → repeat.
4. **Nothing publishes without Saia's GO.** Every draft lives in `Outbox_Drafts/` first.

## 1) THE ONE LOOP (how EVERY piece of content flows)
```
Keyword (OpenSEO / SEO tab)
   → Draft (claude-seo + SEO pipeline)        ← the AI agent does this
   → PAUSED in Outbox_Drafts/                  ← lands here automatically
   → Saia approves (GO)                        ← human gate
   → WordPress DRAFT (via wp-mcp, controlled)  ← bridge, draft-only
   → Human publishes in WordPress              ← brother clicks publish
   → Track (GSC · GA4 · LSA · reviews)         ← weekly
```
That loop never changes. Every task below is just a lap around it.

## 2) WHO DOES WHAT (stop doing everything yourself)
| Role | Owns | Tasks |
|---|---|---|
| **AI agent** (local studio) | drafting + SEO | city/service pages, schema, on-page audits, briefs, content — all → Outbox PAUSED |
| **VA** | the tedious repeat | lead intake, review replies, GBP posts, social scheduling, photo naming — see `M7_VA_TASK_HANDOFF.md` |
| **Brothers** (you + Naa Sione) | judgment + GO | approve drafts, publish, negative reviews, insurance calls, LSA, final branding |

## 3) WHAT'S ALREADY DONE — LAUNCH THESE FIRST (don't re-draft)
Sitting **ready + PAUSED** in `Outbox_Drafts/`:
- **3 city pages:** Frisco, Allen, Grapevine roofing pages (`SEO/2026-08-10_*`)
- **Schema:** `schema/ALL_12_PAGES_JSONLD.md` + `SEO/…JSON-LD…`
- **Audits/plan:** on-page audit, keyword map, technical + geo audit, 30-60-90 plan
- **Ready copy:** review-request texts, 8 social captions, 30-day content calendar, Grand-Slam offer, CLOSER sales system
> These are **fuel already in the tank.** Phase 1 is about *launching* them, not making more.

---

## 4) THE PRIORITY SEQUENCE (do in this exact order)

### 🥇 PHASE 1 — FIX GOOGLE + LAUNCH WHAT'S DRAFTED (this week)
1. **Fix the new site's broken navigation** — About / Reviews / Process / Contact all bounce to the homepage. (Kills conversions.)
2. **Restore or 301-redirect the 404 pages** Google still indexes (Reviews, Contact, Euless, Grand Prairie, blogs).
3. **Scrub "free" → CPPA** on the new site (52 hits). Fix licensing wording → "RCAT Licensed Roofing Contractor #03-0637" (not "Texas general-contractor license").
4. **Publish the 3 city pages** already in Outbox (Frisco, Allen, Grapevine) + drop in their JSON-LD schema.
5. **Install tracking:** one GTM container, Meta Pixel, Google call tracking. Noindex the thank-you page.

### 🥈 PHASE 2 — CONNECT WP-MCP + TURN JOBS INTO LEADS (weeks 2-3)
- **Wire wp-mcp to WordPress as a CONTROLLED, DRAFT-ONLY bridge** — follow `WP_AI_Bridge_SOP.md` (staged install, least-privilege Editor account, draft-only, approval commands). **Never** give it publish/admin/delete. This lets the studio push Outbox pages straight into WP as drafts you approve.
- **Every completed job → GBP post + review request + neighborhood social** (Glenn Kimball/The Colony, Nazik Nizam/Plano, Bhavin Patel/metal). Reviews = #1 LSA ranking factor.

### 🥉 PHASE 3 — MIGRATE AUTHORITY + SCALE (weeks 4+)
- Migrate the old site's strongest pages (reviews, city, commercial, top blogs) → new site with 1-to-1 301s. Keep old domain live 6-12 mo.
- Scale only channels producing **signed jobs** (not cheap leads).

---

## 5) THE SKILLS — what runs each task (all installed now)
| Skill / tool | Use it for |
|---|---|
| **claude-seo** (`seo-audit`, `seo-content-brief`, `seo-local`, `seo-schema`) | audits, city-page briefs, JSON-LD, local SEO |
| **wp-mcp-ultimate** | push approved drafts → WordPress **drafts** (controlled pilot only) |
| **contractor-social / -ads / -positioning** | GBP posts, social, paid angles, messaging |
| **OpenSEO tab** | striking-distance keywords from your own Search Console |
| **Old playbooks** (Hormozi, CLOSER, Grand Slam — in Outbox) | offer + sales frameworks |
| **/gbp-post · /review-response · /lead-followup** | daily one-click drafts |

## 6) DAILY / WEEKLY CADENCE (which SOP to open)
- **Every day (you, 30-90 min):** `M7_DAILY_LEAD_SOP.md` — morning post + review, noon SEO draft, evening approve+follow-up.
- **VA (daily/weekly/monthly):** `M7_VA_TASK_HANDOFF.md`.
- **Weekly SEO:** OpenSEO export → draft new city page → Outbox → publish → check GSC.

## 7) THE ANSWER TO "how do I get Outbox → the website?"
- **Now (before wp-mcp):** open the Outbox page → paste into WordPress as a **draft** → brother reviews → **publish**.
- **After Phase 2:** the studio pushes it to WP as a draft automatically via wp-mcp; you still click publish.
- **Either way:** the page + its schema go live only after a human hits publish.

---
**Start line:** Phase 1, step 1 — fix the 4 broken menu links. That single fix stops leads walking in circles. Then publish the Frisco page that's already written. Two moves, real needle. 🍍

<!-- M7-FIREWALL-EXEMPT: governance-reference (master SOP; "free" = the banned term → CPPA) -->
