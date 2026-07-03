---
type: systems_architecture_and_marketing_playbook
status: active
version: 2.0 (Unified Engine — Live Document)
last_updated: 2026-06-19
classification: M7_Command_Level_1
agent_origin: Lead Systems Architect
confidence: 100
color_primary: "#1A365D"   # Royal Navy
color_secondary: "#FBC02D" # Pineapple Gold
color_status: "#00BFFF"    # Process Status Cyan
---

# PINEAPPLE CONTRACTORS M7 — AGENTIC OS MASTER PLAYBOOK

> **Single Source of Truth.** All agents (Claude Code, Hermes, OpenClaw, NotebookLM workflows) MUST read this file and ground against it before executing any task. Do not deviate from these rules. Do not hallucinate data. Request human confirmation if a required variable is missing.
>
> **Root Pathway (immutable):** `C:\Pineapple Contractors M7\`
> The legacy `C:\Pineapple-Mana-Global\` environment is decommissioned. No loose files in root. No directory drift.

---

## CORE ARCHITECTURE & MAP

All agents, scripts, and workflows operate strictly inside the **4-Fala Topography** (the woven mat). The structure is immutable: any orphaned directory, legacy folder, or unmapped file is purged by housekeeping daemons to prevent context drift. Agents must verify this exact schema via Model Context Protocol (MCP) reads before issuing any write command.

```text
C:\Pineapple Contractors M7\
├── 01_Command_Center\              # FALA 1 — The Strategic Brain (DNA Core)
│   ├── MASTER_PLAYBOOK.md          # Single source of truth (this file)
│   ├── tatafu.md                   # Brand core metrics & identity parameters
│   ├── GROUNDING.md                # Brand constitution (mirrored to 03_Knowledge_Mat)
│   ├── ANTIGRAVITY_OS.md           # Master system execution prompt config
│   ├── soul.md                     # Brand character bible (tonal persona)
│   ├── OS_Dashboard.html           # Local Mission Control (zero external hosting)
│   └── Outbox_Drafts\              # Locked staging — all live publishing PAUSED here
├── 02_Workspaces\                  # FALA 2 — The Active Mat (staging & execution)
│   └── Active_Campaigns\           # In-flight ad rendering & timeline assembly
├── 02_Media_Vault\                 # Raw drone captures, reels, brand-compliant imagery
│   └── (naming: YEAR_MONTH_CAMPAIGN_ASSET-TYPE)
├── 03_Knowledge_Mat\               # FALA 3 — The Neural Substrate (RAG warehouse)
│   ├── GROUNDING.md                # Redundant brand constitution copy
│   ├── raw\                        # Temporary ingestion bin (transcripts, field data)
│   └── 00_Atlas\                   # Index of all peripheral SOP files
├── 04_Tech_Lab\                    # FALA 4 — The Execution Engine (deterministic ops)
│   └── Scripts\                    # brand_firewall.py, m7_fetch.py, m7_scoring.py,
│                                   # m7_cleanup.py, m7_aggregate.py, video-multiplier.py
└── 05_Campaign_Factory\            # The 4-Fala Assembly Line (Stage Contracts)
    ├── 10_Research_Stage\          # Context: Intent Extraction
    ├── 20_Copy_Drafting\           # Context: Synthesis & Markdown Creation
    └── 30_Compliance_Audit\        # Context: Elite Guardrail Verification
```

**Fala Functions (one line each):**

- **01_Command_Center** — Immutable rulesets, brand constitution, dashboards, system prompts. External models are blocked from guessing brand logic; they read these files first.
- **02_Workspaces / 02_Media_Vault** — Active project execution, timeline assembly, and brand-compliant raw/compiled visual assets.
- **03_Knowledge_Mat** — Flattened, deduplicated markdown for low-latency RAG retrieval; raw input is flattened and mapped into `00_Atlas`.
- **04_Tech_Lab** — Localized sandbox for Python/Node modules, Docker runtimes, and MCP bridges. Zero unhandled exceptions permitted.
- **05_Campaign_Factory** — Strict Stage-Contract pipeline; work must meet programmatic criteria before advancing to the next directory.

---

## FILE SPECIFICATION TABLE

Every generated or migrated file follows the strict **`YYYY-MM-DD_Category_Topic`** naming convention so automation scripts parse data cleanly. Anchor files in `01_Command_Center` are exempt (fixed names).

| Folder Path | File Name | Operational Purpose |
| :--- | :--- | :--- |
| `01_Command_Center/` | `MASTER_PLAYBOOK.md` | Single source of truth rulebook (this file). |
| `01_Command_Center/` | `tatafu.md` | Brand core metrics, heritage rules, executive logic. |
| `01_Command_Center/` | `GROUNDING.md` | Brand constitution: banned lexicon, palette, file isolation laws. |
| `01_Command_Center/` | `ANTIGRAVITY_OS.md` | Master system execution prompt configurations. |
| `01_Command_Center/` | `soul.md` | Brand character bible for correct tonal persona. |
| `01_Command_Center/` | `OS_Dashboard.html` | Local single-page Mission Control interface. |
| `01_Command_Center/Outbox_Drafts/` | `YYYY-MM-DD_Outbox_Asset.md` | Locked draft assets awaiting human authorization. |
| `02_Workspaces/Active_Campaigns/` | `YYYY-MM-DD_Campaign_Brief.md` | Active campaign staging and timeline assembly. |
| `02_Media_Vault/` | `YEAR_MONTH_CAMPAIGN_ASSET-TYPE.*` | Raw drone captures and compiled marketing reels. |
| `03_Knowledge_Mat/00_Atlas/` | `YYYY-MM-DD_SOP_Onboarding.md` | Active member onboarding parameters. |
| `03_Knowledge_Mat/00_Atlas/` | `YYYY-MM-DD_FAQ_Community.md` | Validated consumer answers database. |
| `03_Knowledge_Mat/raw/` | `YYYY-MM-DD_Raw_Transcript.md` | Unstructured ingestion prior to flattening. |
| `04_Tech_Lab/Scripts/` | `YYYY-MM-DD_Script_Cleanup.py` | Local execution and automated housekeeping. |
| `04_Tech_Lab/Scripts/` | `brand_firewall.py` | Production-grade compliance scanner (`--fix`, `--report`). |
| `04_Tech_Lab/Scripts/` | `m7_scoring.py` | Lead scoring + banned-word and readability gating. |
| `05_Campaign_Factory/10_Research_Stage/` | `YYYY-MM-DD_Research_Intent.md` | Extracted market intent and lead scoring. |
| `05_Campaign_Factory/20_Copy_Drafting/` | `YYYY-MM-DD_Draft_Copy.md` | Synthesized campaign copy and video scripts. |
| `05_Campaign_Factory/30_Compliance_Audit/` | `YYYY-MM-DD_Audit_Report.md` | Final validation against brand directives. |

---

## STAGE-CONTRACT CONTEXTS

Every core folder/room contains a `CONTEXT.md` defining the **Input** and **Output** criteria required for data to pass through that node. Data that fails its node contract is rejected and returned upstream.

### `01_Command_Center\CONTEXT.md`
- **Input Criteria:** Authorized strategic updates from the Lead Systems Architect only.
- **Output Criteria:** Immutable, read-only `.md` rulesets for all local agents to ground against.

### `02_Workspaces\CONTEXT.md`
- **Input Criteria:** Approved execution blueprints and active, authorized ad-spend budgets.
- **Output Criteria:** Compiled assets packaged for deployment via local automation or direct API.

### `02_Media_Vault\CONTEXT.md`
- **Input Criteria:** Raw drone/field captures conforming to `YEAR_MONTH_CAMPAIGN_ASSET-TYPE`.
- **Output Criteria:** Brand-compliant imagery parsable by vision-language models without manual tagging.

### `03_Knowledge_Mat\CONTEXT.md`
- **Input Criteria:** Unstructured transcripts, field data, and historical project debriefs.
- **Output Criteria:** Flattened, deduplicated markdown structured strictly for RAG querying.

### `04_Tech_Lab\CONTEXT.md`
- **Input Criteria:** Verified MCPs and vetted Python/Node.js scripts.
- **Output Criteria:** Flawless terminal execution with zero unhandled exceptions.

### `05_Campaign_Factory\CONTEXT.md`
- **10_Research_Stage** — INPUT: Raw Meta webhooks / live search data. OUTPUT: Scored intent profiles (`intent.json`).
- **20_Copy_Drafting** — INPUT: Scored intent profiles. OUTPUT: Unverified markdown copy blocks.
- **30_Compliance_Audit** — INPUT: Draft copy. OUTPUT: 100% brand-compliant text approved for distribution.

---

## AUTOMATION READY CORE CONTENT

Flat, execution-ready procedures for direct consumption by local agents (Claude Code, OpenClaw, Hermes).

### Brand Firewall — Visual Law
- Primary palette: Royal Navy `#1A365D` (alt `#001122` / `#001a33`) and Pineapple Gold `#FBC02D` (alt `#FFD700` / `#E5A93C`).
- Process status highlights: Cyan `#00BFFF`.
- Negative space: White `#FFFFFF`.
- The color green — including all green hex codes, RGBA variants, CSS named greens, and Tailwind green utility classes — is strictly prohibited. Any green reference returns a critical build failure (exit code 1).
- Strict layout envelopes: **Top Banner = 140px** (Pineapple Gold `#FBC02D` · Royal Navy Impact font); Hook Font = 42px; Wrap Envelope = 860px; **Bottom Credential Bar = 95px** (Royal Navy `#1A365D` · Yellow Arial Bold · "Pineapple Contractors | RCAT Licensed #03-0637 | IKO Certified RoofPro Team").
- **Navy Photo Moat:** All before/after project photos must include a 10px solid Royal Navy `#1A365D` border to signal official engineering documentation.

### Brand Firewall — Elite Lexicon (mandatory mutations)
- "Free" / "Free Inspection" / "Free Quote" ➔ **"Complimentary Professional Photo Audit (CPPA)"**.
- "$0 Down" / "$0 Out of Pocket" ➔ **"Full Restoration Coverage"** (also acceptable, non-rewritten: "Insurance-Covered Restoration").
- "Save Money" ➔ **"Protecting your family's investment"**.
- "Adjusters miss damage" ➔ **"Comprehensive documentation for a successful claim"**.
- "GAF Certified" ➔ **"IKO Certified (RCAT License #03-0637)"**.
- Aggressive/generic legacy naming ➔ **"The Pineapple Standard"**.
- All output passes the CLI mutation filter (regex pre-generation gate) before any file is committed to disk.

### Heritage Anchors & Identity Core
- Identity: Polynesian-owned, family-operated, serving North Texas since 2005.
- Core principles: *Tauhi Vā* (sacred obligation to honor and protect shared spaces and relationships) and *Loto Tō* (humility and honest service).
- **Fā'i Kaveikoula (The Four Golden Pillars):** *Faka'apa'apa* (mutual respect), *Angafakatokilalo / Loto-tō* (humility, teachability), *Tauhi Vā* (nurturing relationships), *Mamahi'i me'a* (passion, loyalty, fierce dedication to execution).
- Major announcements and long-form copy close with a heritage wisdom anchor — primary: *"Ko e hala 'o e fononga ko e faka'apa'apa"* (the path of the journey is respect); secondary: *"Si'i pe kae ha'u"* (small but mighty).
- Voice: professional, authoritative, culturally rooted; no robotic corporate filler ("leverage", "synergize").

### High-Value Project Metrics (The Pineapple Standard)
- Minimum baseline entry: **$18,000+**. Projects below this are automatically rejected to protect margins.
- Speed-to-lead: leads contacted within **5 minutes**; any lead older than 5 minutes is classified dead.
- Estimate validity: strict **7-to-14-day** window to defend against material cost volatility.
- Lead Scoring Matrix (1–100): **+25** Frisco ZIPs, **+30** Property Managers, **+20** $700K+ estates, **+20** explicit storm-damage mentions. Score **≥80** triggers immediate same-day dispatch alert to Saia.
- Tagging: Residential Gold (3,500+ sq ft / $1M+ estates in 4.0"–4.75" hail swaths); Commercial Blue (40,000+ sq ft in 2.0"–2.5" swaths, targeting TPO/metal seam micro-fissures).

### Lead Qualification Pipeline (The Elite Filter)
- Meta Instant Forms built with high friction to repel renters and low-intent prospects.
- Required fields: Name, Phone, Home Address, Age of Roof, Insurance Carrier, Claim Status.
- Boss-Level qualifiers: legal deed holder? (disqualify if No); roof age (1–5 / 6–10 / 10+); neighborhood storm impact in last 30 days?
- Infrastructure: Zapier deprecated. Webhooks route natively through local n8n → centralized Google Sheets → AI agents via MCP.

### Digital Marketing Engine — 1-3-12 Meta Offensive
- **1 Campaign:** Centralized Campaign Budget Optimization (CBO) starting at $250/week.
- **3 Ad Sets (avatars):** The Local Fan (Frisco 35–65 near The Star); The Culture Seeker (heritage/community honor, *Tauhi Vā*); The Founder's Circle (B2B commercial owners, property managers, hotel operators, high-equity investors).
- **12 Creatives:** Advantage+ Flex Media, rotating dynamically across the 3 content angles.
- **1% Kill Rule:** Deactivate (set `PAUSED`) any creative below 1.0% CTR after a 48-hour stabilization window or 1,000 impressions.
- **1.5% Scale Rule:** Scale budget weighting by 15% intervals for any creative above 1.5% CTR with CPL under $50.
- **Cost metrics:** Target CPL < $50; absolute maximum threshold $250.
- **Advantage+ Override:** automated creative enhancements hardcoded `OFF` (no auto audio, contrast, or off-palette color injections).

### Digital Marketing Engine — 50/5/3 Lego Video Engine
- Total runtime: exactly **50 seconds** (1500 frames @ 30fps).
- Disruptive hook: frames **0–15** (first 0.5s) — pattern interrupt matched to the local DFW avatar.
- Core body: frames **16–1410** — factual density, drone analytics, active restoration footage.
- End Card: exactly **3 seconds** (frames 1411–1500) — Pineapple Gold text on Royal Navy ground, explicit CTA + 972-928-0788.
- Terminology firewall (zero tolerance) on all overlays/audio: mutate banned hook phrasing per the Elite Lexicon above.

### Copywriting Blueprint — PACT Framework
- **P**roblem identification → **A**nchor cultural context (*Tauhi Vā* / heritage) → **C**omplimentary Professional Photo Audit (CPPA) solution → **T**rust-based call to action.
- 1-3-12 angles map to: Heritage/Local focus · CPPA value · Premium material durability.
- Note on 50/5/3: two compatible readings — (a) runtime spec: 50s total, 5s hook, 3s end card; (b) production batch: 50 raw hooks, 5 narrative sequences, 3 CTAs. Both are sanctioned.

### Content Angle Matrix
- **Angle 1 — The Deadline (Urgency):** 30-day Texas insurance claim window.
- **Angle 2 — The Dream Outcome:** stress-free claims via professional documentation (CPPA).
- **Angle 3 — Social Proof / Heritage:** legacy, 350+ families protected, 5-star ratings, 20+ years in North Texas.
- Hook–Value–CTA structure: 1–2 sentence scroll-stopper → 3–6 sentence offer/transformation → 1 frictionless CTA.
- "Hammer Them" retargeting: micro-budget campaigns serving testimonials to 30-day engagers.

### Outbox Shield (Security Override — non-negotiable)
- Autonomous live publishing to Meta Ads, Google Ads, or live web is illegal under base prompt law.
- Every script, landing page, and post is written locally to `01_Command_Center/Outbox_Drafts/`.
- All campaign delivery variables are forcibly hardcoded to a `PAUSED` state on upload.
- Live activation requires explicit human authorization from an authorized operator. Human-in-the-loop is mandatory.

### Local SEO / GEO Engine
- Shift from blue-link SEO to Generative Engine Optimization (GEO): be cited by AI search engines.
- Extreme factual density, nested H1/H2/H3 headers, clean tables, "Citation Bait" (original case studies, definitive answers).
- AEO mandate: answer the explicit query within the first 40 words; inject "RCAT Licensed #03-0637" and "IKO Certified"; tag ZIPs 75033, 75034, 75035 in schema arrays.

### Regional Expansion Vectors
- Primary hub: 10-to-15 mile operational radius around Frisco, TX HQ (1 Cowboys Way, Ste 270W).
- Target ZIPs: 75033, 75034, 75035, 75067, 75068. Luxury enclaves: Starwood, Newman Village.
- Core DFW territories: Frisco, Lewisville, McKinney, Plano, Allen, The Colony, Castle Hills.
- Active expansion hub: Austin, TX (I-35 corridor). Staged vectors: Houston, San Antonio, West Palm Beach.
- **Rule of 100:** deploy exactly 100 physical touchpoints (A-frames, yard signs, mailers, door knocks) per activated ZIP.
- Rank Map Strategy: localized CPPA landing pages per high-value neighborhood to capture "Near Me" intent without spam-filter triggers.

### Dual-Brand Architecture (Pineapple Standard)

Two distinct brands operate under the M7 OS. **Never cross-contaminate terminology between them.**

| | Brand A — Pineapple Roofing | Brand B — Pineapple Restorations |
|:---|:---|:---|
| **Domain** | pineapplecontractors.com | pineapplerestorations.com |
| **Scope** | Estate & Commercial Portfolio Roofing, Thermal Shock, Hail | Fire Recovery, Water Mitigation, Mold Remediation, Biohazard |
| **Primary Avatars** | Frisco Multi-Unit Property Managers, Luxury Homeowners | Property Managers (emergency interior), Hotel Management |
| **Primary Hook** | Complimentary Professional Photo Audit (CPPA) | Emergency Rapid-Response Mitigation & Full-Scope Damage Documentation |
| **Credential** | IKO Certified (RCAT License #03-0637) | Same license; lead with emergency response SLA |

**Rule:** Roofing terminology must never appear in Restorations workflows and vice versa. Separate ad sets, separate landing pages, separate campaign briefs.

---

### Agentic Stack & Terminal Operations
- Orchestrator: Hermes (24/7 daemon via Docker + PM2) delegating to Claude Code over MCP.
- Knowledge graph: Obsidian local-first vault; bidirectional `[[links]]`; version-controlled to GitHub.
- Local models: Ollama (DeepSeek V4, Gemma 4, Qwen 3.x) routed via LiteLLM proxy (`drop_params: true`).
- Key scripts: `m7_fetch.py` (clean competitor scrape), `m7_scoring.py` (lead + compliance gate), `video-multiplier.py` (FFmpeg 9:16 reels), `firecrawl_drone_audit.py` (CPPA dossier).
- Core CLI: `/goal` (persistent loop), `/loop` (scheduled recurrence), `/compact` (context compress), `/clear` (state wipe), `/vault` (force-sync Obsidian), `/export` (GitHub push).

---

## EXTENDED KNOWLEDGE & TOOLING (linked SOPs)

The single source of truth references these detailed Atlas SOPs (merged from the NotebookLM/Gemini + agent-tooling playbooks):

- `03_Knowledge_Mat/00_Atlas/2026-06-17_SOP_AI_Knowledge_Architecture.md` — Three-Tier AI (Gemini Notebooks / NotebookLM 2.0 / Open NotebookLM), Gemini Gems PACT framework, GEO/AIO, Studio multimedia, QC checklist.
- `03_Knowledge_Mat/00_Atlas/2026-06-17_SOP_Agent_Tooling_Environments.md` — Claude Code vs Cursor vs VS Code, Aion UI multi-agent cowork, Hermes/Jarvis memory, OpenClaw, OMI ingestion, 64k-context fix.
- `03_Knowledge_Mat/00_Atlas/2026-06-18_SOP_Paperclip_Hermes_Empire.md` — Paperclip multi-agent company orchestration, Hermes daemon, cross-agent protocol.
- `03_Knowledge_Mat/00_Atlas/2026-06-19_SOP_YouTube_Analysis_Framework.md` — 8-prompt YouTube video extraction engine, four-agent production team, Protocol 0 persistent state.
- `03_Knowledge_Mat/00_Atlas/2026-06-19_SOP_Master_OS_Blueprint.md` — Architecture selection matrix, WhatsApp Cloud API integration, NotebookLM 3-phase deployment, Gemini modules, Fusion Protocol, SEO rank machine loop.
- `03_Knowledge_Mat/00_Atlas/2026-06-19_SOP_Video_Factory_Pipeline.md` — Google Flow AI video factory, multi-model crew routing, 3-panel Mission Control layout, NotebookLM AutoSync.
- `03_Knowledge_Mat/00_Atlas/2026-06-19_SOP_Local_Memory_Bridge.md` — Left Brain/Right Brain permission model, Obsidian vault init sequence, Ollama fallback config.
- `03_Knowledge_Mat/00_Atlas/2026-06-19_SOP_Obsidian_Interactive_OS.md` — Obsidian as interactive OS: Dataview, Canvas dashboards, custom plugin build, config.md-driven UI.
- `01_Command_Center/ANTIGRAVITY_OS.md` — the 5-Layer Orbit Grid (Capture → Vault → Intelligence → Command → Loop).
- `01_Command_Center/tasks/AGENTS.md` — agent orchestration & state matrix.
- Raw source playbooks preserved in `03_Knowledge_Mat/raw/` (zero-loss).

---

---

## EXTENDED OPERATIONAL FRAMEWORKS (v2.1 — 2026-06-29)

### Toa Lead Scoring Matrix (Routing Tiers)
| Score | Tier | Required Action |
|:---|:---|:---|
| **80–100** | **ELITE** | Same-day personal outreach by Saia. Do not route to setter. |
| **60–79** | **QUALIFIED** | 24-hour field rep assignment + full follow-up sequence. |
| **< 60** | **NURTURE** | 7-day automated email/SMS brand-conditioning sequence. |

Note: "Toa" is an internal routing label only — never use in customer-facing copy (banned term).

### CARPARK Closing Framework
Sequential 7-stage closing logic for calls and in-home presentations:
1. **C — Circumstances:** Confirm structural state. Documentation only, no opinion.
2. **A — Agitation:** Insurance clock + property value loss-aversion framing.
3. **R — Resolve:** Present Premium Estate & Commercial Portfolio Restoration solution.
4. **P — Proof:** 350+ DFW families, 5-star ratings, 20+ years.
5. **A — Agreement:** "Is a temporary patch something you'd settle for?"
6. **R — Review:** Walk through engineering timeline + documentation process.
7. **K — Kickoff:** Secure deposit authorization, schedule crew.

### The Lead Bridge (Phone Script SLA)
- Confirm appointment within 30 seconds: frame as "photo report, not a sales pitch."
- Promise an SMS alert exactly 20 minutes before arriving on-site.
- Speed-to-Lead: ≤ 5 min response · field rep dials within 120 sec of SMS alert.
- Missed call: voicemail + immediate follow-up text + 10-min retry task.
- Max 7 contact attempts. Cease on "Stop" or "Not interested."

### 3-Segment Lead Activation (Post-Close Nurture)
| Segment | Definition | Action |
|:---|:---|:---|
| Ghost Users | 0 purchases, no response | "Value Drop" — new storm data or project case study |
| One-and-Done | 1 purchase, no follow-up | Cross-sell sequence (restoration, adjacent property) |
| Power Users | Multiple referrals or repeat engagement | Referral offer + Founder's Circle status |

### Wednesday Forensic Audit (Weekly Kill Schedule)
Run via Meta Ads CLI every Wednesday:
1. Full account spend audit — flag any ad set over $250 CPL.
2. **1% Kill Rule:** Deactivate (`PAUSED`) any creative below 1.0% CTR after 48hrs / 1,000 impressions.
3. Google Ads Skill 2 (Wasted Spend Finder) — scrub low-intent search terms every 48hrs.
4. **Anti-Spike Bidding Rule:** Never use Auto Bidding when CPM spikes — lower daily budget to reset cost signals.
5. Google Ads Skill 17 (Auction Insights) — track regional competitor changes weekly.

### 12-Month Safety Rule + Outbox Shield (DEC-005)
- All automated social posts pushed to Blotato as drafts scheduled **12 months in the future** — Saia manually drags to "Today" to publish.
- No AI-drafted ad, post, SMS, or carousel goes live until Saia gives explicit GO. All outputs land PAUSED in `01_Command_Center/Outbox_Drafts/` — zero publish/post/send without human approval.

### Meta Pixel Conditioning Rule
Never fire the Meta Pixel for top-of-funnel signals (clicks, page views, DMs). Fire conversion pixel only on high-friction completions:
- Full Instant Form with all qualifier fields completed
- CPPA booking confirmed
- Inbound call from tracked number to 972-928-0788

### Extended Money Shield (Negative Filter — Additional Banned Terms)
Beyond the core lexicon table: `repair patch` · `shingle repair cost` · `DIY` · `discount code` · `job openings` · `salary` — all attract low-value or off-funnel traffic. Hard-block in brand_firewall.py LEXICON_RULES.

### B.L.A.S.T. Execution Protocol
5-phase deployment sequence for any new agent workflow, MCP, or campaign system:
1. **Blueprint** — Vision, schema, success criteria before touching code.
2. **Link** — API connectivity handshake, verify auth tokens.
3. **Architect** — Separate SOPs from Tools and CLIs.
4. **Stylize** — Apply Pineapple Standard formatting + brand compliance pass.
5. **Trigger** — Deploy + activate Self-Annealing Repair Loop (`/goal` + `/loop`).

### TCCA Prompt Stack (Agent Instruction Protocol)
- **T — Task:** State the desired output action precisely.
- **C — Context:** Who/what/why — brand role, audience, constraints.
- **C — Constraints:** Hard rules (banned terms, no green, PAUSED state, word count).
- **A — Ask:** AI must ask clarifying questions before executing if any variable is ambiguous.

### Multi-Model Self-Critique Loop
1. Generate initial asset (Claude Sonnet or Hermes marketing profile).
2. Score own output **1–10** against Elite Compliance criteria.
3. Implement own improvement suggestions.
4. Repeat until score plateaus at **9.5+** (typically 2–3 passes).
5. Cross-check with secondary model (Gemini Flash) to eliminate blind spots.

### Sabri Suby Hyperdopamine Formula
All video scripts and static ad copy use three-part rhythm:
1. **Pattern Interrupt** — Striking visual/statement that stops the scroll cold.
2. **Burning Intrigue** — Open a loop; raise the question without answering in the first 3 seconds.
3. **Big Specific Benefit** — Concrete outcome (not the service), written at 5th-grade reading level.

### Hormozi 3-Angle Matrix
| Angle | Name | Hook |
|:---|:---|:---|
| **1** | The Insurance Deadline | "30-day Texas storm claim window is closing..." |
| **2** | Stress-Free Claim | "Bulletproof engineering documentation. Zero sales pressure." |
| **3** | Local Trust / Heritage | "350+ DFW families. Polynesian heritage. RCAT Licensed." |

### IDEA File System (Obsidian Memory Architecture)
| Letter | Category | Content |
|:---|:---|:---|
| **I** | Insights | Strategic breakthroughs, market shifts, validated frameworks |
| **D** | Data | Raw sheets, specs, competitor data, lead analytics |
| **E** | Execution | SOPs, scripts, logs, deployment records |
| **A** | Assets | Brand kits, creative files, approved visuals |

Naming: `IDEA_YYYY-MM-DD_Category_Topic.md`

### 4-Agent Pipeline (Execution Architecture)
- **Orchestrator:** Traffic controller — routes requests via intent and CLAUDE.md map.
- **Researcher:** BOFU intelligence gatherer — scrapes Voice of Customer (VOC) quotes, outputs `audience-profile.json`.
- **Strategist:** Campaign architect — converts research into actionable SOPs, outputs `creative-brief.json`.
- **Copywriter:** Execution engine — finalizes compliant copy using 6 core hook formulas (Harsh Reality, Contrarian Challenge, Social Proof, Urgency, Dream Outcome, Heritage).

### Facebook Stars Monetization Sequence
1. **Post 1 (Education):** How Stars back the mission to protect local DFW families. No CTA.
2. **Post 2 (Authority):** Video walkthrough of a complex Premium Estate restoration installation.
3. **Post 3 (Conversion):** Testimonial-driven CTA prompting Stars.

### Oracle Cloud Sovereign Infrastructure (Spec)
- Platform: Oracle Cloud Free Tier — ARM Ampere A1 · Ubuntu 24.04 Minimal
- Allocation: 4 vCPUs · 24GB RAM · 200GB Block Storage
- Hardening: PAYG upgrade with strict **$1.00** budget cap
- Firewall: UFW ports 22 · 80/443 · 8000 (Coolify) · 6001-6002 (real-time)
- VPS Alt: Hostinger $5 · Node.js v24 · NPM v11 · ESM/CJS interop · 24/7 persistence

### Key Agent Patterns (from Skills Library)
- **Vault-as-Memory:** CLAUDE.md + `03_Knowledge_Mat/raw/session-notes/` = persistent zero-reset agent context. Archive weekly to `wiki/log.md`.
- **MCP Read/Write Separation:** Read MCPs (CRM, lead data) run always; Write MCPs (Blotato, Meta Ads) gated behind Outbox Shield.
- **Dynamic Loop:** `/goal` + `/loop 08:00` for scheduled overnight batch → results land in `Outbox_Drafts/MORNING_REVIEW.md`.
- **Vault Sync Rhythm:** `/vault` command at 08:00 CT pulls Obsidian state into Claude context; notes tagged `#execute` surface as tasks.

---

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
