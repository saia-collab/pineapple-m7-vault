---
type: cowork_brief
title: Site Consolidation — Cowork Project Brief (merge 2 domains → 1 flagship)
status: PAUSED — hand to Claude Cowork. Requires Saia GO + domain/DNS access.
brand_check: CPPA · IKO Certified · RCAT #03-0637 · zero green
last_updated: 2026-07-20
---

# 🎯 COWORK BRIEF — Consolidate Pineapple's Two Websites

## The problem (from Marco's audit + our build)
We run **two sites** and it's splitting our SEO:
- **pineapplecontractors.com** (Scorpion) — older, has 141 ranked keywords + 455 visits (87% branded), but locked/proprietary, duplicate content, bad schema, weak page speed. Being cancelled.
- **pineappleroofingllc.com** (WordPress) — we fully control it, has our 12 optimized location pages + RoofingContractor schema, but is newer (less link history).

**Two sites = divided authority, divided reviews, divided traffic. We must merge into ONE.**

## ✅ Recommended decision (confirm before executing)
**Flagship = pineappleroofingllc.com (WordPress)** — because we control it, it has the optimized pages, and it matches the "Pineapple Roofing" GBP name.

> ⚠️ **VERIFY FIRST (critical):** before redirecting, check which domain has more **backlinks / domain authority** (via Ahrefs, DataForSEO, or Search Console). If the Scorpion domain has significantly more link equity, we may instead point the Scorpion *domain* at the WordPress *site*. **301-ing the wrong direction loses years of authority — measure before you cut.**

---

## 📋 THE MIGRATION — steps for Cowork

### 1. Inventory + save (don't lose anything)
- Crawl pineapplecontractors.com (Scorpion) → list all indexed URLs (235 sitemap URLs, 79 blog posts, 97 service pages).
- Identify which Scorpion pages actually rank / get traffic (Search Console export) — those are the ones whose authority we must preserve with a redirect.
- Export any unique high-value blog content worth keeping → save as Markdown for review (most city pages are 97% duplicate per Marco — skip those).

### 2. Map the 301 redirects
- Build a redirect map: every old Scorpion URL → its best matching pineappleroofingllc.com page (e.g. `/service-areas/frisco` → `/roofing-storm-restoration-frisco-tx/`). No matches → redirect to the closest city page or homepage. **Never redirect to a 404.**
- Output a clean redirect table (old URL | new URL) for review.

### 3. Implement redirects
- If Scorpion allows redirects: set 301s there. **If Scorpion is locked (Marco flagged this), do it at the DNS/registrar or Cloudflare level** — point pineapplecontractors.com traffic to the WordPress equivalents.
- Verify each 301 returns the new page (HTTP 301 → 200), not a loop or 404.

### 4. Repoint the crown jewels — GBP (do NOT skip)
- Both Google Business Profiles (Lewisville 271 reviews, Frisco 159) → change the **website field** to pineappleroofingllc.com (or the specific city page).
- **This is the most valuable step** — the 430 reviews + local pack are your biggest asset; make sure they point at the flagship.

### 5. Tell Google
- Search Console → submit pineappleroofingllc.com sitemap.
- Use the GSC "Change of Address" tool (if moving the whole domain).
- Keep both properties in GSC during transition to watch traffic move.

### 6. Cancel Scorpion — LAST, not first
- **Only after** redirects are live AND Google has recrawled (2–4 weeks) AND traffic is confirmed moving to WordPress.
- Cancelling before the 301s are working = losing all that authority permanently.

---

## 🚫 HARD RULES for Cowork
- **Measure backlinks before choosing the redirect direction.**
- **301 before cancel.** Never cancel Scorpion first.
- **Brand law:** every migrated/rewritten page → CPPA (never "free"), IKO Certified (never GAF), RCAT #03-0637, zero green.
- **Nothing goes live without Saia's GO** (Outbox Shield).
- Preserve the GBP reviews at all costs.

## 🍍 Why this is the highest-leverage move
Right now Marco's 455 visits (Scorpion) and our 12 optimized pages (WordPress) are two separate half-strength sites. **Merge them and you get one full-strength site** — the reviews, the authority, the branded traffic, AND the optimized storm pages all in one place. That's when the rankings actually move.


<!-- M7-FIREWALL-EXEMPT: cowork-brief -->
