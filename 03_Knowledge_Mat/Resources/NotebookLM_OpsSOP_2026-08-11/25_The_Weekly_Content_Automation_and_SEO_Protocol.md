---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: f66634b5-da54-4e00-8dd9-5c549cb27e42
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# The Weekly Content Automation and SEO Protocol

- [ ] **Monday — Performance Brief & Planning** [1]
  - **Routine:** Select 1 keyword from striking distance (positions 5–20), ingest fresh storm/SERP data, have Hermes write the SEO page in Goal Mode, and post it to WordPress [2, 3].
  - **Dashboard Tab:** OpenSEO → Search Performance, Hermes → Goal Mode, WordPress [2, 3].
  - **Validation Script:** `run-monday-keywords.bat` (triggers GSC keyword extraction via `extract_monday_keywords.py`), followed by `wp_publish.py` for automated draft upload [2, 4].

- [ ] **Tuesday — Asset Planning & Brief Creation** [1]
  - **Routine:** Conduct asset planning, extract case studies, build sourced briefs, and queue 1 Google Business Profile (GBP) update [1, 3].
  - **Dashboard Tab:** Blotato / Outbox [3].
  - **Validation Script:** Outbox Shield check (ensure GBP draft is staged in a **PAUSED** state inside `Outbox_Drafts/`) [5, 6].

- [ ] **Wednesday — Repurposing & High-Volume Production** [1]
  - **Routine:** Execute weekly content production (generate 8–12 branded social captions, repurpose 1 job video into 6 cuts), run the output through the Quality Gate, and stage [1, 7].
  - **Dashboard Tab:** Execute, Skills, Studio [1, 8].
  - **Validation Script:** `python 04_Tech_Lab/scripts/brand_firewall.py --check` (programmatically blocks any green hex codes and enforces strict brand identity rules) [5, 9].

- [ ] **Thursday — Human Approval & Winning Posts** [1]
  - **Routine:** Human Gatekeeper day (Saia reviews, approves, and schedules the winning assets), and post 1 GBP update [1, 3].
  - **Dashboard Tab:** Pipeline (Human Approval column), Blotato, WordPress [3, 10].
  - **Validation Script:** Manual validation of staged drafts inside `01_Command_Center/Outbox_Drafts/` [6, 10].

- [ ] **Friday — Outreach & Local Review Velocity Audit** [1]
  - **Routine:** Run outbound outreach, perform search ranking audits, and review the Google Local Services Ads (LSA) dashboard for incoming leads or disputes [1, 3].
  - **Dashboard Tab:** OpenSEO → Search Performance, LSA Dashboard [2, 3].
  - **Validation Script:** `GSC_Connect.bat` to verify active Google Search Console property synchronization [2].

- [ ] **Saturday — Connection Checks & Speed-to-Lead Monitoring** [1, 3]
  - **Routine:** Monitor incoming LSA and GBP leads, run rank audits, and analyze weekend performance [1, 3, 11].
  - **Dashboard Tab:** Mission Control, LSA Dashboard [2, 3].
  - **Validation Script:** `M7_DOCTOR.bat` to run the system connection health checklist, and `LAUNCH_ALL.bat` to verify server up-time [10, 12].

- [ ] **Sunday — Memory Sync & Cloud Backup** [1]
  - **Routine:** Sync shared memory logs, tidy local workspaces, and backup progress to the GitHub repository [1].
  - **Dashboard Tab:** Shared Memory, Pipeline [8].
  - **Validation Script:** `M7_CLEANUP.bat` to clear the local directory, followed by `git add . && git commit -m "session: drafts + updates" && git push` to snapshot the workspace database [10, 12, 13].