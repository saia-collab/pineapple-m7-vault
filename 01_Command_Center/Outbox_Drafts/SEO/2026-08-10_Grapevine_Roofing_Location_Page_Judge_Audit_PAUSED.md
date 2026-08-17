---
status: PAUSED
delivery_state: PAUSED
human_authorization_required: true
artifact_type: judge_audit
target_keyword: "grapevine roofing company"
gsc_position_supplied: 16.5
publication_state: "NOT LIVE — HUMAN REVIEW REQUIRED"
---

# Grapevine Roofing Location Page — Strict Judge Audit

**STATUS: PAUSED**

## 1. Evaluation protocol

This rubric must be applied in order. The page receives no quality score until all automatic-reject gates are tested. A missing page is **not scorable**; it is not given benefit-of-the-doubt points.

### Gate A — Artifact and governance (automatic reject)

Pass only if all are true:

- A complete page draft exists and is readable.
- The draft is stored only in the approved Outbox draft location.
- The draft prominently states `STATUS: PAUSED` and does not claim to be published, deployed, indexed, or live.
- No publishing, deployment, CMS, indexing, email, ad-spend, or outreach action has occurred.
- Human approval is explicitly required before any live action.

**Failure result:** REJECT; do not score content.

### Gate B — Minimum content completeness (automatic reject)

Pass only if all are true:

- The customer-facing prose is at least **1,200 words**, counted after excluding YAML/frontmatter, editorial notes, navigation labels, and JSON-LD.
- There is exactly one H1.
- The page includes an SEO title recommendation, meta description recommendation, proposed slug/canonical, body copy, CTA copy, and both required JSON-LD blocks.
- No section is a stub, outline-only note, empty heading, or unresolved lorem ipsum.

**Failure result:** REJECT; do not score content.

### Gate C — Factual and brand firewall (automatic reject)

Pass only if all are true:

- The public offer is written as **“free roof inspection”** on first use. It is never marketed as “free.”
- The credential appears exactly as **“IKO Certified.”** The page does not claim GAF certification.
- The license appears exactly as **“RCAT License #03-0637.”**
- The copy says Pineapple Roofing **serves Grapevine**; it does not claim an office, headquarters, storefront, mailing address, branch, or physical presence in Grapevine unless an approved source proves that location.
- No invented or unsupported review quote, reviewer identity, star rating, review count, award, ranking, founding date, customer/project count, price, financing promise, turnaround time, warranty term, manufacturer warranty interpretation, storm date, weather event, insurance coverage decision, claim approval, settlement, deductible outcome, or carrier relationship appears.
- Insurance language does not promise coverage, payment, approval, replacement, the full scope the carrier pays fors, or a particular claim outcome.
- All material trust claims beyond IKO Certified and RCAT #03-0637 either cite the approved source pack or carry a clear editorial `[VERIFY BEFORE PUBLISHING]` flag and are excluded from public-ready copy.
- No visible design specification, CSS token, SVG fill, icon, button, badge, or image direction uses green. Search case-insensitively for `green`, common green color names, and green hex/RGB/HSL values; visual review is still required.

**Failure result:** REJECT; do not score content.

### Gate D — Structured-data validity (automatic reject)

Pass only if all are true:

- JSON parses with a real parser after removing the `<script>` wrapper; zero comments, trailing commas, smart quotes, or duplicate keys.
- One business entity is typed as `LocalBusiness` and `RoofingContractor` (an `@type` array is acceptable) and uses one stable, absolute `@id`.
- The LocalBusiness entity contains only verified values for `name`, canonical `url`, `telephone`, and the company’s real public address. It does not use a fabricated Grapevine address.
- Grapevine is represented through `areaServed` as a `City`, not by changing the company address.
- Any `sameAs`, logo, image, geo coordinates, opening hours, price range, founding date, rating, or review field is present only if verified.
- The `FAQPage` block contains at least three useful question/answer pairs, and every question and answer appears visibly on the page with materially identical wording.
- No `Review` or `AggregateRating` is added unless current, source-verifiable, visible on-page, and approved. Self-serving review markup on a LocalBusiness page should normally be omitted because it is not eligible for Google review-star treatment.
- Absolute canonical URLs use HTTPS; `@id` references resolve consistently; no duplicate or disconnected Pineapple business entities are created.
- The final resolved markup produces no syntax errors in Schema.org Validator and Google Rich Results Test. FAQ rich-result eligibility is not promised: Google generally limits FAQ rich results to authoritative government and health sites.

**Failure result:** REJECT; do not score content.

## 2. Weighted quality gates — 100 points

Score only after Gates A–D pass. Each criterion receives full points only when its measurable test passes; partial credit is allowed only where stated.

### 1) Search intent and answer-first opening — 15 points

- **6:** The first 80 words directly answer what a Grapevine user needs from a roofing company: service availability, core roofing help, and the next action. No generic brand story before the answer.
- **4:** “Grapevine roofing company” appears naturally in the H1 or first 100 words, without awkward exact-match repetition.
- **3:** The opening names IKO Certified and RCAT License #03-0637 accurately.
- **2:** The opening or first screen contains a clear free roof inspection action.

### 2) Local usefulness and original value — 18 points

- **5:** The page explains services relevant to Grapevine property owners without pretending local-office proximity.
- **4:** It provides a practical process from inspection/photo documentation through recommendations and next steps.
- **4:** It includes a decision-useful section on repair versus replacement without promises or invented thresholds.
- **3:** It contains at least four genuinely local/service-intent FAQs, not generic filler or city-name swaps.
- **2:** Local references are accurate, useful, and source-supported; unsupported neighborhoods, climate facts, code claims, or storm history are absent.

### 3) Factual trust and compliance — 20 points

- **6:** IKO Certified and RCAT License #03-0637 are visible, accurate, and not embellished.
- **5:** free roof inspection is explained clearly and does not use “free.”
- **5:** No prohibited or unverifiable claims appear in visible copy, metadata, alt text, CTA, or schema.
- **4:** Trust is built with transparent process, documentation, credential language, and clear contact action—not fabricated social proof.

### 4) On-page SEO quality — 15 points

- **3:** SEO title is approximately 45–65 characters, includes the target concept naturally, and is not stuffed.
- **3:** Meta description is approximately 140–160 characters, reflects the page accurately, includes a useful differentiator/CTA, and contains no unsupported claim.
- **2:** Proposed slug is concise, lowercase, hyphenated, and location-relevant.
- **3:** Exactly one H1; H2/H3 hierarchy is logical and no headings are repeated solely for keywords.
- **2:** Exact phrase use is restrained: normally title/H1 or opening plus no more than two additional natural body uses. Variants carry the rest.
- **2:** Internal-link recommendations use only verified destination URLs and descriptive anchors; unknown URLs are flagged rather than invented.

### 5) Conversion and CTA execution — 10 points

- **4:** At least two visible CTAs exist—one above the fold and one after decision-supporting copy—and both offer the free roof inspection.
- **2:** First use spells out free roof inspection; later uses may use free roof inspection.
- **2:** CTA describes what the user receives without overstating insurer acceptance or guaranteeing results.
- **2:** Phone/link/contact details are included only if verified and are consistent with schema.

### 6) Structured data quality — 12 points

- **6:** LocalBusiness/RoofingContractor JSON-LD passes all Gate D tests and maps the real company to Grapevine using `areaServed`.
- **4:** FAQPage JSON-LD passes all Gate D tests and matches visible content.
- **2:** Entity IDs, canonical URL, page URL, business name, telephone, and visible page facts are internally consistent.

### 7) Readability, accessibility, and design compliance — 10 points

- **3:** Prose is specific, professional, and understandable; paragraphs are generally short and no section is padded to reach 1,200 words.
- **2:** Scannable headings, lists, and answer blocks support mobile reading.
- **2:** Links and CTA labels are descriptive; images have meaningful, non-stuffed alt text; heading order is accessible.
- **2:** No green appears in design directions or assets; approved brand treatment should use Pineapple Blue `#003299`, Pineapple Yellow `#ffdd17`, and optional Status Cyan `#003299`.
- **1:** No keyword stuffing, doorway-page language, or near-duplicate city-swap prose is evident.

## 3. Decision thresholds

- **90–100:** PASS FOR HUMAN REVIEW. Still PAUSED; human approval is the only next step.
- **80–89:** CONDITIONAL. Revise listed defects, rerun all automatic gates, and rescore.
- **Below 80:** REJECT/REWRITE.
- **Any Gate A–D failure:** AUTOMATIC REJECT regardless of weighted score.
- **Any invented location, review, warranty, storm date, or insurance outcome:** AUTOMATIC REJECT and factual-compliance escalation.

## 4. Schema pitfalls most likely to fail

1. **Fake Grapevine NAP:** setting `addressLocality` to Grapevine merely because this is a Grapevine landing page. Use the verified public business address; express Grapevine through `areaServed`.
2. **Duplicate business entities:** creating separate `Organization`, `LocalBusiness`, and `RoofingContractor` nodes with different IDs. Use one business node with a stable `@id` and multiple types.
3. **Unresolved placeholders:** shipping `[CONFIRM]`, `[VERIFY]`, relative URLs, or a placeholder domain in JSON-LD. Placeholders are acceptable only while visibly PAUSED; they fail release readiness.
4. **FAQ mismatch:** schema questions that are absent from the visible page, answers shortened into different claims, or promotional FAQ answers that add unsupported promises.
5. **Unsupported ratings/reviews:** adding `aggregateRating`, review count, or testimonials because older materials mention “5-star.” Omit unless current evidence and on-page visibility are approved.
6. **Warranty markup or copy:** importing an IKO warranty length or coverage interpretation without an approved source. “IKO Certified” does not itself prove a specific warranty.
7. **Insurance guarantees:** using FAQ/schema language such as “insurance companies accept,” “insurance will cover,” or “we get claims approved.” Documentation assistance is not an outcome guarantee.
8. **Invalid JSON-LD:** JavaScript comments, trailing commas, smart punctuation, duplicate keys, HTML entities in raw JSON, malformed arrays, or multiple script fragments that contradict each other.
9. **Inconsistent identity:** schema name, phone, URL, address, and visible page details do not match. Exact consistency is required.
10. **Rich-result promise:** treating valid FAQPage markup as a guarantee of a Google FAQ enhancement. Valid markup and display eligibility are separate.
11. **Invented geo/opening data:** guessed latitude/longitude, hours, map URL, price range, or service radius. Omit unknown optional properties.
12. **Wrong canonical relationship:** the location page’s canonical points to the homepage or another city page, undermining the intended unique page.

## 5. Likely page-level failure points

### Critical

- The page file does not exist in the approved Outbox location.
- Word count is under 1,200 after excluding schema and editorial notes.
- Draft is missing `STATUS: PAUSED` or implies it is live.
- Copy says “Grapevine office,” “located in Grapevine,” or supplies a Grapevine address without proof.
- “Free inspection” replaces the required free roof inspection wording.
- GAF certification appears, or IKO Certified / RCAT License #03-0637 is missing or altered.
- A review, warranty, storm event/date, or insurance outcome is presented without an approved source.
- LocalBusiness or FAQPage JSON-LD is missing, unparsable, contradictory, or not aligned to visible copy.
- Green appears in design/CSS/image direction.

### High

- Generic opening delays the answer beyond the first 80–100 words.
- The exact keyword is stuffed into headings, FAQs, alt text, and CTAs.
- Content is a city-name swap with little Grapevine-specific usefulness.
- Unverified “best,” “top-rated,” “trusted by hundreds,” “decades of experience,” same-day response, or price claims are used as trust signals.
- FAQ answers give legal, code, warranty, weather, or insurance advice as certainty.
- CTA uses an unverified phone number or destination URL inconsistent with schema.

### Medium

- Title/meta length falls outside useful bounds or does not match page content.
- H1/H2 hierarchy is inconsistent.
- Internal links are guessed or broken.
- Long, padded paragraphs weaken the 1,200+ word requirement.
- FAQPage is valid but contains thin, repetitive questions with no decision value.

## 6. Current score after applying the gates

### Gate results

- **Gate A — Artifact and governance: FAIL.** No Grapevine location-page artifact was found in the approved SEO Outbox at the time of this audit. Only prior research/audit files were available.
- **Gate B — Minimum content completeness: NOT TESTABLE.** No page draft was available for word count or component review.
- **Gate C — Factual and brand firewall: NOT TESTABLE.** No page copy was available.
- **Gate D — Structured-data validity: NOT TESTABLE.** No page-specific LocalBusiness and FAQPage blocks were available.

### Score

**Quality score: N/A — NOT SCORABLE.**

**Disposition: AUTOMATIC REJECT FOR MISSING ARTIFACT.** This is an administrative/evidence failure, not a judgment that unseen copy is poor. No points are awarded or deducted from an absent page. Once a complete PAUSED draft is saved in the approved Outbox, rerun Gates A–D first and only then apply the 100-point rubric.

## 7. Required resubmission package

Submit one complete PAUSED location-page file containing:

1. SEO title, meta description, proposed slug, and canonical.
2. At least 1,200 words of customer-facing body copy.
3. Answer-first opening and free roof inspection CTAs.
4. Visible IKO Certified and RCAT License #03-0637 trust signals.
5. Visible FAQs.
6. LocalBusiness/RoofingContractor and FAQPage JSON-LD.
7. Source notes for every material claim beyond the supplied verified facts.
8. A short verification register listing unresolved domain, address, phone, URL, image, and internal-link fields.

**Single next approval needed after a passing rescore:** human approval to move beyond PAUSED draft status. No publication is authorized by this audit.
