

# +11 prompt/code blocks (PM7 Ops & SOP (Mission Control))

## from: Automating Julian Goldie SEO Strategies with Hermes Agent Skills
```markdown
---
name: julian-goldie-seo-campaign
description: Automates striking-distance keyword extraction, content drafting, and WordPress scheduling.
version: 1.0
---

### 🎯 TRIGGER CONDITIONS
- Active when the operator requests a "Monday keyword run", "striking distance campaign", or "Goldie prompt execution" [11, 12].
- Loads automatically when keywords are identified in the OpenSEO Search Performance tab [5, 11].

### 📋 PROCEDURE

#### Step 1: Extract & Filter
- Pull live GSC data via `GSC_Connect.bat` [11].
- Open the OpenSEO Search Performance tab and identify keywords currently in "striking distance" (ranking positions 5–20) that exhibit high impressions [5, 11].

#### Step 2: Feed & Plan
- Feed the selected high-impression keyword to Hermes in Goal Mode [5, 11].
- Instruct Hermes to read the active business context inside `03_Knowledge_Mat/active_context/` [5].

#### Step 3: Execute (The Goldie Prompts)
- Apply the corresponding prompt from the 30-day sequence to generate a long-form, schema-ready city landing page [4, 13].
- Target dated, hyper-local structures (e.g., `/hail-storm-july-2026-frisco-tx/`) when executing event-driven plays [14].

#### Step 4: Staging (The Outbox Shield)
- Output the generated draft strictly in a PAUSED state inside `01_Command_Center/Outbox_Drafts/` [10].
- Never auto-publish directly to production [10].

#### Step 5: Compliance Audit (The Brand Firewall)
- Run the compliance checker: `python 04_Tech_Lab/scripts/brand_firewall.py --check` [15].
- Ensure 100% compliance: 0 green color references, correct brand lexicon (never say "free", use "CPPA"), and inclusion of all required identity anchors [10, 15].

#### Step 6: Deploy & Track
- Once Saia manually approves, publish to WordPress (via `wp_publish.py`) and schedule social syndication via Blotato [11, 16].
- Track keyword position climbs weekly on the OpenSEO Search Performance tab [11].

### ⚠️ PITFALLS TO AVOID
1. **The Goldfish Memory Trap:** Do not run broad content generations without confirming `03_Knowledge_Mat/` is fully synced [1, 5].
2. **Outbox Violations:** Never allow any agent to bypass the PAUSED staging folder or write directly to live production [10].
3. **Lexicon Contamination:** Programmatically reject any draft containing IKO Certified (must be IKO Certified) or referring to competitor names [10].
```

## from: Goldie Infinite Knowledge Engine Loop Operational Guide
```bash
   Enter relative path: 01_Command_Center/Outbox_Drafts/Content/McKinney_Lead_Campaign.md
   ```

## from: Goldie Infinite Knowledge Engine Loop Operational Guide
```bash
   git add . && git commit -m "session: automated backup launchpad v2" && git push
   ```

## from: The Pineapple Standard: Storm Response Canvassing and Token Optimization
```markdown
---
name: storm-response-canvassing
description: Coordinates the 72-hour hyper-local digital loop and physical door-to-door canvassing sequence following a North Texas hail event.
version: 1.0
---

### 🎯 TRIGGER CONDITIONS
- Active immediately after a hail storm hits a North Texas ZIP code (e.g., Frisco, Lewisville, Plano, McKinney) [3, 4].
- Triggered on-demand when the operator provides a ZIP code and commands a "Storm Playbook Run" [5, 6].

### 📋 PROCEDURE

#### Phase 1: Hour 0–24 — Data Sourcing & Instant Claiming
1. **Extract Storm Data:** Pull live weather data from NWS Fort Worth (weather.gov/fwd) or NOAA SPC Storm Reports (spc.noaa.gov/climo/reports) to pinpoint the exact ZIP codes hit and hail sizes [5].
2. **Instant GBP Push:** Draft storm updates for both Google Business Profiles: *"Hail hit [Neighborhood] last night. Ground-level damage is often invisible. Book your Complimentary Professional Photo Audit — (972) 928-0788."* [5, 7].
3. **Build Storm-Event Page:** Generate a dated, hyper-local landing page formatted strictly as `/hail-storm-[month]-[year]-[city]-tx/` that cites the official NWS weather data [5].

#### Phase 2: Hour 24–72 — Neighborhood Dominance & Canvassing
4. **Deploy Physical Canvassing:** Dispatch the crew to knock doors in the hit ZIP code [4, 8].
5. **Print QR Door Hangers:** Generate a print-ready door hanger design containing a QR code that routes homeowners directly to the newly published storm page's Complimentary Professional Photo Audit (CPPA) form [8].
6. **Escalate Ads:** Temporarily bump the Google Local Services Ads (LSA) budget for that specific geographic area for 2 weeks [8].

#### Phase 3: Week 1–2 — Conversion & Geolocation Compounding
7. **Document & Track:** Convert every signed CPPA into a documented photo report to handle insurance claims [8].
8. **Request Location-Specific Reviews:** Text completed jobs to request Google reviews that explicitly mention the neighborhood name (e.g., "we did a roof in [neighborhood]") to boost local map pack authority [8].
9. **Capture Proof:** Post before/after photos with geotargeted captions to GBP and social channels [8].

### ⚠️ PITFALLS TO AVOID
1. **Never Mix Vocab / Lexicon Rules:** Ensure the Brand Firewall blocks banned terms: never write "free" (always "CPPA"), never write "$0 down" (always "Full Restoration Coverage"), and never mention "IKO Certified" (always "IKO Certified") [2].
2. **Visual Palette Defense:** Programmatically reject any design assets referencing the color green. Only Royal Navy (#1A365D), Pineapple Gold (#FBC02D), and Status Cyan (#00BFFF) are permitted [2].
3. **Identity Anchors:** Every generated page and post must clearly display: *Polynesian-owned, RCAT #03-0637, IKO Certified, since 2005, 972-928-0788* [2].
4. **Automate the Machine, Never the Handshake:** Use AI to build pages, draft posts, and write review replies [9]. The operator (Saia) must physically knock doors, inspect roofs, and close the street [9].
```

## from: Claude Agent OS: Architecture and Workflow Design
```
  HUMAN OPERATOR (Saia)
         │
         ▼
  COMMAND CENTER (Dashboard on Port 3737/3000)
         │  (Tabs: Mission Control, Pipeline, Shared Memory, Execute, Skills, Studio, Jarvis)
         ▼
  AI AGENTS (Claude Code, Hermes, NotebookLM, Paperclip, Higgsfield)
         │  (All read Shared Memory & local vault files as context)
         ▼
  PIPELINE (5-Column Kanban: Idea → Plan → Human Approval (PAUSED) → Implement → Shipped)
         │
         ▼
  OUTPUT (Staged as PAUSED drafts in Outbox_Drafts/ to protect the brand)
         │
         ▼
  MEMORY (Obsidian, SHARED_MEMORY.md, and local markdown files)
```

## from: Hermes OS: Voice Control and Autonomous Agent Workflows
```
┌────────────────────────────────────────────────────────┐
│             THE INFINITE KNOWLEDGE ENGINE              │
├────────────────────────────────────────────────────────┤
│                                                        │
│   [ Layer 1: GEMINI NOTEBOOK (The Knowledge Vault) ]   │
│   • Ingests Collin/Denton building codes, GSC data,    │
│     and OMI voice-notes.                               │
│                        │                               │
│                        ▼ (Connected via MCP Bridge)    │
│                                                        │
│   [ Layer 2: HERMES / AGENT OS (The Operating Core) ]  │
│   • Runs unmetered local & cloud models (Sol/Luna).   │
│   • Triggers and pulls reports, audios, and layouts.   │
│                        │                               │
│                        ▼                               │
│                                                        │
│   [ Layer 3: OBSIDIAN VAULT (The Long-Term Memory) ]   │
│   • Shared database where every output is logged.      │
│   • Feeds fresh context back into the Knowledge Vault.  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

## from: Hermes OS: Voice Control and Autonomous Agent Workflows
```text
Act as the Lead Systems Architect running an autonomous Claude Gauntlet Loop. 
Our target goal is: [Draft a hyper-local, high-converting storm-restoration service page for our Plano, TX campaign].

GAUNTLET CONSTRAINTS:
1. Spawn specialized builder sub-agents in parallel to draft separate sections: the Hero block, the Local Building Code block, the IKO Certified shingle proof block, and the FAQ section.
2. Spawn blind critic sub-agents to evaluate each section. The benchmark for evaluation is Alex Hormozi's Value Equation: Dream Outcome (articulated using the "so that" headline formula), maximum Perceived Likelihood of Success, minimal Time Delay, and zero friction.
3. Apply our Brand Compliance Firewall: Convert all instances of "Complimentary Professional Photo Audit (CPPA)" to "Complimentary Professional Photo Audit (CPPA)", map "$0 down" to "Full Restoration Coverage", specify shingles as "IKO Certified RoofPro" or "IKO Certified Roofing Contractor", completely prohibit green colors, and embed the trust footer: Polynesian-owned · RCAT #03-0637 · IKO Certified · since 2005 · (972) 928-0788 · Frisco, TX.
4. Run the feedback loops autonomously. Builder agents must edit and refine their outputs. The critics must reject any draft that falls short of 9.5/10 against the benchmark.
5. Do not terminate the loop or write the output to our local C:/Pineapple Contractors M7/01_Command_Center/Outbox_Drafts/ folder until the critics are utterly wowed by the quality and our brand_firewall.py compliance script returns 0 errors. Mark the final compiled file status as STATUS: PAUSED.
```

## from: Optimizing AI Search Citations and Vault Listener Automation
```text
[2026-08-11 19:27:16] [INFO] === PM7 Obsidian Vault Listener Active ===
[2026-08-11 19:27:16] [INFO] Trust Anchors: Polynesian-owned · RCAT #03-0637 · IKO Certified · since 2005 · (972) 928-0788 · Frisco, TX
[2026-08-11 19:27:16] [INFO] Scanning target notes folder: C:/Pineapple Contractors M7/03_Knowledge_Mat/active_context/notes
```

## from: Optimizing AI Search Citations and Vault Listener Automation
```bash
python 04_Tech_Lab/python/vault_listener.py --test
```

## from: Hermes Agent OS: OMI Lead Extraction and Publishing SOP
```env
# WordPress Automated Publishing Configuration
WP_SITE_URL=https://pineappleroofingllc.com
WP_USERNAME=saia
WP_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx-xxxx
```

## from: Hermes Agent OS: OMI Lead Extraction and Publishing SOP
```bash
python 04_Tech_Lab/scripts/brand_firewall.py --check "01_Command_Center/Outbox_Drafts/plano_roofing_reconstruction.md"
```
