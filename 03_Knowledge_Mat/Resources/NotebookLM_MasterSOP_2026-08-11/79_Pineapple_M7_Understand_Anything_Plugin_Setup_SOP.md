---
source: "NotebookLM - Master SOP 8/26"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: d969df54-04d2-4521-ba27-cf6b79b1b411
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW free?,green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# Pineapple M7: Understand Anything Plugin Setup SOP

### 🛰️ PINEAPPLE M7 — "UNDERSTAND ANYTHING" PLUG-IN SETUP
**Document ID:** `04_Tech_Lab/config/SOP_M7_Understand_Anything_Setup.md` [cite: 52]  
**Authority:** JR. Moeakiola (Principal) & Saia Moeakiola (Senior Operations Manager) [cite: 186]  
**Security Status:** Gated under the Outbox Shield (DEC-005) [cite: 15] — **Active Plugin Configuration Block** [cite: 227].  
**Operations Blueprint:** Polynesian-owned | RCAT Licensed `#03-0637` | IKO Certified [cite: 18, 126, 256].  

---

### 🗺️ THE VISUAL CONCEPT MAP: HOW UNDERSTAND ANYTHING WORKS

Instead of letting your agents guess how your files are structured, this plugin allows **Claude Code** to generate a complete, interactive, color-coded map of your vault (`C:\Pineapple Contractors M7`) [cite: 265]. 

```
  C:\Pineapple Contractors M7\  ──►  /understand Scan  ──►  .understand-anything/knowledge-graph.json
                                                                            │
      ┌─────────────────────────────────────────────────────────────────────┴─────────────────────────────────────┐
      ▼                                                                     ▼                                     ▼
 /understand-dashboard                                             /understand-onboard                            /understand-diff
 Interactive clickable visual map of layers (API, UI, Utility) [cite: 265]  Guided tours ordered by dependencies [cite: 265]  Evaluates blast radius of edits [cite: 267]
``` [cite: 265]

---

### 🔌 STEP 1: THE HANDS-FREE AUTOMATED INSTALLATION PROMPT

Because you run a **zero-error, agent-driven environment** [cite: 114, 288], you do not need to touch the terminal yourself to download or install this plugin [cite: 188]. Simply copy the prompt block below, paste it directly into your **Claude Code** or **Hermes** session, and let the agent configure it for you [cite: 188, 190, 191]:

```text
/goal "Act as the Lead Systems Engineer for PM7 [cite: 50, 197]. We need to install and configure the 'Understand Anything' visual codebase plugin [cite: 265]. Please perform these actions in order [cite: 6]:
1. Run the Claude Code plugin marketplace commands to add and install the utility:
   /plugin marketplace add Egonex-AI/Understand-Anything
   /plugin install understand-anything [cite: 266]
2. Once installed, verify that the directories '.understand-anything/' are successfully initialized [cite: 265].
3. Create a clean system documentation note in '03_Knowledge_Mat/00_Atlas/SOP_Understand_Anything.md' outlining usage guidelines [cite: 186, 201].
4. Run our local '04_Tech_Lab/scripts/brand_firewall.py' scan over the configuration directory to ensure zero green color styling leaks or banned terms [cite: 4, 80].
5. Respond with a completed checklist, then pause and wait for Saia's review [cite: 192, 205]."
```

---

### ⚙️ STEP 2: DYNAMIC SYSTEM CONFIGURATION (`config.yaml`)

To ensure that your **Agent OS** knows how to coordinate this plugin as an automated, background-run tool [cite: 140, 161], save this configuration block inside your active profile settings:

📁 **`%LOCALAPPDATA%\hermes\profiles\seo\config.yaml`** [cite: 311]  
*(Also mirrored in your active workspace configuration directories)* [cite: 311]

```yaml
# %LOCALAPPDATA%\hermes\profiles\seo\config.yaml
# Add this under your active mcp_servers configuration block [cite: 227]

mcp_servers:
  # 🗺️ Understand Anything Codebase Graphing Engine [cite: 265]
  understand_anything:
    command: "npx"
    args:
      - "-y"
      - "@egonex/understand-anything"
      - "--project-path"
      - "C:\\Pineapple Contractors M7"
      - "--auto-update"                  # Keeps sitemaps and dependency graphs synced post-commit [cite: 266]
      - "--exclude-dirs"
      - "node_modules,02_Media_Vault,.git" # Ignores heavy media directories to conserve tokens [cite: 144, 266]

permissions:
  # Safe-fence parameters for the visualization engine [cite: 78]
  smart_approvals:
    require_approval_on:
      - "generate-tours"
      - "rebuild-graph"
```

---

### 📋 STEP 3: ESSENTIAL COMMAND CHEATSHEET

Once the agent completes the installation, you can run these simple commands natively inside your **Claude Code** workspace [cite: 265]:

*   **`/understand`** — Performs an incremental analysis of your vault. It scans changed files, identifies dependencies, and updates the local metadata [cite: 265]. *Tip: Run the first scan on your local Ollama engine (`gemma2`) to check file associations for \$0 before running it on flagship models [cite: 195, 266].*
*   **`/understand-dashboard`** — Launches an interactive, clickable HTML representation of your entire contracting architecture [cite: 265].
*   **`/understand-onboard`** — Instantly generates a structured tour of the codebase ordered by priority dependencies, perfect for onboarding new technicians [cite: 265, 267].
*   **`/understand-diff`** — Compares active staging edits with your target master files and alerts you to the exact **"blast radius"** (files that will break) before you commit or push code changes to GitHub [cite: 143, 267].

---


🎬 **Next Step Suggestion:**  
I can configure your local **`outbox_watcher-v3.py`** to automatically trigger a brief `/understand-diff` scan every time you save a new static page template, ensuring that layout changes do not break any visual dependencies across your active directories [cite: 80, 267]. Would you like me to connect this diagnostic sweep?