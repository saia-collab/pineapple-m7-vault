---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: ce31a5e2-f93b-458b-9bb1-6a2df10ed5e2
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA"
status: DRAFT - review before publish/run (Outbox Shield)
---

# The Solo Entrepreneur Weekly Operations Protocol

- [ ] **Monday: GSC Keyword Mining & Striking-Distance Ingestion**
  - **Solo Entrepreneur Objective:** Act as the Chief Executive Officer to isolate high-impression, "striking-distance" keywords (average positions 5.0 to 20.0) with low click-through rates (< 3.0%) [1-3]. Ingest new local storm and weather data into the project's Gemini Notebook [4].
  - **Required Dashboard Tab:** `OpenSEO → Search Performance` / `Notebook` [5, 6]
  - **Validation Script:** `gsc_striking_distance.py` (via `run-monday-keywords.bat`) [2, 7]

- [ ] **Tuesday: Creative Planning & Field Photo Syndication**
  - **Solo Entrepreneur Objective:** Organize your weekly creative asset plan, review newly transcribed OMI voice notes, and extract localized client-specific proof points [8-10]. Upload high-resolution job site photography from Denton or Collin County projects to Google Business Profile (GBP) and the local media staging folder [4, 11].
  - **Required Dashboard Tab:** `Blotato` / `Outbox_Drafts` [11, 12]
  - **Validation Script:** `brand_firewall.py --check` on visual layouts and ad copy [10, 13]

- [ ] **Wednesday: Automated Review Request & Video Rendering**
  - **Solo Entrepreneur Objective:** Automatically text or email yesterday's completed-job customers a Google review link to boost local map pack authority [11, 14]. Trigger the content generation engine (Remotion, Pomelli, or Higgsfield) to render vertical reels and compile scroll-cinematic landing pages with zero cuts to capture local storm victims [4, 15, 16].
  - **Required Dashboard Tab:** `Execute` / `Studio` [4, 17]
  - **Validation Script:** `brand_firewall.py --check` on all generated drafts [10, 13]

- [ ] **Thursday: Outbox Shield Audit & Review Reply Targeting**
  - **Solo Entrepreneur Objective:** Enforce the non-negotiable Outbox Shield [13, 18]. Manually review, approve, and publish the winning content drafts [4, 18]. Individually reply to new customer reviews on your Google Business Profile by explicitly naming the target neighborhood [11, 19].
  - **Required Dashboard Tab:** `Pipeline` / `WordPress` / `Blotato` [4, 17]
  - **Validation Script:** Manual check and verification of PAUSED drafts in `01_Command_Center/Outbox_Drafts/` [13, 20]

- [ ] **Friday: Speed-to-Lead Response Audit & GSC Scan**
  - **Solo Entrepreneur Objective:** Run a lead speed-to-lead verification pass to confirm that every new inbound lead from Google Local Services Ads (LSA) and Meta Ads was contacted or called within 5 minutes [11, 14]. Scan Google Search Console to track newly indexed pages and impression climbs [2, 11].
  - **Required Dashboard Tab:** `OpenSEO` / `LSA Dashboard` [11, 21]
  - **Validation Script:** `GSC_Connect.bat` [6, 11]

- [ ] **Saturday: Vertical Reel Repurposing & Scoreboard Analysis**
  - **Solo Entrepreneur Objective:** Publish one short-form vertical video reel across connected platforms according to your social media Repurpose Plan [11]. Review your overall keyword rankings and audit ad campaign CTR metrics [6, 12].
  - **Required Dashboard Tab:** `Video Editor` / `Blotato` / `Mission Control` [6, 11]
  - **Validation Script:** `LAUNCH_ALL.bat` and `M7_DOCTOR.bat` [6, 22]

- [ ] **Sunday: Long-Term Memory Sync & Private GitHub Backup**
  - **Solo Entrepreneur Objective:** Prevent your agents from suffering from "goldfish amnesia" [23, 24]. Sync all OMI passive voice notes, update your central `brand_vault.json` log, perform filesystem housecleaning, and backup your local vault directly to your private GitHub repository [11, 25, 26].
  - **Required Dashboard Tab:** `Shared Memory` / `Pipeline` [4, 17]
  - **Validation Script:** `M7_CLEANUP.bat` (followed by local terminal execution of `git add . && git commit -m "session backup: drafts + updates" && git push`) [27, 28]