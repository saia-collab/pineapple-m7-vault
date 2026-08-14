# CEO verdict

Do **not** shut down or redirect the old website yet.

The new WordPress site is the better long-term home because Pineapple controls it. But today, the old agency site has far more SEO authority, content, customer proof, city pages, tracking and commercial depth.

Think of it this way:

* **New site:** cleaner new building, but several rooms are unfinished.  
* **Old site:** crowded and outdated, but it owns valuable land on Google.

The winning move is to make `pineappleroofingllc.com` the conversion-focused primary brand, while carefully transferring the old domain’s authority through a page-by-page migration.

I audited all 14 URLs in the [new sitemap](https://pineappleroofingllc.com/sitemap_index.xml) and 220 of the 235 URLs in the [old sitemap](https://www.pineapplecontractors.com/sitemap.xml). This is a public-facing audit; GA4, Search Console, LSA, CRM and advertising-account data would be needed for a full profitability audit.

## Head-to-head comparison

| Area | New WordPress site | Old agency site | Winner today |
| :---- | :---- | :---- | :---- |
| Website ownership | Pineapple controls WordPress/Elementor | Agency-managed Scorpion platform | New |
| Searchable pages | 14 sitemap URLs | 235 sitemap URLs | Old |
| Local pages | One general DFW service-area page | Approximately 97 service-area pages | Old |
| Blog/content | Empty “Archives” page | Approximately 79 blog/archive URLs | Old |
| Customer reviews | Navigation currently returns to homepage | Large dedicated review library | Old |
| Commercial roofing | Very limited | TPO, EPDM, metal, BUR, PVC, emergency and industrial content | Old |
| Brand compliance | 52 uses of “free” across 15 crawled pages | 166 uses across 99 pages | Neither |
| Tracking detected | Direct GA4 only; no GTM or Meta Pixel detected | GTM, GA4 and Meta Pixel detected | Old |
| Form friction | Five required fields in the hero | Seven or more required fields | New, but still too long |
| Trust content | License, logos, financing and basic FAQs | Reviews, videos, gallery, press, certifications and locations | Old |
| Technical weight | Approximately 94 KB average HTML | Approximately 147 KB average HTML | New |
| Accessibility | 30 of 96 image instances missing alt text | 1,328 of 3,457 missing alt text | New |
| Future scalability | High, because Pineapple owns the system | Limited by agency control | New |

# New website audit

## What the new site does well

* It clearly explains roof replacement, roof repair, gutters, siding and storm damage.  
* The [insurance-claims page](https://pineappleroofingllc.com/roof-insurance-claims-help-in-dfw-pineapple-contractors/) introduces the CPPA and documentation-first process.  
* The [financing page](https://pineappleroofingllc.com/roof-financing-in-dfw-full-restoration-coverage-pineapple-contractors/) is one of the strongest pages: it explains GreenSky, financing limits, disclaimers and the process.  
* Phone number `972-928-0788` and RCAT number `03-0637` are highly visible.  
* Service pages contain FAQs and FAQ structured data.  
* Privacy policy and thank-you pages exist.  
* The site uses self-referencing canonical URLs.  
* The site is easier for Pineapple to change without waiting on an agency.

## Critical new-site problems

### 1\. Important navigation is broken

The menu links for:

* About Us  
* Reviews  
* Process  
* Contact

currently return customers to the homepage instead of opening the appropriate page.

This is a serious conversion problem. Customers wanting proof or contact information are taken in circles.

### 2\. Google has indexed pages that now return 404 errors

Google still shows previously published pages for:

* Reviews  
* Contact  
* Euless roofing  
* Grand Prairie roofing  
* Several blog articles

Those URLs currently return real `404` responses. They should be restored or permanently redirected to a relevant replacement page.

### 3\. The blog is essentially empty

The [blog page](https://pineappleroofingllc.com/blog/) only displays “Archives.” There are no visible articles, categories or useful customer resources.

### 4\. The site violates PM7 brand law

“Free” appears 52 times across 15 pages, including ten times on the homepage.

Replace all versions of:

* “Get a FREE Quote”  
* “Free inspection”  
* “Free estimate”

with:

* **Reserve Your Complimentary Professional Photo Audit**  
* **Complimentary Professional Photo Audit**  
* **Request Your Full Asset Restoration Coverage Evaluation**

### 5\. The site lacks real customer proof

The homepage talks about reviews but does not expose meaningful review content. It contains many generic logo images, but customers need:

* Named customer testimonials  
* Google review rating and count  
* Before-and-after projects  
* Photo-audit examples  
* Video testimonials  
* Actual Six Brothers/team story  
* Warranty information  
* Verified certification explanations  
* Residential and commercial case studies

The old site already has much of this material available to migrate. Its [review page](https://www.pineapplecontractors.com/reviews/) contains detailed customer experiences involving Jr, Will and George.

### 6\. Location targeting is confused

The homepage targets “Dallas,” the visible address is Lewisville, while the service page calls The Star in Frisco the headquarters.

From a customer and Google perspective, Pineapple needs one clear identity:

> Pineapple Contractors — Frisco/Lewisville-based roofing and construction company serving DFW.

Use separate, unique pages for Dallas, Frisco, Lewisville and each priority market.

### 7\. Conversion tracking is incomplete

I detected:

* GA4: `G-RP333WJP39`  
* No Google Tag Manager container  
* No Meta Pixel  
* No detectable Reddit Pixel

The thank-you page is indexable and still contains a form. It should be `noindex`, and it should only be reached after a verified submission.

### 8\. Forms ask for too much

The hero requires:

* Service  
* Address  
* Name  
* Phone  
* Email

Email should be optional. The ideal first-contact form is:

1. Name  
2. Phone  
3. Property address  
4. Roof concern, optional  
5. Email, optional

The site should also offer tap-to-call and tap-to-text.

### 9\. Technical and security work remains

* Four important pages are missing an H1.  
* The blog and thank-you pages are missing meta descriptions.  
* 30 of 96 image instances lack alt text.  
* Few images use WebP/AVIF.  
* Only part of the imagery is lazy-loaded.  
* The server sends `no-store/no-cache`, limiting effective caching.  
* Security headers such as HSTS, `X-Content-Type-Options` and `Referrer-Policy` were not detected.  
* Server-response times were inconsistent and often slow.

### 10\. Licensing language must be corrected

The construction page says Pineapple is a “licensed Texas general contractor” and uses RCAT \#03-0637 as proof. RCAT explains that Texas has no mandatory statewide roofing license; RCAT operates its own voluntary roofing-licensing program. Use:

> **RCAT Licensed Roofing Contractor \#03-0637**

Do not present RCAT as a Texas general-contractor license. [RCAT licensing information](https://roofingcontractors-texas.com/)

# Old website audit

## What the old site does well

The old site contains valuable digital assets:

* Approximately 235 sitemap URLs  
* Roughly 97 service-area pages  
* Roughly 79 blog/archive pages  
* Dedicated About, Reviews, Press, Financing and Gallery pages  
* Residential and commercial roofing sections  
* TPO, PVC, EPDM, metal, tile, slate and shingle information  
* Construction, restoration, hospitality and multifamily content  
* Careers, subcontractor and referral pages  
* Videos and substantial customer-testimonial content  
* General Contractor, address and geographic structured data  
* GTM `GTM-MDBKDTMM`  
* GA4 `G-2RHD103YQ5`  
* Meta Pixel `2545389655696737`  
* Better security headers and accessibility controls

Its city pages for Frisco, Grapevine and Euless are already appearing in search, and the [old blog](https://www.pineapplecontractors.com/blog/) contains years of accumulated content.

## Old-site problems

* The homepage tries to sell roofing, remodeling, flooring, pools, construction and restoration simultaneously.  
* The primary form contains too many required fields.  
* “Free” appears 166 times across 99 crawled pages.  
* Many city pages reuse the same Lewisville customer testimonial, which feels manufactured.  
* Multiple pages are missing H1 headings or contain two H1 headings.  
* Blog month archives reuse titles and descriptions.  
* Much of the city content is generic and location-swapped.  
* Thousands of image instances are missing alt text.  
* Lazy-loading is largely absent.  
* Nearly all imagery is in older formats.  
* “Roofing Licencse” is misspelled in the header.  
* Insurance language makes risky statements about getting claims approved.  
* The site lists Lewisville, Frisco, Austin and “coming soon” Houston/San Antonio locations. Only legitimate staffed locations should appear.  
* Social accounts and directories still point to the old domain.  
* The tracking container differs from the previously discussed Pineapple GTM container, so ownership and configuration need verification.  
* Branding shifts between Pineapple Roofing, Pineapple Contractors and Pineapple Construction.

There is also a certification and phone-number conflict. The sites emphasize IKO, while Pineapple has a live [GAF Certified profile](https://www.gaf.com/en-us/roofing-contractors/residential/usa/tx/plano/pineapple-roofing-llc-1135492) showing a different phone number. Verify every active certification and choose one canonical business phone across Google, GAF, RCAT, BBB, Yelp and social profiles.

# What I would build from the customer’s perspective

A homeowner is silently asking six questions:

1. “Do you service my city?”  
2. “Can I trust you?”  
3. “Can you prove what is wrong with my roof?”  
4. “Will you help me understand insurance and financing?”  
5. “What happens after I contact you?”  
6. “How quickly will someone respond?”

The new homepage should answer those questions in this order:

1. Location-specific headline  
2. RCAT, certification, review and warranty proof  
3. CPPA offer  
4. Three-field form plus phone/text  
5. Six Brothers/family story  
6. Before-and-after project proof  
7. Three-step process  
8. Insurance and financing explanations  
9. Verified customer reviews  
10. City/service FAQs

The marketing flywheel should work like this:

flowchart TD

    A\["Google, LSA, Yelp, Reddit and Social"\] \--\> B\["City \+ Service Landing Page"\]

    B \--\> C\["CPPA, Call or Text"\]

    C \--\> D\["CRM \+ 60-Second Response"\]

    D \--\> E\["Inspection, Proposal and Signed Job"\]

    E \--\> F\["Reviews, Photos and Case Studies"\]

    F \--\> A

# CEO resource allocation

I would not spread money equally across every platform. High-intent channels receive the majority.

| Investment | Share |
| :---- | ----: |
| Google Local Services Ads | 30% |
| Google Search Ads | 25% |
| SEO, website migration and Google Business Profile | 15% |
| Facebook and Instagram | 10% |
| Yelp | 5% |
| Reddit | 3% |
| Video and creative production | 5% |
| CRM, call tracking and automation | 4% |
| Controlled experiments/reserve | 3% |

Scale budgets based on **cost per signed job**, not cheap leads.

Google recommends Maximize Leads for LSA and enough budget to support approximately ten leads per week, while reviews and responsiveness also influence performance. [Google LSA bidding guidance](https://support.google.com/localservices/answer/10125017?hl=en)

For PM7, I would keep LSA focused on Roof Replacement initially, run coverage continuously, respond within 60 seconds and mark every lead as booked, completed, disputed or lost.

## Lean marketing team

These can be employees, contractors or assigned responsibilities:

* **Growth owner:** owns revenue, budget and weekly scoreboard.  
* **SEO/migration specialist:** WordPress, city pages, redirects and Search Console.  
* **Paid-media specialist:** Google, LSA, Meta, Yelp and controlled Reddit tests.  
* **Creative producer:** project videos, reviews, before/after and Six Brothers content.  
* **Revenue operations owner:** CRM, tracking, call attribution and automation.  
* **Lead-response coverage:** human or approved AI receptionist with a 60-second SLA.  
* **PM7 brand approver:** reviews every page, advertisement and post before publication.

PM7 can produce drafts at scale, but campaigns and posts remain paused until human approval.

# Channel plan

## Google and Maps

This is the primary battlefield.

* Create unique roofing, hail, repair and commercial pages for Frisco, Lewisville, Allen, Grapevine, Euless, Plano and McKinney.  
* Maintain exact name, address and phone consistency.  
* Add weekly GBP photos, project updates, services and approved Q\&A.  
* Request a review after every completed project—never gate or purchase reviews.  
* Add UTM tracking to GBP links.  
* Build separate residential, emergency and commercial campaigns.

Google says local visibility is based mainly on relevance, distance and prominence. [Google local-ranking guidance](https://support.google.com/business/answer/7091?hl=en)

## Tracking

Build one Pineapple-owned tracking system:

* One GTM container  
* One primary GA4 property  
* Google Ads website-call tracking  
* Dynamic call tracking with the main number preserved in business listings  
* Meta Pixel plus Conversions API  
* Reddit Pixel  
* Source, campaign, keyword and landing-page fields in CRM  
* Qualified, booked, inspected, signed and revenue stages  
* Offline signed-job data returned to Google and Meta

Google’s enhanced conversions can feed qualified and signed outcomes back to advertising instead of optimizing only for form submissions. [Google enhanced conversions for leads](https://support.google.com/google-ads/answer/15713840?hl=en)

## Yelp

* Claim and completely optimize the profile.  
* Correct category, service areas, business story, photos and canonical phone.  
* Respond to every review and message.  
* Test Yelp Ads with only 5% of budget.  
* Pause if cost per booked inspection or signed job exceeds Google.

Yelp positions its roofing product around customers actively requesting local roofing quotes. [Yelp roofing resources](https://business.yelp.com/services/roofing/)

## Reddit

Reddit should be education-first, never spam.

* Answer genuine North Texas roofing, hail and insurance-process questions.  
* Publish “what homeowners should photograph after hail” and similar guides.  
* Use a small DFW Lead Gen test.  
* Keep ads native and conversational.  
* Do not pretend to be a customer or hide Pineapple’s identity.

Reddit Lead Gen Ads can collect name, email and phone without forcing customers to leave Reddit. [Reddit Lead Gen Ads](https://www.business.reddit.com/advertise/ad-types/lead-gen)

## Social media

Every completed job should produce:

* One before-and-after Reel  
* One homeowner explanation  
* One CPPA educational post  
* One team/family story  
* One commercial or craftsmanship post  
* One Google Business update  
* One short YouTube video  
* One approved Reddit or community answer  
* One LinkedIn commercial case study

Meta should receive qualified-lead and signed-job feedback through its CRM/Conversions API—not just raw forms. [Meta Conversions API for CRM](https://www.facebook.com/business/help/571704773472628)

# 90–180 day execution plan

## Days 1–14: Stop the leaks

* Keep the old site live.  
* Fix every new-site navigation link.  
* Restore or redirect the indexed 404 pages.  
* Replace all banned “free” wording.  
* Correct licensing, insurance and certification claims.  
* Shorten forms and add consent language everywhere.  
* Install Pineapple-owned GTM, Meta Pixel and call tracking.  
* Noindex the thank-you page.  
* Fix caching, security headers, image formats and missing alt text.  
* Create a complete 235-URL migration spreadsheet.

## Days 15–45: Build customer trust

* Publish About the Six Brothers.  
* Publish real Reviews, Process, Contact and Project Gallery pages.  
* Build residential and commercial funnels.  
* Add warranty and verified certification pages.  
* Rebuild the seven priority city pages.  
* Connect every form, call and text to the CRM.  
* Activate the review-request workflow.  
* Launch LSA and tightly controlled Google Search campaigns after tracking passes.

## Days 46–90: Transfer authority

* Prioritize old URLs using Search Console traffic, rankings and backlinks.  
* Move the strongest blogs, service pages, reviews and case studies.  
* Apply one-to-one 301 redirects.  
* Never send hundreds of unrelated URLs to the homepage; Google warns this can confuse users and be treated as a soft 404\. [Google site-migration guidance](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)  
* Submit both sitemaps and the domain change through Search Console.  
* Update GBP, social profiles, directories and certification profiles.

## Days 91–180: Scale the winners

* Scale only channels producing qualified appointments and signed jobs.  
* Expand commercial TPO/property-manager campaigns.  
* Add controlled Yelp and Reddit tests.  
* Publish weekly local-answer content.  
* Convert every job into reviews, video and location proof.  
* Reach the target of **55% of total leads coming from tracked online channels**.

The first executive decision is simple: **keep the old website alive, repair the new website immediately, and turn the old site’s 235-page authority into fuel for the new Pineapple-controlled marketing machine.**

PM7 WordPress AI Bridge SOP

WP MCP Ultimate \+ Documents \+ Google Drive \+ Sites

**Purpose:** Add the supplied WordPress MCP workflow to the PM7 SEO operating system without granting AI uncontrolled production access.

**Applies to:** pineappleroofingllc.com as the owned WordPress property. The legacy pineapplecontractors.com authority migration remains page-by-page and separately approved.

**Status:** CONTROLLED PILOT ONLY. No live installation, credential creation, publication, plugin change, redirect, or deployment is authorized by this document.

# Executive decision

**Recommendation:** Adopt WP MCP Ultimate only as a staged, least-privilege WordPress execution bridge. Use Documents and Google Drive as the evidence and content layer, PM7 approval gates as the control layer, and WordPress drafts as the only permitted write target during the pilot.

**Production hold:** The supplied video and PDFs document v1.1.0. The current repository main branch identifies v2.1.0 and adds security hardening, while the public Releases page still shows v1.1.0 as the latest tagged release. PM7 must not install the older tagged package or an unreviewed development branch on production. Approve only a tested release artifact or pinned commit after security review, staging QA, checksum recording, and rollback preparation.

**Critical distinction:** The plugin connects an MCP-capable AI client to WordPress. It does not natively connect WordPress to Google Drive, Documents, or Sites. The AI workspace orchestrates those separate systems under PM7 rules.

# Evidence reviewed

| Source | Item | Decision value |
| :---- | :---- | :---- |
| YouTube demo | Claude Code Now Manages My WordPress Site \- MCP Plugin Demo | Shows install, health check, endpoint connection, post queries, draft/content rewriting, media and alt-text work. |
| Supplied PDF | WP MCP Ultimate \- Presentation, v1.1.0 | Claims 58 abilities in 10 categories and describes the endpoint, setup, troubleshooting, and then-pending security work. |
| Supplied PDF | WP MCP Ultimate Setup Guide, v1.1.0 | Documents WordPress 6.7+, PHP 8.0+, pretty permalinks, Application Passwords, Streamable HTTP, and the no-/sse endpoint rule. |
| Current repository | README, setup guide, abilities reference, plugin header, and security policy | Shows main-branch v2.1.0 code and current hardening defaults; creates a version/release discrepancy requiring a production hold. |

# What WP MCP Ultimate provides

**Endpoint:** https://YOUR-SITE.com/wp-json/mcp/wp-mcp-ultimate. Use the base endpoint exactly; do not append /sse. The transport is Streamable HTTP.

**Documented surface:** The repository describes 58 abilities covering posts, pages, media, users, plugins, menus, widgets, comments, taxonomy, options, and system operations, plus discovery tools.

**Authentication:** Application Passwords are supported. Current repository documentation also describes bundled OAuth 2.1 with PKCE for clients that require OAuth. Credentials and tokens must never be stored in a Google Doc, Google Drive content file, prompt, screenshot, repository, or WordPress page.

**Permissions:** Current security documentation says the endpoint requires edit\_posts by default and respects WordPress capabilities. This enables a dedicated least-privilege account rather than an administrator account for the PM7 pilot.

## What it does not provide

* A native Google Drive or Google Docs synchronization engine.  
* A native Google Sites publishing connector.  
* Automatic approval, claim verification, legal review, or SEO quality control.  
* A safe reason to give an AI administrator, plugin-management, user-management, options, delete, or production-publish access.  
* A replacement for backups, staging, activity logs, change records, redirect governance, Search Console, analytics, CRM attribution, or human publication approval.

# PM7 system architecture

| Layer | Role | PM7 rule |
| :---- | :---- | :---- |
| Google Drive | Evidence and asset source | Approved claims, briefs, source PDFs, real project media, review evidence, QA records. No secrets. |
| Documents / Google Docs | Structured working layer | SOPs, claims matrices, page briefs, review notes, approval records, and final copy. |
| PM7 AI workspace | Orchestration and QA | Reads approved sources, drafts, checks claims/brand/SEO, and prepares bounded WordPress actions. |
| WP MCP Ultimate | WordPress execution bridge | Read site state and create or update approved drafts/media only during the pilot. |
| Sites | Optional internal control center | May later display workflow status or approvals. It is not the PM7 production website and must not store credentials. |
| WordPress | Production CMS | Receives approved drafts; publication remains a separate human action after staging and final QA. |

# Authority model and permission policy

| Risk class | Default policy | Examples |
| :---- | :---- | :---- |
| Read-only | Allowed after connection approval | Site info, search, list/get posts and pages, media inventory, revisions, menus, categories, and current settings needed for diagnosis. |
| Draft content | Allowed only in staging or draft status after brief approval | Create/update draft posts or pages, upload approved media, update alt text, add approved categories/tags, and prepare internal links. |
| Publish or public navigation | Manual approval every time | Publish/schedule, live menu changes, homepage edits, public options, redirects, and any action that changes the customer experience. |
| Administrative/destructive | Disabled for the content agent | Users, roles, plugin install/activate/delete, options update, system debug, deletions, comment moderation, and bulk operations. |
| Credentials | Never placed in content systems | Application Passwords, Basic authorization values, OAuth tokens, recovery codes, and private configuration remain in an approved secret store. |

# PM7 brand and publishing guardrails

* Use CPPA and Complimentary language. The primary CTA is Reserve Your Complimentary Professional Photo Audit.  
* Use phone 972-928-0788 and RCAT Licensed Roofing Contractor \#03-0637 only from the approved claims matrix.  
* Use IKO Certified only while current evidence is recorded. Never substitute GAF.  
* Approved palette: navy \#1A365D, gold \#FBC02D, and sky blue \#00BFFF. No green.  
* Do not use free, cheap, bargain, warrior, toa, or six brothers in public copy unless a future approved claims decision explicitly changes the rule.  
* AI output remains in Outbox\_Drafts or WordPress draft/staging state. Nothing is published automatically.  
* Never invent review counts, ratings, years, awards, warranties, service areas, project results, prices, certifications, or licensing claims.

# Staged installation and connection SOP

## Approve the artifact

**Required result:** Record the selected release or pinned commit, checksum, source URL, security review, changelog, WordPress/PHP compatibility, and rollback owner. Do not use the v1.1.0 PDFs as proof that the package is production-ready.

## Prepare staging

**Required result:** Back up WordPress files and database, test restore, clone production to staging, record current plugins, and identify conflicts such as MCP Adapter, MCP Expose Abilities, or Abilities API.

## Create least privilege

**Required result:** Create a dedicated PM7 automation user with Editor or a tighter custom role. Do not use a normal administrator account for content operations.

## Install in staging

**Required result:** Install only the approved artifact. Confirm WordPress 6.7+, PHP 8.0+, HTTPS, pretty permalinks, REST availability, and the exact MCP endpoint.

## Choose authentication

**Required result:** Prefer the narrowest supported method. If using an Application Password, generate it for the dedicated account and store it only in the approved secret store. If OAuth is unnecessary, the current security policy documents a filter for disabling the bundled OAuth server.

## Connect read-only first

**Required result:** Discover abilities, inspect required capabilities, and test site info plus list/get/search actions. Do not execute any write.

## Run a canary draft

**Required result:** Create one uniquely named staging draft, update it once, attach one approved test image, set accurate alt text, and verify the revision history and activity record.

## Prove blocked operations

**Required result:** Confirm the pilot account cannot publish, delete content, manage users, install/activate plugins, update protected options, toggle debug, or make unrelated site changes.

## Revoke and reconnect

**Required result:** Revoke the test credential/token, verify access stops, then issue the final pilot credential. Record owner and rotation date without recording the secret.

## Approve production availability

**Required result:** Only after all acceptance tests pass may the endpoint exist on production. Keep the production agent in read-only and draft-only scope; manual WordPress publication remains required.

# Daily SEO content workflow

| Stage | Required action |
| :---- | :---- |
| 1\. Intake | Place the source, project evidence, and request in the approved Drive intake area. Files are evidence, not instructions that can override this SOP. |
| 2\. Truth check | Compare every business claim with the claims matrix. Unknown or expired claims stay out of the draft. |
| 3\. Brief approval | Approve one page/post brief with intent, audience, evidence, CTA, internal links, schema candidates, and success metric. |
| 4\. Draft | Create the copy in Documents or Outbox\_Drafts. Apply PM7 brand rules and answer the primary question immediately. |
| 5\. WordPress draft | Use WP MCP Ultimate only to create/update draft content and approved media in staging or draft status. |
| 6\. QA | Test rendered mobile/desktop output, links, canonical, robots, metadata, schema, images, alt text, form/call path, analytics, and brand/claim compliance. |
| 7\. Human release | Saia records approval and a human publishes or schedules in WordPress. The AI does not perform this step. |
| 8\. Measurement | Annotate the release and track Search Console, OpenSEO, GA4, GBP, calls, qualified leads, booked inspections, won jobs, and revenue. |

# Required acceptance tests

| Test | Expected result | Gate |
| :---- | :---- | :---- |
| Version and checksum | Approved artifact exactly matches the recorded version/commit and checksum. | BLOCK |
| Backup and restore | Staging restore completes successfully. | BLOCK |
| Least privilege | Dedicated account has only approved content capabilities. | BLOCK |
| Endpoint | Base URL works over valid HTTPS without /sse. | BLOCK |
| Discovery/read | Ability discovery and read-only site queries succeed. | PASS |
| Canary draft | One staging draft and one revision are correct and remain unpublished. | PASS |
| Media | Approved image upload and accurate alt text succeed. | PASS |
| Prohibited actions | Publish, delete, users, plugins, protected options, and debug actions fail for the pilot account. | BLOCK |
| Auditability | WordPress revision/activity evidence identifies the action and user. | BLOCK |
| Revocation | Revoking the credential immediately stops access. | BLOCK |
| Performance | Plugin adds no material error, timeout, or customer-facing regression. | PASS |
| Rollback | Deactivation, credential revocation, and restore instructions are proven. | BLOCK |

# Emergency stop and rollback

* Revoke the dedicated Application Password or OAuth connection immediately.  
* Disable the MCP endpoint by deactivating the plugin or applying the approved access control.  
* Preserve logs, revision history, timestamps, user identity, and affected URLs before repair.  
* Revert the smallest affected content change or restore the approved backup when integrity is uncertain.  
* Re-crawl affected pages and retest forms, analytics, canonicals, redirects, and index directives.  
* Reopen access only after root cause, corrective action, and Saia approval are recorded.

# How this changes the PM7 SEO SOP

**New controlled capability:** WP MCP Ultimate becomes an optional execution adapter between approved PM7 drafts and WordPress. It does not become the project manager, evidence store, approval authority, or publisher.

**No change to the core SEO loop:** OpenSEO striking-distance export \-\> Agent Kanban \-\> PAUSED Outbox\_Drafts \-\> human publish/update \-\> weekly OpenSEO, Search Console, lead, and revenue tracking.

**No change to migration safety:** Back up both sites, complete the exact URL map, publish destination parity first, test one-to-one 301s, keep the old domain controlled for 6-12 months, and use Search Console Change of Address only after the migration is technically ready and approved.

**Sites boundary:** A future Sites control center may display workflow status, approvals, and QA outcomes. It must remain separate from the production WordPress site, store no credentials, and require a separate build/deployment authorization.

# Approval commands

* APPROVE WP MCP ARTIFACT \<version-or-commit\> \<checksum\>  
* APPROVE STAGING INSTALL WP MCP ULTIMATE  
* APPROVE READ-ONLY CONNECTION TEST  
* APPROVE CANARY DRAFT TEST  
* APPROVE PRODUCTION ENDPOINT AVAILABILITY  
* APPROVE WORDPRESS DRAFT \<content-id\>  
* AUTHORIZE HUMAN PUBLICATION \<content-id\>

**Important:** These commands are intentionally separate. Approving installation does not approve a credential, production access, content creation, or publication.

# Sources

[Source video: Claude Code Now Manages My WordPress Site \- MCP Plugin Demo](https://www.youtube.com/watch?v=lJtAsSfTvNI)

[Official WP MCP Ultimate repository](https://github.com/AgriciDaniel/wp-mcp-ultimate)

[Official setup guide](https://github.com/AgriciDaniel/wp-mcp-ultimate/blob/main/docs/SETUP.md)

[Official security policy](https://github.com/AgriciDaniel/wp-mcp-ultimate/blob/main/SECURITY.md)

[Official abilities reference](https://github.com/AgriciDaniel/wp-mcp-ultimate/blob/main/docs/ABILITIES.md)

[Official releases page](https://github.com/AgriciDaniel/wp-mcp-ultimate/releases)

**Supplied attachments:** WP MCP Ultimate \- Presentation (11 pages, v1.1.0) and WP MCP Ultimate Setup Guide (4 pages, v1.1.0). Both were reviewed visually and textually. They are retained as historical setup evidence, not current production-security authority.
<!-- M7-FIREWALL-EXEMPT: governance-reference (CEO audit + WP MCP controlled-pilot SOP; "free"/"GAF" named only as issues to fix) -->
