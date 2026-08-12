---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: e45e8288-bde8-41b0-aa98-d2e0cda59f14
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA"
status: DRAFT - review before publish/run (Outbox Shield)
---

# The Seven-Day Automated Orchestration Protocol

- [ ] **Monday: Automated SEO & Keyword Dispatching**
  - **Routine:** The Dispatcher wakes up background worker profiles (Default Profile running on Qwen/Gemma local sockets) to run GSC keyword sweeps. The model filters striking-distance keywords (positions 5.0 to 20.0) and auto-saves them as actionable target goals in the active memory vault.
  - **Dashboard Tab:** `OpenSEO → Search Performance` / `Notebook`
  - **Validation Script:** `run-monday-keywords.bat` (executing `gsc_striking_distance.py`)

- [ ] **Tuesday: Orchestration & Field Asset Ingestion**
  - **Routine:** Field workers sync local job site photos. The OMI (Open Microphone Interface) transcribes client updates into the local Obsidian vault. Sub-agents parse these notes, score new leads, and prepare structured assets for the week's campaigns.
  - **Dashboard Tab:** `Blotato` / `Outbox_Drafts`
  - **Validation Script:** `brand_firewall.py --check` on visual schemas and drafts

- [ ] **Wednesday: Video Generation & Automated Build Loops**
  - **Routine:** The Coder profile (Sol) and Higgsfield MCP are activated via voice commands to render 30-second scroll-cinematic videos (Seedance 2.5) and compile local HTML landing pages. Automated scripts dispatch SMS/email review campaigns to completed customers.
  - **Dashboard Tab:** `Execute` / `Studio`
  - **Validation Script:** `brand_firewall.py --check`

- [ ] **Thursday: Outbox Shield Review & Multi-Agent Quality Gate**
  - **Routine:** Run the Claude Gauntlet Loop where blind critic agents evaluate the drafted landing pages and captions. The business owner reviews compliance and moves files from `PAUSED` to `Approved` to trigger automatic publication.
  - **Dashboard Tab:** `Pipeline` / `WordPress` / `Blotato`
  - **Validation Script:** Manual check of PAUSED drafts in `01_Command_Center/Outbox_Drafts/`

- [ ] **Friday: Speed-to-Lead Response Auditing**
  - **Routine:** System-wide audit of lead response speeds. Ensure that all inbound LSA (Local Services Ads) and Meta Ads leads were engaged or scored by the lead parser script within 5 minutes.
  - **Dashboard Tab:** `OpenSEO` / `LSA Dashboard`
  - **Validation Script:** `GSC_Connect.bat` (verifying active GSC and API connector statuses)

- [ ] **Saturday: Automated Reel Syndication & System Performance Check**
  - **Routine:** Execute automated social media content repurposing. The Oracle profile syndicates one high-converting vertical reel across platforms. Audit overall dashboard CTRs and rank improvements.
  - **Dashboard Tab:** `Video Editor` / `Blotato` / `Mission Control`
  - **Validation Script:** `LAUNCH_ALL.bat` and `M7_DOCTOR.bat`

- [ ] **Sunday: Long-Term Memory Sync & Repository Backups**
  - **Routine:** Clean up the local folder system. Prime Agent runs a self-upgrade pass (`/refine`) to save lessons to behavior notebooks. Sync Obsidian vault files and backup the entire local studio OS workspace to GitHub.
  - **Dashboard Tab:** `Shared Memory` / `Pipeline`
  - **Validation Script:** `M7_CLEANUP.bat` (followed by local terminal execution of `git add . && git commit -m "session backup: automated organizational structures" && git push`)