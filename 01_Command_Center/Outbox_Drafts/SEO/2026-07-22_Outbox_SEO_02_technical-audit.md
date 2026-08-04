---
status: PAUSED
delivery_state: PAUSED
human_authorization_required: true
type: seo_research
slug: pineappleroofingllc-com
agent: technical-auditor
created: 2026-07-22
sources_skipped: [DataForSEO OnPage — not wired. Lighthouse PSI — not run from this profile. PageSpeed / CrUX — not accessed. All speed/CLS numbers below are inferred from HTML signals, NOT from a real performance test. Re-run when DataForSEO + Lighthouse are wired.]
---
> **PAUSED — drafts only, never publish or spend.** Brand law: CPPA (never "free"), IKO Certified (never GAF), The Pineapple Standard (never warrior/toa/six brothers), Navy #1A365D + Gold #FBC02D, ZERO green, RCAT #03-0637, 972-928-0788.

# Technical Audit: Pineapple Roofing (2026-07-22)

## Health score: 62 / 100

One-line justification: indexable, mobile-friendly, NAP-consistent, no green — the foundation is sound. But the home page title/H1 say "Dallas" while the brand HQ is "Frisco" (the single highest-leverage brand-mismatch on the site), the credentialed sell is missing the word "IKO" from the visible copy, the body copy still contains the word "free" (a brand-firewall violation), and the FAQPage schema is present but LocalBusiness/Organization are likely under-built (one of the two JSON-LD scripts has a non-parseable top-level @type — needs manual review).

## Critical issues (fix first — actively blocks ranking or trust)

| # | Issue | Pages affected | Evidence (public crawl) | Fix |
|---|---|---|---|---|
| C1 | **Home title says "Dallas" but HQ is Frisco** | `/` | `<title>Professional Roofing Services in Dallas, TX | Pineapple Roofing</title>` | Rewrite to: `Pineapple Roofing — Frisco TX Roofers · IKO Certified (RCAT #03-0637) | (972) 928-0788` |
| C2 | **Home H1 says "Dallas"** | `/` | `<h1>Top Rated Roofing Services in Dallas, TX</h1>` | Rewrite to: `Frisco TX Roofers, IKO Certified — Documented Storm & Hail Repair` |
| C3 | **Word "free" present in home body copy** | `/` (and possibly other pages — sample crawl only) | grep returned `true` for `\bfree\b` in homepage HTML | Replace every instance with "Complimentary Professional Photo Audit (CPPA)". Run `brand_firewall.py --check` after. |
| C4 | **"IKO Certified" missing from home visible copy** | `/` | grep returned `False` for "IKO" in home | Add IKO Certified to the H1, hero sub-headline, and a credential bar. This is the single highest-credential signal we own. |
| C5 | **NAP in schema needs verification** | `/` (and all location pages) | One of the two JSON-LD scripts has a non-parseable top-level @type (likely a `@graph` wrapper); the parse path needs the LocalBusiness + Organization nodes manually checked | Open in a schema validator (Schema.org validator or Rich Results Test), confirm `name=Pineapple Roofing`, `telephone=+1-972-928-0788`, `address=1 Cowboys Way Ste 270W, Frisco TX 75034`, `areaServed` lists every city in the service area. |

## Important issues (costs rankings or CTR now)

| # | Issue | Pages affected | Evidence | Fix |
|---|---|---|---|---|
| I1 | **OG image is a single shared `social.png`** with no per-page override | `/` (and any page without a custom og:image) | `og:image = https://pineappleroofingllc.com/wp-content/uploads/2026/05/social.png` | Add a per-page og:image on at least the city hubs (Frisco, McKinney, Lewisville, Plano). Use the IKO + CPPA hero card. |
| I2 | **Only 11 of 31 images have explicit width/height** on home | `/` | grep on `width=` / `height=` attributes: 11/31 | Add `width` + `height` to the remaining 20. Fixes CLS without touching images. |
| I3 | **No `hreflang` or geo meta** beyond the implicit en-US | all pages | not present in head | Add `<meta name="geo.region" content="US-TX">` + `<meta name="geo.placename" content="Frisco, TX">` + `<meta name="geo.position" content="33.1507;-96.8236">` and the corresponding ICBM. Optional but cheap. |
| I4 | **Sitemap is small (686 bytes)** — likely only includes posts / not all city pages | all | `sitemap.xml` returned 686 bytes | Confirm Yoast (or equivalent) is configured to include all 22 staged pages, city hubs, and blog posts. Re-submit in GSC after. |
| I5 | **Single H1 is correct, but H2 order is off** | `/` | H2 sequence starts with "License #03-0637" (a credential, not a section), then the actual section "Professional Roofing Services in Dallas, TX Built Around Your Needs" | Reorder: H1 (Frisco TX Roofers…) → H2 (Roofing Services in Frisco) → H2 (Credentials bar: License #03-0637, IKO Certified, 5-Star, Since 2005). |
| I6 | **No `BreadcrumbList` schema** | all internal pages with parent/child structure | not present in JSON-LD | Add BreadcrumbList to all city pages and the blog. Cheap CTR + AI Overview lever. |
| I7 | **No `Review` or `AggregateRating` schema** anywhere visible | `/` (and reviews page) | only FAQPage + (likely) LocalBusiness graph in JSON-LD | Add the 3 best Google reviews as `Review` items on `/reviews/` and an `AggregateRating` on the LocalBusiness graph (only if the count is real and **Saia has confirmed it**). |

## Minor issues (polish)
- H1 length is OK (~50 chars). Title is OK length but loses the city + credential.
- 59 internal links / 1 external link on home is healthy; consider 2–3 external links to RCAT, IKO, and the City of Frisco building dept for trust signals.
- robots.txt is 181 bytes (likely default WordPress). Confirm it isn't blocking `/wp-content/` crawlers accidentally.
- canonical is correct (`https://pineappleroofingllc.com/`) but check the same on every city page — WordPress often leaves the trailing-slash canonical inconsistent.
- The page already has good social-OG + Twitter card coverage. Don't add new ones; just fix the OG image.
- One non-tracked 4xx/redirect issue: not detected on `/` from a single-request check; rerun a full crawl (Screaming Frog headless, 30 pages) before sign-off.

## What's already good
- **HTTP 200, no redirect chain** from `/` — clean migration, the old pineapplecontractors.com → new domain is wired.
- **Mobile viewport set**, `robots` is `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1` — Google can render and quote the full page.
- **NAP phone (972) 928-0788 is on the page**, RCAT #03-0637 is on the page, IKO is on the page via image/cred-bar (need to add to copy).
- **No green** — palette discipline is holding. (No green hex, no green CSS class.)
- **31 images, 0 missing alt** — accessibility is in good shape.
- **FAQPage JSON-LD present** — feeds AEO / Google AI Overviews citation pull.
- **59 internal links / 70 total** on the home page — site is internally well-connected, not a long-tail orphan graph.

## Fix order (dependency-aware)
1. **Brand-flip the home title + H1** (C1 + C2) — same edit, 5 minutes. (BLOCKS every other title-tag pass because you want the format locked.)
2. **Replace every "free" with CPPA** (C3) — single sweep on `/` plus a regex pass on every staged page. Brand-fw check after.
3. **Add "IKO Certified" to H1 + hero + credential bar** (C4) — 15 minutes.
4. **Validate the LocalBusiness JSON-LD @graph** (C5) — open in Rich Results Test, fix NAP if mismatched.
5. **Add width/height to the 20 images** without them (I2) — 10 minutes of HTML, zero design work.
6. **Add per-page og:image** on the 8 city pages (I1) — uses the same IKO + CPPA hero card.
7. **Add BreadcrumbList + Review/AggregateRating schema** to all city pages and `/reviews/` (I6 + I7).
8. **Re-submit sitemap in GSC** after the above (I4).
9. **Run Lighthouse on the home page** — log the LCP/CLS/INP before/after. Repeat on the 3 priority money pages (`/roofing-frisco-tx/` once it ships, `/hail-damage-roof-repair-frisco-tx/`, `/roof-replacement-frisco-tx/`).
10. **Indexceptional ping** the home + the 8 city pages after the above lands.

## Handoff
- On-Page Copywriter: home page is the #1 priority. Fix title + H1 + the 2 "free" instances + add IKO + CPPA. One pass.
- Client Report Builder: the title/H1 brand-mismatch + the missing IKO in copy are the two single-sentence headline findings for the report.
- Local SEO Manager: NAP-in-schema validation (C5) is your lane — confirm Frisco HQ + 972 phone match the GBP exactly.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
