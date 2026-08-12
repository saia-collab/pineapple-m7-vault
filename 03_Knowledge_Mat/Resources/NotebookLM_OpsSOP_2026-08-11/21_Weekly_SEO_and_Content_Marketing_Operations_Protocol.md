---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: d830a302-fb1f-4630-a736-b1b4eedbfd44
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA"
status: DRAFT - review before publish/run (Outbox Shield)
---

# Weekly SEO and Content Marketing Operations Protocol

- [ ] **Monday: Search Performance & Keyword Mining**
  - **Weekly Routine:** Extract Google Search Console (GSC) performance metrics covering the last 90 days [1]. Isolate easy-win "striking-distance" keywords ranking between average positions 5.0 and 20.0 with high impressions (> 250/month) and low CTR (< 3.0%) [1, 2]. Ingest fresh storm and SERP data into the project's Gemini Notebook [3, 4].
  - **Required Dashboard Tab:** `OpenSEO → Search Performance` [4] / `Notebook` [3, 4]
  - **Required Validation Script:** `run-monday-keywords.bat` [2, 5] running `gsc_striking_distance.py` [2, 6]

- [ ] **Tuesday: Above-the-Fold Creative Planning & Field Asset Uploads**
  - **Weekly Routine:** Organize your weekly creative asset plan, review newly synced OMI voice notes, and extract localized client-specific proof points [3, 7]. Upload high-resolution job site photography and drone thermal captures from Denton or Collin County projects directly to Google Business Profile (GBP) and Google Drive `01_READY_TO_POST` [3, 7-9].
  - **Required Dashboard Tab:** `Blotato` / `Outbox_Drafts` [4, 10]
  - **Required Validation Script:** `brand_firewall.py --check` on draft campaigns and social graphics [11-13]

- [ ] **Wednesday: Content Production, Multi-Modal Video Renders & Review Campaigns**
  - **Weekly Routine:** Automatically text or email yesterday's completed-job customers a Google review link to boost local map pack authority [3, 14]. Trigger the content generation engine (Remotion, Pomelli, or Higgsfield) to render vertical reels and compile scroll-cinematic landing pages with zero cuts to capture local storm victims [3, 15, 16].
  - **Required Dashboard Tab:** `Execute` / `Studio` [4, 17]
  - **Required Validation Script:** `brand_firewall.py --check` [11-13] to verify terminology replacements (CPPA [Complimentary Professional Photo Audit], IKO Certified RoofPro) and colors (Navy `#1A365D`, Gold `#FBC02D`, Cyan `#00BFFF`) [11, 18]

- [ ] **Thursday: Outbox Shield Review & Geotargeted Review Engagement**
  - **Weekly Routine:** Enforce the non-negotiable Outbox Shield by manually reviewing, approving, and publishing winning content drafts [3, 11]. Individually reply to new Google reviews by explicitly naming the homeowner's neighborhood to boost geolocation power, and publish one GBP update post [3, 8].
  - **Required Dashboard Tab:** `Pipeline` / `WordPress` [4, 17] / `Blotato` [4]
  - **Required Validation Script:** Manual check and verification of PAUSED drafts in `01_Command_Center/Outbox_Drafts/` [10, 11]

- [ ] **Friday: Speed-to-Lead Response Audit & GSC Indexing Sweep**
  - **Weekly Routine:** Run a lead speed-to-lead verification pass to confirm that every new inbound lead from Google Local Services Ads (LSA) and Meta Ads was contacted, called, or qualified via AI voice scheduling within 5 minutes [3, 7, 19, 20]. Scan GSC to verify that yesterday's published pages have successfully indexed [3, 8].
  - **Required Dashboard Tab:** `OpenSEO` / `LSA Dashboard` [4, 19]
  - **Required Validation Script:** `GSC_Connect.bat` [4] (verifying active GSC and API connector statuses)

- [ ] **Saturday: Vertical Reel Repurposing & Scoreboard Analysis**
  - **Weekly Routine:** Publish one short-form vertical video reel across connected platforms according to your social media Repurpose Plan [3, 8]. Review your overall keyword rankings and audit ad campaign CTR metrics [3, 8, 21].
  - **Required Dashboard Tab:** `Video Editor` / `Blotato` [4] / `Mission Control` [17, 22]
  - **Required Validation Script:** `LAUNCH_ALL.bat` and `M7_DOCTOR.bat` [10, 22, 23]

- [ ] **Sunday: Long-Term Memory Sync & Private GitHub Backup**
  - **Weekly Routine:** Run deep housecleaning across your workspace. Sync OMI voice transcripts and log completed campaign metrics into your shared brain file (`SHARED_MEMORY.md` or `brand_vault.json`) to prevent agents from suffering from amnesia [1, 3, 24, 25]. Backup your local workspace to your private GitHub repository [24, 26, 27].
  - **Required Dashboard Tab:** `Shared Memory` [17, 19] / `Pipeline` [17]
  - **Required Validation Script:** `M7_CLEANUP.bat` [10, 23] followed by `git add . && git commit -m "session backup" && git push` [24, 27]