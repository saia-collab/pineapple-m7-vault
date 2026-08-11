---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: b4becd29-c95e-4f13-9f32-45821da9c407
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Pineapple M7 System Automation and SEO Configuration Guide

### 🧹 What the Folder-Tidy Automation Script (`M7_TIDY.bat`) Does

The **`M7_TIDY.bat`** script acts as an automated filing assistant for your root directory (`C:\Pineapple Contractors M7\`). Over time, active development and system setups can leave behind loose zip files, backup installers, and duplicate batch shortcuts that create digital clutter and cause your local AI models to experience **context drift** (wasting API tokens by scanning old, irrelevant draft configurations). 

To prevent this, the script safely automates three operations:
1. **Creates a Secure Vault Archive:** Checks for and builds a dedicated folder named **`_Archive/`** right in your root directory.
2. **Sweeps Heavy Installation Packages:** Automatically sweeps up and archives bulk legacy `.zip` installer files (such as old `agent-os-pack` or `LAUNCH_CLAUDE_CODE` installers) that are hogging hard drive space.
3. **Flushes Empty & Broken Root Launchers:** Collects old, broken root `.bat` files and desktop shortcut links and archives them, ensuring you only ever use your high-performance morning launcher (**`LAUNCH_ALL.bat`**).
4. **Unifies Your Knowledge Base:** Gathers loose markdown files (such as your *"Near Me" Domination* guide, *Accessing and Editing WordPress* tutorial, and *Understand Anything codebase mapping* guide) and moves them cleanly into **`03_Knowledge_Mat\00_Atlas\`**. This makes them immediately searchable and indexable for your local AI agents' **shared memory**.

---

### 🗺️ Mapped-Out Code: `M7_TIDY.bat`

Save this exact code to your local machine as a batch file:  
📁 **`C:\Pineapple Contractors M7\M7_TIDY.bat`**

```cmd
@echo off
:: PINEAPPLE M7 — AGENT OS FOLDER CLEANUP & TIDY AUTOMATION
:: Target Root: C:\Pineapple Contractors M7\

echo ===================================================
echo 🍍 PINEAPPLE M7 — FOLDER TIDY AUTOMATION ACTIVE
echo ===================================================

cd "C:\Pineapple Contractors M7" 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Root directory C:\Pineapple Contractors M7 not found!
    echo Please make sure this script is located or run inside your vault root.
    pause
    exit /b
)

:: 1. Create _Archive folder if it doesn't exist
if not exist "_Archive" (
    echo Creating _Archive directory...
    mkdir "_Archive"
)

:: 2. Move old zip installation packs to _Archive
echo Archiving obsolete zip archives...
move /y "agent-os-pack-2026-07-03.zip" "_Archive\" >nul 2>&1
move /y "agent-os-pack-2026-07-05.zip" "_Archive\" >nul 2>&1
move /y "mobbin-sample-pack-100.zip" "_Archive\" >nul 2>&1
move /y "seo-pack.zip" "_Archive\" >nul 2>&1
move /y "CLAUDE MOBILE.zip" "_Archive\" >nul 2>&1
move /y "AM_STARTUP.zip" "_Archive\" >nul 2>&1
move /y "AM_STARTUP (2).zip" "_Archive\" >nul 2>&1
move /y "LAUNCH_CLAUDE_CODE.zip" "_Archive\" >nul 2>&1
move /y "M7_CLEANUP.zip" "_Archive\" >nul 2>&1
move /y "M7_DOCTOR.zip" "_Archive\" >nul 2>&1
move /y "ORGANIZE_MEDIA.zip" "_Archive\" >nul 2>&1

:: 3. Move empty/broken root launchers and shortcuts to _Archive
echo Archiving broken legacy launchers...
move /y "RUN_AGENT_OS.bat" "_Archive\" >nul 2>&1
move /y "RUN_AGENT_OS.bat - Shortcut.lnk" "_Archive\" >nul 2>&1
move /y "START_LOCAL_STUDIO.bat" "_Archive\" >nul 2>&1
move /y "START_PAPERCLIP.bat" "_Archive\" >nul 2>&1
move /y "UPDATE_AGENT_OS.bat" "_Archive\" >nul 2>&1

:: 4. Move loose markdown SOPs and reference files to the Atlas directory
echo Tidying loose Markdown reference documents to the Atlas...
if not exist "03_Knowledge_Mat\00_Atlas" mkdir "03_Knowledge_Mat\00_Atlas"

move /y "How to Dominate _Near Me_ Searches PM7.md" "03_Knowledge_Mat\00_Atlas\" >nul 2>&1
move /y "HERMES AGENTIC SOP_ _Near Me_ Domination Pipeline.md" "03_Knowledge_Mat\00_Atlas\" >nul 2>&1
move /y "EXCTRACT 23rd May_ Hermes Agent SEO SOP AND THE.md" "03_Knowledge_Mat\00_Atlas\" >nul 2>&1
move /y "Accessing and Editing WordPress Website.md" "03_Knowledge_Mat\00_Atlas\" >nul 2>&1
move /y "ElevenLabs_ Spoken Voice Output Choice.md" "03_Knowledge_Mat\00_Atlas\" >nul 2>&1
move /y "Understand Anything_ Turn Any Codebase Into an Interactive Knowledge Graph.md" "03_Knowledge_Mat\00_Atlas\" >nul 2>&1
move /y "USER.md" "03_Knowledge_Mat\00_Atlas\" >nul 2>&1
move /y "LAUNCHERS_README.md" "03_Knowledge_Mat\00_Atlas\" >nul 2>&1

echo ===================================================
echo ✅ FOLDER CLEANUP & TIDY COMPLETE!
echo No active system files or core folders were modified.
echo Broken root files archived; loose guides moved to Atlas.
echo ===================================================
```

**How to Run It:** Save the code, place the script directly inside your local root `C:\Pineapple Contractors M7\`, and double-click. Your workspace root is instantly cleared of layout noise!

---

### 📈 How to Configure Your Google Search Console (GSC) Tracker

Your local server API running on **`localhost:3737`** displays a live dashboard mapping your keyword positions, click leaks, and AI Overview (AIO) citation data. To link this tracker directly to your Google Search Console domain property and multi-platform profiles (YouTube, TikTok, Instagram, X), follow this 3-step setup:

#### Step 1: Create OAuth 2.0 Keys in Google Cloud Console
1. Open the **Google Cloud Console** (`console.cloud.google.com`) and log in.
2. Create a new project called **`M7-Search-Console-Link`**.
3. Go to **APIs & Services → Library**, search for the **Google Search Console API**, and click **Enable**.
4. Go to the **OAuth Consent Screen** tab:
   * Select **External** and fill out the basic developer contact details.
   * Under Scopes, add: `https://www.googleapis.com/auth/webmasters.readonly`.
   * Under Test Users, add your primary Google account email.
5. Go to **Credentials → Create Credentials → OAuth Client ID**:
   * Set Application Type to **Web Application**.
   * Under **Authorized Redirect URIs**, paste these two addresses to allow connection with your local ports:
     * `http://localhost:3737/oauth2callback`
     * `http://localhost:3000/oauth2callback`
6. Click **Create** and copy your generated **Client ID** and **Client Secret**.

#### Step 2: Configure `gsc_m7_config.json`
Open your local configuration file inside your workspace's tool config directory:  
📁 **`C:\Pineapple Contractors M7\04_Tech_Lab\config\gsc_m7_config.json`**

Replace the placeholders inside the `oauth2_config` object with your actual keys from Step 1:

```json
{
  "gsc_platform_tracker": {
    "version": "M7.2.1",
    "port": 3737,
    "api_endpoint": "http://localhost:3737/api/v1/seo/tracker",
    "oauth2_config": {
      "client_id": "PASTE_YOUR_GOOGLE_CLIENT_ID_HERE.apps.googleusercontent.com",
      "client_secret": "PASTE_YOUR_GOOGLE_CLIENT_SECRET_HERE",
      "redirect_uris": [
        "http://localhost:3737/oauth2callback",
        "http://localhost:3000/oauth2callback"
      ],
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token"
    },
    "monitored_domains": [
      "pineappleroofingllc.com",
      "pineapplecontractors.com"
    ],
    "monitored_platforms": [
      {
        "platform": "YouTube",
        "property_url": "sc-set:https://www.youtube.com/@PineappleRoofing"
      },
      {
        "platform": "Instagram",
        "property_url": "sc-set:https://www.instagram.com/pineappleroofing"
      },
      {
        "platform": "TikTok",
        "property_url": "sc-set:https://www.tiktok.com/@pineappleroofing"
      },
      {
        "platform": "X (Twitter)",
        "property_url": "sc-set:https://x.com/pineappleroof"
      }
    ],
    "thresholds": {
      "striking_distance": {
        "min_position": 5.0,
        "max_position": 20.0,
        "min_impressions": 100
      },
      "leak_alerts": {
        "min_impressions": 1000,
        "max_ctr_percentage": 1.0
      }
    },
    "telemetry": {
      "tracking_interval_hours": 24,
      "auto_index_pings": true,
      "save_baseline_path": "C:\\Pineapple Contractors M7\\03_Knowledge_Mat\\raw_analytics\\seo_baselines\\"
    }
  }
}
```

#### Step 3: Run Handshake & Verify
1. Double-click your daily launcher **`LAUNCH_ALL.bat`** to boot up your local system.
2. Open your web browser and go to **`http://localhost:3737`**.
3. Click the **"Authenticate Search Console"** button. Follow Google's prompts to approve the connection.
4. Once completed, your dashboard will link directly to Google's Search Console API. It will automatically populate your "SEO" tab with striking-distance keywords and notify you if your social media channels (YouTube, TikTok, Instagram, X) rank for any local roofing queries!

---

📊 I can write a custom CLI scraper command for your local **`seo` profile** that crawls Google's local map pack results for Frisco roofing companies and maps their visible trust badges directly to your local spreadsheet workspace. Would you like me to output this local mapping script?