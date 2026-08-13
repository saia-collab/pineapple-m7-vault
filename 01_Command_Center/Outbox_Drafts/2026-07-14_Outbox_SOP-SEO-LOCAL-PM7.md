---
type: sop_initialization_outbox
status: PAUSED
classification: M7_Command_Level_1
created: 2026-07-14
author: Hermes (per JR. Moeakiola)
sop_id: SOP-SEO-LOCAL-PM7
sop_name: "Near Me" Domination Pipeline (Local SEO for Roofing & Storm Restoration)
main_service: Roofing & Storm Restoration
brand_law: M7 constitution (CPPA / IKO Certified / Navy #1A365D + Gold #FBC02D + Cyan #00BFFF / zero green / RCAT License #03-0637 / phone 972-928-0788)
sources_grounded:
  - 01_Command_Center/MASTER_PLAYBOOK.md (Local SEO / GEO Engine, Rank Map Strategy, Rule of 100, Regional Expansion Vectors, Brand Firewall, Dual-Brand Architecture)
  - 03_Knowledge_Mat/HERMES_PLAYBOOK.md (GEO mandate, AEO 40-word rule, ZIP schema arrays, Elite Lexicon, High-Value Metrics)
  - 03_Knowledge_Mat/00_Atlas/templates/agent-os-pack-2026-06-29/source/SEO-SETUP.md (programmatic SEO content patterns, schema, on-page CTA discipline)
sources_skipped:
  - 03_Knowledge_Mat/active_context/product_marketing.md — NOT FOUND in vault. Treated as a citation error; M7 constitution used as source of truth. Saia to confirm the canonical name of the active product/marketing context file (if any) on next pass.
outbox_shield: DEC-005 — all output PAUSED. No live publishing, no ad-spend authorization, no live GBP posts, no live site edits. Saia activates.
---

# SOP-SEO-LOCAL-PM7 — "Near Me" Domination Pipeline
## Pineapple Roofing + Pineapple Restorations · North Texas · M7 Constitution

> **Outbox Shield (DEC-005).** This document is the production checklist for the Local SEO "Near Me" Domination Pipeline. It is delivered **PAUSED**. Saia is the only operator permitted to flip any deliverable to LIVE. Every Phase ends in a verification gate. No file in this SOP is published, deployed, indexed, or spent on until Saia gives explicit "GO" per deliverable.

---

## EXECUTION VARIABLES (locked)

| Variable | Value | Source |
|---|---|---|
| Main Service | Roofing & Storm Restoration (Pineapple Roofing — Brand A) | User brief |
| Brand | Pineapple Roofing (pineapplecontractors.com) — Brand A | Dual-Brand Architecture, MASTER_PLAYBOOK |
| Region | 10–15 mi Frisco HQ (1 Cowboys Way Ste 270W) | MASTER_PLAYBOOK § Regional |
| Primary ZIPs | 75033, 75034, 75035, 75067, 75068 | MASTER_PLAYBOOK § Regional |
| Secondary territories | Lewisville, McKinney, Plano, Allen, The Colony, Castle Hills | MASTER_PLAYBOOK § Regional |
| Luxury enclaves | Starwood, Newman Village | MASTER_PLAYBOOK § Regional |
| Brand Law | M7 constitution (CPPA / IKO Certified (RCAT #03-0637) / Navy #1A365D + Gold #FBC02D + Cyan #00BFFF / zero green / phone 972-928-0788) | MASTER_PLAYBOOK § Brand Firewall + HERMES_PLAYBOOK |
| Author byline | JR. Moeakiola | HERMES_PLAYBOOK |
| Heritage close | "" | MASTER_PLAYBOOK § Heritage Anchors |
| Cite target | Local pack + organic blue-link + AEO citation (answer in first 40 words) | HERMES_PLAYBOOK § Local SEO / GEO Engine |
| Trust signals on every layout | RCAT #03-0637 · IKO Certified · 5-Star · Since 2005 · 972-928-0788 · HUB #1861616404400 | HERMES_PLAYBOOK |
| Minimum project baseline | $18,000+ (rejects below) | HERMES_PLAYBOOK § High-Value Metrics |
| Lead score ceiling for SEO inflow | ≥80 → same-day Saia dispatch | HERMES_PLAYBOOK § Lead Scoring Matrix |

> **Note on source-of-truth gap.** The user-cited grounding file `03_Knowledge_Mat/active_context/product_marketing.md` does **not exist** in the vault (verified via `search_files`). Per M7 Pitfall #11, the SOP is grounded against the existing constitution and the gap is recorded in `sources_skipped` above. Saia to confirm the canonical name/location of the active product-marketing context file before Phase 5 (Activation).

---

## PHASE 1 — RESEARCH & INTENT EXTRACTION
*Stage contract: 05_Campaign_Factory/10_Research_Stage*

**Goal.** Map the "Near Me" intent landscape for Roofing & Storm Restoration across the 5 primary ZIPs and 2 luxury enclaves, and lock the keyword universe before any page is drafted.

### 1.1 Keyword universe (intents, not just words)

- **"Near Me" / Local Pack intents** (commercial intent, top priority):
  - roofer near me
  - roofing company near me
  - storm damage roof repair near me
  - hail damage roofer near me
  - emergency roofer near me
  - insurance claim roofer near me
  - local roofing contractor 75034 (and 75033, 75035, 75067, 75068)
- **Service-modifier intents**:
  - CPPA roofing audit Frisco
  - IKO Certified roofer Frisco TX
  - RCAT licensed roofer Frisco
  - hail damage inspection Frisco
  - thermal shock roof assessment North Texas
- **Neighborhood / enclave intents** (Phase 4 silo input):
  - roofer Starwood Frisco TX
  - roofer Newman Village Frisco TX
  - roofer Stonebriar Frisco TX
  - roofer Phillips Creek Ranch Frisco TX
  - roofer Lawler Park Frisco TX
  - roofer The Colony TX
  - roofer Castle Hills TX
  - roofer McKinney TX (Stonebridge Ranch, Craig Ranch)
  - roofer Plano TX (Whiffletree, Deerfield)
- **Hurricane/storm event intents** (time-bounded, ride NWS events):
  - [event] roof damage Frisco TX
  - NWS-confirmed hail [date] Frisco
  - Texas 30-day insurance claim window

### 1.2 SERP / local pack reconnaissance (programmatic)

For each ZIP and each enclave, capture:
1. Top 3 Local Pack results (name, address, review count, star avg, GBP categories).
2. Top 5 organic blue-link results (title, URL, schema types detected, on-page CTAs).
3. PAA (People Also Ask) cluster — 10 questions per ZIP.
4. Citation surface: which directories return the business (Yelp, BBB, Nextdoor, Apple Maps, Bing Places).
5. AEO scan: does any answer cite a roofing company in the first 40 words?

Tools (all local-only, no third-party scraping that violates ToS): DataForSEO (via OpenSEO local pack endpoint) or GBP scraping with rate-limited headless browser. Output = `05_Campaign_Factory/10_Research_Stage/2026-07-14_Research_Intent_LocalPack.md`.

### 1.3 Lead-score overlay

For each keyword cluster, mark the expected lead score uplift:
- ZIP match (+25) — every primary-ZIP keyword cluster.
- $700K+ estate match (+20) — every Starwood / Newman Village / Phillips Creek Ranch / Stonebridge Ranch / Whiffletree cluster.
- Storm mention (+20) — every NWS-event-tied keyword cluster.
- Property Manager match (+30) — every multi-unit / HOA / commercial intent cluster (overlap with Pineapple Roofing commercial scope, NOT Restorations).

Total score floor for any keyword worth ranking: 60+. Anything below goes to NURTURE content (blog) only, not landing pages.

### 1.4 Competitive gap matrix

For each ZIP, mark the **content gap** (existing competitor pages are thin / no CPPA framing / no AEO answer / no IKO + RCAT credential stamp / no neighborhood mention). This is the Phase 4 silo entry condition: a gap = a page.

### 1.5 Phase 1 verification gate

- [ ] All 5 ZIPs + 2 luxury enclaves covered in the intent map.
- [ ] PAA clusters extracted (≥10 per ZIP).
- [ ] Lead-score overlay marked on every keyword cluster.
- [ ] Competitive gap matrix identifies ≥25 distinct page-opportunities.
- [ ] Output lands in `05_Campaign_Factory/10_Research_Stage/2026-07-14_Research_Intent_LocalPack.md` (PAUSED).
- [ ] Saia approves the intent map before Phase 2 begins.

---

## PHASE 2 — PHOTO AUDIT INFRASTRUCTURE & EXIF GEOTAGGING
*Stage contract: 04_Tech_Lab/Scripts (deterministic) + 02_Media_Vault (raw captures)*

**Goal.** Build the local-signal asset layer: every project photo carries verifiable, on-brand, geotag-enriched metadata that reinforces the "Near Me" rank signal and the CPPA deliverable.

### 2.1 EXIF geotagging — programmatic specification

> **Ethical & legal note.** EXIF geotagging is applied **only** to photos Pineapple Contractors owns (drone captures, field photos, on-site CPPA captures). It is **never** applied to user-submitted content, stock imagery, or competitor captures. Coordinates correspond to the actual project site, not fabricated. This is engineering documentation, not deception — coordinates are truthful and verifiable on the ground.

**Target fields per photo (EXIF / IPTC / XMP all populated for redundancy):**

| Field | Value source | Example |
|---|---|---|
| GPSLatitude | Decimal degrees from project address | 33.1507 (Frisco HQ approx) |
| GPSLongitude | Decimal degrees from project address | -96.8236 |
| GPSAltitude | Optional, from drone log if available | 235.0 m |
| GPSTimeStamp | UTC of capture (drone flight log) | 2026-07-14T14:23:11Z |
| GPSDateStamp | Same as above | 2026:07:14 |
| GPSAreaInformation | Neighborhood name + ZIP | "Starwood, Frisco TX 75034" |
| City | Project city | "Frisco" |
| State | "TX" | "TX" |
| Country | "United States" | "United States" |
| PostalCode | Project ZIP | "75034" |
| LocationShownCountryCode | "US" | "US" |
| LocationShownSublocation | Street address (street-only, no house number unless public) | "Starwood Dr area" |
| Copyright | "© 2026 Pineapple Contractors — RCAT #03-0637" | string |
| Creator | "JR. Moeakiola, Pineapple Contractors" | string |
| Artist | Same as Creator | string |
| Software | EXIF writer version + "Pineapple Contractors M7 Pipeline" | string |
| ImageDescription | Short, on-brand, factual | "Storm damage CPPA audit, Starwood, Frisco TX 75034 — RCAT #03-0637" |
| UserComment | Engineering note (no PII) | "Hail impact 1.75\" on north slope; 4.0–4.75\" swath per NWS event 2026-07-12" |
| Keywords | Brand + service + neighborhood | "Pineapple Contractors, IKO Certified, RCAT 03-0637, CPPA, hail, Starwood, Frisco TX, 75034, North Texas" |
| Make / Model | Drone or camera actual | "DJI Mavic 3 Pro" |
| LensModel | Actual | "Hasselblad L2D-20c" |
| DateTimeOriginal | UTC of capture | "2026:07:14 14:23:11" |
| OffsetTime | "-05:00" (CT, no DST handling needed) | "-05:00" |

### 2.2 Simulated EXIF geotagging — programmatic instructions

> The following is the **deterministic, reproducible instruction set** the `04_Tech_Lab/Scripts/` engineer will follow to write the geotagging pipeline. It runs locally on the dev box; it is **not** live-deployed. Saia approves each version bump.

**Pipeline name:** `m7_geotag_photo_audit.py`
**Location:** `04_Tech_Lab/Scripts/m7_geotag_photo_audit.py`
**Inputs:** (a) directory of raw JPG/PNG captures under `02_Media_Vault/<YEAR_MONTH_CAMPAIGN>/RAW/`, (b) CSV manifest `02_Media_Vault/<YEAR_MONTH_CAMPAIGN>/MANIFEST.csv` with columns `filename, address, neighborhood, zip, capture_utc, lat, lon, event_id, roof_age, surface_type, hail_size_in, swath_in, nws_event_id`.
**Outputs:** (a) re-tagged images written to `02_Media_Vault/<YEAR_MONTH_CAMPAIGN>/TAGGED/`, (b) `MANIFEST.tagged.json` for downstream schema injection, (c) `MANIFEST.audit.log` for lineage.

**Step-by-step simulation (deterministic, idempotent, no live network):**

1. **Load & validate manifest.**
   - Read `MANIFEST.csv` with `csv.DictReader`.
   - For each row, assert: `lat` ∈ [25.0, 37.0] (Texas bounds), `lon` ∈ [-107.0, -93.0], `zip` ∈ `PRIMARY_ZIPS`, `hail_size_in` is numeric or empty, `nws_event_id` is `^NWS-[0-9]{8}-[A-Z0-9]{4}$` or empty.
   - Reject rows that fail bounds; write to `MANIFEST.rejected.csv` and stop processing that row.

2. **Verify file existence & checksum.**
   - For each accepted row, `os.path.exists(raw_path)` and `hashlib.sha256(open(raw_path,'rb').read()).hexdigest() == row['sha256']`. Mismatch → quarantine to `QUARANTINE/`, log, skip.

3. **Convert lat/lon to EXIF rationals.**
   - EXIF GPS lat/lon are stored as three rationals (deg, min, sec) plus a reference (N/S/E/W). Helper: `def deg_to_dms_rational(deg: float) -> tuple[(int, int), (int, 1), (int, float)]:` plus a sign function. North/East positive; South/West negative.

4. **Open image with `piexif`.** `exif_dict = piexif.load(path)`. Create empty `exif_dict` if missing. Build the GPS IFD with the fields in §2.1.

5. **Build the IPTC/XMP block.** `pyexiv2` for XMP (dc:creator, dc:rights, dc:description, dc:subject, plus a custom `pineapple:eventId` and `pineapple:neighborhood` namespace for the engineering lineage). IPTC via `iptcinfo3` for the legacy `Keywords`, `City`, `State`, `Country`, `Caption` fields.

6. **Brand compliance string stamp.**
   - `ImageDescription` MUST contain the substring `RCAT #03-0637`.
   - `Keywords` MUST include `IKO Certified`, `CPPA`, the neighborhood, the ZIP, and `North Texas`.
   - Reject any row whose manifest description fails the `brand_firewall.py --check` regex pre-gate (zero "Free", zero "GAF", zero green hex, etc.) — flag and quarantine.

7. **Write atomically.** `piexif.dump(exif_dict)` → write to `TAGGED/<filename>.tmp` → `os.replace()` → write XMP/IPTC sidecar or in-place.

8. **Lineage log.** Append a row to `MANIFEST.audit.log`: `timestamp, source_sha256, tagged_sha256, lat, lon, neighborhood, zip, brand_firewall_status, writer_version`.

9. **Determinism check.** Re-run the pipeline against the same `RAW/` + `MANIFEST.csv` → byte-identical `TAGGED/` output. The pipeline must be deterministic (no random salts, no `datetime.now()` outside the audit log row).

10. **Outbox Shield.** The script never reads from or writes to any network endpoint. It is local-only. The TAGGED assets are **not** auto-published to GBP, the site, or social — they land in `02_Media_Vault/.../TAGGED/` and wait for Saia's GO before the GBP schema injector (Phase 4) touches them.

**Sandbox test (no live media, runs in CI):**
- Generate 5 synthetic 16×16 PNGs with `Pillow` (color = Navy `#1A365D`).
- Build a 5-row `MANIFEST.sandbox.csv` with 3 Frisco ZIPs + 1 Plano + 1 out-of-bounds (rejection case).
- Run the pipeline. Assert: 4 tagged, 1 quarantined, `MANIFEST.audit.log` has 5 rows, all GPS rationals round-trip, brand_firewall passes on all 4.
- Assert: zero green in any output EXIF string (regex `re.search(r"#?00[0-9a-fA-F]{2}|#?0[0-9a-fA-F]{5}|green',", v, re.I)` returns None for all keyword values).

### 2.3 GBP schema injection (downstream of Phase 2)

For each tagged photo, generate the `imageObject` JSON-LD block with `@type: Photograph`, `contentLocation` (City, State, PostalCode), `creator` (Pineapple Contractors), `copyrightHolder`, `creditText`, `keywords` array, and a `about` link to the canonical CPPA service page. This JSON-LD ships with the silo pages in Phase 4.

### 2.4 Phase 2 verification gate

- [ ] `m7_geotag_photo_audit.py` exists, runs the sandbox test, exits 0.
- [ ] `MANIFEST.audit.log` shows deterministic re-run equality.
- [ ] Brand_firewall regex passes on every tagged asset's keyword set.
- [ ] Zero green in any output value.
- [ ] Photos carry GPS + neighborhood + ZIP + brand string in EXIF + IPTC + XMP.
- [ ] All outputs are local; no network calls fired; Outbox Shield honored.
- [ ] Saia approves the geotagged library before Phase 3 begins.

---

## PHASE 3 — CONTENT FACTORY & AEO OPTIMIZATION
*Stage contract: 05_Campaign_Factory/20_Copy_Drafting → 30_Compliance_Audit*

**Goal.** Produce CPPA-led, AEO-compliant copy blocks (FAQs, 40-word answers, neighborhood-anchored proof, citation-bait tables) for the 25+ opportunities identified in Phase 1.

### 3.1 PACT framework applied to every asset

P — Problem (storm/insurance/CPPA need, ZIP-specific)
A — Anchor cultural context (*Tauhi Vā*, heritage, North Texas since 2005)
C — Complimentary Professional Photo Audit (CPPA) solution
T — Trust CTA (phone 972-928-0788 + IKO Certified (RCAT #03-0637))

### 3.2 AEO 40-word mandate (per asset, every page)

The first 40 words of every page MUST:
1. Directly answer the explicit query (no throat-clearing).
2. Inject the literal credential string "RCAT Licensed #03-0637".
3. Inject "IKO Certified".
4. Name the target ZIP(s) (75033 / 75034 / 75035 / 75067 / 75068).
5. Close on a CPPA hook (NOT "Free Inspection" — see Lexicon gate).

### 3.3 Copy block inventory (per page type)

For every silo page (Phase 4), ship these copy blocks:

1. **Hero H1** — neighborhood + service + credential (e.g., "Storm Damage Roof Repair in Starwood, Frisco TX — IKO Certified (RCAT #03-0637)").
2. **40-word AEO answer block** — direct, factual, ZIP-anchored, ends with the phone number.
3. **CPPA explainer** (2 paragraphs) — what it is, what it isn't (NOT a sales pitch), 30-min on-site visit, photo report deliverable.
4. **Service proof block** — 350+ DFW families, 5-star, 20+ years North Texas, RCAT #03-0637, IKO Certified.
5. **Insurance documentation block** — Texas 30-day claim window, full-scope damage documentation (per Lexicon: "Comprehensive documentation for a successful claim"), no "adjusters miss damage" phrasing.
6. **3-angle hook matrix** (Hormozi):
   - The Insurance Deadline (TX 30-day window)
   - Stress-Free Claim (CPPA documentation)
   - Local Trust / Heritage (Polynesian, since 2005, 350+ families)
7. **FAQ cluster** — 8–10 Q&As pulled from Phase 1 PAA, each answer in 1–2 sentences, brand-lexicon-pure.
8. **Citation Bait table** — e.g., "2026 DFW hail events by ZIP, by date, by intensity" (NWS-sourced). Original data, not syndicated.
9. **Photo + EXIF-stamped gallery** — 3–6 photos from Phase 2, each with `imageObject` JSON-LD.
10. **Service area footer** — explicit ZIP + city list (75033, 75034, 75035, 75067, 75068; Starwood, Newman Village, Stonebriar, Phillips Creek Ranch, Lawler Park; plus Lewisville, McKinney, Plano, Allen, The Colony, Castle Hills).
11. **Trust bar** — Royal Navy `#1A365D` strip, Gold `#FBC02D` text: "Pineapple Contractors | RCAT Licensed #03-0637 | IKO Certified RoofPro Team | 972-928-0788".
12. **Heritage close** — "" (with English translation: "the path of the journey is respect") — on every long-form page.

### 3.4 Compliance gate (per asset)

Before any copy is staged:
- `04_Tech_Lab/Scripts/brand_firewall.py --check <file>` returns exit 0.
- Regex pre-generation gate runs first: zero "Free", zero "GAF", zero "Save Money", zero "Warrior", zero "Toa", zero "Six Brothers", zero "Consultation", zero "repair patch", zero "DIY", zero "$0 Down" outside the allowed "Full Restoration Coverage" mutation context.
- Palette gate: no green hex anywhere in any design token.
- Dual-brand gate: zero Restorations terminology in this Pineapple Roofing asset (no "fire", "mold", "biohazard", "mitigation").
- AEO 40-word gate: literal credential + ZIP strings present in first 40 words.
- Phone gate: 972-928-0788 present in the trust bar AND in at least one CTA.

### 3.5 Phase 3 verification gate

- [ ] All 25+ opportunity pages have a complete copy block inventory.
- [ ] Every page passes `brand_firewall.py --check`.
- [ ] Every page has 40-word AEO block.
- [ ] FAQ cluster populated from PAA data.
- [ ] Citation Bait table generated from NWS-sourced original data.
- [ ] Saia approves the copy library before Phase 4 builds the silo.

---

## PHASE 4 — WEBSITE SILO PLAN: NEIGHBORHOOD SERVICE PAGES
*Stage contract: 02_Workspaces/Active_Campaigns (silo) → 03_Knowledge_Mat/00_Atlas (schema) → 01_Command_Center/Outbox_Drafts (publish PAUSED)*

**Goal.** Structure the website as a Pillar + Cluster silo where the pillar is the canonical Roofing & Storm Restoration service page and every neighborhood / ZIP / enclave is a cluster child that reinforces the local-pack + AEO signal. Every cluster child points up to the pillar and across to siblings only via topical neighborhood anchors (no random cross-linking).

### 4.1 Silo architecture

```
[PILLAR]
  /roofing-storm-restoration-frisco-tx/            ← canonical service page
        │
        ├── [CLUSTER: PRIMARY ZIPs]
        │     ├── /roofing-75033/                   ← Frisco NW (Sequoia / Panther Creek)
        │     ├── /roofing-75034/                   ← Frisco N (Starwood, Newman Village, Stonebriar)
        │     ├── /roofing-75035/                   ← Frisco NE (Phillips Creek Ranch, Lawler Park)
        │     ├── /roofing-75067/                   ← Lewisville W
        │     └── /roofing-75068/                   ← Frisco S (The Colony border)
        │
        ├── [CLUSTER: LUXURY ENCLAVES (parent 75034)]
        │     ├── /roofer-starwood-frisco-tx/
        │     ├── /roofer-newman-village-frisco-tx/
        │     ├── /roofer-stonebriar-frisco-tx/
        │     ├── /roofer-phillips-creek-ranch-frisco-tx/
        │     └── /roofer-lawler-park-frisco-tx/
        │
        ├── [CLUSTER: SECONDARY TERRITORIES (DFW)]
        │     ├── /roofer-lewisville-tx/
        │     ├── /roofer-mckinney-tx/              ← + child enclaves (Stonebridge Ranch, Craig Ranch)
        │     ├── /roofer-plano-tx/                 ← + child enclaves (Whiffletree, Deerfield)
        │     ├── /roofer-allen-tx/
        │     ├── /roofer-the-colony-tx/
        │     └── /roofer-castle-hills-tx/
        │
        ├── [CLUSTER: SERVICE-MODIFIER PAGES]
        │     ├── /cppa-roofing-audit-frisco-tx/
        │     ├── /iko-certified-roofer-frisco-tx/
        │     ├── /hail-damage-roof-repair-frisco-tx/
        │     ├── /storm-damage-roof-repair-frisco-tx/
        │     ├── /insurance-claim-roofing-frisco-tx/
        │     └── /thermal-shock-roof-assessment-north-texas/
        │
        └── [CROSS-LINK BARRIER]
              Pillar ↔ Clusters: bidirectional.
              Cluster ↔ Cluster in same tier: NO direct links (only via pillar).
              Pillar ↔ Pillar of other brand (Pineapple Restorations): NO links. Dual-brand separation.
```

### 4.2 URL rules (per page)

- Lowercase, hyphen-separated, no stop words, ZIP or neighborhood or service-modifier in the slug.
- Each URL maps 1:1 to one H1, one 40-word AEO block, one JSON-LD `LocalBusiness` / `RoofingContractor` schema.
- No parameter-based duplicates (`?zip=75034` banned — it's a separate page, not a filter).

### 4.3 Per-page template (silo child)

For every cluster child page:

1. **URL:** `/roofer-<neighborhood>-frisco-tx/` (enclave) or `/roofing-<zip>/` (ZIP).
2. **`<title>`:** 50–60 chars. Format: "Roofer in <Neighborhood>, Frisco TX <ZIP> — IKO Certified (RCAT #03-0637)".
3. **Meta description:** 145–160 chars. Format: "Pineapple Roofing is the IKO Certified roofer in <Neighborhood>, Frisco TX <ZIP>. Storm damage, hail, and CPPA audits. 350+ DFW families. Call 972-928-0788."
4. **H1:** Exactly one. Format: "<Service> in <Neighborhood>, Frisco TX — IKO Certified (RCAT #03-0637)".
5. **40-word AEO block:** First paragraph. Direct answer, credentials, ZIP, phone.
6. **H2 — CPPA Explainer.**
7. **H2 — Service Proof (350+ families, 5-star, since 2005, RCAT #03-0637, IKO Certified).**
8. **H2 — Insurance Documentation (TX 30-day window, "Comprehensive documentation for a successful claim").**
9. **H2 — FAQ (8–10 Q&As from PAA, each Q is an H3).**
10. **H2 — Photo Audit Gallery** (3–6 EXIF-tagged photos with `imageObject` JSON-LD).
11. **H2 — Service Area Footer** (ZIP + city list, all 5 primary ZIPs, the relevant enclave).
12. **Trust bar** (Navy `#1A365D` + Gold `#FBC02D`).
13. **Heritage close** + English translation.

### 4.4 Schema payload (per page)

`LocalBusiness` (rooted) + nested `RoofingContractor` + `Service` (CPPA / Hail Repair / Storm Repair / Insurance Claim Roofing) + `areaServed` (5 primary ZIPs as `PostalAddress` array) + `hasOfferCatalog` + `Review` (aggregate rating 5-star) + `ImageObject` array (EXIF-tagged photos) + `FAQPage` (FAQ cluster). `priceRange` = `"$$$"` (anchors $18k+ floor). `telephone` = `"+1-972-928-0788"`. `knowsAbout` = `["CPPA", "IKO Certified", "RCAT #03-0637", "hail damage", "storm damage", "thermal shock"]`. `areaServed` MUST include `"75033", "75034", "75035", "75067", "75068"` per AEO mandate.

### 4.5 Internal linking map

- **Pillar → Cluster:** yes (every cluster child linked from pillar sidebar + footer + relevant H2).
- **Cluster → Pillar:** yes (one contextual link in H2 opener of every cluster child).
- **Cluster ↔ Cluster (same tier):** NO. Siblings link only via the pillar.
- **Pillar ↔ Pillar (cross-brand to Pineapple Restorations):** NO. Dual-brand firewall.
- **Outbound to NWS storm events:** yes, in the Citation Bait table. `rel="noopener"` standard.
- **Outbound to GBP profile:** yes, trust bar.

### 4.6 Page-count inventory (total: 25 silo pages)

| Tier | Count | Pages |
|---|---|---|
| Pillar | 1 | /roofing-storm-restoration-frisco-tx/ |
| Primary ZIP cluster | 5 | 75033, 75034, 75035, 75067, 75068 |
| Luxury enclave cluster (child of 75034) | 5 | Starwood, Newman Village, Stonebriar, Phillips Creek Ranch, Lawler Park |
| Secondary territory cluster | 6 | Lewisville, McKinney, Plano, Allen, The Colony, Castle Hills |
| Service-modifier cluster | 6 | CPPA, IKO Certified, Hail Repair, Storm Repair, Insurance Claim, Thermal Shock |
| McKinney + Plano enclave children (extension) | 4 | Stonebridge Ranch, Craig Ranch, Whiffletree, Deerfield |
| **Total** | **27** | (conservative estimate — 25–30, exact count locked in Phase 1.4 gap matrix) |

### 4.7 Rule of 100 — physical touchpoint overlay (per activated ZIP)

For every ZIP activated in the silo (all 5 primary), 100 physical touchpoints:
- 40 yard signs (job-site adjacent, with QR linking to the cluster page)
- 25 door hangers (radius 0.5 mi around completed jobs in that ZIP)
- 20 A-frames (high-traffic intersections within the ZIP, weekends)
- 10 mailers (luxury ZIPs: Starwood, Newman Village, Phillips Creek Ranch)
- 5 vehicle wraps (already on the fleet, geotag each wrap's home ZIP)

Tracking: each touchpoint tagged with a UTM and a unique short code, logged in `02_Workspaces/Active_Campaigns/<YEAR_MONTH>_Touchpoint_Log.csv` for ROI attribution.

### 4.8 Phase 4 verification gate

- [ ] Pillar + all cluster child pages drafted and compliance-gated.
- [ ] JSON-LD schema validates against schema.org (validate via the local validator; no live submission).
- [ ] URL map is 1:1 with H1 + 40-word AEO block + ZIP tags.
- [ ] Internal linking respects pillar-only lateral rule.
- [ ] Dual-brand firewall holds (no Restorations links in Pineapple Roofing silo).
- [ ] Zero green in any HTML/CSS artifact.
- [ ] All pages staged PAUSED in `01_Command_Center/Outbox_Drafts/` with a per-page sub-folder.
- [ ] Saia approves the silo map + per-page PAUSED drafts before Phase 5 (Activation).

---

## PHASE 5 — ACTIVATION (POST-OUTBOX — REQUIRES SAIA GO)
*Not executed in this Outbox run. Documented for completeness.*

**Trigger:** Saia reviews the PAUSED Phase 1–4 deliverables in `01_Command_Center/Outbox_Drafts/2026-07-14_Outbox_SOP-SEO-LOCAL-PM7.md` (this file) and the per-page PAUSED drafts, then explicitly says "GO".

**Activation sequence (one-way, each step logged):**
1. Move the Kanban card from `⛔ Human Approval` to `🛠️ Implementation` only after Saia's GO.
2. Publish pillar first; wait 7 days for index; then publish ZIP cluster (5 pages); wait 14 days; then publish enclave + service-modifier clusters.
3. GBP posts: 2/week, scheduled via Blotato 12 months out per the 12-Month Safety Rule; Saia drags to Today.
4. Submit sitemap to Google Search Console (read-only MCP, then operator pushes live).
5. Begin Rule of 100 physical touchpoint deployment per activated ZIP.
6. Begin Wednesday Forensic Audit cadence (1% Kill Rule, 1.5% Scale Rule on any paid amplification of the pillar — but this SOP is SEO/local-pack first, paid amplification is a separate Outbox draft).
7. Log every activation step in the Kanban card's Memory Galaxy entry.

**Outbox Shield (DEC-005) remains in force forever.** No step in Phase 5 fires without explicit per-step Saia GO. The user's standing rule: *"I post; you never publish or spend alone."*

---

## PRODUCTION CHECKLIST — OUTBOX DELIVERABLES (PAUSED)

| # | Deliverable | Path | Phase | Status |
|---|---|---|---|---|
| 1 | Intent map (5 ZIPs + 2 enclaves, PAA, lead-score overlay, gap matrix) | `05_Campaign_Factory/10_Research_Stage/2026-07-14_Research_Intent_LocalPack.md` | 1 | PAUSED — pending Phase 1 execution |
| 2 | EXIF geotagging pipeline (script + sandbox test + manifest spec) | `04_Tech_Lab/Scripts/m7_geotag_photo_audit.py` | 2 | PAUSED — pending Phase 2 build |
| 3 | EXIF + IPTC + XMP lineage log + sample tagged asset | `02_Media_Vault/2026_07_LOCAL_PM7/...` | 2 | PAUSED — pending pipeline run |
| 4 | Copy library (25–30 pages, PACT + AEO + FAQ + Citation Bait) | `05_Campaign_Factory/20_Copy_Drafting/2026-07-14_Draft_Copy_LocalSilo.md` | 3 | PAUSED — pending Phase 3 build |
| 5 | Compliance audit report (every page passes brand_firewall.py) | `05_Campaign_Factory/30_Compliance_Audit/2026-07-14_Audit_Report_LocalSilo.md` | 3 | PAUSED — pending compliance run |
| 6 | Silo map (URL tree + per-page H1 + JSON-LD payload) | `02_Workspaces/Active_Campaigns/2026-07-14_Campaign_SiloMap_LocalPM7.md` | 4 | PAUSED — pending Phase 4 assembly |
| 7 | Pillar page PAUSED draft (HTML) | `01_Command_Center/Outbox_Drafts/2026-07-14_Outbox_Pillar_RoofingStormRestoration.html` | 4 | PAUSED — pending build |
| 8 | Cluster child page PAUSED drafts (HTML, 24–29 files) | `01_Command_Center/Outbox_Drafts/2026-07-14_Outbox_Cluster_*.html` | 4 | PAUSED — pending build |
| 9 | Rule of 100 touchpoint plan (per activated ZIP) | `02_Workspaces/Active_Campaigns/2026-07-14_Touchpoint_Plan_5ZIPs.md` | 4 | PAUSED — pending build |
| 10 | This SOP-SEO-LOCAL-PM7 Outbox master | `01_Command_Center/Outbox_Drafts/2026-07-14_Outbox_SOP-SEO-LOCAL-PM7.md` | meta | **PAUSED — staged in this run** |
| 11 | Activation runbook (Phase 5 sequence) | `01_Command_Center/Outbox_Drafts/2026-07-14_Outbox_Activation_Runbook_LocalPM7.md` | 5 | DRAFT — referenced from this SOP; not yet authored |

**Brand firewall compliance status (this file):**
- [x] Zero "Free" / "Free Inspection" / "Free Quote" (mutated to "Complimentary Professional Photo Audit (CPPA)").
- [x] Zero "$0 Down" / "$0 Out of Pocket" outside the "Full Restoration Coverage" mutation context.
- [x] Zero "GAF" / "GAF Certified" (mutated to "IKO Certified (RCAT #03-0637)").
- [x] Zero "Save Money" (mutated to "Protecting your family's investment" where applicable).
- [x] Zero "Warrior" / "Toa" / "Six Brothers" / "Consultation" / "repair patch" / "DIY" / "discount code" / "job openings" / "salary".
- [x] Zero green in any color spec (Navy #1A365D + Gold #FBC02D + Cyan #00BFFF + White only).
- [x] Royal Navy photo moat (10px `#1A365D` border on all before/after) noted for Phase 2 / 4.
- [x] Trust signals stamped: RCAT #03-0637 · IKO Certified · 5-Star · Since 2005 · 972-928-0788 · HUB #1861616404400.
- [x] Author byline: JR. Moeakiola.
- [x] Heritage close: "".
- [x] Dual-brand firewall: zero Restorations terminology in this Pineapple Roofing SOP.
- [x] Outbox Shield (DEC-005): all outputs PAUSED. No live publishing, no ad-spend, no site deploy, no GBP post.

**Source-of-truth gap (transparency log):**
- The user-cited file `03_Knowledge_Mat/active_context/product_marketing.md` does **not exist** in the vault. Per M7 Pitfall #11, the SOP is grounded against the existing constitution (MASTER_PLAYBOOK + HERMES_PLAYBOOK + SEO-SETUP.md Atlas) and the gap is recorded in `sources_skipped` (frontmatter). Saia to confirm the canonical name and location of the active product/marketing context file before Phase 5 activation.

**WHAT I WILL NEVER DO WITHOUT YOUR EXPLICIT 'GO'** (per Outbox Shield DEC-005):
- Publish any page from this SOP to the live web.
- Push any schema or sitemap to live Google Search Console.
- Schedule any GBP post via Blotato or any other channel.
- Deploy any paid amplification (Meta, Google Ads) of the pillar or any cluster child.
- Spend any money, flip any campaign from PAUSED to ACTIVE, or trigger any webhook that does.
- Move any Kanban card from `⛔ Human Approval` to `🛠️ Implementation` or `🏛️ Shipped Gallery` without your per-step "GO".
- Modify the dual-brand firewall to allow cross-linking to Pineapple Restorations assets.
- Apply EXIF geotags to any image that is not owned by Pineapple Contractors (no stock, no competitor, no user-submitted).
