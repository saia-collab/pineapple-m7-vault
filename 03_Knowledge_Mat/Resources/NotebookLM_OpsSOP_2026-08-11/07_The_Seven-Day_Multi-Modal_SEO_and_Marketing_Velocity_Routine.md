---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: 512be374-da69-4fc1-86ae-13c7764e91e7
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA"
status: DRAFT - review before publish/run (Outbox Shield)
---

# The Seven-Day Multi-Modal SEO and Marketing Velocity Routine

- [ ] **Monday: GSC Striking-Distance Mining & Ingesting Vault Sources (Week 1 & 3 Roadmap Focus)**
  - **Weekly Routine:** Extract Google Search Console (GSC) keywords at striking distance (positions 5.0 to 20.0). Ingest GSC performance data, local weather files, and case study files into the project's Gemini Notebook as Week 1 Vault Sources.
  - **Required Dashboard Tab:** `OpenSEO → Search Performance` / `Notebook`
  - **Required Validation Script:** `run-monday-keywords.bat` (running `gsc_striking_distance.py`)

- [ ] **Tuesday: Above-the-Fold Creative Planning & Field Photo Uploads (Week 1 & 2 Roadmap Focus)**
  - **Weekly Routine:** Upload the week's job site photos and drone thermal captures from North Texas projects to GBP and Google Drive `01_READY_TO_POST`. Map these as visual proof assets for your planned copy layout drafts.
  - **Required Dashboard Tab:** `Blotato` / `Outbox_Drafts`
  - **Required Validation Script:** `brand_firewall.py --check` on visual layouts and ad copy

- [ ] **Wednesday: Content Production, Multi-Modal Video Renders & Review Campaigns (Week 1 & 3 Roadmap Focus)**
  - **Weekly Routine:** Text or email yesterday's completed-job customers a Google review link to boost local pack authority. Run your video generation engine (Higgsfield Seedance 2.5 or Remotion) to render 30-second scroll-cinematic videos that wrap around your written copy.
  - **Required Dashboard Tab:** `Execute` / `Studio`
  - **Required Validation Script:** `brand_firewall.py --check` on all generated drafts

- [ ] **Thursday: Enforce the Outbox Shield, A2A Review & Automated Publishing (Week 2 & 3 Roadmap Focus)**
  - **Weekly Routine:** Run the Claude Gauntlet Loop where specialized blind critic agents review your draft text, images, and HTML. Transition winning drafts from `PAUSED` to `ACTIVE` to trigger automatic WordPress publishing via `wp_publish.py`. Individually reply to new Google reviews by explicitly naming the target neighborhood.
  - **Required Dashboard Tab:** `Pipeline` / `WordPress` / `Blotato`
  - **Required Validation Script:** Manual review and approval of PAUSED drafts in `01_Command_Center/Outbox_Drafts/`

- [ ] **Friday: Speed-to-Lead Response Audit & GSC Indexing Sweep (Week 3 & 4 Roadmap Focus)**
  - **Weekly Routine:** Run a lead speed-to-lead verification sweep to confirm that every new inbound lead from Google LSA and Meta Ads was contacted or called within 5 minutes. Scan Google Search Console to verify that yesterday's published pages have indexed.
  - **Required Dashboard Tab:** `OpenSEO` / `LSA Dashboard`
  - **Required Validation Script:** `GSC_Connect.bat`

- [ ] **Saturday: Short-Form Reel Syndication & Campaign Performance Scoreboard (Week 3 & 4 Roadmap Focus)**
  - **Weekly Routine:** Publish one short-form vertical video reel across connected platforms according to your social media Repurpose Plan. Review overall landing page CTR and search rankings to plan next week's split tests.
  - **Required Dashboard Tab:** `Video Editor` / `Blotato` / `Mission Control`
  - **Required Validation Script:** `LAUNCH_ALL.bat` and `M7_DOCTOR.bat`

- [ ] **Sunday: Long-Term Memory Sync, Prime Agent Self-Refinement & GitHub Backup (Week 4 Roadmap Focus)**
  - **Weekly Routine:** Sync all OMI passive voice transcripts, update your central `brand_vault.json` log, and tidy up the local file system. Let Prime Agent run its self-upgrade pass (`/refine`) to write lessons back to its behavior notebooks. Backup your entire local studio OS workspace to your private GitHub repository.
  - **Required Dashboard Tab:** `Shared Memory` / `Pipeline`
  - **Required Validation Script:** `M7_CLEANUP.bat` (followed by local terminal execution of `git add . && git commit -m "session backup" && git push`)