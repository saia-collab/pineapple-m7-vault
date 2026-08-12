---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: 7ad6b2e2-fd56-4371-9067-675e81130f68
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA"
status: DRAFT - review before publish/run (Outbox Shield)
---

# The Seven-Day Copy-First Marketing Architecture

- [ ] **Monday: Copy Strategy & High-Impression Search Intent Mining**
  - **Copy-First Action:** Extract Google Search Console (GSC) keywords at striking distance (positions 5.0 to 20.0). Instead of starting with design templates, isolate the high-impression search queries to define the exact copy angles and headline promises needed to match user intent.
  - **Required Dashboard Tab:** `OpenSEO → Search Performance` / `Notebook`
  - **Required Validation Script:** `run-monday-keywords.bat` (running `gsc_striking_distance.py`)

- [ ] **Tuesday: Above-the-Fold Messaging Architecture & Field Asset Mapping**
  - **Copy-First Action:** Draft the "Above-the-Fold" layout copy before designing anything. Define the **Dream Outcome Headline** using the **"So That" formula** (e.g., *"Finally get a premium restored roof so that your family stays safe and dry"*), write the agitating subheadline, and select two visual social proof assets from Denton/Collin County field drone logs.
  - **Required Dashboard Tab:** `Blotato` / `Outbox_Drafts`
  - **Required Validation Script:** `brand_firewall.py --check` on copywriting drafts and photo assets

- [ ] **Wednesday: Pain-Agitation Content & Multi-Modal Video Scripting**
  - **Copy-First Action:** Structure the "Below-the-Fold" sections. For cold Meta traffic, write the three-step pain-point copy: **Problem** \\(\rightarrow\\) **Agitate** \\(\rightarrow\\) **Solution**. For warm search traffic, compile before/after reviews into a "Wall of Love". Trigger Higgsfield to render cinematic clips that wrap around this copy, and automate email/SMS review campaigns.
  - **Required Dashboard Tab:** `Execute` / `Studio`
  - **Required Validation Script:** `brand_firewall.py --check` on generated content drafts

- [ ] **Thursday: Value Propositions & Human Approval Gates (The Outbox Shield)**
  - **Copy-First Action:** Draft the 4 to 8 unique value propositions, combining hard features with emotional benefits (e.g., *"IKO Certified shingles so that you never worry about North Texas hail again"*). Outline the how-it-works section in 3 to 4 simple steps to reduce effort. Enforce the Outbox Shield to review and approve PAUSED drafts.
  - **Required Dashboard Tab:** `Pipeline` / `WordPress` / `Blotato`
  - **Required Validation Script:** Manual review and approval of PAUSED drafts in `01_Command_Center/Outbox_Drafts/`

- [ ] **Friday: FAQ/FUD Reduction & Speed-to-Lead Copy Auditing**
  - **Copy-First Action:** Compile question-shaped H2 FAQ blocks with direct 30–50 word answer capsules for Generative Engine Optimization (GEO). Run a speed-to-lead qualification sweep, ensuring that CRM follow-up messages utilize approved CPPA (Complimentary Professional Photo Audit) copy.
  - **Required Dashboard Tab:** `OpenSEO` / `LSA Dashboard`
  - **Required Validation Script:** `GSC_Connect.bat` (verifying live API connector status)

- [ ] **Saturday: Video Reel Syndication & Conversion Rate Optimization (CRO) Audit**
  - **Copy-First Action:** Publish one high-converting vertical reel built around a 60-second copy-first script structure (Hook \\(\rightarrow\\) Problem \\(\rightarrow\\) Solution \\(\rightarrow\\) CTA). Review overall landing page click-through rates (CTR) and search engine rankings to plan next week's split test.
  - **Required Dashboard Tab:** `Video Editor` / `Blotato` / `Mission Control`
  - **Required Validation Script:** `LAUNCH_ALL.bat` and `M7_DOCTOR.bat`

- [ ] **Sunday: Long-Term Memory Sync & Repository Backups**
  - **Copy-First Action:** Log successful copy angles, GSC rankings, and customer feedback back into your shared brain. Let Prime Agent run a self-upgrade pass (`/refine`) to save winning copy rules to its behavior notebooks so your writing style compounds. Backup the local workspace to your private GitHub repository.
  - **Required Dashboard Tab:** `Shared Memory` / `Pipeline`
  - **Required Validation Script:** `M7_CLEANUP.bat` (followed by local terminal execution of `git add . && git commit -m "session backup: copy-first design execution" && git push`)