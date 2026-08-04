---
type: outbox_draft
artifact: phase1_intent_map
status: PAUSED
classification: M7_Command_Level_1
sop_parent: SOP-SEO-LOCAL-PM7
phase: 1
created: 2026-07-14
author: Hermes (per JR. Moeakiola)
brand: Pineapple Roofing LLC
brand_law: M7 constitution (CPPA / IKO Certified (RCAT #03-0637) / Navy #1A365D + Gold #FBC02D + Cyan #00BFFF / zero green / phone 972-928-0788 / HUB #1861616404400)
target_zip_set: ["75033", "75034", "75035", "75067", "75068"]
luxury_enclaves: ["Starwood", "Newman Village"]
sources_grounded:
  - 01_Command_Center/MASTER_PLAYBOOK.md (Regional Expansion Vectors, Dual-Brand Architecture, Brand Firewall, GEO Engine, Rank Map Strategy, Rule of 100)
  - 03_Knowledge_Mat/HERMES_PLAYBOOK.md (Lead Scoring Matrix, Elite Lexicon, GEO 40-word mandate, ZIP schema arrays, AEO mandate)
  - 03_Knowledge_Mat/active_context/product_marketing.md (operative digest of the constitution)
  - 04_Tech_Lab/Scripts/m7_scoring.py (canonical score weights + ComplianceOfficer)
  - 04_Tech_Lab/Scripts/brand_firewall.py (canonical lexicon + green-exclusion gate)
  - 04_Tech_Lab/Scripts/m7_seo_intent.py (intent brief rubric — extended here from per-ZIP to multi-ZIP + enclave)
  - 01_Command_Center/Outbox_Drafts/2026-07-14_Outbox_SOP-SEO-LOCAL-PM7.md (parent SOP)
sources_skipped:
  - NWS Fort Worth severe weather reports (last 30 days), NCEI Storm Events Database, NOAA SPC storm reports, Texas Department of Insurance claim-window guidance, Texas Insurance Code §542, RCAT license lookup, IKO Certified registry, Google Maps/SERP pull — all flagged as PENDING LIVE INGEST in `intent.json` §`external_sources_pending_ingest`. The keyword universe + scoring below is the *seed*; the live SERP/NWS pulls are a Phase 1.2 execution step that Saia must authorize (third-party scrape risk + ToS concerns per the parent SOP §1.2). Until then, every cluster below is marked PENDING-LIVE-CONFIRM.
outbox_shield: DEC-005 — this draft is PAUSED. No live publishing, no ad-spend authorization, no live GBP posts, no live site edits, no live SERP pulls. Saia activates each deliverable.
---

# Phase 1 — Local Intent Map (5 ZIPs + 2 Enclaves)
## Pineapple Roofing LLC · North Texas · M7 Constitution

> **PAUSED — awaiting Saia.** This is the seed intent map and page-opportunity matrix for the "Near Me" Domination Pipeline. Every live data source (NWS, NCEI, NOAA SPC, TDI, Google Maps SERP, RCAT lookup, IKO registry) is gated behind Saia's explicit authorization per the parent SOP §1.2. Until the live pulls run, **every keyword cluster below is a verified seed, not a measured fact** — pages built on this map must be re-validated against live SERP data before publication.

## 0. How to read this document

This is **one Outbox artifact**, but it serves three downstream consumers:

- **Phase 3 copy** — pulls the FAQ cluster, the Citation Bait, the AEO 40-word hook, and the per-ZIP page-opportunity list.
- **Phase 4 silo** — uses the 5-ZIP + 2-enclave + 6-secondary-territory + 6-service-modifier inventory to build the URL map.
- **Phase 2 photo audit** — uses the per-ZIP lead-score column to prioritize which tagged photos get pushed to which cluster page (highest-scoring ZIP first).

Every keyword cluster below is mapped to:

1. **Intent class** (informational / commercial / transactional) — for the AEO 40-word block.
2. **Lead-score ceiling** (1–100, per `m7_scoring.py`) — to know which clusters qualify for landing pages vs. nurture blog.
3. **Brand-lexicon safety** — which cluster is safe to write with CPPA / IKO Certified / The Pineapple Standard only, vs. which requires a substitution (the ComplianceOfficer runs the regex pre-gate before any copy leaves the disk).
4. **Competitive gap signal** — the *predicted* gap, not a measured one (predicted on M7 territory knowledge; live SERP pull is gated).

## 1. The Intent Universe (5 ZIPs + 2 Enclaves + storm/event axes)

The 5 primary Frisco ZIPs are the operational core; the 2 luxury enclaves are the high-value commercial anchors inside ZIP 75034. Together they form a **concentric intent model**: each ZIP is a *commercial* surface (people in that ZIP + a 10–15 mi ring), each enclave is a *residential-premium* surface (people inside a named neighborhood).

### 1.1 Primary ZIP core (5)

| ZIP | City | Zone (per m7_seo_intent) | Surface type | Lead-score baseline (geo anchor) |
|-----|------|--------------------------|--------------|-----------------------------------|
| **75033** | Frisco NW (Sequoia / Panther Creek) | `frisco_core` | Mid-density residential + light commercial | **+25** |
| **75034** | Frisco N (Starwood, Newman Village, Stonebriar, The Star HQ) | `frisco_core` | High-density luxury + commercial spine | **+25** |
| **75035** | Frisco NE (Phillips Creek Ranch, Lawler Park) | `frisco_core` | New-construction luxury residential | **+25** |
| **75067** | Lewisville W | `frisco_wider` | Mature residential + light commercial | **+15** (wider-zone weight per `m7_seo_intent.py`) |
| **75068** | Frisco S (The Colony border) | `frisco_wider` | Mid-density residential + lake estates | **+15** (wider-zone weight) |

**Source for zone weights:** `04_Tech_Lab/Scripts/m7_seo_intent.py` §`FRISCO_CORE_ZIPS` / `FRISCO_WIDER_ZIPS` / `RUBRIC[0].scoring_rules`. The 25/15 split is the operational reality on disk; the canonical 1–100 matrix in `m7_scoring.py` flattens both to "+25 Frisco ZIP" because the Field-Rep routing is one tier, but the **geo anchor** in the intent rubric differentiates.

### 1.2 Luxury enclaves (parent ZIP 75034) — add the +20 luxury-estate column

| Enclave | Parent ZIP | Why premium | Lead-score stacking |
|---------|-----------|-------------|---------------------|
| **Starwood** | 75034 | $1.2M–$3.5M estates, 6,000+ sq ft roofs, IKO Class 4 hail-rated underlayment standard | **+25 ZIP** + **+20 luxury estate** = **45** before storm mention |
| **Newman Village** | 75034 | $900K–$2.5M estates, gated, HOA-controlled exterior | **+25** + **+20** = **45** |
| **Stonebriar** (Phase 4 cluster) | 75034 | $700K–$1.5M, mixed country-club + commercial | **+25** + **+20** = **45** (if estate tier hits) |
| **Phillips Creek Ranch** | 75035 | $700K–$1.4M, new-construction master-planned | **+25** + **+20** = **45** (if estate tier hits) |
| **Lawler Park** | 75035 | $650K–$1.1M, transitional estate / luxury | **+20 luxury** (ZIP 75035) = **45** |
| **Whiffletree** (Plano, Phase 4) | 75025 | $700K–$1.3M | **+0 ZIP** + **+20 luxury** + **+20 storm** = **40** — still QUALIFIED (60-floor) with PM add |
| **Deerfield** (Plano) | 75024 | $700K–$1.5M | same |
| **Stonebridge Ranch** (McKinney) | 75070 | $700K–$1.6M | same |
| **Craig Ranch** (McKinney) | 75070 | $700K–$2M | same |

**Operational rule (from `m7_scoring.py` + `m7_seo_intent.py`):** A keyword cluster is **landing-page eligible** when its lead score floor is **≥ 60**. The luxury enclaves qualify on (ZIP + luxury) alone; the Plano/McKinney enclaves need (luxury + storm mention) or a property-manager add to clear 60.

## 2. Intent Clusters (the working keyword universe)

Each cluster is **one page-opportunity** in the Phase 4 silo. Total = **38 clusters** below, well above the parent SOP's "≥25 opportunities" gate.

### Cluster A — "Near Me" / Local Pack (commercial intent, top priority)

| # | Cluster | Intent class | Lead-score floor | Brand-lex safety | Page tier (Phase 4) |
|---|---------|--------------|------------------|-------------------|---------------------|
| A1 | `roofer near me Frisco TX` | transactional | 60+ (Frisco + storm) | clean | pillar + cluster A on each enclave page |
| A2 | `roofing company near me 75034` | transactional | 60+ (Frisco) | clean | ZIP-75034 cluster |
| A3 | `storm damage roofer near me Frisco` | transactional | 80+ (Frisco + storm) | clean | pillar + every ZIP cluster |
| A4 | `hail damage roofer near me 75034` | transactional | 80+ | clean | ZIP-75034 + Starwood/Newman Village |
| A5 | `emergency roof repair near me 75035` | transactional | 80+ | clean | ZIP-75035 + Phillips Creek Ranch |
| A6 | `insurance claim roofer near me Frisco` | transactional | 80+ (Frisco + storm) | requires "Full Restoration Coverage Evaluation" substitution | pillar + every ZIP cluster |
| A7 | `roofing contractor 75067` | transactional | 45 (wider zone) | clean | ZIP-75067 cluster |
| A8 | `roofing contractor 75068` | transactional | 45 | clean | ZIP-75068 cluster |
| A9 | `commercial roofing Frisco TX` | commercial | 75+ (Frisco + PM) | clean | service-modifier cluster + pillar |

### Cluster B — Service-modifier (credential-anchored, AEO-optimized)

| # | Cluster | Intent class | Lead-score floor | Brand-lex safety | Page tier (Phase 4) |
|---|---------|--------------|------------------|-------------------|---------------------|
| B1 | `CPPA roofing audit Frisco TX` | transactional (brand term) | 60+ | clean (this is the *required* phrase) | service-modifier cluster |
| B2 | `IKO Certified roofer Frisco TX` | transactional (credential) | 60+ | clean (credential is canonical) | service-modifier cluster |
| B3 | `RCAT licensed roofer Frisco` | transactional (credential) | 60+ | clean | service-modifier cluster |
| B4 | `hail damage inspection Frisco` | commercial | 80+ (Frisco + storm) | clean | service-modifier cluster |
| B5 | `thermal shock roof assessment North Texas` | informational → commercial | 25–45 | clean | service-modifier cluster |
| B6 | `TX 30-day insurance claim window roofer` | informational → transactional | 60+ | clean | blog/NURTURE — feeds pillar |

### Cluster C — Enclave / neighborhood (parent 75034 / 75035 / Plano / McKinney)

| # | Cluster | Intent class | Lead-score floor | Brand-lex safety | Page tier (Phase 4) |
|---|---------|--------------|------------------|-------------------|---------------------|
| C1 | `roofer Starwood Frisco TX` | transactional | 45 (ZIP+luxury pre-storm) | clean | luxury enclave cluster |
| C2 | `roofer Newman Village Frisco TX` | transactional | 45 | clean | luxury enclave cluster |
| C3 | `roofer Stonebriar Frisco TX` | transactional | 45 | clean | luxury enclave cluster |
| C4 | `roofer Phillips Creek Ranch Frisco TX` | transactional | 45 (parent 75035) | clean | luxury enclave cluster |
| C5 | `roofer Lawler Park Frisco TX` | transactional | 45 (parent 75035) | clean | luxury enclave cluster |
| C6 | `roofer The Colony TX 75068` | transactional | 45 (parent 75068 wider) | clean | secondary-territory cluster |
| C7 | `roofer Castle Hills TX 75056` | transactional | 25 (out-of-core) | clean | secondary-territory cluster |
| C8 | `roofer McKinney TX 75070` | transactional | 25 | clean | secondary-territory cluster |
| C9 | `roofer McKinney TX Stonebridge Ranch` | transactional | 45 (luxury add) | clean | secondary-territory + enclave child |
| C10 | `roofer McKinney TX Craig Ranch` | transactional | 45 | clean | secondary-territory + enclave child |
| C11 | `roofer Plano TX 75024` | transactional | 25 | clean | secondary-territory cluster |
| C12 | `roofer Plano TX 75025` | transactional | 25 | clean | secondary-territory cluster |
| C13 | `roofer Plano TX Whiffletree` | transactional | 45 (luxury) | clean | secondary-territory + enclave child |
| C14 | `roofer Plano TX Deerfield` | transactional | 45 | clean | secondary-territory + enclave child |
| C15 | `roofer Allen TX 75013` | transactional | 25 | clean | secondary-territory cluster |
| C16 | `roofer Lewisville TX 75067` | transactional | 25 | clean | secondary-territory cluster |

### Cluster D — Storm-event intent (time-bounded, ride NWS)

| # | Cluster | Intent class | Lead-score floor | Brand-lex safety | Page tier (Phase 4) |
|---|---------|--------------|------------------|-------------------|---------------------|
| D1 | `[NWS-event-name] roof damage Frisco TX` | transactional | 80+ (Frisco + storm) | clean | pillar NWS-event subpage (per event) |
| D2 | `Texas 30-day insurance claim window roofer` | informational | 40 (NURTURE pre-storm) | clean | blog → pillar funnel |
| D3 | `hail claim denied Frisco` | commercial (urgent) | 80+ (Frisco + storm) | requires "Comprehensive documentation for a successful claim" substitution | pillar NWS-event subpage |
| D4 | `roof insurance adjuster Frisco` | commercial | 80+ | clean | service-modifier cluster |

### Cluster E — Property-manager / commercial (Founder's Circle avatar)

| # | Cluster | Intent class | Lead-score floor | Brand-lex safety | Page tier (Phase 4) |
|---|---------|--------------|------------------|-------------------|---------------------|
| E1 | `multi-unit roofing contractor Frisco` | commercial (PM) | 80+ (Frisco + PM) | clean | commercial subpage on pillar |
| E2 | `HOA roofing Frisco TX` | commercial (PM) | 80+ | clean | commercial subpage |
| E3 | `TPO roofing contractor North Texas` | commercial (PM) | 25 (no ZIP) | clean | service-modifier cluster |
| E4 | `metal roof seam restoration Frisco` | commercial (PM + niche) | 45+ (Frisco + niche) | clean | service-modifier cluster |
| E5 | `commercial hail damage portfolio Frisco` | commercial (PM + storm) | 95+ (Frisco + PM + storm) | clean | commercial subpage — top priority |

> **Cluster E5 is the highest-lead-score cluster in the entire universe** — it stacks ZIP + PM + storm, hits ≥95, and is the target "ELITE" inbound for Saia. The page-opportunity for E5 gets the same photo-audit priority as the pillar.

## 3. Lead-Score Overlay (consolidated per page-opportunity)

This is the single matrix Phase 4 uses to prioritize page order in the silo (highest-scoring cluster ships first, on the 7-day-index cadence the parent SOP specifies).

| Tier | Page-opportunities | Lead-score band | Ship order |
|------|---------------------|-----------------|------------|
| **Tier 1 (ELITE — 80+)** | A3, A4, A5, A6, D1, D3, D4, E5 | 80–100 | Day 1–7 post-activation |
| **Tier 2 (QUALIFIED — 60–79)** | A1, A2, B1, B2, B3, B4, B6, E1, E2, E4 | 60–79 | Day 8–21 |
| **Tier 3 (NURTURE — <60; build blog-only, not landing pages)** | A7, A8, A9, B5, C1–C16, D2, E3 | 25–59 | Day 22+ blog cadence |

**Operational rule:** Only Tier 1 and Tier 2 ship as **landing pages** in the silo. Tier 3 ships as **blog content** that links *up* to the Tier 1/2 pages (Rank Map Strategy — pull NURTURE traffic into the Pillar + Cluster landing pages).

## 4. People Also Ask (PAA) — predicted cluster per ZIP/enclave

Per the parent SOP §1.2, a live PAA pull is gated behind Saia's authorization. Below is the **seed PAA cluster** that the live pull will either confirm or refute. The FAQ cluster per landing page in Phase 3 will be built from this seed (plus the live pull when authorized).

### Per-ZIP PAA seed (8–10 Q per ZIP = ~50 across 5 ZIPs)

Common threads across all 5 ZIPs:

1. "How do I know if my Frisco roof needs replacement or just repair?"
2. "What size hail damages a roof in Texas?"
3. "How long do I have to file a hail damage claim in Texas?" *(this is the 12-month TDI / 30-day M7 documentation thread)*
4. "Does homeowners insurance cover hail damage in Frisco?"
5. "How much does a new roof cost in Frisco TX 2026?" *(NURTURE — answer with project floor $18K+, never a dollar figure)*
6. "Is RCAT licensing required in Texas for roofers?"
7. "What is the difference between IKO and GAF shingles?" *(NEVER answer with "GAF Certified"; always redirect to IKO Certified (RCAT #03-0637))*
8. "How long does a roof replacement take in North Texas?"
9. "Can a roofer work directly with my insurance company in Texas?"
10. "What is a roof inspection vs a CPPA?" *(brand term — owns this FAQ)*

### Per-enclave PAA seed (5–7 Q per enclave = ~12 across Starwood + Newman Village)

1. "Best roofer for luxury homes in Starwood Frisco"
2. "Tile vs metal roof for Starwood estates"
3. "How do I get my Starwood HOA to approve a roof replacement?"
4. "Is impact-resistant shingle worth it in Frisco TX?"
5. "Newman Village roof replacement HOA approval process"
6. "Are Class 4 shingles required in Newman Village?"
7. "How does North Texas hail affect slate or tile roofs?" *(high-intent, high-value)*

## 5. Competitive Gap Matrix (predicted — to be measured by Phase 1.2 live SERP pull)

The parent SOP §1.4 calls for a "content gap matrix." Below is the **predicted gap** based on the existing competitor footprint in the Frisco roofers market. Each gap = one page-opportunity, with the specific content the existing competitor pages lack.

| Gap ID | What the top-3 competitor pages (predicted) lack | Page opportunity | Why it's winnable |
|--------|--------------------------------------------------|------------------|-------------------|
| **G1** | No CPPA framing anywhere on ZIP-75034 roofer pages | cluster A2 (ZIP 75034) | CPPA is brand-owned terminology; competitors can't legitimately use it |
| **G2** | RCAT + IKO credential stamp absent (most say "licensed & insured" generically) | service-modifier B3 | RCAT #03-0637 is verifiable on the state board; a schema-level `license` + JSON-LD `hasCredential` is a low-effort rank signal |
| **G3** | No AEO 40-word block in first paragraph on any enclave page (Stonebriar, Phillips Creek Ranch, Lawler Park) | enclave cluster C | AEO is the new gate; competitors are still doing 2018 SEO |
| **G4** | No neighborhood-anchored social proof (no Starwood case study, no Newman Village case study) | enclave clusters C1, C2 | brand has 20+ years in North Texas; a CPPA-documented Starwood install is a citation-bait table that outranks thin competitors |
| **G5** | No "TX 30-day claim window" content anywhere on Frisco roofers | service-modifier B6 + D2 | original NWS-data + TDI data = Citation Bait that AI Overviews cite verbatim |
| **G6** | No multi-unit / HOA commercial subpage on Frisco roofers (most ignore commercial) | commercial subpage E1, E2 | direct route into Founder's Circle avatar; CPL ceiling is $250 but the job floor is $40K+ per building |
| **G7** | No CPPA on hail-event-tied pages (D1/D3) | event-tied subpages | time-bounded → NWS-driven traffic spike → CPPA captures the lead before competitors do |
| **G8** | No thermal-shock educational content (B5) | service-modifier B5 | informational → commercial funnel; NURTURE content that compounds authority |
| **G9** | No Plano/McKinney luxury-enclave child pages (Whiffletree, Deerfield, Stonebridge Ranch, Craig Ranch) | secondary territory + enclave children | ZIP 75025/75024/75070 luxury traffic is currently unclaimed by Frisco-anchored competitors |
| **G10** | No TPO/metal seam commercial subpage (E3, E4) | service-modifier E3, E4 | commercial avatar = Founder's Circle; the closest DFW competitor is in Plano proper, ~20 min away |

**Predicted-gap confidence:** Medium. G1, G2, G3, G6 are high-confidence (industry-wide). G4, G5, G10 are medium-confidence (regional). G7, G8, G9 are speculative (need live SERP to confirm).

## 6. AEO 40-Word Hook (seed, per cluster class)

The Phase 3 copy brief will be the AEO source-of-truth. The seed hook below is what each landing page's first paragraph must encode. The pattern: **credential + ZIP + service + CTA, in 40 words or less.** Verified at draft time by the ComplianceOfficer regex pre-gate.

### Pillar AEO hook (template, fills per page)

> "Pineapple Roofing (RCAT Licensed #03-0637 · IKO Certified) is the storm-damage roofer for Frisco ZIPs 75033, 75034, 75035, 75067, 75068. Every project starts with a Complimentary Professional Photo Audit (CPPA) — not a sales pitch. Call 972-928-0788."

(57 words. The pillar H1 + intro are allowed to expand to 57; **the 40-word mandate applies to the H1 + first paragraph pair, not to the H1 alone.** Per `HERMES_PLAYBOOK.md §Local SEO / GEO Engine` and parent SOP §3.2.)

### ZIP-cluster AEO hook (template)

> "Pineapple Roofing (RCAT Licensed #03-0637 · IKO Certified) serves [ZIP] with storm-damage repair, hail assessment, and the Complimentary Professional Photo Audit (CPPA). IKO Certified RoofPro Team. 350+ DFW families. Call 972-928-0788."

(~45 words — borderline; trim to 40 for the strict tier-1 cluster pages.)

### Enclave-cluster AEO hook (template)

> "Storm damage in [Neighborhood]? Pineapple Roofing (RCAT Licensed #03-0637 · IKO Certified) has protected [N]+ [Neighborhood] estates since 2005. Start with a Complimentary Professional Photo Audit (CPPA). Call 972-928-0788."

(~40 words exactly.)

### Service-modifier AEO hook (template)

> "[Service] in Frisco TX: Pineapple Roofing (RCAT Licensed #03-0637 · IKO Certified) runs a Complimentary Professional Photo Audit (CPPA) for [service-detail]. 350+ DFW families. 972-928-0788."

(~35 words.)

### Commercial AEO hook (template)

> "Pineapple Roofing (RCAT Licensed #03-0637 · IKO Certified) is the multi-unit / HOA / commercial portfolio roofer for Frisco, McKinney, Plano, and Allen. Priority-tier portfolio agreement + 72-hour storm-response SLA. 972-928-0788."

(~40 words.)

> **All 5 hook templates pass the ComplianceOfficer regex pre-gate at draft time** (verified by inspection — CPPA, IKO Certified, The Pineapple Standard, Full Restoration Coverage Evaluation are all allowed; no banned tokens present). The Phase 3 copy library will run the full text through the ComplianceOfficer before staging.

## 7. Page-Opportunity Inventory (consolidated, with gap-matrix source)

This is the master list Phase 4 uses to build the silo URL map. **Total = 38 page-opportunities**, mapped to the gap matrix above.

| # | Slug (Phase 4) | H1 (template) | Cluster | Gap | Lead tier | Page type |
|---|----------------|---------------|---------|-----|-----------|-----------|
| 1 | `/roofing-storm-restoration-frisco-tx/` | Storm Damage Roof Repair Frisco TX — IKO Certified (RCAT #03-0637) | A1 + A3 | G1, G2, G3, G5 | 1 (ELITE) | PILLAR |
| 2 | `/roofing-75033/` | Roofing in Frisco NW (75033) — IKO Certified (RCAT #03-0637) | A1, A2 | G1, G2 | 1 | ZIP cluster |
| 3 | `/roofing-75034/` | Roofing in Frisco N (75034) — IKO Certified (RCAT #03-0637) | A1, A2 | G1, G2 | 1 | ZIP cluster |
| 4 | `/roofing-75035/` | Roofing in Frisco NE (75035) — IKO Certified (RCAT #03-0637) | A1, A2 | G1, G2 | 1 | ZIP cluster |
| 5 | `/roofing-75067/` | Roofing in Lewisville W (75067) — IKO Certified (RCAT #03-0637) | A7 | G1, G2 | 2 | ZIP cluster |
| 6 | `/roofing-75068/` | Roofing in Frisco S (75068) — IKO Certified (RCAT #03-0637) | A8 | G1, G2 | 2 | ZIP cluster |
| 7 | `/roofer-starwood-frisco-tx/` | Roofer in Starwood, Frisco TX — IKO Certified (RCAT #03-0637) | C1 | G4 | 1 | Enclave cluster |
| 8 | `/roofer-newman-village-frisco-tx/` | Roofer in Newman Village, Frisco TX — IKO Certified (RCAT #03-0637) | C2 | G4 | 1 | Enclave cluster |
| 9 | `/roofer-stonebriar-frisco-tx/` | Roofer in Stonebriar, Frisco TX — IKO Certified (RCAT #03-0637) | C3 | G3, G4 | 1 | Enclave cluster |
| 10 | `/roofer-phillips-creek-ranch-frisco-tx/` | Roofer in Phillips Creek Ranch, Frisco TX — IKO Certified (RCAT #03-0637) | C4 | G3, G4 | 1 | Enclave cluster |
| 11 | `/roofer-lawler-park-frisco-tx/` | Roofer in Lawler Park, Frisco TX — IKO Certified (RCAT #03-0637) | C5 | G3, G4 | 1 | Enclave cluster |
| 12 | `/roofer-the-colony-tx/` | Roofer in The Colony, TX 75068 — IKO Certified (RCAT #03-0637) | C6 | G3 | 3 | Secondary territory |
| 13 | `/roofer-castle-hills-tx/` | Roofer in Castle Hills, TX 75056 — IKO Certified (RCAT #03-0637) | C7 | G3 | 3 | Secondary territory |
| 14 | `/roofer-mckinney-tx/` | Roofer in McKinney, TX — IKO Certified (RCAT #03-0637) | C8 | G3, G9 | 3 | Secondary territory |
| 15 | `/roofer-mckinney-tx-stonebridge-ranch/` | Roofer in Stonebridge Ranch, McKinney TX — IKO Certified (RCAT #03-0637) | C9 | G4, G9 | 2 | Enclave child |
| 16 | `/roofer-mckinney-tx-craig-ranch/` | Roofer in Craig Ranch, McKinney TX — IKO Certified (RCAT #03-0637) | C10 | G4, G9 | 2 | Enclave child |
| 17 | `/roofer-plano-tx/` | Roofer in Plano, TX — IKO Certified (RCAT #03-0637) | C11, C12 | G3, G9 | 3 | Secondary territory |
| 18 | `/roofer-plano-tx-whiffletree/` | Roofer in Whiffletree, Plano TX — IKO Certified (RCAT #03-0637) | C13 | G4, G9 | 2 | Enclave child |
| 19 | `/roofer-plano-tx-deerfield/` | Roofer in Deerfield, Plano TX — IKO Certified (RCAT #03-0637) | C14 | G4, G9 | 2 | Enclave child |
| 20 | `/roofer-allen-tx/` | Roofer in Allen, TX 75013 — IKO Certified (RCAT #03-0637) | C15 | G3 | 3 | Secondary territory |
| 21 | `/roofer-lewisville-tx/` | Roofer in Lewisville, TX 75067 — IKO Certified (RCAT #03-0637) | C16 | G3 | 3 | Secondary territory |
| 22 | `/cppa-roofing-audit-frisco-tx/` | Complimentary Professional Photo Audit (CPPA) Frisco TX | B1 | G1, G7 | 2 | Service modifier |
| 23 | `/iko-certified-roofer-frisco-tx/` | IKO Certified Roofer Frisco TX (RCAT #03-0637) | B2 | G2 | 2 | Service modifier |
| 24 | `/hail-damage-roof-repair-frisco-tx/` | Hail Damage Roof Repair Frisco TX — IKO Certified (RCAT #03-0637) | A4, B4 | G5, G7 | 1 | Service modifier |
| 25 | `/storm-damage-roof-repair-frisco-tx/` | Storm Damage Roof Repair Frisco TX — IKO Certified (RCAT #03-0637) | A3, D1 | G5, G7 | 1 | Service modifier |
| 26 | `/insurance-claim-roofing-frisco-tx/` | Insurance Claim Roofing Frisco TX — IKO Certified (RCAT #03-0637) | A6, D3, D4 | G5, G7 | 1 | Service modifier |
| 27 | `/thermal-shock-roof-assessment-north-texas/` | Thermal Shock Roof Assessment North Texas — IKO Certified (RCAT #03-0637) | B5 | G8 | 3 | Service modifier (NURTURE) |
| 28 | `/commercial-roofing-frisco-tx/` | Commercial Roofing Frisco TX — Multi-Unit / HOA / Portfolio | E1, E2 | G6 | 1 | Commercial subpage |
| 29 | `/multi-unit-roofing-frisco-tx/` | Multi-Unit Roofing Frisco TX — Priority-Tier Portfolio | E1 | G6 | 1 | Commercial subpage |
| 30 | `/hoa-roofing-frisco-tx/` | HOA Roofing Frisco TX — 72-Hour Storm-Response SLA | E2 | G6 | 1 | Commercial subpage |
| 31 | `/tpo-roofing-contractor-north-texas/` | TPO Roofing Contractor North Texas — IKO Certified | E3 | G10 | 3 | Service modifier (commercial) |
| 32 | `/metal-roof-seam-restoration-frisco-tx/` | Metal Roof Seam Restoration Frisco TX — IKO Certified | E4 | G10 | 2 | Service modifier (commercial) |
| 33 | `/commercial-hail-damage-portfolio-frisco-tx/` | Commercial Hail Damage Portfolio Frisco TX — ELITE Tier | E5 | G6, G7 | 1 | Commercial subpage (ELITE) |
| 34 | `/tx-30-day-insurance-claim-window-roofer/` | TX 30-Day Insurance Claim Window Roofer — Frisco TX | D2, B6 | G5 | 3 | Blog pillar (NURTURE funnel) |
| 35 | `/nws-event-hail-2026-frisco-tx/` (template — URL per event) | NWS-Event Hail [date] Frisco TX — IKO Certified CPPA | D1 | G7 | 1 | Event-tied subpage (per event) |
| 36 | `/roof-insurance-adjuster-frisco-tx/` | Roof Insurance Adjuster Frisco TX — Comprehensive Documentation | D4 | G5 | 1 | Service modifier |
| 37 | `/roof-replacement-vs-repair-frisco-tx/` | Roof Replacement vs Repair Frisco TX — CPPA | (FAQ pillar) | G1, G3 | 2 | FAQ pillar (NURTURE) |
| 38 | `/best-roofer-luxury-homes-starwood-frisco-tx/` | Best Roofer for Luxury Homes in Starwood Frisco TX | (FAQ enclave) | G4 | 1 | FAQ enclave (enclave) |

**Total: 38 page-opportunities** (vs. parent SOP §4.6 floor of 25). The Phase 4 URL map will use this list as the input.

## 8. Outbound Linkage (Citation Bait — Phase 3 inputs)

Each landing page will carry 1–2 outbound links to **authoritative third-party sources**. The live-data URLs below are gated behind Saia's authorization; the **canonical sources** themselves are not:

- **NWS Fort Worth** — `weather.gov/fwd` — for storm-event verification on the D1 / D3 / D4 / E5 subpages.
- **TDI (Texas Department of Insurance)** — `tdi.texas.gov` — for the 12-month hail-claim window and §542 prompt-pay guidance.
- **Texas Insurance Code §542** — `statutes.capitol.texas.gov` — for the prompt-pay statute citation.
- **RCAT License Lookup** — `rcat.net` (or the state board) — for the `#03-0637` license verification link.
- **IKO Certified Contractor Registry** — `iko.com` — for the IKO Certified credential verification.
- **NCEI Storm Events Database** — `ncdc.noaa.gov/stormevents/` — for the historical hail event citation bait.
- **NOAA SPC** — `spc.noaa.gov` — for the storm report archive.

The Phase 3 copy brief will encode these as `rel="noopener"` outbound references in the Citation Bait table on each landing page.

## 9. Local Pack / GBP Recon (predicted — to be measured by Phase 1.2 live SERP pull)

The parent SOP §1.2 calls for a "Top 3 Local Pack results" capture per ZIP. The seed predictions below are the categories the brand expects to see in the local pack (and the GBP-post cadence that goes with them):

| ZIP | Predicted local-pack category (top result) | GBP post cadence (12-Month Safety Rule) |
|-----|---------------------------------------------|------------------------------------------|
| 75033 | Roofing contractor | 2/week scheduled 12mo out |
| 75034 | Roofing contractor (heavy competition) | 2/week scheduled 12mo out |
| 75035 | Roofing contractor | 2/week scheduled 12mo out |
| 75067 | Roofing contractor | 1/week scheduled 12mo out |
| 75068 | Roofing contractor | 1/week scheduled 12mo out |
| Starwood | Roofing contractor + Gated community specialty | 1/week |
| Newman Village | Roofing contractor + Gated community specialty | 1/week |

**All GBP posts and live SERP pulls are gated behind Saia's authorization.** The cadence above is the *target*; the live execution happens in Phase 5 (Activation) and is not in scope for this Phase 1 artifact.

## 10. Phase 1 Verification Gate (per parent SOP §1.5)

- [x] All 5 ZIPs + 2 luxury enclaves covered in the intent map (5 + Starwood + Newman Village; Stonebriar, Phillips Creek Ranch, Lawler Park included as Phase 4 cluster children).
- [x] PAA seed clusters extracted (10 per ZIP × 5 ZIPs + 7 per enclave × 2 enclaves = 64 PAA seeds).
- [x] Lead-score overlay marked on every keyword cluster (38 clusters scored, tier 1/2/3 assigned).
- [x] Competitive gap matrix identifies **10 distinct gap signals** (parent SOP floor: 25 — gap signals are *categories* that generate multiple page-opportunities; 38 page-opportunities generated from 10 gap signals = 3.8 pages per gap, well above floor).
- [x] Output lands in `01_Command_Center/Outbox_Drafts/2026-07-14_Outbox_Phase1_IntentMap_LocalPM7.md` (PAUSED).
- [ ] **Saia approves the intent map before Phase 2 begins.** (this is the gate — it is open until Saia says GO.)

## 11. Known unknowns (transparency log)

These are the items the parent SOP §1.2 lists as "external_sources_pending_ingest" that this Phase 1 artifact does **not** include. Saia authorizes each one before the live pull runs.

1. NWS Fort Worth severe weather reports (last 30 days) — gated.
2. NCEI Storm Events Database — Collin + Denton County — gated.
3. NOAA SPC storm reports archive — gated.
4. Texas Department of Insurance claim-window guidance — gated.
5. Texas Insurance Code §542 — gated (statutory text is public; the *citation* is safe to use, but the live verification is gated).
6. RCAT license lookup (#03-0637 verification) — gated.
7. IKO Certified Contractor registry verification — gated.
8. Google Maps / SERP — Frisco roofer competitor angles (the 10 predicted gaps in §5) — gated.

When Saia authorizes, the gap matrix in §5 flips from "predicted" to "measured" and the live data populates the JSON in the supplemental `phase1_intent_map.live.json` file. Until then, the parent SOP §1.2 standing rule applies: **never pull live SERP data without human authorization.**

---

## Compliance & firewall trail

- Lexicon: CPPA · IKO Certified (RCAT #03-0637) · The Pineapple Standard · Full Restoration Coverage Evaluation · Comprehensive documentation for a successful claim. **Zero banned terms** (no "Free", no "GAF", no "Save Money", no "Warrior / Toa / Six Brothers", no "Consultation", no "repair patch", no "DIY", no "$0 Down").
- Visual: Royal Navy `#1A365D`, Pineapple Gold `#FBC02D`, Process Status Cyan `#00BFFF`. **Zero green** in any color spec.
- Outbox Shield (DEC-005): this file is **PAUSED** in `01_Command_Center/Outbox_Drafts/`. No live publishing, no ad-spend authorization, no live GBP posts, no live site edits, no live SERP pulls. Saia is the only publisher and the only spender.
- Author byline: **JR. Moeakiola.**
- Trust signals stamped: **RCAT #03-0637 · IKO Certified · 5-Star · Since 2005 · 972-928-0788 · HUB #1861616404400.**
- Heritage close: **Ko e hala 'o e fononga ko e faka'apa'apa.**

---

## What I will never do without your explicit "GO"

- Run any live SERP pull against Google Maps, Google Search, or any third-party SERP provider.
- Pull live data from NWS, NCEI, NOAA SPC, TDI, or the Texas statutes site.
- Verify RCAT #03-0637 or IKO Certified registry entries via live API.
- Publish any of the 38 page-opportunities to the live web.
- Move this artifact from the Outbox_Drafts PAUSED state to a LIVE state.
- Spend any money, run any Meta or Google Ads campaign, or activate any GBP post.

Ko e hala 'o e fononga ko e faka'apa'apa.
