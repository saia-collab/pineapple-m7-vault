---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 5f557dbb-36df-4552-b50c-6257cd5366f8
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Pineapple M7 Agent OS Configuration and Workflow Guide

I have built, verified, and published two vital custom assets directly into your Studio panel to integrate these new workflows:
1.  **`M7_TIDY.bat`** — Your automated, one-click Windows root cleanup utility [cite: 160].
2.  **`gsc_m7_config.json`** — The API and property schema configuration to wire up your Google Search Console (GSC) and AI Overview (AIO) dashboard [cite: 242, 401].

---

### 📈 1. CONFIGURING YOUR LIVE GSC & AI OVERVIEW TRACKER (:3737)

The local server running on **`localhost:3737`** (`server.js`) features a dedicated visual dashboard mapping your organic traffic, search queries, and AI Overview citations [cite: 159, 160, 376]. To configure the tracker to pull directly from Google’s GSC API, use the newly published **`gsc_m7_config.json`** file [cite: 401].

#### Step A: Google Cloud Platform (GCP) Configuration
To authorize your local dashboard to read your live Search Console data, you must configure a secure Google OAuth loop [cite: 221, 385]:
1.  Log into the **Google Cloud Console** (`console.cloud.google.com`).
2.  Create a new project named **`M7-Search-Console-Link`**.
3.  Navigate to **APIs & Services \\(\rightarrow\\) Library**, search for the **Google Search Console API**, and click **Enable** [cite: 401].
4.  Go to the **OAuth Consent Screen** tab:
    *   Set the User Type to **External**.
    *   Add your primary GSC email as a test user.
    *   Add the following scope: `https://www.googleapis.com/auth/webmasters.readonly`.
5.  Navigate to **Credentials \\(\rightarrow\\) Create Credentials \\(\rightarrow\\) OAuth Client ID**:
    *   Set Application Type to **Web Application**.
    *   Set **Authorized Redirect URIs** to the exact ports handled by your Node and Agent OS servers [cite: 221]:
        *   `http://localhost:3737/oauth2callback`
        *   `http://localhost:3000/oauth2callback`
6.  Click **Create**, and copy your generated **Client ID** and **Client Secret**.

#### Step B: Code Integration
1.  Open your published **`gsc_m7_config.json`** file in your Studio panel.
2.  Replace the placeholders `"PASTE_YOUR_GOOGLE_CLIENT_ID_HERE"` and `"PASTE_YOUR_GOOGLE_CLIENT_SECRET_HERE"` with your actual Google Cloud keys.
3.  Save this file locally under your tool directory [cite: 159]:  
    📁 `C:\Pineapple Contractors M7\04_Tech_Lab\config\gsc_m7_config.json`
4.  Restart your local servers by running **`LAUNCH_ALL.bat`** [cite: 160]. Your dashboard's "SEO" tab will now dynamically display your GSC search metrics, automatically grouping low-performing page-2 queries into the **"Striking Distance"** list for your agents to optimize [cite: 171, 336].

---

### 🧹 2. THE `M7_TIDY.bat` ROOT AUTOMATION

To prevent folder clutter and token-wasting context drift from legacy install packs and loose files [cite: 141, 181], your new **`M7_TIDY.bat`** script acts as an automated, non-destructive filing assistant [cite: 141, 238].

#### What It Does:
*   **Keeps Absolute System Integrity:** It guarantees your core directories (`01_Command_Center`, `02_Media_Vault`, `02_Workspaces`, `03_Knowledge_Mat`, `04_Tech_Lab`, `05_Campaign_Factory`) and system hooks (`CLAUDE.md`, `m7_execution_manifest.md`, `GSC_Connect.bat`, `.git`) are completely untouched [cite: 142, 144].
*   **Archives Obsolete Installations:** Moves heavy, duplicated, or outdated ZIP files (such as old `agent-os-pack` variants and broken 0KB root launchers) into a newly created `_Archive/` folder to clear hard drive space [cite: 141, 142, 143].
*   **Organizes Loose SOPs:** It automatically sweeps stray `.md` documents found at the root folder (such as your *"Near Me" Domination* or *Accessing WordPress* guides) [cite: 144] and drops them cleanly into your structured Atlas vault so your agents can index them [cite: 144, 216].

#### How to Execute It:
1.  Save the **`M7_TIDY.bat`** file from your Studio panel directly to your vault root:  
    📁 `C:\Pineapple Contractors M7\M7_TIDY.bat` [cite: 159, 160]
2.  Double-click the file.
3.  The terminal window will quickly open, categorize your folders, move loose guides into your second brain, and display a completion message [cite: 160].

---

### 🎮 3. UNDERSTANDING YOUR ENTIRE AGENT OS FEATURES

Your local **Pineapple M7 Agent OS** is a unified, secure system where your various models and workspaces communicate with each other [cite: 133, 158].

```
                     ┌──────────────────────────────┐
                     │    C:\Pineapple Contractors  │
                     │          M7 Root             │
                     └──────────────┬───────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
🎙️ Hermes Jarvis            🗂️ Idea Factory             📈 SEO Room
 wake-word, voice,        5-column Kanban board,      OpenSEO keyword research,
 and local model control     Planner->Builder->Reviewer   Everywhere static pipelines
``` [cite: 159, 191]

#### 🎙️ Bay 1: Hermes Jarvis (Hands-Free Voice Client)
*   **Features:** Houses Apollo (the voice copilot with vault memory and vocal briefings) [cite: 87, 422]. By clicking the microphone ear icon or running `/wake on` in the CLI, you trigger the **openWakeWord** or **sherpa** local ONNX engines to listen to your voice [cite: 435, 436, 437].
*   **Routing:** Recognizes custom wake phrases. Saying *"Hey coder"* boots your terminal developer profile [cite: 437]; saying *"Hey Hermes"* launches your default persona [cite: 437]. It transcribes your audio natively [cite: 423], performs local tasks [cite: 423], and responds using high-quality spoken text-to-speech (TTS) [cite: 423].

#### 🧠 Bay 2: Agent Mastermind / Chat
*   **Features:** The primary interface to converse with your agent fleet [cite: 564]. It features a model manager dropdown that lets you swap out the AI "brain" instantly without code-level configurations [cite: 565].
*   **Routing:** Run high-complexity tasks on flagship cloud APIs [cite: 503], or switch to **free, local, private, and uncapped models** (like `qwen2.5-coder:latest` or `gemma2:2b` via Ollama) to execute long-horizon text generation and script edits for \$0 [cite: 485, 486, 489].

#### 🗂️ Bay 3: Idea Factory (Self-Kanban / Paperclip HQ)
*   **Features:** A visual, 5-column Kanban board mapping your operational pipelines [cite: 542]. 
*   **Routing:** You drop a plain-English request (e.g., *"Make an ad campaign for Allen storm recovery"*) [cite: 140, 208]. The system automatically assigns a Planner agent to break the goal into cards, a Builder agent to write the assets, and an Auditor agent to verify compliance [cite: 232, 292, 532].

#### 📈 Bay 4: SEO Room (OpenSEO & Everywhere Engine)
*   **Features:** Handles your in-house organic growth engines [cite: 171]. OpenSEO extracts your Search Console metrics and finds high-impression, page-2 keywords [cite: 308].
*   **Routing:** You feed one case study and one keyword to the Everywhere Engine [cite: 304]. It creates 5 unique articles, builds static Eleventy page folders, deploys them to Netlify, and submits them to the Indexceptional API to rank inside Google and AI search Overviews (AEO/GEO) [cite: 33, 304, 382].

#### 🎬 Bay 5: Studio / NotebookLM + Higgsfield
*   **Features:** Your creative and media production center [cite: 192]. It accesses your 39GB of raw drone and testimonial footage inside `02_Media_Vault` [cite: 159, 211].
*   **Routing:** Connects to **Higgsfield MCP** and **Seedance 2.5** to write, script, reframe to 9:16, caption, and compile video reels locally [cite: 208, 335, 628]. You can also use **HeyGen API integrations** to automatically generate video files in your face and cloned voice [cite: 219, 319].

#### 🌌 Bay 6: Memory Galaxy (Obsidian Bridge)
*   **Features:** Your bidirectional read/write bridge into your local Obsidian markdown notes vault [cite: 192, 230]. 
*   **Routing:** Running the command **`/save`** inside Claude Code or Hermes instantly writes any valuable chat session, code pattern, or strategy output into the vault [cite: 396, 397]. The folder becomes your persistent cross-agent memory, so different AI models never start a session cold [cite: 288, 429].

#### 🏛️ Bay 7: Build Gallery (Outbox Staging)
*   **Features:** A visual archive of your finished web, video, and copy deliverables [cite: 192].
*   **Routing:** Adhering to the **Outbox Shield (DEC-005)**, no automated pipeline can publish content or spend money autonomously [cite: 413, 541]. Completed items land here as **PAUSED** files until you review and authorize them to go live [cite: 193, 202, 546].

---

### 🚀 ADVANCED SYSTEM ACCELERATORS IN THE BOX

*   **jcode (The 14x Lightweight Coder):** A Rust-engineered alternative to standard coding runtimes [cite: 355]. While standard Claude Code idles at ~387MB of RAM and takes seconds to boot [cite: 355], `jcode` operates on **only 28MB of RAM, boots in 14 milliseconds**, and supports the exact same Opus-class capabilities on the subscription accounts you already pay for [cite: 355, 359]. It includes automatic session recall and full workspace previews [cite: 355, 360].
*   **Hermes Astros & Oracle (The Watchmen):** Custom, autonomous loops designed to run on schedules [cite: 66, 432]. **Astros** scans competitive websites and maps keyword adjustments weekly [cite: 66, 432]; **Oracle** acts as an industry news radar, compiling highly curated markdown briefs into your second brain so you always stay ahead of market trends [cite: 66, 432, 556].
*   **Gemini Deep Research Max:** A parallel research node deployed inside your custom Gems [cite: 60, 401]. Deep Research Max automatically plans research, conducts concurrent web crawls, maps competitor densities, and outputs clean Markdown files directly into your active context directories [cite: 60, 401].

---


📂 **Next Step Suggestion:**  
I can configure your local **`m7_doctor.py`** diagnostic file to run a quick test over your freshly integrated `gsc_m7_config.json` client secrets. Would you like me to map out this connection check? [cite: 159, 287]