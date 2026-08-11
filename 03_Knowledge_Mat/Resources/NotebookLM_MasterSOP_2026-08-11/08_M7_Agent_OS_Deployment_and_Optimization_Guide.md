---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 48cf63c5-5bb3-4db1-802e-a6398fe168e0
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# M7 Agent OS: Deployment and Optimization Guide

I have built and published your customized **`brand-firewall.py`** compliance script. It is now live in your Studio panel, ready to protect your brand assets from accidental style leaks. 

---

### 🛡️ 1. SETTING UP THE BRAND FIREWALL COMPLIANCE SCRIPT

The **`brand-firewall.py`** script acts as the automated gatekeeper (or "bouncer") for your system [cite: 256, 314]. It scans staged text blocks or files, guarantees **zero green elements**, blocks prohibited marketing terms, and verifies that required local trust signals are locked in place before anything goes live [cite: 256, 354].

#### Local Code Integration:
Save the published python script directly to your local workspace under:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\brand_firewall.py` [cite: 257]

#### How to Execute checks on your machine:
Your local AI agents can execute this check behind the scenes automatically [cite: 303], or you can trigger it manually in your terminal [cite: 240, 260]:

*   **To check a specific markdown draft:**
    ```bash
    python 04_Tech_Lab/scripts/brand_firewall.py 01_Command_Center/Outbox_Drafts/draft_page.md
    ``` [cite: 240, 260]
*   **To check raw text strings directly in the terminal:**
    ```bash
    python 04_Tech_Lab/scripts/brand_firewall.py "Book a free inspection with our IKO Certified roofing team today!"
    ``` [cite: 260]
    *(This will trigger a fail, flagging "free inspection" and "IKO Certified" and outputting mandated fixes like "CPPA" and "IKO Certified") [cite: 90].*

---

### 📉 2. TOKEN SAVINGS WITH HEADROOM & PONYTAIL

When running advanced multi-agent development sessions, context window inflation is your main cost bottleneck [cite: 4, 298]. Implementing open-source pre-processors keeps your model expenses down:

*   **Headroom (60% to 95% Context Savings):** Headroom intercepts conversation payloads before they hit the API [cite: 4, 57]. It automatically trims repetitive rules, directory readouts, and redundant files, shrinking payload sizes down to **60–95% of their original token volume** [cite: 4, 57, 58].
*   **Ponytail (54% to 94% Code Compression):** Designed specifically for code writing tasks [cite: 58, 59], Ponytail acts like a "lazy senior developer" [cite: 58]. It prevents agents from re-reading and writing code segments that haven't changed, reducing generated code bloat by **54% to 94%** [cite: 58, 59]. 

Combining both tools allows you to run long development loops at a fraction of standard API costs [cite: 58].

---

### 💻 3. DEPLOYING A LOCAL DESKTOP SETUP FOR YOUR AGENT OS

To run a localized command center without cloud fees, organize your desktop directory structure exactly to the **4-Fala Vault topography** [cite: 205, 334]:

#### Step 1: Scaffold the Directory Layout
Create a root folder named **`C:\Pineapple Contractors M7`** and build these four distinct rooms [cite: 294, 314]:
1.  📁 **`01_Command_Center/`:** The Main Office. Contains your rules, playbooks, master SOPs, and the secure **`Outbox_Drafts/`** folder where all AI work lands **PAUSED** [cite: 257, 314].
2.  📁 **`02_Media_Vault/`:** The Media Locker. Hosts your drone photos, job images, and customer reviews [cite: 257, 314].
3.  📁 **`03_Knowledge_Mat/`:** The Memory Vault. Houses your permanent SOP atlas (`00_Atlas/`) and your core **`SHARED_MEMORY.md`** file [cite: 257, 314].
4.  📁 **`04_Tech_Lab/`:** The Tool Shed. Holds python scripts, launchers, local configurations, and your secure API keys [cite: 257, 314].

#### Step 2: Initialize Your Services
Launch your local stack every morning by double-clicking the launcher file in your root folder [cite: 321]:
*   **`LAUNCH_ALL.bat`**  
    This file boots your Node API gateway (`server.js`) on port **`:3737`**, your front-end Agent OS UI on port **`:3000`**, the Paperclip agent engine on port **`:3100`**, and the python services on port **`:51763`** [cite: 257, 321].
*   **`M7_DOCTOR.bat`**  
    Double-click this right after boot to run a diagnostic connection test and verify your local database, models, and directory health [cite: 257, 258].

---

### 🛰️ 4. CONFIGURING THE DIFFERENT HERMES PROFILES

To prevent **context contamination** (like the AI offering a roof audit to a streetwear customer) [cite: 295, 314], split your work across specialized profile directories located at:  
📁 **`%LOCALAPPDATA%\hermes\profiles\`** [cite: 323]

#### The Profile Matrix:
Inside your dashboard profile manager, configure your seven specialized personas:
*   **`main` / `default`:** Runs on the fast local model (**`qwen2.5-coder:latest`** or **`gemma2:2b`**) to handle file cleanups, folder updates, and routine terminal jobs [cite: 237, 264, 270].
*   **`leads`:** Grounded against `M7_LEAD_ENGINE.md`. Connected to your local `Leadstack CRM` pipeline to run speed-to-lead routing [cite: 270, 324].
*   **`seo`:** Grounded against `M7_SEO_DAILY_SOP.md`. Wired to OpenSEO and GSC data to build location-specific ranking landing pages [cite: 251, 270, 324].
*   **`marketing`:** Runs copywriting framework parameters like **PACT** and **CARPARK** to draft campaigns [cite: 92, 270, 324].
*   **`content`:** Wired to `02_Media_Vault/` and **`video-multiplier.py`** to stitch together 50/5/3 Lego video reels [cite: 295, 324].
*   **`roofing`** and **`restoration`:** Strictly partitioned business profiles utilizing exclusive service vocabularies [cite: 270, 324].

#### 🔌 Integrating Your Local Obsidian MCP Bridge
To allow your coding agents (such as Claude Code) to seamlessly search and edit your local notes vault [cite: 311], save this configuration block directly on your machine [cite: 311]:

*   **Target File Path:** `C:\Pineapple Contractors M7\04_Tech_Lab\config\claude_desktop_obsidian_mcp.json` [cite: 311]

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
``` [cite: 311, 314]

---

📂 **Next Step Suggestion:**  
We can map out a custom local n8n workflow file that captures inbound leads from your website forms and routes them directly to Saia's phone via a Telegram alert. Would you like me to output that webhook setup?