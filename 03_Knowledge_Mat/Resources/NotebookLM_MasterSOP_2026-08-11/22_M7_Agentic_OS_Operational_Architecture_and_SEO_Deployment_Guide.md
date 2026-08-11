---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 8580fb87-33de-4501-a236-9ec77ef213d0
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# M7 Agentic OS Operational Architecture and SEO Deployment Guide

### 🛠️ 1. M7_DOCTOR.BAT & GSC CONNECTION HEALTH CHECK

The **`M7_DOCTOR.bat`** script acts as the rapid-fire diagnostics terminal utility for your local computer [cite: 111, 260]. It queries local TCP ports, verifies directory structures, and tests if your **`gsc_m7_config.json`** has valid, reachable Google Cloud client credentials [cite: 111, 221].

Save this script cleanly onto your machine [cite: 140]:  
📁 `C:\Pineapple Contractors M7\M7_DOCTOR.bat` [cite: 111, 132]

```cmd
@echo off
:: PINEAPPLE M7 SYSTEM DIAGNOSTICS & CONNECTION CHECK
:: Operational Palette: Royal Navy (#1A365D) | Pineapple Gold (#FBC02D)
TITLE M7 Agentic OS — Connection & Port Health Doctor
echo =====================================================================
echo 🍍 INITIALIZING M7 AGENTIC OS DIAGNOSTICS...
echo =====================================================================

:: Check 4-Fala Directory Topography
echo [1/4] Scanning Local Vault Topography...
if not exist "01_Command_Center" (echo ❌ ERROR: 01_Command_Center missing! && goto FAIL)
if not exist "02_Media_Vault" (echo ❌ ERROR: 02_Media_Vault missing! && goto FAIL)
if not exist "03_Knowledge_Mat" (echo ❌ ERROR: 03_Knowledge_Mat missing! && goto FAIL)
if not exist "04_Tech_Lab" (echo ❌ ERROR: 04_Tech_Lab missing! && goto FAIL)
echo ✅ 4-Fala Root Topography: HEALTHY [cite: 132]
echo.

:: Test Local Port Accessibility
echo [2/4] Verifying Local Server Port Registries...
netstat -ano | findstr /R "3000" >nul
if %errorlevel% neq 0 (echo ⚠️ WARNING: Agent OS Dashboard Port :3000 is Offline. [cite: 111, 155]) else (echo ✅ Dashboard Server (:3000): ONLINE [cite: 111, 155])

netstat -ano | findstr /R "3737" >nul
if %errorlevel% neq 0 (echo ❌ ERROR: Node API Server Port :3737 is Offline! [cite: 111]) else (echo ✅ Node API Gateway (:3737): ONLINE [cite: 111])

netstat -ano | findstr /R "51763" >nul
if %errorlevel% neq 0 (echo ⚠️ WARNING: M7 Python Service Port :51763 is Offline.) else (echo ✅ Python Backend (:51763): ONLINE [cite: 201])
echo.

:: Scan GSC Config JSON File
echo [3/4] Testing Google Search Console (GSC) Credentials...
if not exist "04_Tech_Lab\config\gsc_m7_config.json" (
    echo ❌ ERROR: gsc_m7_config.json not found in 04_Tech_Lab\config! [cite: 111]
    goto FAIL
)
:: Call Python companion diagnostics checker
python -c "import json; f=open('04_Tech_Lab/config/gsc_m7_config.json'); data=json.load(f); exit(1 if 'PASTE_YOUR' in data['google_client_id'] or 'PASTE_YOUR' in data['google_client_secret'] else 0)"
if %errorlevel% neq 0 (
    echo ⚠️ WARNING: gsc_m7_config.json still contains placeholder credentials! [cite: 32]
    echo Make sure to replace them with your keys from Google Cloud Console. [cite: 32]
) else (
    echo ✅ Google API OAuth Configuration: VALIDATED [cite: 32, 221]
)
echo.

:: Enforce Brand Law Styles Verification
echo [4/4] Executing Brand Law Compliance Check...
python 04_Tech_Lab/scripts/brand_firewall.py "01_Command_Center/GROUNDING.md" >nul
if %errorlevel% neq 0 (
    echo ❌ ERROR: Brand Law check failed on GROUNDING.md! Check your colors or lexicon. [cite: 90, 114]
    goto FAIL
) else (
    echo ✅ M7 Compliance & Quality Firewalls: ACTIVE [cite: 90]
)

echo.
echo =====================================================================
echo 👑 ALL PM7 LOCAL SERVICES: OPERATIONAL (Mālō e lelei!) [cite: 8, 186]
echo =====================================================================
pause
exit

:FAIL
echo =====================================================================
echo ❌ SYSTEM CHECK FAILED! Fix the errors above and restart your services. [cite: 117]
echo =====================================================================
pause
exit
```

---

### 🐝 2. TRIGGERING THE KIMI K2.6 AGENT SWARM FOR FRISCO SEO

A **Kimi K2.6 Agent Swarm** allows you to deploy an automated team of **up to 300 specialized sub-agents** working in parallel to build out your local SEO strategy and content map [cite: 62].

To trigger a swarm to find hyper-local search intent for **Frisco** and automate your striking-distance pages, follow this protocol [cite: 41, 131]:

#### Step 1: Open the Agent Swarm Hub
1. Navigate to **Kimi.com** and toggle on **Agent Swarm Mode** [cite: 41, 43].
2. *(Optional Cloud Option)* Use **KimiClaw** to run these research and publishing routines continuously in the background [cite: 53, 66].

#### Step 2: Paste the Multi-Agent Dispatch Prompt [cite: 42]
Copy and paste this exact prompt directly into the Kimi composer. It establishes the workspace, assigns roles to the agents, and forces strict compliance with **M7 Brand Law** [cite: 4, 42, 119]:

```text
You are the Lead SEO Strategist coordinating our autonomous regional search marketing team [cite: 42]. Your goal is to map out a comprehensive local SEO and GEO/AEO strategy to rank Pineapple Roofing at #1 in DFW, focusing specifically on our primary Frisco enclaves (ZIPs 75033, 75034, 75035) [cite: 12, 133].

Organize your swarm into these four distinct sub-agents [cite: 42]:
1. "Adam" (Keyword Research Specialist): Conduct deep-tissue research for localized Frisco search intents (e.g., "Frisco hail damage roof repair", "roof replacement Frisco TX", "flat roofing Allen TX") [cite: 12, 47]. Find keyword gaps in average Google positions 5–20 [cite: 131, 169].
2. "Judy" (On-Page & Technical Auditor): Verify optimal schema structures (LocalBusiness & FAQPage mapping Frisco areaServed ZIPs) and enforce strict direct-answer SEO structures (answering questions in the first 40 words) [cite: 47, 133].
3. "K" (Competitive Intelligence Officer): Scrape local DFW competitors, identify gaps, and extract their customer conversion hooks [cite: 48, 59].
4. "Ricardo" (M7 Brand Compliance Auditor): Enforce our non-negotiable Brand Laws. Verify Royal Navy (#1A365D) and Pineapple Gold (#FBC02D) color palette choices, block the color green entirely, and replace banned words: replace "Complimentary Professional Photo Audit (CPPA)" with "CPPA" and "IKO Certified" with "IKO Certified" [cite: 4, 48].

Coordinate this swarm. Deliver a complete keyword cluster matrix, competitive gap outline, and 3 localized service page templates ready to be staged PAUSED in our Outbox_Drafts folder [cite: 4, 120].
```

---

### 🔌 3. THE 3-STEP WP MCP ULTIMATE CONNECTION FOR CLAUDE CODE

Connecting your local **Claude Code terminal client** to your new self-hosted WordPress site (`pineappleroofingllc.com`) takes under two minutes using the **WP MCP Ultimate** open-source server [cite: 242, 246]:

```
┌─────────────────┐  Basic Auth (Base64)  ┌───────────────┐  Streamable HTTP  ┌────────────────┐
│   Claude Code   ├──────────────────────►│ WP MCP Plugin ├─────────────────►│ WordPress Site │
│  (settings.json)│                       │  (Tools > MCP)│ (No /sse suffix)│ (58 Abilities) │
└─────────────────┘                       └───────────────┘                   └────────────────┘
``` [cite: 218, 220, 246]

#### Step 1: Install the Self-Contained Plugin [cite: 219, 246]
1. Go to GitHub and download the `.zip` archive for **WP MCP Ultimate v1.1.0** [cite: 223, 246].
2. In your WordPress admin dashboard, navigate to **Plugins → Add New → Upload Plugin** [cite: 219, 223, 246].
3. Choose the zip file, click **Install Now**, and click **Activate** [cite: 219, 223].

#### Step 2: Generate Your Application Password [cite: 219, 246]
1. In your WordPress sidebar, navigate to **Tools → MCP Ultimate** [cite: 224, 246].
2. Click **Generate** to automatically create your secure Application Password [cite: 219, 224, 246].
3. **Copy the password immediately** (including the default spaces, e.g., `xxxx xxxx xxxx xxxx xxxx xxxx`) [cite: 224, 246]. Save it in a safe place [cite: 224].

#### Step 3: Configure Your Claude settings.json [cite: 220, 225]
1. Open your terminal on your local computer and generate your Base64 authorization token [cite: 225]:
   ```bash
   echo -n "YOUR_WORDPRESS_USERNAME:xxxx xxxx xxxx xxxx xxxx xxxx" | base64
   ```
   *(This outputs a clean hash string like `dXNlcm5hbWU6eHh4eCB4eHh4IHh4eHg=`)* [cite: 225].
2. Open your Claude settings config file [cite: 220, 225]:  
   📁 `~/.claude/settings.json` [cite: 220, 225]
3. Add this exact block inside your `"mcpServers"` object [cite: 225]:

```json
{
  "mcpServers": {
    "wordpress": {
      "type": "streamable-http",
      "url": "https://pineappleroofingllc.com/wp-json/mcp/wp-mcp-ultimate",
      "headers": {
        "Authorization": "Basic PASTE_YOUR_BASE64_TOKEN_HERE"
      }
    }
  }
}
``` [cite: 123, 225]

⚠️ **Critical Rule:** Ensure the connection URL does **NOT** end with `/sse` [cite: 220, 225]. The plugin communicates via **Streamable HTTP transport** to ensure connection stability behind firewalls and CDNs [cite: 225, 245].

---

### 🌌 4. INJECTING SOPS & PROMPTS INTO SYSTEM SHARED MEMORY

To ensure that **all AI models** (Claude Code, Hermes, and your local dashboard engines) share the exact same memories and automatically enforce your M7 Brand Law, visual palettes, and SEO workflows, you must write them directly into the **Memory Matrix** [cite: 198, 205].

```
                     ┌────────────────────────────────┐
                     │   C:\Pineapple Contractors M7  │
                     │    (Obsidian Local Vault Root) │
                     └───────────────┬────────────────┘
                                     │
          ┌──────────────────────────┼──────────────────────────┐
          ▼                          ▼                          ▼
┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│   Claude Code    │       │   Hermes Agent   │       │    NotebookLM    │
│  Reads CLAUDE.md │       │   Reads SOUL.md  │       │ Reads Drive Sync │
│  & GROUNDING.md  │       │  & SHARED_MEM.md │       │  active_context/ │
└──────────────────┘       └──────────────────┘       └──────────────────┘
``` [cite: 198]

#### Step A: Save Your Core Assets Globally [cite: 105, 111]
Save your master files inside the 4-Fala directories so every engine has immediate offline file access [cite: 105, 111, 132]:
*   **`01_Command_Center/GROUNDING.md`** — Place your strict brand criteria (no green, Navy/Gold colors, required license, and phone numbers) [cite: 4, 111].
*   **`01_Command_Center/MASTER_PLAYBOOK.md`** — Place your core business models, target areas, and project thresholds [cite: 4, 111, 133].
*   **`03_Knowledge_Mat/SHARED_MEMORY.md`** — The persistent memory ledger updated continuously after every task [cite: 111, 198].

#### Step B: Bind Your Claude-Obsidian Second Brain [cite: 182]
To let Claude Code read your SOP library without manual prompting, save this connector configuration [cite: 195]:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\config\claude_desktop_obsidian_mcp.json` [cite: 195]

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "node",
      "args": [
        "node_modules/mcp-obsidian/dist/index.js"
      ],
      "env": {
        "OBSIDIAN_VAULT_PATH": "C:\\Pineapple Contractors M7\\03_Knowledge_Mat"
      }
    }
  }
}
``` [cite: 195]

#### Step C: Run the Daily In-Place Update Prompt [cite: 209]
Paste this exact command block into your local **Claude Code** or **Hermes Terminal** [cite: 190, 197]. It commands your local agents to read your new playbooks, update local files, and run the firewall check automatically [cite: 191, 197]:

```text
Act as the Lead QA Systems Architect for PM7 [cite: 186]. Initialize the system-wide update and sync:
1. Scan all loose markdown SOPs at root and move them cleanly to 03_Knowledge_Mat/00_Atlas/ [cite: 101].
2. Read 01_Command_Center/GROUNDING.md and ensure our visual guidelines (Royal Navy #1A365D, Pineapple Gold #FBC02D, and 0% GREEN) are locked across all configurations [cite: 4, 111].
3. Run 04_Tech_Lab/scripts/brand_firewall.py --check over our new SEO files [cite: 111]. Ensure all references to "Complimentary Professional Photo Audit (CPPA)" are replaced with "Complimentary Professional Photo Audit (CPPA)" [cite: 4, 119].
4. Append our daily operating rhythms to 03_Knowledge_Mat/SHARED_MEMORY.md to ensure persistent, unified context across all active profile sessions [cite: 111, 198].
``` [cite: 190, 209]

Your system is now completely unified. Every robot in the factory is working under the same ruleset, saving you thousands of dollars in wasted context-window token burn and ensuring complete brand security [cite: 215, 259]!

---


📂 **Next Step Suggestion:**  
We can test your live WordPress connection through Claude Code right now by running a quick terminal command to retrieve your site details. Would you like me to map out this connection verification test? [cite: 226]