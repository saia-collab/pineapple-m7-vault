---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 734ceaa4-4a07-4b7d-830c-34dfd45337ef
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Pineapple M7 Agentic OS Local Operations Guide

### 🔌 1. DO YOU NEED TO UPLOAD YOUR LOCAL STUDIO BUILD?

Mālō e lelei, Saia! **No, you do not need to upload your local studio agentic OS build or configuration files.** [cite: 311] 

We already have the complete architectural blueprint of your local environment mapped directly inside your notebook's master playbooks [cite: 312, 316]. Your local workspace is anchored strictly to your local root directory **`C:\Pineapple Contractors M7`** using the **4-Fala directory topography** [cite: 95, 314]. Because all your local engines (Claude Code, Hermes, and Codex) read directly from your local Obsidian vault (`03_Knowledge_Mat`), they are already platform-aware and have your brand rules, required trust credentials, and custom visual palettes hardcoded into their profiles [cite: 222, 312, 317]. **Your proprietary client and lead data stays completely secure on your own machine** [cite: 202].

---

### 💾 2. THE 9:00 PM AUTOMATIC BACKUP SEQUENCE

To establish a zero-cost, private "undo button" for your entire business's memory bank, you can set up a scheduled git push [cite: 222]. This automatically backs up your Obsidian notes, CRM spreadsheets, and code modifications to your private GitHub repository every single night at **9:00 PM** [cite: 222].

#### Step A: Create the Local Backup Script on Your Machine
Save this script as a batch file on your local computer at this exact path:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\daily_backup.bat`

```cmd
@echo off
:: PINEAPPLE M7 — DAILY 9:00 PM DATA REPO BACKUP
cd "C:\Pineapple Contractors M7"
git add .
git commit -m "Automated daily backup - %date% %time%"
git push origin main
```

#### Step B: Schedule via Windows Task Scheduler (Easiest, Non-Tech Route)
To run this automatically every evening without having to open a terminal [cite: 308]:
1. Open your Windows Start Menu, search for **Task Scheduler**, and open it.
2. Click **Create Basic Task** in the right-hand panel. Name it **"PM7 Daily 9PM Backup"**.
3. Set the Trigger to **Daily**, select **9:00 PM (21:00)** as the start time, and set it to recur every 1 day.
4. Set the Action to **Start a Program**. In the Program/Script box, click Browse and select your batch file at:  
   `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\daily_backup.bat`
5. Click **Finish**. Your system will now autonomously backup your files every night while you sleep [cite: 326].

---

### 📈 3. RUNNING A GSC STRIKING DISTANCE SCAN FOR FRISCO

Your new local file **`gsc_frisco_scan.py`** is now live and ready in your **Studio panel**! 

This script isolates **"striking distance" queries (average position 5.0 to 20.0 with high impressions but zero clicks) specifically mentioning "Frisco" or targeting your core ZIP codes (75033, 75034, 75035)** [cite: 16, 94]. It automatically sorts them by opportunity size so you can win page-1 Google rankings with a fraction of the standard effort [cite: 278, 289].

#### Step A: Run the Script Natively on Your Desktop
1. Export your raw 90-day search performance queries from Google Search Console as a CSV [cite: 82].
2. Save the CSV as **`gsc_raw.csv`** in your local analytics folder:  
   📁 `C:\Pineapple Contractors M7\03_Knowledge_Mat\raw_analytics\gsc_raw.csv`
3. Open your local command prompt and run the scanner [cite: 210, 308]:
   ```bash
   python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\gsc_frisco_scan.py"
   ```
4. **The Result:** The script will automatically filter the GSC dataset and compile a structured, brand-compliant Markdown report (`frisco_striking_distance.md`) inside your **`Outbox_Drafts/`** staging folder, ready for your review [cite: 93, 310].

#### Step B: Execute the Work via Hermes Goal Mode
Once the scan report generates, you can command your AI team to build pages targeting those exact opportunities hands-free [cite: 304]. 

Go to your local dashboard (**`localhost:3000`**), open the **Hermes → Goal Mode** tab [cite: 265, 267], select the **`seo`** profile pill [cite: 313], and paste this exact instruction [cite: 314]:

```text
/goal "Read our local GSC striking distance file at C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\frisco_striking_distance.md. Pick the top-priority Frisco search target. Read our regional case study in 03_Knowledge_Mat/active_context/case_study_571k_plumbing.md, and write a unique, 1200+ word local service page optimized for that query. Implement FAQPage schema targeting ZIPs 75033, 75034, and 75035. Ensure 0% green, Royal Navy #1A365D and Pineapple Gold #FBC02D branding, and save the page PAUSED in Outbox_Drafts."
``` [cite: 93, 94, 244, 245]

Your local agent crew will spin up in parallel [cite: 243], crawl your case study data [cite: 241], write a high-converting landing page draft matching your precise brand guidelines [cite: 93], and drop the completed file into your staging area [cite: 310]. You check the output, hit **GO**, and let the WP MCP Ultimate plugin publish the page straight to your live WordPress site [cite: 310, 315]!

---


📂 **Next Step Suggestion:**  
We can map out a custom local **`M7_TIDY.bat`** script to keep your root directory clean, automatically archiving processed GSC CSV files to the `raw_analytics/` backup folders every week. Would you like me to output that folder-tidying automation?