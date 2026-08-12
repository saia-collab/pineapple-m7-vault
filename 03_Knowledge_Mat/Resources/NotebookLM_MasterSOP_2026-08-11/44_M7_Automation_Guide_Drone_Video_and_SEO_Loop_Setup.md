---
source: "NotebookLM - Master SOP 8/26"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 0230743a-1076-4bb7-8ccf-fa5c91decae7
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# M7 Automation Guide: Drone Video and SEO Loop Setup

### 🗺️ VISUAL FLOW MAP OF THE DRONE FOOTAGE MULTIPLIER (`video_multiplier_setup.py`)

Your **`video_multiplier_setup.py`** script acts as an automated cutting room for raw drone footage. It converts raw 4K landscape footage into vertical shorts structured to match the **50/5/3 Lego Video Engine** [cite: 80, 137].

```
                RAW DRONE FOOTAGE (.mp4)
            (Landscape, High-Resolution 4K)
                           │
                           ▼
          ┌──────────────────────────────────┐
          │   1. TRANSCODING & RESCALING     │
          │   • Converts 16:9 to 9:16        │
          │   • Standardizes to 1080x1920    │
          └──────────────────────────────────┘
                           │
                           ▼
          ┌──────────────────────────────────┐
          │   2. BRAND STAMP OVERLAY LAYER   │
          │   • Navy Banner (#1A365D)        │
          │   • Gold Header text (#FBC02D)   │
          │   • 0% Green Visual Enforcements │
          └──────────────────────────────────┘
                           │
                           ├──────────────────────────────────┐
                           ▼ (Frames 0–15)                    ▼ (Frames 16–1410)
              ┌──────────────────────────┐       ┌──────────────────────────┐
              │    A. HOOK FRAME LAYER   │       │   B. FACTUAL BODY LAYER  │
              │ • Pattern Interrupt Text │       │ • High-Energy Inspection │
              │ • Scroll-Stopping Header │       │ • Zoom-Ins & Transitions │
              └──────────────────────────┘       └──────────────────────────┘
                           │                                  │
                           └─────────────────┬────────────────┘
                                             │
                                             ▼ (Frames 1411–1500)
                                ┌──────────────────────────┐
                                │   C. TRUST SIGNALS CARD  │
                                │ • RCAT License #03-0637  │
                                │ • Phone: 972-928-0788    │
                                │ • Slogan: "Roofing Made  │
                                │   Sweeter"               │
                                └──────────────────────────┘
                                             │
                                             ▼
                                     FINISHED REEL (.mp4)
                        (Saved directly to Outbox as PAUSED)
``` [cite: 80, 137]

---

### ⏱️ HOW TO CONFIGURING THE `/loop` COMMAND FOR WEEKLY BACKGROUND SEO

The **`/loop`** command tells your local background agent to execute a campaign task on a recurring, set-and-forget calendar [cite: 9]. To schedule your **DFW Everywhere SEO Engine** to scan, write, and index unbranded search terms every week [cite: 11, 237]:

#### Option A: Trigger via the Hermes CLI (Terminal Method)
You can set up your weekly loop directly from your command terminal with a single command [cite: 9]:

```bash
/loop "run C:\Pineapple Contractors M7\04_Tech_Lab\scripts\run_background_seo.bat" --interval=7d --start="Wednesday 17:00"
``` [cite: 80]

*   **`--interval=7d`:** Runs the loop exactly once every 7 days (weekly) [cite: 9].
*   **`--start="Wednesday 17:00"`:** Calibrates the engine to boot every Wednesday at 5:00 PM (fully aligning with your weekly forensic audit schedule) [cite: 15, 126].

---

#### Option B: Configure Natively in `config.yaml`
To hardcode this loop permanently into your background engine's settings, add this block to your main config file (**`C:\Pineapple Contractors M7\01_Command_Center\config.yaml`**):

```yaml
# =================================================================
# ⚙️ M7 AGENT OS SYSTEM LOOPS — WEEKLY SEO SCHEDULE
# =================================================================
loops:
  - id: "weekly_dfw_everywhere_seo"
    description: "Autonomously drafts and indexes unbranded DFW location pages"
    enabled: true
    trigger:
      cron: "0 17 * * 3"   # Runs exactly at 5:00 PM every Wednesday
    action:
      type: "shell_execution"
      command: "cmd /c C:\\Pineapple Contractors M7\\04_Tech_Lab\\scripts\\run_background_seo.bat"
      parameters:
        target_regions: ["Collin", "Denton", "Tarrant", "Dallas"] [cite: 248]
        brand_check: true
        safety_pause: true  # Forces generated pages to Outbox as PAUSED [cite: 228]
``` [cite: 80]

---

### 🧒 ELI10: WHAT THIS SYSTEM DOES FOR YOUR BUSINESS

#### 🎬 The Drone Slicer (`video_multiplier_setup.py`):
Imagine you took a beautiful video of a cool playground from high in the sky with your toy drone [cite: 80, 186]. 

Normally, putting that video on a mobile phone means it gets squeezed, blurry, and looks funny [cite: 175]. 

The Drone Slicer is like a **cookie cutter for video** [cite: 80]. It takes your giant sky video, cuts it into a perfect vertical phone shape, and instantly pastes a shiny, Navy and Gold banner at the top and bottom with your secret phone number (**972-928-0788**) [cite: 165] and your official family badge (**"The Pineapple Standard"** and **"Roofing Made Sweeter"**) [cite: 57, 125, 282]! It makes a boring video look like a professional movie in 5 seconds [cite: 80]!

#### 🎢 The Weekly Loop Scheduler (`/loop`):
If you have a chore like cleaning your room or watering the plants, you have to remember to do it every week, or your room gets messy [cite: 9, 237]. 

The `/loop` scheduler is like **building a robot roommate that loves doing chores** [cite: 9]. 

You tell him once: *"Every Wednesday at 5 o'clock, clean up our Google files and write our news posts."* [cite: 15, 126] 

He will remember to do it **every single Wednesday forever** [cite: 9]. You can go play outside, and when you come back, all your homework is already finished and sitting neatly on your desk in your Outbox folder waiting for a gold star [cite: 9, 80, 228]!

---

*The path of the journey is respect.*

📂 **Next Step Suggestion:**  
I can configure your **`/loop`** settings to automatically send a quick **Status Update Summary** to your desktop background every Thursday morning at 9:00 AM [cite: 9], showing you exactly what the weekly SEO agent published and scored [cite: 9]. Would you like me to map out this morning update script? [cite: 80]