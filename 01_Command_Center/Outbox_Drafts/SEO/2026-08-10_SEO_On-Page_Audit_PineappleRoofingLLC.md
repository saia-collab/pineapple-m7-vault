---
status: PAUSED
asset: on_page_seo_audit
domain: https://pineappleroofingllc.com/
audit_date: 2026-08-10
author: JR. Moeakiola
publication_state: NOT LIVE — HUMAN REVIEW REQUIRED
---

# Pineapple Roofing On-Page SEO Audit

Trust baseline: RCAT License #03-0637 · IKO Certified · 5-Star · Since 2021 · 972-928-0788

## Executive verdict

The site is crawlable and its 14 sitemap URLs returned HTTP 200 with self-referencing canonicals. The largest risk is not a title-length issue: the sitewide Organization schema identifies two unrelated businesses. The next priorities are Pineapple brand-law violations in shared calls to action, missing Frisco/local-intent coverage, weak heading structure, thin or misindexed utility pages, and Roofing/Restorations cross-contamination.

No live edits were made. Keyword recommendations below are crawl-gap hypotheses, not ranking or search-volume claims; validate them against Google Search Console before changing established Dallas pages.

## Prioritized fix list

### P0 — Correct immediately

1. Resolve entity, canonical-domain, and NAP ownership; then replace the incorrect schema.
   - Verified: Yoast emits Organization name “Mosso and Sons Land Management,” alternate name “Unboxed Organizing and Packing,” and an empty logo on audited pages.
   - M7 identifies pineapplecontractors.com as the Roofing brand domain, while this audit covers pineappleroofingllc.com.
   - The live footer shows 4400 State Hwy 121 #300, Lewisville, while the M7 truth set lists 1 Cowboys Way Ste 270W, Frisco, TX 75034.
   - Saia must confirm the public canonical domain and public address. Do not guess or silently overwrite either value.
   - After confirmation, replace the incorrect entity with one verified Pineapple Roofing entity and a valid logo URL. Add telephone, verified address, URL, sameAs profiles, founding date, areaServed, and credentials only where supported.
   - Use the most specific supported business type, such as RoofingContractor, connected to Organization/WebSite/WebPage via stable @id values.
   - Do not add aggregateRating unless the displayed review count and rating are current and source-verifiable.

2. Replace every legacy quote CTA with “free roof inspection.”
   - Verified: prohibited legacy CTA language appears through the shared header, modal/form, body buttons, and footer across the crawl; the homepage contains the highest concentration.
   - Also replace the banned discovery-stage label used in the homepage process heading and the construction-page CTA.
   - Standard CTA: “Book Your free roof inspection” with 972-928-0788 and “IKO Certified · RCAT License #03-0637.”

3. Separate Roofing from Restorations.
   - Verified: the Roofing navigation and sitemap include a restoration-services page covering water, fire, and mold.
   - Fix: remove restoration terminology and navigation from the Roofing site. Check traffic, links, and relevance before migrating the verified equivalent to pineapplerestorations.com through an approved redirect plan. Do not mix restoration schema, FAQs, or internal links into Roofing pages.

4. Remove prohibited color tokens from the source/theme.
   - A rendered homepage scan found no active prohibited-color styling, but source review found two non-approved WordPress preset color tokens.
   - Remove or override those global presets so the approved palette is the only available system: Navy #003299, Gold #ffdd17, Cyan #003299 for status, and White.

5. Fix indexation hygiene.
   - Set /thank-you/ to noindex, follow and remove it from the XML sitemap. Do not block it in robots.txt before crawlers process the noindex directive.
   - The /blog/ archive is indexable, empty, has no meta description, uses H1 “Archives,” and is absent from the page sitemap. Either publish a useful Roofing resource hub and include it correctly, or noindex it until content exists.
   - Retest robots directives, sitemap membership, canonicals, and status codes after changes.

### P1 — High-impact on-page corrections

6. Repair missing and generic H1s.
   - Missing H1: /services/, /roof-insurance-claims-help-in-dfw-pineapple-contractors/, and /roof-financing-in-dfw-full-restoration-coverage-pineapple-contractors/.
   - Empty blog uses generic H1 “Archives.”
   - The license badge is coded as H2 and can appear before the page topic. Convert the badge to non-heading text.
   - Keep one descriptive H1 per indexable page; use H2/H3 for genuine subsections.

7. Restore internal-link depth on three service pages.
   - /services/roof-repair-dallas-tx/, /services/gutter-installation-dallas-tx/, and /services/storm-damage-repair-dallas-tx/ exposed only two unique same-domain links in the HTML crawl, versus roughly 14 on most templates.
   - Check the shared header/footer template, breadcrumbs, related services, service-area links, and contextual anchors.

8. Add page-specific Service schema.
   - Current structured data is primarily WebPage, BreadcrumbList, WebSite, Organization, and FAQPage on selected pages.
   - Add one Service entity per legitimate service page, linked to the RoofingContractor provider and relevant areaServed. Keep FAQPage only where the same questions and answers are visible on-page.

9. Establish a Frisco-first local architecture without destroying existing Dallas relevance.
   - Verified crawl gap: Frisco appears only on the thin service-area page; ZIPs 75033, 75034, 75035, 75067, and 75068 are absent sitewide.
   - Keep useful Dallas service pages if Search Console proves demand. Build a strong Frisco hub and unique Frisco service pages rather than mass-swapping city names.
   - Add unique evidence for Frisco, Lewisville, McKinney, Plano, Allen, and The Colony; avoid doorway-page duplication.
   - Add supported areaServed data and target ZIP arrays to schema only on genuinely relevant pages.

### P2 — Relevance, CTR, and trust improvements

10. Rewrite generic titles and descriptions around real intent.

| Page | Recommended title |
|---|---|
| Home | Frisco Roofing Contractor \| Pineapple Roofing |
| Services | Roofing Services in Frisco, TX \| Pineapple Roofing |
| Roof replacement | Roof Replacement in Dallas, TX \| Pineapple Roofing |
| Roof repair | Roof Repair in Dallas, TX \| Pineapple Roofing |
| Gutters | Gutter Installation in Dallas, TX \| Pineapple Roofing |
| Siding | Siding Installation in Dallas, TX \| Pineapple Roofing |
| Storm page | Hail & Storm Damage Roofing in Dallas, TX \| Pineapple Roofing |
| Service areas | DFW Roofing Service Areas \| Pineapple Roofing |
| Claims | Roof Insurance Claim Help in DFW \| Pineapple Roofing |
| Financing | Roof Financing in DFW \| Pineapple Roofing |

Do not retitle established Dallas pages until Search Console confirms query/page alignment. Write unique meta descriptions with the service, location, free roof inspection, phone, and one verified trust signal; avoid generic “Call now” duplication.

11. Add missing keyword themes naturally.

Primary local themes:
- Frisco roofing contractor; roofer in Frisco, TX
- Frisco hail-damage roofing; storm-damage roof documentation
- roof replacement Frisco; commercial roofing Frisco
- roofing for property managers; multi-property roofing documentation
- estate roofing and premium roofing systems, where supported by real project evidence

Trust/entity themes:
- IKO Certified
- RCAT License #03-0637
- serving North Texas since 2021
- Polynesian-owned and family-operated
- 5-Star, only with a current verifiable source
- free roof inspection

Geo themes:
- Frisco 75033, 75034, 75035
- Lewisville 75067; Little Elm 75068
- Starwood and Newman Village, only with unique local evidence

Verified gap: commercial roofing, luxury/estate positioning, Polynesian heritage, free roof inspection, IKO, RCAT, and Since 2021 are missing or nearly absent from core homepage/service content. Do not keyword-stuff; answer the query in the first 40 words and support each page with local proof, project photos, FAQs, and internal links.

12. Strengthen E-E-A-T and media signals.
   - Add author/reviewer byline: JR. Moeakiola, with a verified profile page.
   - Put the five trust signals on core layouts.
   - Add real project examples and location-specific photo captions/alt text. The crawl found missing alt text on multiple service-page images.
   - Add visible, sourced answers before marking them up as FAQPage.

## Page-level findings snapshot

- Homepage: title 63 characters; one H1; FAQ schema present; Dallas-heavy; core Frisco/free roof inspection/IKO/RCAT/Since 2021 themes absent; shared brand-law CTA violations; two images missing alt text.
- Services hub: no H1; only 391 words; no Frisco or core credential themes.
- Roof replacement: title 63 characters; FAQ schema present; two images missing alt text; no free roof inspection/IKO/RCAT/Since 2021.
- Siding: title 61 characters; three images missing alt text; no credential themes.
- Roof repair, gutters, storm: valid H1s and FAQ schema, but only two unique internal links each and three missing image alts each.
- Service areas: only 132 words; generic title; no city/ZIP landing-page depth or Service schema.
- Claims and financing: no H1; generic titles. They are the only audited pages with meaningful free roof inspection usage.
- Blog: empty indexable archive, no meta description, generic H1, absent from page sitemap.
- Thank-you: indexable and included in sitemap; no H1 or meta description.

## Acceptance criteria

- Correct Pineapple entity in schema; no unrelated organization names; valid logo and verified NAP.
- Exactly one topical H1 on every indexable page; license badge is not a heading.
- Utility confirmation page noindexed and removed from sitemap.
- Empty blog noindexed or rebuilt as a useful Roofing resource hub.
- All shared CTAs use free roof inspection language; banned terms return zero matches.
- Roofing and Restorations have separate pages, internal links, schemas, and domains.
- No prohibited-color tokens remain in source, theme settings, generated CSS, or rendered components.
- Core Roofing layouts include RCAT License #03-0637, IKO Certified, 5-Star, Since 2021, and 972-928-0788 where factually verified.
- Search Console query/page data reviewed before mass title, URL, or city-target changes.
- Structured data validates and matches visible page content.

## Sources and limitations

Sources: live HTML crawl of robots.txt, sitemap_index.xml, page-sitemap.xml, 14 sitemap URLs, and linked /blog/ archive on 2026-08-10; rendered homepage DOM/color inspection; M7 GROUNDING.md, MASTER_PLAYBOOK.md, HERMES_PLAYBOOK.md, and M7_GROWTH_ENGINE.md.

Limitations: no Google Search Console, GBP, analytics, backlink, rank-tracker, or server-log data was available. This is an on-page crawl audit, not proof of rankings, traffic, or search volume.

## Human approval gate

STATUS: PAUSED. No website, schema, GBP, redirect, indexation, or domain change may be made without Saia’s explicit GO.

Ko e hala 'o e fononga ko e faka'apa'apa.
