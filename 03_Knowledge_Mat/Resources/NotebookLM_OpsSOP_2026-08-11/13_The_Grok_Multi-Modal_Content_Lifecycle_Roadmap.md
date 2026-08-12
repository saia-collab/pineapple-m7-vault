---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: 9409ac41-e477-428d-b74c-58485bb3eb77
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA"
status: DRAFT - review before publish/run (Outbox Shield)
---

# The Grok Multi-Modal Content Lifecycle Roadmap

- [ ] **Monday: Real-Time Signal Capture & Keyword Ingestion**
  - **Weekly Routine:** Extract Google Search Console (GSC) striking-distance keywords (positions 5.0 to 20.0). Run your Hermes Research layer to execute Grok X Search sweeps, identifying real-time localized storm trends and competitor activity on X. Ingest GSC data and X-trend signals as fresh sources inside Gemini Notebook.
  - **Required Dashboard Tab:** `OpenSEO → Search Performance` / `Notebook`
  - **Required Validation Script:** `run-monday-keywords.bat` (running `gsc_striking_distance.py`)

- [ ] **Tuesday: Creative Storyboarding & Photo Uploads**
  - **Weekly Routine:** Plan your weekly multi-modal campaigns and design layouts. Analyze newly captured OMI voice notes to extract local case study highlights. Map high-resolution job site photography from Denton or Collin County to your planned copy, and upload assets to Google Business Profile (GBP) and the local media folder.
  - **Required Dashboard Tab:** `Blotato` / `Outbox_Drafts`
  - **Required Validation Script:** `brand_firewall.py --check` on drafts and graphics

- [ ] **Wednesday: Multi-Modal Content Generation & Review Requests**
  - **Weekly Routine:** Execute your automated Grok production loop in a single run: command Grok Imagine to output premium Navy/Gold hero graphics, Grok Video to render high-fidelity 25-second B-roll clips, and Grok TTS to output professional voice-over tracks. Automate SMS/email review campaigns to yesterday's completed customers.
  - **Required Dashboard Tab:** `Execute` / `Studio`
  - **Required Validation Script:** `brand_firewall.py --check` on all generated video, image, and copy files

- [ ] **Thursday: Gauntlet Loop Evaluation & Automated Publishing**
  - **Weekly Routine:** Deploy the Claude Gauntlet Loop where specialized blind critic agents review your draft text, images, and audio against Alex Hormozi's Value Equation. Approve and transition winning drafts from `PAUSED` to `ACTIVE` to trigger automatic WordPress sitemap publishing via `wp_publish.py`. Individually reply to new Google reviews naming the local neighborhood.
  - **Required Dashboard Tab:** `Pipeline` / `WordPress` / `Blotato`
  - **Required Validation Script:** Manual review and approval of PAUSED drafts in `01_Command_Center/Outbox_Drafts/`

- [ ] **Friday: Speed-to-Lead Response Audit & Indexing Checks**
  - **Weekly Routine:** Perform an end-to-end lead qualification check, ensuring that every inbound prospect generated from your Grok campaigns was called or messaged within 5 minutes. Audit GSC to confirm that yesterday's published pages have successfully indexed.
  - **Required Dashboard Tab:** `OpenSEO` / `LSA Dashboard`
  - **Required Validation Script:** `GSC_Connect.bat`

- [ ] **Saturday: Video Syndication & Campaign Optimization**
  - **Weekly Routine:** Publish your compiled vertical Grok video reel across connected platforms using Blotato's scheduler. Review overall CTR and conversion stats on your landing pages to plan next week's creative tests.
  - **Required Dashboard Tab:** `Video Editor` / `Blotato` / `Mission Control`
  - **Required Validation Script:** `LAUNCH_ALL.bat` and `M7_DOCTOR.bat`

- [ ] **Sunday: Long-Term Memory Sync & Repository Backups**
  - **Weekly Routine:** Tidy up the local directory system. Sync OMI voice note logs and write campaign performance tags back into `brand_vault.json` to prevent your agents from suffering from context amnesia. Execute your backup sequence to upload the entire workspace to your private GitHub repository.
  - **Required Dashboard Tab:** `Shared Memory` / `Pipeline`
  - **Required Validation Script:** `M7_CLEANUP.bat` (followed by local terminal execution of `git add . && git commit -m "session: Grok multi-modal content pipeline execution" && git push`)