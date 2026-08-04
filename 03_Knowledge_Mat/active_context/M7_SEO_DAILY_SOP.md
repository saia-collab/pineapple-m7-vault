---
title: M7 SEO DAILY SOP — The AI SEO Command Center
type: hermes_learnable_sop
status: active
for: Hermes (/learn → save → execute daily)
grounds_against: MASTER_PLAYBOOK.md · CLAUDE.md · NotebookLM (PM7 SEO Mastery, SEO Playbook Goldie Stack, AI SEO Command Center, 2026 Search Strategy)
date: 2026-07-24
---

# 🍍 M7 SEO DAILY SOP — The AI SEO Command Center

> **Hermes: read this file fully, save it to memory, and run the DAILY ROUTINE below every day.**
> Everything you produce lands PAUSED in `01_Command_Center/Outbox_Drafts/` — never publish
> without Saia's explicit GO (Outbox Shield). Ground every fact against the Master Playbook.

---

## 1. THE MISSION (what this system does)
Rank Pineapple Roofing for high-intent local roofing searches across DFW by building
**hyper-local, differentiated pages**, optimizing the **Google Business Profile**, automating
**review responses**, and running a **monthly audit loop** — all measured in Google Search Console.

## 2. THE NON-NEGOTIABLE RULES
1. **The 50% Differentiation Rule** — every AI-generated service or location page must be
   **40–50% unique** (own intro, own local details, own FAQ). Duplicate pages do NOT index.
2. **Brand law** — CPPA (never "free"), IKO Certified (never "GAF"), RCAT #03-0637, zero green,
   Navy #1A365D + Gold #FBC02D. Run `brand_firewall.py --check` before staging anything.
3. **Outbox Shield** — all output PAUSED in `Outbox_Drafts/`; Saia gives the GO to publish.
4. **Verify, don't hallucinate** — reviews and stats must be REAL. Never invent a review.

## 3. THE STRATEGY (from the 2026 Search Blueprint)
- **One page per service × suburb** — a dedicated page for each service in each town
  (e.g. "flat roofing allen tx", "gutter installation lewisville"), matching high-intent queries.
- **The 100-Image Rule** — 100+ photos on the Google Business Profile correlates with a large
  lift in calls, clicks, and direction requests. Keep adding real job photos.
- **Search Everywhere** — optimize for Google *and* AI answer engines (GEO/AEO): answer the query
  in the first 40 words, use clean tables, inject RCAT #03-0637 + IKO Certified + ZIPs in schema.

## 4. ⭐ THE DAILY ROUTINE (Hermes runs this each morning)
1. **Pull Search Console** → save the striking-distance report as
   `03_Knowledge_Mat/active_context/gsc_striking_distance_[YYYY-MM-DD].md`.
2. **Pick today's target** — the keyword at **position 5–20 with the most impressions and
   fewest clicks** (biggest quick win). Log it.
3. **Draft ONE improvement** for that keyword's page — sharper title tag + first-40-words answer +
   one local detail — as a `[service]-[city]-tx.md` file, ≥40% unique, brand-clean.
4. **Firewall check** the draft (`brand_firewall.py --check`). Fix any flag.
5. **Stage it PAUSED** in `Outbox_Drafts/` with a one-line note: keyword, current position, the change.
6. **Report to Saia** in `Outbox_Drafts/MORNING_REVIEW.md`: today's target, the draft, expected impact.

## 5. WEEKLY (once a week)
- **Review sweep** — check new Google/Yelp reviews; draft responses per the automation rules (§7).
- **GBP photos** — add any new real job photos toward the 100-image goal.
- **Title-tag audit** — find pages ranking 3–10 with low CTR (like "24 hour roofers" at #4, 0 clicks) → rewrite the title to earn the click.

## 6. MONTHLY (the audit loop)
1. Full striking-distance pull + competitor gap analysis → `gsc_striking_distance_[Month].md`.
2. Verified on-page content refresh for the top 5 opportunity pages (`[service]-[city]-tx.md`).
3. **Submit `sitemap_index.xml` in Google Search Console** to force a recrawl.
4. Log results; pick next month's 5 targets.

## 7. GOOGLE BUSINESS PROFILE — REVIEW AUTOMATION (Pably)
Tool: `pably-gbp-responder.json` (import into Pably, plug in the API key).
- **Positive review →** auto-draft a warm thank-you naming the CPPA + IKO Certified + RCAT #03-0637.
  Example: *"Thank you so much for the trust, [Name]! Proud to serve [City] as a licensed
  RCAT #03-0637 contractor — glad our Complimentary Professional Photo Audit and IKO Certified
  workmanship gave you peace of mind."*
- **Negative review (≤2 star) →** **HALT public posting**, freeze the automation, send a private
  alert to Saia's inbox, and prepare a private draft response (apologize, invite to resolve at
  info@pineapple-roofing.com). **Never auto-post a reply to a negative review.**

## 8. OUTPUT SCHEMA (where things live)
| Artifact | Path |
|---|---|
| Striking-distance keyword pulls | `03_Knowledge_Mat/active_context/gsc_striking_distance_[Date].md` |
| Verified on-page drafts | `03_Knowledge_Mat/active_context/[service]-[city]-tx.md` |
| Automation / validation scripts | `04_Tech_Lab/scripts/` |
| Anything for publishing | `01_Command_Center/Outbox_Drafts/` (PAUSED) |
| Daily report to Saia | `01_Command_Center/Outbox_Drafts/MORNING_REVIEW.md` |

## 9. CURRENT TARGET LIST (Saia's real striking-distance data, 2026-07)
| Keyword | Position | Priority |
|---|---|---|
| 24 hour roofers | 4.1 | 🔥 title-tag fix (0 clicks) |
| roofing companies near me | 7.0 | growing |
| flat roofing allen tx | 9.1 | one spot from page 1 |
| gutter installation lewisville | 9.4 | almost there |
| pineapple (brand) | 10.0 | protect |
| grapevine roofing company | 16.1 | most impressions |
| euless roofing | 17.1 | build page |

## 10. THE TOOLS IN PLAY
- **Google Search Console** — the source of truth for rankings/keywords (both domains verified).
- **OpenSEO** — local dashboard reading GSC (the Striking Distance tab = the keyword list).
- **DataForSEO MCP** — live keyword/competitor data for the research agents.
- **Site Kit** (GA4) + **Meta Pixel** — installed and tracking.

---

Ko e hala 'o e fononga ko e faka'apa'apa. *(The path of the journey is respect.)*

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
