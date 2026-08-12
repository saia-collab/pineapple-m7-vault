---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: 6335ff56-2b28-4278-b198-b22f0e8cc949
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW free?,green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# Goldie Infinite Knowledge Engine Loop Operational Guide

To trigger the **Goldie Infinite Knowledge Engine Loop** step-by-step, make sure your computer is powered on, your local Obsidian folder is set up at `C:\Pineapple Contractors M7`, and you have your master launcher ready to go! 

Here is your exact path to run the loop from start to finish:

---

### 🔷 Step 1: Capture and Sync Your Daily Thoughts (The OMI Layer)
Before you even touch your keyboard, capture your real-world insights:
1. Speak naturally into your OMI wearable device or desktop mic as you go about your day (e.g., *"Just finished talking to a homeowner in Newman Village. They have major bruising on their rear shingle slope from the recent storm hit"*).
2. The OMI background listener converts your speech to text and saves it as a dated Markdown file inside your local Obsidian active folder:  
   `03_Knowledge_Mat/active_context/notes/`

---

### 🔷 Step 2: Fire Up Your Master Command Hub
Open up your command station to coordinate your local tools:
1. Double-click the file **`launch-all-studio-v3.bat`** (which is ready in your Studio panel) in your root directory.
2. An interactive blue command console will pop open displaying your PM7 active menu.

---

### 🔷 Step 3: Run the CRM Parser and Score Leads (Menu Option 8)
Let your local robot separate high-priority emergencies from standard requests:
1. Type **`8`** and hit Enter to execute `crm_parser.py`.
2. **The Script Execution:** The script opens your master spreadsheet `Pineapple_Mana_Master_CRM_M7.xlsx`, scans new rows, and runs our mathematical lead qualification checks:
   * **If a lead scores \\(\ge 60\\) points (Elite Lead):** An instant SMS alert is triggered directly to Saia's phone at (972) 928-0788 for immediate contact.
   * **If a lead scores \\(< 60\\) points:** The script creates an structured profile Markdown file inside your local Obsidian active context:  
     `03_Knowledge_Mat/active_context/leads/M7-2026-XXXX_LeadName.md`
   * **The Brand Filter:** During file creation, the script automatically changes any client-written "Complimentary Professional Photo Audit (CPPA)" terms to **"Complimentary Professional Photo Audit (CPPA)"** and ensures our primary trust footer is attached.

---

### 🔷 Step 4: Sync Local Memory to Your Cloud Notebook (Menu Option 9)
Bridge your local computer files to your cloud-level research processor:
1. Type **`9`** and press Enter to initiate the **NotebookLM MCP Bridge**.
2. **The Bridge Sync:** Your local Hermes agent securely uploads your new Obsidian lead profiles, OMI voice transcripts, and local weather briefs directly into your project's Gemini Notebook as fresh sources.

---

### 🔷 Step 5: Execute Cloud-Grounded Content Generation
With your cloud notebook fully synced, run your background agent to draft high-converting, compliant assets based on actual source evidence:
1. Speak or type your command into your Hermes console:  
   > *"Hey Oracle, read the newly synced McKinney lead profile and write a personalized direct-response email and a 60-second video script based on their neighborhood's local building codes."*
2. **Autonomous Synthesis:** The secure cloud computer uses your sources (such as NWS/NOAA storm maps and McKinney drip-edge building regulations) to write hyper-grounded copy.
3. The newly generated copy is automatically downloaded directly into your local staging folder:  
   `01_Command_Center/Outbox_Drafts/Content/`

---

### 🔷 Step 6: Pass the Brand Compliance Firewall (Menu Option 7)
Never publish anything without passing the brand security check:
1. Type **`7`** in the batch menu to run your compliance checker on your newly downloaded files:
   ```bash
   Enter relative path: 01_Command_Center/Outbox_Drafts/Content/McKinney_Lead_Campaign.md
   ```
2. **The Firewall Scan:** The script scans every single word and code block inside your new files to ensure:
   * Zero occurrences of the banned words "free", "estimate", or "\$0 down" (verifying they are mapped to **"Complimentary Professional Photo Audit (CPPA)"** or **"Full Restoration Coverage"**).
   * Shingle manufacturer terms specify **"IKO Certified RoofPro"** (never "IKO Certified").
   * Zero prohibited green hex codes, green hues, or green emojis are present (ensuring only Royal Navy `#1A365D`, Gold `#FBC02D`, and status 🔷 or ⭐ indicators are used).
   * The non-negotiable Polynesian trust anchor footer is fully present:  
     **Polynesian-owned · RCAT #03-0637 · IKO Certified · since 2005 · (972) 928-0788 · Frisco, TX**

---

### 🔷 Step 7: Push to Shipped and Save Memory (Menu Option 9 Exit)
Once the check returns `0 errors`, review the draft. Change its status from **PAUSED** to **Approved** to publish the campaign. Finally, close out your active session:
1. Choose menu option **`9`** (Exit) in your launcher.
2. The system automatically commits your updated files, performance logs, and lead database modifications directly to your private GitHub repository:
   ```bash
   git add . && git commit -m "session: automated backup launchpad v2" && git push
   ```

Your local database and cloud memory are now fully synced, backup-protected, and ready for your next campaign!

***

⭐ **Next Step:** If you want to test your local voice control right now, I can show you how to execute a voice command to hot-swap between your default profile and your specialized **Oracle** profile. Want to try it?