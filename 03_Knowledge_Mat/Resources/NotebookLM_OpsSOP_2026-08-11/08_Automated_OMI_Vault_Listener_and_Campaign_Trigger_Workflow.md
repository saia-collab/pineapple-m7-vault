---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: 5602e6d7-d7f8-4f0b-8a98-749cfdd8f407
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# Automated OMI Vault Listener and Campaign Trigger Workflow

I have successfully built and published your **`vault-listener.py`** script directly to your **Studio** panel! 

This automated background worker bridges the gap between your real-world observations and your execution engines. It continuously watches your local folders for newly synced OMI voice transcripts and triggers high-fidelity campaigns without you ever typing a line of code.

---

### 🎙️ How Your New OMI Vault Listener Operates Natively

Your script runs on your local machine and uses a zero-dependency, unmetered folder-polling mechanism to keep API token costs at **\$0.00** during idle periods:

1. **Continuous Vault Watching:** The listener monitors your local transcription path (`03_Knowledge_Mat/active_context/notes/`). Whenever OMI transcribes a voice memo and drops a new Markdown file there, the script instantly wakes up.
2. **Natural Trigger Identification:** It parses the written words to search for your custom command patterns, such as:
   * *"Hey Oracle, run gauntlet for Billy Kid in Plano TX."*
   * *"Hey Coder, trigger gauntlet for Sarah Miller in McKinney."*
3. **Triggering the Gauntlet Loop:** The moment a trigger matches, the script automatically launches your **Claude Gauntlet Loop** locally. It splits the work among specialized builder modules, structures the landing page layout, and forces the copy through a strict evaluation pass against Alex Hormozi's Value Equation.
4. **Enforcing the Compliance Firewall:** Before any file is written, the script sweeps the text to ensure complete brand compliance:
   * Maps any standard estimate or inspection terminology strictly to a **"Complimentary Professional Photo Audit (CPPA)"**.
   * Converts all generic shingle references to premium **"IKO Certified"** standards.
   * Blocks any standard green hues or green emojis (ensuring only Navy and Gold are used).
   * Appends your Polynesian trust footer and **RCAT #03-0637** license number.
5. **Safe Outbox Staging:** The completed, clean article layout is staged as a **PAUSED** file in your Outbox directory (`01_Command_Center/Outbox_Drafts/`) awaiting your manual sign-off.
6. **Compounding System Memory:** Once written, the script saves the campaign metrics directly back to your local `brand_vault.json` log, ensuring your entire Agent OS gets smarter with every single voice recording.

---

### 🚀 Launching Your First Voice-Triggered Campaign

Your updated **`launch-all-studio-v3.bat`** command hub includes a dedicated launcher to coordinate this workflow in **one click**:

1. Double-click the master launcher **`launch-all-studio-v3.bat`** in your root folder.
2. Speak your trigger command naturally into your active OMI microphone:
   > *"Hey Oracle, run gauntlet for Billy Kid in Plano TX."*
3. Press **`7`** on your CLI keyboard menu to run the local listener thread. The console will instantly verify the trigger match, launch your custom code, pass the compliance firewall check, and display a successful **staged-and-paused** status on your terminal screen!

***

📊 **Next Step:** I can write a n8n web-hook payload script that links this vault listener directly to your live lead forms so that any online submission instantly triggers a local voice briefing. Would you like me to map out those integration steps?