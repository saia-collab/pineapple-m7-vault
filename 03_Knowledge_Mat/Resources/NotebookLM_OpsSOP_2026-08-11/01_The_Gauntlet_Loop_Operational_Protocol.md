---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: 0411e8a1-b821-4de6-9c6f-407119339342
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# The Gauntlet Loop Operational Protocol

- [ ] **Monday: Target Goal Extraction & Keyword Signal Ingestion**
  - **Weekly Routine:** Extract Google Search Console (GSC) striking-distance keywords (positions 5.0 to 20.0). Select your top 3 localized target keywords (e.g., Plano storm roofing) to define the specific objective for your Gauntlet Loop prompt. Ingest fresh storm metrics and GSC queries as active sources inside Gemini Notebook.
  - **Required Dashboard Tab:** `OpenSEO → Search Performance` / `Notebook`
  - **Required Validation Script:** `run-monday-keywords.bat` (running `gsc_striking_distance.py`)

- [ ] **Tuesday: Brand Variables Mapping & Critic Structure Planning**
  - **Weekly Routine:** Review local case studies and newly transcribed OMI field voice notes. Map these into your prompt's builder context as real-world proof parameters. Define your strict brand compliance rules: map all estimate terms to "Complimentary Professional Photo Audit (CPPA)", enforce IKO Certified shingle language, and outlaw green colors.
  - **Required Dashboard Tab:** `Blotato` / `Outbox_Drafts`
  - **Required Validation Script:** `brand_firewall.py --check` on ad copy and visual layouts

- [ ] **Wednesday: Active Prompt Execution & Multi-Agent Compilation**
  - **Weekly Routine:** Paste your compiled 10-minute Gauntlet Loop prompt into your local Codex or Claude Code workspace. Trigger parallel sub-agents (builder bots) to draft the landing page code and media scripts while background blind critic agents run iterative evaluations against Alex Hormozi’s Value Equation.
  - **Required Dashboard Tab:** `Execute` / `Studio`
  - **Required Validation Script:** `brand_firewall.py --check` on all generated copy, HTML, and script assets

- [ ] **Thursday: Outbox Shield Audit & Automated WordPress Publishing**
  - **Weekly Routine:** Enforce the non-negotiable Outbox Shield by manually reviewing the Gauntlet-approved page drafts. Change the file header status from `status: PAUSED` to `status: ACTIVE` to trigger automated sitemap publishing via `wp_publish.py`. Individually reply to new Google Business Profile reviews naming the target neighborhood.
  - **Required Dashboard Tab:** `Pipeline` / `WordPress` / `Blotato`
  - **Required Validation Script:** Manual review and approval of PAUSED drafts in `01_Command_Center/Outbox_Drafts/`

- [ ] **Friday: Inbound Lead Parsing & GSC Indexation Verification**
  - **Weekly Routine:** Run a lead speed-to-lead verification pass to confirm that every new lead captured by your newly published Gauntlet landing pages was contacted or called within 5 minutes. Scan Google Search Console to verify that yesterday's published URLs have indexed.
  - **Required Dashboard Tab:** `OpenSEO` / `LSA Dashboard`
  - **Required Validation Script:** `GSC_Connect.bat`

- [ ] **Saturday: Content Repurposing & Performance Dashboard Audit**
  - **Weekly Routine:** Extract the highest-performing copy block from your Gauntlet landing page and format it into a 60-second vertical video script. Publish the reel across connected profiles and audit overall campaign CTR and search rankings.
  - **Required Dashboard Tab:** `Video Editor` / `Blotato` / `Mission Control`
  - **Required Validation Script:** `LAUNCH_ALL.bat` and `M7_DOCTOR.bat`

- [ ] **Sunday: Long-Term Memory Sync & Private GitHub Backup**
  - **Weekly Routine:** Sync all transcribed OMI voice notes and update your central `brand_vault.json` log with the successful prompt configurations and campaign metrics. Run a cleanup of the local directory system and backup your entire workspace to your private GitHub repository.
  - **Required Dashboard Tab:** `Shared Memory` / `Pipeline`
  - **Required Validation Script:** `M7_CLEANUP.bat` (followed by terminal execution of `git add . && git commit -m "session backup: gauntlet loop prompt execution" && git push`)