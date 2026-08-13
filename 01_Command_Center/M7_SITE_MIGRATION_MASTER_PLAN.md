---
type: migration_plan
title: M7 — Site Migration Master Plan (old pineapplecontractors.com → new pineappleroofingllc.com)
status: active
last_updated: 2026-07-21
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🏗️ M7 — SITE MIGRATION MASTER PLAN

**Goal:** move everything from the OLD site (`pineapplecontractors.com`, Scorpion-built) into the NEW
WordPress (`pineappleroofingllc.com`) in our new format (Neal-style, editorial, CPPA-compliant, navy/gold,
zero green, no GAF), **without losing Google rankings.**

## 🚨 #1 RULE — DON'T KILL YOUR SEO (read this first)
Your old site has a **huge indexed footprint** (100+ city + service pages). If you just switch sites, you
lose all that ranking. **Every old URL must 301-redirect to its new match.** Two non-negotiables:
1. **301 redirects** from every `pineapplecontractors.com` URL → the equivalent new URL (preserves rankings).
2. **One primary domain.** Two live sites with the same content = duplicate-content penalty. Pick ONE
   (you chose `pineappleroofingllc.com`), migrate content, then 301 the old domain to it.
> VP note: `pineapplecontractors.com` is older + bigger + likely has more authority. Moving to the smaller
> domain is fine **only if** the 301s are complete. Budget this as the most important step, not an afterthought.

---

## 🗺️ WHAT THE OLD SITE HAS (the full inventory — nothing gets missed)
**Core pages:** Home · About · Insurance Claims · Press · Financing · Reviews · Blog · Photo Gallery · FAQ ·
Contact · Careers · Referrals · Subcontractors · Site Map · Privacy.

**Services tree:**
- **Construction:** Remodeling & Renovations (Painting · Home Additions · Flooring · Fencing) · New
  Construction (ACM Panel · Drywall · Framing · Siding) · Emergency Roof Repairs · Pool Builders ·
  Hospitality Renovations · Multifamily Renovations.
- **Restoration Services** (→ note: also its own brand, pineapplerestorations.com).
- **Roofing:** Residential (Sheet Metal · Gutters) · Commercial (Metal · Slate · Tile) · Roof Installation ·
  Leak Repair · Shingle · TPO · PVC · Case Studies.

**Service-area pages (the SEO gold — ~100 pages):** Collin (Frisco, McKinney, Allen, Plano, Melissa, Prosper,
Celina, Van Alstyne, Wylie, Lucas, Fairview) · Denton (Lewisville, The Colony, Flower Mound, Denton, Sanger,
Castle Hills, Little Elm, Aubrey, Pilot Point) · Tarrant (Hurst, Euless, Bedford, Grapevine, Colleyville,
Southlake, Keller, Arlington, Fort Worth, Mansfield) · Dallas (Dallas, Garland, Irving, Mesquite, Duncanville,
Desoto, Grand Prairie, Rowlett) · Rockwall · Parker (Weatherford) · Harris (Houston) · Ellis · Titus · Bell ·
Eastland · Smith (Tyler). Many have Roof Replacement / Roof Repair sub-pages.

**Trust assets to carry over:** RCAT #03-0637 · IKO · BBB · NMSDC (minority/MBE) · HUB · SBE · ProCore ·
NTRCA · Lead Safe Firm · BOMA · 5.0★ 100+ reviews · 50-year warranty · video testimonials (YouTube).
**Offices:** Lewisville (4400 TX-121 Ste 300) · Frisco (1 Cowboys Way Ste 270W) · Austin · Houston/San Antonio (coming).

---

## 🧹 FIX DURING MIGRATION (brand law — every page)
| Found on old site | Change to |
|---|---|
| "free estimate" / "Schedule a Free Roof Inspection" / "free inspection" | **Complimentary Professional Photo Audit (CPPA)** |
| **"GAF Certified"** badge/links | **remove — lead with IKO Certified** (keep IKO, drop GAF) |
| any green | Navy #1A365D + Gold #FBC02D + Cyan #00BFFF only |
| "$0 down" (financing) | **Full Restoration Coverage** framing |
| Keep as-is | RCAT #03-0637, IKO, BBB, NMSDC/HUB/SBE (minority certs = valuable), 50-yr warranty, 5.0★ |

---

## 🏛️ BRAND ARCHITECTURE DECISION (pick one — quick)
The old site is an umbrella ("Contractors" = roofing + construction + restoration). The new domain says
"roofing." Two clean options:
- **A) Roofing-focused (recommended):** `pineappleroofingllc.com` = roofing + storm + insurance. Link
  Construction and Restoration out to their own brands (pineapplerestorations.com + a construction page).
  Cleaner SEO, sharper message.
- **B) Umbrella:** rebuild the full contractors tree on the new domain (construction + restoration + roofing).
  More pages, broader, but dilutes the "roofing" focus.
> VP lean: **A** — but keep the money pages (roofing + city pages + insurance claims). Decide before build.

---

## 📅 THE PHASED PLAN (safe order)
1. **Backup + map.** Export the old site's URL list (Screaming Frog free, or the Site Map page). Build a
   redirect map: every old URL → new URL. (This is the critical artifact.)
2. **Build the new pages** in WordPress, in our format (Neal structure, CPPA, no green) — Home → core pages →
   roofing services → the city pages (highest-traffic first: Frisco, Plano, McKinney, Allen, Lewisville).
3. **Add tracking** (your Meta Pixel 2545389655696737 + GA4 + the CPPA lead form → CRM).
4. **301 redirects.** In WordPress use **"Redirection"** plugin (or host-level): map every old URL to new.
5. **Go live + Search Console.** Submit the new sitemap, use the "Change of Address" tool if moving domains,
   keep the old domain live (redirecting) for 6–12 months.
6. **Verify rankings** weekly; fix any 404s the Redirection plugin logs.

---

## 🤝 HAND THIS TO CHATGPT / FABLE (the build)
```
Act as my senior web engineer + SEO. I'm migrating pineapplecontractors.com into a new WordPress site at
pineappleroofingllc.com, in a premium editorial format (fonts Libre Caslon Display + DM Sans; palette navy
#1A365D, gold #FBC02D, cyan #00BFFF, paper #F7F5EF; ZERO green; Neal Roofing structure). Use my attached
capture page as the design system, and my brand law: CPPA (never "free"), IKO Certified (never GAF), RCAT
#03-0637, 972-928-0788, Full Restoration Coverage (never "$0 down").

Do this in order:
1. Build the CORE pages (Home, About, Insurance Claims, Financing, Reviews, Contact, FAQ) in the new format.
2. Build the ROOFING service pages (Residential, Commercial, Roof Installation, Leak Repair, Shingle, TPO,
   PVC, Metal, Tile, Slate, Gutters, Sheet Metal, Storm/Emergency).
3. Build the CITY pages (start: Frisco, Plano, McKinney, Allen, Lewisville, The Colony, Flower Mound, Denton,
   Little Elm, Fort Worth, Arlington, Dallas, Irving) with LocalBusiness + FAQ JSON-LD, answer in first 40 words.
4. Give me a 301 REDIRECT MAP (old URL → new URL) for every migrated page, ready for the WordPress Redirection
   plugin.
Every CTA = "Reserve Your Complimentary Professional Photo Audit." Keep the Meta Pixel + a lead form that
posts to my Apps Script CRM endpoint. Output pages as clean HTML/Elementor-ready blocks, and the redirect map
as a CSV.
```

## ✅ WHAT'S ALREADY DONE (reuse it)
- **Design system + capture page** (compliant, tracked) — `Outbox_Drafts/CPPA_Capture_Page/`.
- **Neal format benchmark** — `03_Knowledge_Mat/00_Atlas/M7_DESIGN_BENCHMARK_NEAL_AND_SITE_FIX.md`.
- **City-page build prompt** — `01_Command_Center/M7_CHATGPT_HANDOFF.md`.

## 🌅 THE ONE MOVE FIRST
Before any building: **export the old site's full URL list and build the 301 redirect map.** Without it,
migration costs you rankings. With it, you keep every lead the old site quietly sends you.


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
