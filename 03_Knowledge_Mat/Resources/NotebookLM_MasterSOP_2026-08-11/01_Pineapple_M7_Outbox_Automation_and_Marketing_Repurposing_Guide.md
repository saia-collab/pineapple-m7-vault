---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 012b555d-a95a-4e49-9089-62f8fa7c4f9d
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Pineapple M7: Outbox Automation and Marketing Repurposing Guide

### 🛰️ PINEAPPLE M7 — OUTBOX AUTOMATION & MULTI-CHANNEL REPURPOSING
**Document ID:** `03_Knowledge_Mat/00_Atlas/SOP_M7_Watcher_and_CaseStudy_Video_Repurpose.md` [cite: 54, 129]  
**Authority:** JR. Moeakiola (Founder) & Saia Moeakiola (Senior Operations Manager) [cite: 56, 139]  
**Security Status:** Gated under the Outbox Shield (DEC-005) — **All drafts must land PAUSED in `01_Command_Center/Outbox_Drafts/`** [cite: 127, 134, 188].  
**Brand Law Verification:** Polynesian-owned | RCAT Licensed `#03-0637` | IKO Certified [cite: 9, 125, 166].  

---

### 🚀 PART 1: HOW TO TRIGGER THE AUTOMATED FRISCO DAMAGE CAMPAIGN

To trigger your automated **10-page Frisco storm damage campaign** inside your local Agent OS [cite: 136, 218], you instruct your specialized sub-agents (Planner, Builder, and Critic) using your visual Kanban dashboard (`localhost:3000`) or the Hermes Goal Mode Console (`localhost:9119`) [cite: 77, 187, 257]. 

This bypasses manual page construction entirely, allowing your agents to crawl, write, style, and double-audit your pages in the background [cite: 113, 222, 260].

```
┌────────────────────────┐      /goal Mode       ┌────────────────────────┐
│  Saia Inputs Command   ├──────────────────────►│  Hermes Dispatcher     │
│  (Kanban or Console)   │                       │  Spawns Sub-Agent Crew │
└────────────────────────┘                       └───────────┬────────────┘
                                                             │
                                                             ▼
┌────────────────────────┐      Auto-Checks      ┌────────────────────────┐
│  Outbox Watcher        │◄──────────────────────┤  Staged PAUSED Drafts  │
│  Pings Webhook Alerts  │  brand_firewall Scan  │  (Outbox_Drafts/)      │
└────────────────────────┘                       └────────────────────────┘
``` [cite: 41, 113, 114, 257, 260]

#### Step 1: Open Your Active Work Desk
*   **The Interface:** Go to your web browser and open either your visual **Agent Kanban** board at `http://localhost:3000` or your active **Hermes Dashboard** at `http://localhost:9119` [cite: 187].
*   **The Profile:** In the profile dropdown selector, ensure you switch your active workspace persona to **`seo`** to load your local search data, schema sets, and target city profiles [cite: 139].

#### Step 2: Feed the Multi-Step Target Brief
Copy this operational command block, paste it directly into the **"Assemble Board"** input box inside your Kanban tab or type it next to the `/goal` parameter in Hermes [cite: 201, 203], then press Enter:

```text
/goal "Act as the Lead SEO Architect for PM7 [cite: 204]. Let's trigger our 10-page Frisco Storm Damage campaign cluster targeting high-intent local search queries [cite: 12, 136]:
1. Read our business coordinates from '01_Command_Center/MASTER_PLAYBOOK.md' [cite: 129] and our $571,000 plumbing campaign case study from '03_Knowledge_Mat/active_context/case_study_571k_plumbing.md' [cite: 111, 221].
2. Set our primary target city to Frisco, TX, focusing on ZIP codes 75033, 75034, and 75035 [cite: 150].
3. Spawn a researcher sub-agent to study competitor pages and extract the top 10 local-SEO storm-damage search terms [cite: 74, 172].
4. Spawn a writer sub-agent to draft optimized, 1,200+ word landing pages for each city service variant (e.g., roof-repair, storm-restoration, gutter-services) [cite: 74, 79, 125].
5. Enforce our strict CNBC-style, answer-first AEO copywriting layout (answer the primary query within the first 40 words) [cite: 150, 207].
6. Embed a LocalBusiness schema block containing our RCAT License #03-0637 and IKO Certified trust badges [cite: 150, 166].
7. Save all generated page files in a strictly PAUSED state inside '01_Command_Center/Outbox_Drafts/Website_Pages/' [cite: 129, 159]. Do not publish live [cite: 127]."
```

#### Step 3: Let the Loop Run
The **Hermes Dispatcher** will autonomously plan the tasks [cite: 77, 257], spawn three sub-agents in parallel [cite: 74, 228], write the required files straight to your folder [cite: 228], run the `brand_firewall.py` check, and leave the compliant, brand-clean pages waiting for your final manual "GO" approval [cite: 113, 222].

---

### 📁 PART 2: THE STARTUP WATCHER LAUNCHER (`LAUNCH_WATCHER.bat`)

I have successfully programmed and synced the batch launcher directly to your **Studio panel** [cite: 80]. 

#### What the Code Does:
When you turn on your Windows computer, you don't want to waste time opening the terminal, manually CD-ing into directories, and typing startup commands [cite: 80, 185]. This script automates your morning routine [cite: 80]:
1.  **Sets the Workspace Root:** Changes your active command line terminal directory directly to your root folder: `C:\Pineapple Contractors M7` [cite: 117].
2.  **Runs Pre-Flight Checks:** Inspects your directories to verify that the upgraded daemon file (`outbox_watcher-v2.py`) is downloaded and in place [cite: 80]. If the python script is missing, it alerts you with a clear screen message [cite: 80].
3.  **Boots the Background Guard-Dog:** Initializes a separate, dedicated background console window and starts your real-time brand scanner [cite: 80]. The window stays open, monitoring your folder changes and routing Webhook alerts without using up your CPU [cite: 80].

#### 🔌 Copy-Paste Batch Launcher Code:
Save this exact code block as your morning startup shortcut:  
📁 **`C:\Users\<Your_User_Name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\LAUNCH_WATCHER.bat`**

```cmd
@echo off
:: PINEAPPLE M7 — OUTBOX REAL-TIME WATCHER STARTUP LAUNCHER
:: Target: Launches outbox_watcher-v2.py in a dedicated background window upon computer boot.

title PINEAPPLE M7 — AUTOMATED WATCHER DAEMON ACTIVE
echo ===================================================
echo 🍍 PINEAPPLE M7 — INITIALIZING BRAND WATCHDOG
echo ===================================================

:: 1. Navigate to your local project root folder
cd "C:\Pineapple Contractors M7" 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Root folder C:\Pineapple Contractors M7 was not found!
    echo Please verify your local folder path is correct and restart.
    pause
    exit /b
)

:: 2. Pre-flight check: ensure the upgraded watcher script is present
if not exist "04_Tech_Lab\scripts\outbox_watcher-v2.py" (
    echo [ERROR] Upgraded outbox_watcher-v2.py was not found in 04_Tech_Lab\scripts\!
    echo Please download it from your Studio Panel and save it locally.
    pause
    exit /b
)

echo [STARTING] Launching live daemon in a separate guard window...
start "M7 Outbox Guard-Dog Daemon" cmd /k "python \"04_Tech_Lab\scripts\outbox_watcher-v2.py\""

echo ===================================================
echo ✅ BRAND FIREWALL ACTIVE AND GUARDING YOUR WORKSPACE!
echo This startup launcher will now close. Keep the puppy window open!
echo Stay safe, Saia!
echo ===================================================
timeout /t 5
exit
```

---

### 🎬 PART 3: REPURPOSING THE \$571K CASE STUDY INTO A VIDEO SCRIPT

To turn your real-world **\$571,000 gross revenue and 595 booked jobs case study** into a viral, high-retention vertical video (Instagram Reel, YouTube Short, or TikTok) [cite: 161, 221], you must optimize for extreme pacing and immediate credibility [cite: 65, 147].

This script is written using your strict **50/5/3 Lego Video framework** (exactly 50 seconds runtime, a 5-second disruptive hook, a 42-second fast-paced proof body, and a 3-second trust CTA end card) [cite: 65, 147]:

```
 0-5s Hook              5-47s Fast-Paced Proof Body             47-50s End Card
┌───────────┐ ┌──────────────────────────────────────────────┐ ┌──────────────┐
│  REVEAL   │ │ - Polynesian heritage & Tauhi Vā            │ │  GOLD/NAVY   │
│  PATTERN  │ │ - $571,000 gross revenue stats               │ │  TRUST CARD  │
│ INTERRUPT │ │ - IKO 50-year warranty, CPPA, no green style │ │ RCAT #03-0637│
└───────────┘ └──────────────────────────────────────────────┘ └──────────────┘
``` [cite: 9, 65, 126, 147, 148]

---

#### 🎬 THE 50/5/3 LEGO VIDEO SCRIPT SHEET
*   **Total Runtime:** Exactly 50 Seconds (1,500 frames @ 30fps) [cite: 65, 147]
*   **Tone:** Alex Hormozi Style (Punched, visual breaks, single sentence per line) [cite: 32]
*   **Visual Parameters:** No green elements allowed [cite: 9, 127]. Screen text strictly styled in Pineapple Gold (`#FBC02D`) on Royal Navy (`#1A365D`) backgrounds [cite: 9, 127, 147].

| Time / Frame Range | Video & Camera Cues (B-Roll) | On-Screen Text Overlay (Pineapple Gold) | Spoken Voiceover Script (Hormozi Tone) |
| :--- | :--- | :--- | :--- |
| **0:00 - 0:05**<br>*(Frames 0 - 150)*<br><br>**🚨 THE HOOK** [cite: 147] | Fast drone flyover reveals a massive hail-damaged shingle split in half [cite: 161]. High-energy visual pattern interrupt [cite: 147]. | **HIDDEN ROOF DAMAGE?**<br>*(Royal Navy Box / Gold Text)* [cite: 9, 127, 147] | Your roof survived the DFW storm. But did it really? [cite: 163, 211, 215] |
| **0:05 - 0:12**<br>*(Frames 151 - 360)*<br><br>**📈 PROOF POINT** | Cut to closeup of a drone showing micro-cracks from structural hail strikes on a roof [cite: 175]. | **\$571,000 PROVEN RESULT** [cite: 221] | Most local roofing companies lie to you after a storm [cite: 32]. We don't. We let the engineering data speak [cite: 5, 221]. |
| **0:12 - 0:20**<br>*(Frames 361 - 600)*<br><br>**👥 THE SCALE** | Smooth transition to a gorgeous drone tracking shot of completed roofing jobs in Starwood, Frisco [cite: 162]. | **595 LOCAL HOMES SAFE** [cite: 221] | We ran a 9-month sprint in North Texas [cite: 221]. Over 595 local DFW families trusted us to secure their homes [cite: 149, 221]. |
| **0:20 - 0:30**<br>*(Frames 601 - 900)*<br><br>**🤝 OUR VALUE** | Cut to a high-quality closeup of IKO Dynasty shingles being nailed into place with the ArmourZone® woven band visible [cite: 309]. | **IKO CERTIFIED REINFORCED** [cite: 125, 226, 309] | We do things differently [cite: 32]. We standardize strictly on premium IKO Certified materials [cite: 9, 256]. They resist 130 mph wind storms [cite: 309]. |
| **0:30 - 0:38**<br>*(Frames 901 - 1140)*<br><br>**🌺 HERITAGE** | Short, heartfelt shot of Saia smiling, shaking hands with a Frisco homeowner in their driveway [cite: 135]. | **POLYNESIAN RUN SINCE 2005** [cite: 18, 126, 256] | We are Polynesian-owned and family-operated since 2005 [cite: 18, 126]. We treat your home like family—that's Tauhi Vā [cite: 148, 177]. |
| **0:38 - 0:47**<br>*(Frames 1141 - 1410)*<br><br>**🛡️ THE VALUE** | High-definition screen recording showing a customer opening an iPad with a detailed roof-damage photo audit file [cite: 5]. | **YOUR DFW CLAIM COMPLIANT** [cite: 127] | Do not let your storm-claim filing window close [cite: 149, 177]. Get a Complimentary Professional Photo Audit [cite: 9, 125]. We document everything for you [cite: 5]. |
| **0:47 - 0:50**<br>*(Frames 1411 - 1500)*<br><br>**🎙️ CTA END-CARD** [cite: 147] | Solid Royal Navy background pops up [cite: 147]. Display phone number and RCAT credentials in bold Pineapple Gold [cite: 9, 147]. | **BOOK YOUR CPPA**<br>**972-928-0788**<br>**RCAT LICENSE #03-0637** [cite: 9, 125, 147] | Call us now at 972-928-0788 [cite: 9, 125, 147]. Experience the Pineapple Standard [cite: 9, 126]. |

---


📂 **Next Step Suggestion:**  
I can configure your local **`content` profile** inside your Hermes dashboard to batch-generate **12 unique social media captions** styled under this exact Hormozi copywriting framework [cite: 139, 220]. Would you like me to map out this batch prompt? [cite: 220]