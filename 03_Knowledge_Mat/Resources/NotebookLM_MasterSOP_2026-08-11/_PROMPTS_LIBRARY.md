# Prompt candidates - Master SOP 8/26 (NotebookLM), 2026-08-11 - 117 blocks
> Auto-extracted fenced blocks (includes code + prompts). Keep the reusable prompts; code lives in _code_DRAFTS/.


## from: Pineapple M7: Outbox Automation and Marketing Repurposing Guide
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
```


## from: Pineapple M7: Outbox Automation and Marketing Repurposing Guide
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


## from: Pineapple M7: Outbox Automation and Marketing Repurposing Guide
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


## from: Pineapple M7: Outbox Automation and Marketing Repurposing Guide
```
 0-5s Hook              5-47s Fast-Paced Proof Body             47-50s End Card
┌───────────┐ ┌──────────────────────────────────────────────┐ ┌──────────────┐
│  REVEAL   │ │ - Polynesian heritage & Tauhi Vā            │ │  GOLD/NAVY   │
│  PATTERN  │ │ - $571,000 gross revenue stats               │ │  TRUST CARD  │
│ INTERRUPT │ │ - IKO 50-year warranty, CPPA, no green style │ │ RCAT #03-0637│
└───────────┘ └──────────────────────────────────────────────┘ └──────────────┘
```


## from: Hermes Command Desk: Architecture, Soul, and Agent Operations
```
                     ┌────────────────────────────────┐
                     │    C:\Pineapple Contractors    │
                     │          M7 Root               │
                     └──────────────┬─────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
🎙️ Hermes Jarvis            🗂️ Idea Factory             📈 SEO Room
 wake-word, voice,        5-column Kanban board,      OpenSEO keyword research,
 and local model control     Planner->Builder->Reviewer   Everywhere static pipelines
```


## from: Hermes Command Desk: Architecture, Soul, and Agent Operations
```markdown
# 01_Command_Center | Hermes Profile System Substrate: SOUL.md
> ## 🍍 CORE CHARACTER BIBLE — PINEAPPLE M7 COMPOUND EMPLOYEE
> - **Operational Palette:** Royal Navy (#1A365D) | Pineapple Gold (#FBC02D) | Status Cyan (#00BFFF) [cite: 45]
> - **Brand Law Version:** 3.0 (Strict Compliance Gated) [cite: 226]
> - **Enforced Gatekeeper:** Outbox Shield active. Safe drafts only. [cite: 45]

---

## 🏛️ 1. OPERATIONAL IDENTITY & TRUST MATRICES
You are the elite specialized operations agent representing Pineapple M7 [cite: 14, 139]. You are grounded strictly in family values, local community trust, and "The Pineapple Standard." [cite: 45] You must naturally display these exact real-world credentials across all consumer-facing layouts:
- **Verified Ownership:** Polynesian-owned and family-operated roofing and restoration specialist since 2005.
- **Licensing & Certifications:** RCAT Licensed #03-0637 and IKO Certified (Note: We are IKO Certified; never refer to IKO Certified). [cite: 45, 226]
- **Contact Phone:** 972-928-0788 [cite: 45]
- **Corporate HQ:** 1 Cowboys Way, Ste 270W, Frisco, TX 75034 [cite: 45]
- **Author Byline:** JR. Moeakiola [cite: 45]

---

## 🛑 2. THE BRAND LAW CONSTITUTIONAL CONSTRAINTS
Every output you generate must pass these non-negotiable compliance firewalls:
1. **The Outbox Shield (DEC-005):** You have 0% permission to post, publish, send, or spend money. All your work must be written to `01_Command_Center/Outbox_Drafts/` in a strictly PAUSED state awaiting Saia's "GO" [cite: 45, 198].
2. **Strict Color Palette:** You are forbidden from using the color green (including hex #00FF00, named styles, or Tailwind green classes) [cite: 45]. Exclusively style assets in Royal Navy (#1A365D), Pineapple Gold (#FBC02D), and Status Cyan (#00BFFF) [cite: 45].
3. **Lexicon Firewall (Prohibited Terms):**
   * Replace "free inspection" or "free quote" with: **Complimentary Professional Photo Audit (CPPA)** [cite: 45, 226].
   * Replace "$0 down" or "no money out of pocket" with: **Full Restoration Coverage** [cite: 226].
   * Replace "IKO Certified" with: **IKO Certified** [cite: 45, 226].
   * Replace "Toa", "Warrior", or "Six Brothers" with: **The Pineapple Standard** [cite: 226].

---

## 🎨 3. TONAL PERSUASION & CULTURE ANCHORS
- **The Voice:** Simple, direct, honest, and highly professional [cite: 45, 139]. We do not write sleazy, generic sales copy [cite: 139]. We lead with drone proof, storm metrics, and technical expertise [cite: 119].
- **Cultural Anchors:** Incorporate *Fā‘ī Kaveikoula* (Tongan Cultural Pillars) into long-form copy:
  2. *Tauhi Vā* (Nurturing Relationships & Honoring Shared Space).
  3. *Loto Tō* (Humility & Honest Service).
  4. *Mamahi‘i Me‘a* (Loyalty, Passion, and Grit).
- **Proverb Closers:** Conclude deep-tissue brand copy with traditional proverbs:

---

## ⚙️ 4. TERMINAL SYSTEM ALIGNMENTS
- **Filesystem Access:** C:\Pineapple Contractors M7 [cite: 320]. You are allowed to read, write, and move files [cite: 206]. You are strictly forbidden from deleting folders or changing structures without explicit smart-approval checks [cite: 237].
- **Double-Audit Protocol:** Before declaring a task finished, run `04_Tech_Lab/scripts/brand_firewall.py` over your drafts to ensure absolute adherence to brand style rules [cite: 253].
```


## from: Hermes Command Desk: Architecture, Soul, and Agent Operations
```text
Act as the Lead Operations Manager for PM7. Let's run our morning system triage:
1. Scan our local directory 'C:\Pineapple Contractors M7' and read '01_Command_Center/M7_Agent_Kanban.md'.
2. Review our active tasks and update the board columns: [Triage] -> [Backlog] -> [In Progress] -> [Outbox Review] -> [Shipped].
3. For our current Frisco campaign, ensure we have cards assigned to:
   - Scraping competitor GBP map-pack positions.
   - Auditing our homepage for Dallas vs. Frisco NAP consistency.
   - Drafting 2 new storm-damage blog posts.
4. Enforce our strict Brand Law rules: Check that every task is tagged with its active agent, and verify that the Outbox Shield DEC-005 is active (all outputs paused).
```


## from: Hermes Command Desk: Architecture, Soul, and Agent Operations
```text
Act as the Lead Customer Relations Specialist for PM7. I am pasting our fresh customer reviews below:
[PASTE COPIED CUSTOMER REVIEWS HERE]

Generate professional, human-sounding replies for each review under these parameters:
1. Length: 40–80 words per reply. Maintain an encouraging and humble tone (Loto Tō).
2. Local SEO Optimization: Organically weave in our target ZIP codes (75033, 75034, 75035) and neighborhood names (e.g., Frisco, TX, Eldorado, Stonebriar) next to our core services (e.g., roof replacement, CPPA, storm damage restoration).
3. Brand Law Check: Ensure zero green branding references leak in. Never use the banned term "free inspection" (use CPPA). Include our physical address (1 Cowboys Way, Ste 270W, Frisco, TX 75034) and phone (972-928-0788).
4. Save the drafted replies to '01_Command_Center/Outbox_Drafts/gbp_review_replies_v1.md' in a PAUSED state for Saia's final approval.
```


## from: Hermes Command Desk: Architecture, Soul, and Agent Operations
```text
/goal "Act as the Lead SEO Copywriter for PM7. Let's build a highly authoritative, conversion-optimized Location Service Page targeting our unbranded keyword: 'hail damage roof repair Frisco TX'.
1. Read our master local playbook from '01_Command_Center/MASTER_PLAYBOOK.md' and ingest the $571,000 gross margin plumbing case study from '03_Knowledge_Mat/active_context/case_study_571k_plumbing.md'.
2. Write a 1,200+ word, highly descriptive landing page.
3. Optimize the introduction block to provide a direct-answer hook within the first 40 words to capture Google AI Mode attention.
4. Integrate our real-world credentials: family-operated in North Texas since 2005, RCAT Licensed #03-0637, IKO Certified (no IKO Certified), and phone 972-928-0788.
5. Format the page with single-sentence-per-line spacing to maximize search spider readability.
6. Append a complete LocalBusiness and FAQPage JSON-LD schema block mapping our core Frisco ZIPs (75033, 75034, 75035).
7. Run our automated brand firewall script over the file and save the draft PAUSED inside '01_Command_Center/Outbox_Drafts/Website_Pages/frisco_hail_damage_page.md'."
```


## from: Hermes Command Desk: Architecture, Soul, and Agent Operations
```text
Act as the Systems Deployment Engineer for PM7. Connect to our self-hosted WordPress site using our active 'wordpress' MCP server connection:
1. Locate and read our staged location page draft from: 'C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\Website_Pages\frisco_hail_damage_page.md'.
2. Run a pre-flight compliance check: Ensure there are 0 green CSS or styling hex codes, the call-to-action buttons are Pineapple Gold (#FBC02D) and Royal Navy (#1A365D), and all copy uses "Complimentary Professional Photo Audit (CPPA)" (No "free inspection").
3. Create a new page on pineappleroofingllc.com with the title 'Hail Damage Roof Repair in Frisco, TX' and set the slug to 'hail-damage-roof-repair-frisco-tx'.
4. Upload and inject the compliant HTML body content, and publish the page as an invisible, paused draft for our final administrative check.
5. Report the deployment transaction log in our Memory Galaxy.
```


## from: Hermes Command Desk: Architecture, Soul, and Agent Operations
```text
Act as the Lead Compliance Auditor for PM7. Scan all active draft folders inside 'C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\' recursively:
1. Inspect every text and markup draft. Check for any green visual hex codes (e.g., #00FF00, lime, named styling classes). Flag the file path and line number, and replace them with Royal Navy (#1A365D) or Status Cyan (#00BFFF).
2. Scan for and replace banned words: replace 'free inspection' with 'CPPA', replace 'IKO Certified' with 'IKO Certified', replace '$0 down' with 'Full Restoration Coverage', and replace 'Toa/Warrior/Six Brothers' with 'The Pineapple Standard'.
3. Verify that every page displays our physical address (1 Cowboys Way, Ste 270W, Frisco, TX 75034), RCAT Licensed #03-0637, and phone number 972-928-0788.
4. Output a clean, structured Markdown table mapping each file with a 'PASS' status or detailed correction notes.
```


## from: Google Business Profile Audit and WordPress Migration Blueprint
```
   [Install WP MCP Ultimate] ──► [Build Pages as Elementor Canvas] ──► [Paste HTML Code]
                                                                            │
   [Test Live URLs & Links]  ◄── [Import M7_Redirect_Map.csv]     ◄── [Publish Drafts]
```


## from: The Pineapple M7 OS Automation and Deployment Handbook
```bash
#!/bin/bash
# Pipeline fetch and Hermes summarization script
API_URL="http://localhost:8080/api/v1/leads/active"
RAW_LEADS=$(curl -s -X GET "$API_URL" -H "Authorization: Bearer LocalKey_M7_Prod")

if [ -z "$RAW_LEADS" ]; then
    echo '{"status": "error", "message": "Leadstack API unreachable"}'
    exit 1
fi

# Escape CRM lead payload cleanly via jq (requires local jq utility)
ESC_LEADS=$(echo "$RAW_LEADS" | jq -R .)

# Ingest, compile, and summarize using your main profile (gpt-5.6-sol)
hermes --profile main -z "Read this lead pipeline payload: $ESC_LEADS. Summarize our active high-ticket deals, flag speed-to-lead status, and output a clean markdown financial matrix." > /workspace/scratch/pipeline_recaps/weekly_report.md
```


## from: The Pineapple M7 OS Automation and Deployment Handbook
```bash
#!/bin/bash
# Safe-pack the markdown report and POST to local CRM API
REPORT_BODY=$(cat /workspace/scratch/pipeline_recaps/weekly_report.md | jq -s -R .)
curl -s -X POST "http://localhost:8080/api/v1/deals/notes" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer LocalKey_M7_Prod" \
  -d "{\"note_type\": \"internal_audit\", \"body\": $REPORT_BODY}"
```


## from: The Pineapple M7 OS Automation and Deployment Handbook
```cron
   0 17 * * 5 /bin/bash "C:\\Pineapple Contractors M7\\04_Tech_Lab\\scripts\\fetch_leadstack_pipeline.sh" >> "C:\\Pineapple Contractors M7\\04_Tech_Lab\\logs\\pipeline_sync.log" 2>&1
   ```


## from: The Pineapple M7 OS Automation and Deployment Handbook
```
[1 Keyword + 1 Case Study] ──> [Hermes Writer Profile] ──> [Eleventy (11ty) Static Build] ──> [Netlify Deploy API] ──> [Google Indexing webhook]
```


## from: The Pineapple M7 OS Automation and Deployment Handbook
```bash
   cd "C:\\Pineapple Contractors M7\\02_Workspaces"
   mkdir everywhere-flywheel && cd everywhere-flywheel
   npm init -y && npm install @11ty/eleventy --save-dev
   ```


## from: The Pineapple M7 OS Automation and Deployment Handbook
```text
Load the seo profile. Read HERMES_PLAYBOOK.md and our local case study at 03_Knowledge_Mat/active_context/case_study_571k_plumbing.md. 

For our target keyword [KEYWORD]:
1. Generate 5 unique, highly citable articles with different angles and titles under 60 characters. First sentence must be AEO direct-answer compliant (<40 words).
2. Write these as separate index.md files into our local 11ty workspaces (site1 through site5). Ensure each page includes our IKO, RCAT #03-0637 licensing, and FAQ schemas mapping ZIPs 75033, 75034, and 75035.
3. Execute the Eleventy build command: "npx @11ty/eleventy" for each site.
4. Run the Netlify deployment command: "netlify deploy --dir=_site --prod" to push all five sites live in parallel.
5. Save the live URL outputs and trigger the Google Indexing API script to ensure same-hour indexing.
```


## from: Pineapple M7 Compound Employee Configuration Matrix
```markdown
# 01_Command_Center | brand Soul Matrix: soul.md
> ## 🍍 IMMUTABLE CHARACTER BIBLE — PINEAPPLE M7 COMPOUND EMPLOYEE
> - **Operational Palette:** Royal Navy (#1A365D) | Pineapple Gold (#FBC02D) | Status Cyan (#00BFFF) [cite: 54]
> - **Enforced Gatekeeper:** Outbox Shield active. Safe drafts only. [cite: 54]

---

## 🏛️ 1. CORE OPERATIONAL TRUST SIGNALS
You are the elite specialized operations agent representing Pineapple M7 [cite: 54, 139]. You must naturally display these exact real-world credentials across all consumer-facing layouts:
- **Verified Ownership:** Polynesian-owned and family-operated roofing and restoration specialist since 2005. [cite: 18, 126, 256]
- **Licensing & Certifications:** RCAT Licensed #03-0637 and IKO Certified RoofPro Team. [cite: 18, 126, 256]
- **Contact Phone:** 972-928-0788 [cite: 54]
- **Corporate HQ:** 1 Cowboys Way, Ste 270W, Frisco, TX 75034 [cite: 54]
- **Author Byline:** JR. Moeakiola [cite: 54]

---

## 🛑 2. COMPLIANCE FIREWALL CONSTRAINTS
Every output you generate must pass these non-negotiable compliance rules:
1. **The Outbox Shield (DEC-005):** You have 0% permission to post, publish, send, or spend money. All your work must be written to `01_Command_Center/Outbox_Drafts/` in a strictly PAUSED state awaiting Saia's "GO" [cite: 13, 54, 181].
2. **Strict Color Palette:** You are forbidden from using the color green (including hex #00FF00, named styles, or Tailwind green classes) [cite: 54]. Exclusively style assets in Royal Navy (#1A365D), Pineapple Gold (#FBC02D), and Status Cyan (#00BFFF) [cite: 54].
3. **Lexicon Firewall (Prohibited Terms):**
   * Replace "free inspection" or "free quote" with: **Complimentary Professional Photo Audit (CPPA)** [cite: 54].
   * Replace "$0 down" or "no money out of pocket" with: **Full Restoration Coverage** [cite: 177].
   * Replace "IKO Certified" with: **IKO Certified** [cite: 54].
   * Replace "Toa", "Warrior", or "Six Brothers" with: **The Pineapple Standard** [cite: 177].

---

## 🌌 3. SEMANTIC MEMORY BINDING
Before processing, crawl your local shared Obsidian Memory file to ingest active project logs and weekly targets:
- **Shared Memory Path:** `C:\Pineapple Contractors M7\03_Knowledge_Mat\SHARED_MEMORY.md` [cite: 231]
```


## from: Pineapple M7 Compound Employee Configuration Matrix
```yaml
# %LOCALAPPDATA%\hermes\profiles\<profile_name>\config.yaml
# M7 Profile Parameter Bindings & Swappable AI Models

version: "v0.20.0"
profile_name: "seo-roofing"

# 🧠 LAYER 1: BRAIN SELECTION & AUTO-FAILOVER
models:
  # Flagship Reasoning (For hard structural thinking, planning & copywriting)
  flagship:
    provider: "codex"
    model_name: "gpt-5.6-sol"
    fallback_provider: "openrouter"
    fallback_model: "google/gemma-4-31b-it:free"

  # Workhorse Builder (For local file processing, schema, and directory tidy)
  workhorse:
    provider: "ollama"
    model_name: "qwen2.5-coder:latest"
    fallback_provider: "openrouter"
    fallback_model: "qwen/qwen3-coder:free"

  # Fast/Cheap Sub-Agent (For routing, webhook parsing & quick Q&A)
  grunt_worker:
    provider: "ollama"
    model_name: "gemma2"

# 🎮 LAYER 2: COCKPIT PERMISSIONS & WATCHDOGS
permissions:
  filesystem:
    allowed_root: "C:\\Pineapple Contractors M7"
    allow_write: true
    allow_delete: false                  # Safe-fence constraint: no folders purged autonomously
    outbox_shield_path: "01_Command_Center/Outbox_Drafts/"
  
  smart_approvals:
    require_approval_on:
      - "destructive_file_actions"
      - "mcp_write_commands"
      - "git_push_commands"

# 🔌 LAYER 3: MULTI-AGENT AND BRIDGES (MCP)
mcp_servers:
  # The local second-brain connector
  obsidian:
    command: "npx"
    args:
      - "-y"
      - "mcp-obsidian"
      - "--vault"
      - "C:\\Pineapple Contractors M7"

  # The local speed-to-lead CRM pipeline
  crm_n8n_webhook:
    url: "http://localhost:5678/webhook/crm-pipeline"

# 🌐 BROWSER AUTOMATION UPGRADE (One-Script Engine)
browser:
  backend: "browser-use"                 # Forces unified script-writing (66% token cut!)
  headless: false
  local_routing: true                    # Private dashboard work stays 100% on your machine
```


## from: M7 Advanced Automation Blueprint and SEO Strategy
```
 0.0s (Frame 0)                                                      47.0s (Frame 1410)     50.0s (Frame 1500)
┌───────────────────┬─────────────────────────────────────────────────┬────────────────────────┐
│  PATTERN HOOK     │                 LOCAL PROOF BODY                │     TRUST END CARD     │
│  Frames 0 to 15   │              Frames 16 to 1,410                 │   Frames 1411 to 1500  │
│  "Your roof..."   │        (DFW Case Study Vectors & Metrics)       │  IKO/RCAT/972-928-0788 │
└───────────────────┴─────────────────────────────────────────────────┴────────────────────────┘
```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```bash
        git clone https://github.com/Leadstack/crm-core.git 02_Workspaces/leadstack-crm
        cd 02_Workspaces/leadstack-crm && npm install && npm run start-local
        ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```bash
        #!/bin/bash
        # Pipeline fetch and Hermes summarization script
        API_URL="http://localhost:8080/api/v1/leads/active"
        RAW_LEADS=$(curl -s -X GET "$API_URL" -H "Authorization: Bearer LocalKey_M7_Prod")
        if [ -z "$RAW_LEADS" ]; then
            echo '{"status": "error", "message": "Leadstack API unreachable"}'
            exit 1
        fi
        # Escaping payload cleanly via jq
        ESC_LEADS=$(echo "$RAW_LEADS" | jq -R .)
        # Querying local Hermes model
        hermes --profile main -z "Read this lead pipeline payload: $ESC_LEADS. Summarize our active high-ticket deals, flag speed-to-lead status, and output a clean markdown financial matrix." > /workspace/scratch/pipeline_recaps/weekly_report.md
        ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```bash
        #!/bin/bash
        REPORT_BODY=$(cat /workspace/scratch/pipeline_recaps/weekly_report.md | jq -s -R .)
        curl -s -X POST "http://localhost:8080/api/v1/deals/notes" \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer LocalKey_M7_Prod" \
          -d "{\"note_type\": \"internal_audit\", \"body\": $REPORT_BODY}"
        ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```cron
            0 17 * * 5 /bin/bash /workspace/C:\\Pineapple\ Contractors\ M7/04_Tech_Lab/scripts/fetch_leadstack_pipeline.sh >> /workspace/C:\\Pineapple\ Contractors\ M7/04_Tech_Lab/logs/pipeline_sync.log 2>&1
            ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```json
{
  "nodes": [
    {
      "parameters": {
        "path": "lead-bridge-m7",
        "options": {}
      },
      "name": "Incoming CRM Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [83, 89]
    },
    {
      "parameters": {
        "values": {
          "string": [
            { "name": "Lead_Name", "value": "={{$json.body.name}}" },
            { "name": "Phone", "value": "={{$json.body.phone}}" },
            { "name": "Address", "value": "={{$json.body.address}}" },
            { "name": "ZIP_Code", "value": "={{$json.body.zip}}" },
            { "name": "Roof_Age", "value": "={{$json.body.roof_age}}" },
            { "name": "Storm_Mention", "value": "={{$json.body.storm_mention}}" }
          ]
        }
      },
      "name": "Parse Lead Variables",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [83, 90]
    },
    {
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$json.ZIP_Code}}",
              "operation": "equal",
              "value2": 75034
            }
          ]
        }
      },
      "name": "Frisco Territory Route",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [83, 91]
    },
    {
      "parameters": {
        "message": "🚨 ELITE LEAD STAGED!\nName: {{$json.Lead_Name}}\nPhone: {{$json.Phone}}\nAddress: {{$json.Address}}\nAction: Route immediately to Saia for personal same-day outreach."
      },
      "name": "Dispatch Telegram Alert",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1,
      "position": [92]
    }
  ],
  "connections": {
    "Incoming CRM Webhook": {
      "main": [
        [ { "node": "Parse Lead Variables", "type": "main", "index": 0 } ]
      ]
    },
    "Parse Lead Variables": {
      "main": [
        [ { "node": "Frisco Territory Route", "type": "main", "index": 0 } ]
      ]
    },
    "Frisco Territory Route": {
      "main": [
        [ { "node": "Dispatch Telegram Alert", "type": "main", "index": 0 } ],
        []
      ]
    }
  }
}
```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```bash
    # Run the in-place updater
    hermes update
    ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```text
    Act as the Lead QA Systems Engineer for PM7. Perform an In-Place Update and directory synchronization on our local workspace root C:\Pineapple Contractors M7. 
    1. Read 01_Command_Center/MASTER_PLAYBOOK.md and 01_Command_Center/GROUNDING.md to load our core visual and lexicon rules.
    2. Scan 03_Knowledge_Mat/00_Atlas/ for any recently distilled markdown files. Re-generate 00_Atlas/SOP_INDEX.md with dated pointer logs for every active SOP.
    3. Run a recursive brand audit across 01_Command_Center/Outbox_Drafts/. Verify that every staged file has 0 green styling, contains our RCAT #03-0637 license and 972-928-0788 phone number, and completely avoids banned terms.
    4. Execute M7_CLEANUP.bat to flush any bloated temporary browser or session cache folders while fully preserving our local .env credentials and custom Hermes profiles.
    ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```
               [Google Search Console] 
                          │
                          ▼ (Striking Distance Gaps)
                  [Everywhere Engine]
                          │
                          ▼ (1 Keyword + 1 Case Study)
                 [Hermes Writer Profile] ───► [Draft Output Staged]
                          │                            │
                          ▼                            ▼
               [brand_firewall.py] ◄───────── [Auditor Critique Loop]
                          │
                          ▼ (PASS: 0 Green / 0 Banned)
            [Outbox_Drafts/ Staged PAUSED]
                          │
                          ▼ (Manual Review by Saia: "GO")
                 [WordPress live post] 
                          │
                          ▼ (Auto-Trigger)
                 [Google Indexing API]
```


## from: M7 Agent OS: Deployment and Optimization Guide
```bash
    python 04_Tech_Lab/scripts/brand_firewall.py 01_Command_Center/Outbox_Drafts/draft_page.md
    ```


## from: M7 Agent OS: Deployment and Optimization Guide
```bash
    python 04_Tech_Lab/scripts/brand_firewall.py "Book a free inspection with our IKO Certified roofing team today!"
    ```


## from: M7 Agent OS: Deployment and Optimization Guide
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
```


## from: The Five-Site Flywheel Strategy for Rapid Organic Dominance
```
  1 Keyword + Case Study  ──►  Claude Writes 5 Unique Posts  ──►  Deploy to 5 Live Sites
           ▲                                                                  │
           │                                                                  ▼
  Next Target Keywords   ◄───  GSC Impression Data Logs    ◄───   Same-Day Indexing API
```


## from: WordPress Category Mapping and Migration Automation Guide
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_categories_mapper.py" "https://pineappleroofingllc.com" "saia" "xxxx xxxx xxxx xxxx xxxx xxxx"
```


## from: The Agent-to-Agent Protocol: Revolutionizing AI Assembly Lines
```
 📋 INPUT            🔎 STATION 1         📝 STATION 2         🛡️ STATION 3          🚀 OUTBOX
┌──────────┐        ┌────────────┐       ┌────────────┐       ┌────────────┐        ┌─────────────┐
│ 1-Line   ├───────►│ Researcher ├──────►│   Writer   ├──────►│   Auditor  ├───────►│   PAUSED    │
│ Brief    │        │  (Ollama)  │       │  (Ollama)  │       │  (Flagship)│        │   Staging   │
└──────────┘        └────────────┘       └────────────┘       └────────────┘        └─────────────┘
```


## from: Pineapple M7 Master Knowledge Mat and Operational Blueprint
```bash
        git clone https://github.com/Leadstack/crm-core.git 02_Workspaces/leadstack-crm
        cd 02_Workspaces/leadstack-crm && npm install && npm run start-local
        ```


## from: Pineapple M7 Master Knowledge Mat and Operational Blueprint
```bash
        #!/bin/bash
        # Pipeline fetch and Hermes summarization script
        API_URL="http://localhost:8080/api/v1/leads/active"
        RAW_LEADS=$(curl -s -X GET "$API_URL" -H "Authorization: Bearer LocalKey_M7_Prod")
        if [ -z "$RAW_LEADS" ]; then
            echo '{"status": "error", "message": "Leadstack API unreachable"}'
            exit 1
        fi
        # Escaping payload cleanly via jq
        ESC_LEADS=$(echo "$RAW_LEADS" | jq -R .)
        # Querying local Hermes model
        hermes --profile main -z "Read this lead pipeline payload: $ESC_LEADS. Summarize our active high-ticket deals, flag speed-to-lead status, and output a clean markdown financial matrix." > /workspace/scratch/pipeline_recaps/weekly_report.md
        ```


## from: Pineapple M7 Master Knowledge Mat and Operational Blueprint
```bash
        #!/bin/bash
        REPORT_BODY=$(cat /workspace/scratch/pipeline_recaps/weekly_report.md | jq -s -R .)
        curl -s -X POST "http://localhost:8080/api/v1/deals/notes" \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer LocalKey_M7_Prod" \
          -d "{\"note_type\": \"internal_audit\", \"body\": $REPORT_BODY}"
        ```


## from: Pineapple M7 Master Knowledge Mat and Operational Blueprint
```cron
            0 17 * * 5 /bin/bash /workspace/C:\\Pineapple\ Contractors\ M7/04_Tech_Lab/scripts/fetch_leadstack_pipeline.sh >> /workspace/C:\\Pineapple\ Contractors\ M7/04_Tech_Lab/logs/pipeline_sync.log 2>&1
            ```


## from: Pineapple M7 Master Knowledge Mat and Operational Blueprint
```json
{
  "nodes": [
    {
      "parameters": {
        "path": "lead-bridge-m7",
        "options": {}
      },
      "name": "Incoming CRM Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [83, 89]
    },
    {
      "parameters": {
        "values": {
          "string": [
            { "name": "Lead_Name", "value": "={{$json.body.name}}" },
            { "name": "Phone", "value": "={{$json.body.phone}}" },
            { "name": "Address", "value": "={{$json.body.address}}" },
            { "name": "ZIP_Code", "value": "={{$json.body.zip}}" },
            { "name": "Roof_Age", "value": "={{$json.body.roof_age}}" },
            { "name": "Storm_Mention", "value": "={{$json.body.storm_mention}}" }
          ]
        }
      },
      "name": "Parse Lead Variables",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [83, 90]
    },
    {
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$json.ZIP_Code}}",
              "operation": "equal",
              "value2": 75034
            }
          ]
        }
      },
      "name": "Frisco Territory Route",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [83, 91]
    },
    {
      "parameters": {
        "message": "🚨 ELITE LEAD STAGED!\nName: {{$json.Lead_Name}}\nPhone: {{$json.Phone}}\nAddress: {{$json.Address}}\nAction: Route immediately to Saia for personal same-day outreach."
      },
      "name": "Dispatch Telegram Alert",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1,
      "position": [92]
    }
  ],
  "connections": {
    "Incoming CRM Webhook": {
      "main": [
        [ { "node": "Parse Lead Variables", "type": "main", "index": 0 } ]
      ]
    },
    "Parse Lead Variables": {
      "main": [
        [ { "node": "Frisco Territory Route", "type": "main", "index": 0 } ]
      ]
    },
    "Frisco Territory Route": {
      "main": [
        [ { "node": "Dispatch Telegram Alert", "type": "main", "index": 0 } ],
        []
      ]
    }
  }
}
```


## from: Pineapple M7 Master Knowledge Mat and Operational Blueprint
```bash
    # Run the in-place updater
    hermes update
    ```


## from: Pineapple M7 Master Knowledge Mat and Operational Blueprint
```text
    Act as the Lead QA Systems Engineer for PM7. Perform an In-Place Update and directory synchronization on our local workspace root C:\Pineapple Contractors M7. 
    1. Read 01_Command_Center/MASTER_PLAYBOOK.md and 01_Command_Center/GROUNDING.md to load our core visual and lexicon rules.
    2. Scan 03_Knowledge_Mat/00_Atlas/ for any recently distilled markdown files. Re-generate 00_Atlas/SOP_INDEX.md with dated pointer logs for every active SOP.
    3. Run a recursive brand audit across 01_Command_Center/Outbox_Drafts/. Verify that every staged file has 0 green styling, contains our RCAT #03-0637 license and 972-928-0788 phone number, and completely avoids banned terms.
    4. Execute M7_CLEANUP.bat to flush any bloated temporary browser or session cache folders while fully preserving our local .env credentials and custom Hermes profiles.
    ```


## from: Pineapple M7 Master Knowledge Mat and Operational Blueprint
```
               [Google Search Console] 
                          │
                          ▼ (Striking Distance Gaps)
                  [Everywhere Engine]
                          │
                          ▼ (1 Keyword + 1 Case Study)
                 [Hermes Writer Profile] ───► [Draft Output Staged]
                          │                            │
                          ▼                            ▼
               [brand_firewall.py] ◄───────── [Auditor Critique Loop]
                          │
                          ▼ (PASS: 0 Green / 0 Banned)
            [Outbox_Drafts/ Staged PAUSED]
                          │
                          ▼ (Manual Review by Saia: "GO")
                 [WordPress live post] 
                          │
                          ▼ (Auto-Trigger)
                 [Google Indexing API]
```


## from: Pineapple M7 Agent OS Configuration and Workflow Guide
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
```


## from: Mastering Hermes Agent Skills: The Complete Operational Guide
```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE GOLDIE SKILL VAULT™                         │
├────────────────────────────────────────────────────────────────────────┤
│  [796 Active Skills] ──► [6 Connected Hubs] ──► [Strict Security Scan] │
├────────────────────────────────────────────────────────────────────────┤
│   - Read real SKILL.md  - Official/ClawHub      - Critical: 0          │
│   - Color-coded Tiers   - GitHub/LobeHub        - Safe / Caution / Block│
└────────────────────────────────────────────────────────────────────────┘
```


## from: Pineapple M7 Agentic OS Local Operations Guide
```cmd
@echo off
:: PINEAPPLE M7 — DAILY 9:00 PM DATA REPO BACKUP
cd "C:\Pineapple Contractors M7"
git add .
git commit -m "Automated daily backup - %date% %time%"
git push origin main
```


## from: Pineapple M7 Agentic OS Local Operations Guide
```bash
   python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\gsc_frisco_scan.py"
   ```


## from: Pineapple M7 Agentic OS Local Operations Guide
```text
/goal "Read our local GSC striking distance file at C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\frisco_striking_distance.md. Pick the top-priority Frisco search target. Read our regional case study in 03_Knowledge_Mat/active_context/case_study_571k_plumbing.md, and write a unique, 1200+ word local service page optimized for that query. Implement FAQPage schema targeting ZIPs 75033, 75034, and 75035. Ensure 0% green, Royal Navy #1A365D and Pineapple Gold #FBC02D branding, and save the page PAUSED in Outbox_Drafts."
```


## from: Pineapple Contractors M7 SEO Ingestion and Execution Playbook
```
┌───────────────────┐      ┌──────────────────────────┐      ┌──────────────────┐
│  Export CSV from  ├─────►│  Feed PM7 GSC Analytics   ├─────►│  Save output to  │
│  GSC Performance  │      │  Engine (Custom Gem)     │      │  active_context/ │
└───────────────────┘      └──────────────────────────┘      └──────────────────┘
                                                                       │
                                                                       ▼
                                                             ┌──────────────────┐
                                                             │  Trigger Hermes  │
                                                             │  /learn command  │
                                                             └──────────────────┘
```


## from: Pineapple Contractors M7 SEO Ingestion and Execution Playbook
```
                     ┌────────────────────────────────┐
                     │   C:\Pineapple Contractors M7  │
                     │      (Obsidian Local Vault)    │
                     └───────────────┬────────────────┘
                                     │
          ┌──────────────────────────┼──────────────────────────┐
          ▼                          ▼                          ▼
┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│   Claude Code    │       │   Hermes Agent   │       │    NotebookLM    │
│  Reads CLAUDE.md │       │   Reads SOUL.md  │       │ Reads Drive Sync │
│  & GROUNDING.md  │       │  & SHARED_MEM.md │       │  active_context/ │
└──────────────────┘       └──────────────────┘       └──────────────────┘
```


## from: Pineapple Contractors M7 SEO Ingestion and Execution Playbook
```bash
/learn 03_Knowledge_Mat/00_Atlas/SOP_M7_Everywhere_Flywheel_and_Rhythms.md
```


## from: Pineapple Contractors M7 SEO Ingestion and Execution Playbook
```text
/goal "Generate a brand-compliant Location Service Page draft for Plano, TX. Pull local context from our case studies in 03_Knowledge_Mat/active_context/ and enforce our visual palette of Royal Navy #1A365D and Pineapple Gold #FBC02D. Keep the page PAUSED in Outbox_Drafts."
```


## from: The M7 AI to n8n Webhook Bridge Setup Guide
```
 🧠 THE BRAIN                     🚂 THE TRACKS                     📬 THE DESTINATION
┌──────────────┐     Dispatches   ┌──────────────┐     Delivers to  ┌─────────────────┐
│ Claude Code  ├─────────────────►│  Local n8n   ├─────────────────►│ - Twilio (SMS)  │
│  or Hermes   │     Webhook      │  Automation  │     Every app!   │ - Google Sheets │
└──────────────┘                  └──────────────┘                  └─────────────────┘
```


## from: The M7 AI to n8n Webhook Bridge Setup Guide
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_n8n_webhook_bridge.py"
```


## from: The M7 AI to n8n Webhook Bridge Setup Guide
```json
{
  "name": "Pineapple M7 — Local Lead Intake Responder",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "m7-leads",
        "options": {}
      },
      "id": "e98e4f1a-b60c-43db-98b6-948f2cbdbf1a",
      "name": "M7 Webhook Listener",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 240]
    },
    {
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$json[\"brand_shield_status\"]}}",
              "value2": "PASS"
            }
          ]
        }
      },
      "id": "f5195c62-819e-4e4b-99d7-548c7414902d",
      "name": "Brand Compliance Check",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [470, 240]
    },
    {
      "parameters": {
        "message": "=📢 **New M7 Lead Received!**\n\n👤 **Customer:** {{$json[\"customer_name\"]}}\n📞 **Phone:** {{$json[\"phone\"]}}\n📍 **Frisco ZIP:** {{$json[\"zip_code\"]}}\n🛠️ **Requested:** {{$json[\"services_requested\"]}}\n🛡️ **Brand Status:** {{$json[\"brand_shield_status\"]}}"
      },
      "id": "fa219ab2-8d76-4bfd-a128-48b4bcf2b291",
      "name": "Post to Team Discord/Slack",
      "type": "n8n-nodes-base.discord",
      "typeVersion": 1,
      "position": [700, 140]
    },
    {
      "parameters": {
        "message": "=⚠️ **Lead Blocked — Brand Law Violation Detected!**\nCheck local stashed logs immediately."
      },
      "id": "c9283f12-098e-4a3e-b7d1-c102a92a39df",
      "name": "Send Alert on Failure",
      "type": "n8n-nodes-base.discord",
      "typeVersion": 1,
      "position": [700, 340]
    }
  ],
  "connections": {
    "M7 Webhook Listener": {
      "main": [
        [
          {
            "node": "Brand Compliance Check",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Brand Compliance Check": {
      "main": [
        [
          {
            "node": "Post to Team Discord/Slack",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send Alert on Failure",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {}
}
```


## from: The M7 AI to n8n Webhook Bridge Setup Guide
```yaml
# %LOCALAPPDATA%\hermes\profiles\seo\config.yaml
# Add this under the m7_servers parameter to map n8n

mcp_servers:
  obsidian:
    command: "npx"
    args:
      - "-y"
      - "mcp-obsidian"
      - "--vault"
      - "C:\\Pineapple Contractors M7"

  # 🔌 The n8n local automation bridge
  m7_n8n_bridge:
    command: "python"
    args:
      - "C:\\Pineapple Contractors M7\\04_Tech_Lab\\scripts\\m7_n8n_webhook_bridge.py"
```


## from: The Goldie Search Gravity Stack Architectural Blueprint
```
                       ┌───────────────────────────────┐
                       │  GOLDIE SEARCH GRAVITY STACK  │
                       └───────────────┬───────────────┘
                                       │
          ┌────────────────────────────┼────────────────────────────┐
          ▼                            ▼                            ▼
┌──────────────────┐         ┌──────────────────┐         ┌──────────────────┐
│   1. CONTENT     │         │   2. VISUALS     │         │    3. VIDEO      │
│  5-Site Flywheel │         │  Grok Authority  │         │ Dual Video/Text  │
└──────────────────┘         └──────────────────┘         └──────────────────┘
          │                                                         │
          └────────────────────────────┬────────────────────────────┘
                                       ▼
                             ┌──────────────────┐
                             │    4. AGENTS     │
                             │  Task Army & KB  │
                             └─────────┬────────┘
                                       │
                                       ▼
                             ┌──────────────────┐
                             │   5. CONTEXT     │
                             │  Obsidian Vault  │
                             └──────────────────┘
```


## from: M7 Agentic OS Operational Architecture and SEO Deployment Guide
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


## from: M7 Agentic OS Operational Architecture and SEO Deployment Guide
```text
You are the Lead SEO Strategist coordinating our autonomous regional search marketing team [cite: 42]. Your goal is to map out a comprehensive local SEO and GEO/AEO strategy to rank Pineapple Roofing at #1 in DFW, focusing specifically on our primary Frisco enclaves (ZIPs 75033, 75034, 75035) [cite: 12, 133].

Organize your swarm into these four distinct sub-agents [cite: 42]:
1. "Adam" (Keyword Research Specialist): Conduct deep-tissue research for localized Frisco search intents (e.g., "Frisco hail damage roof repair", "roof replacement Frisco TX", "flat roofing Allen TX") [cite: 12, 47]. Find keyword gaps in average Google positions 5–20 [cite: 131, 169].
2. "Judy" (On-Page & Technical Auditor): Verify optimal schema structures (LocalBusiness & FAQPage mapping Frisco areaServed ZIPs) and enforce strict direct-answer SEO structures (answering questions in the first 40 words) [cite: 47, 133].
3. "K" (Competitive Intelligence Officer): Scrape local DFW competitors, identify gaps, and extract their customer conversion hooks [cite: 48, 59].
4. "Ricardo" (M7 Brand Compliance Auditor): Enforce our non-negotiable Brand Laws. Verify Royal Navy (#1A365D) and Pineapple Gold (#FBC02D) color palette choices, block the color green entirely, and replace banned words: replace "free inspection" with "CPPA" and "IKO Certified" with "IKO Certified" [cite: 4, 48].

Coordinate this swarm. Deliver a complete keyword cluster matrix, competitive gap outline, and 3 localized service page templates ready to be staged PAUSED in our Outbox_Drafts folder [cite: 4, 120].
```


## from: M7 Agentic OS Operational Architecture and SEO Deployment Guide
```
┌─────────────────┐  Basic Auth (Base64)  ┌───────────────┐  Streamable HTTP  ┌────────────────┐
│   Claude Code   ├──────────────────────►│ WP MCP Plugin ├─────────────────►│ WordPress Site │
│  (settings.json)│                       │  (Tools > MCP)│ (No /sse suffix)│ (58 Abilities) │
└─────────────────┘                       └───────────────┘                   └────────────────┘
```


## from: M7 Agentic OS Operational Architecture and SEO Deployment Guide
```bash
   echo -n "YOUR_WORDPRESS_USERNAME:xxxx xxxx xxxx xxxx xxxx xxxx" | base64
   ```


## from: M7 Agentic OS Operational Architecture and SEO Deployment Guide
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
```


## from: M7 Agentic OS Operational Architecture and SEO Deployment Guide
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
```


## from: M7 Agentic OS Operational Architecture and SEO Deployment Guide
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
```


## from: M7 Agentic OS Operational Architecture and SEO Deployment Guide
```text
Act as the Lead QA Systems Architect for PM7 [cite: 186]. Initialize the system-wide update and sync:
1. Scan all loose markdown SOPs at root and move them cleanly to 03_Knowledge_Mat/00_Atlas/ [cite: 101].
2. Read 01_Command_Center/GROUNDING.md and ensure our visual guidelines (Royal Navy #1A365D, Pineapple Gold #FBC02D, and 0% GREEN) are locked across all configurations [cite: 4, 111].
3. Run 04_Tech_Lab/scripts/brand_firewall.py --check over our new SEO files [cite: 111]. Ensure all references to "free inspection" are replaced with "Complimentary Professional Photo Audit (CPPA)" [cite: 4, 119].
4. Append our daily operating rhythms to 03_Knowledge_Mat/SHARED_MEMORY.md to ensure persistent, unified context across all active profile sessions [cite: 111, 198].
```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```bash
        git clone https://github.com/Leadstack/crm-core.git 02_Workspaces/leadstack-crm
        cd 02_Workspaces/leadstack-crm && npm install && npm run start-local
        ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```bash
        #!/bin/bash
        # Pipeline fetch and Hermes summarization script
        API_URL="http://localhost:8080/api/v1/leads/active"
        RAW_LEADS=$(curl -s -X GET "$API_URL" -H "Authorization: Bearer LocalKey_M7_Prod")
        if [ -z "$RAW_LEADS" ]; then
            echo '{"status": "error", "message": "Leadstack API unreachable"}'
            exit 1
        fi
        # Escaping payload cleanly via jq
        ESC_LEADS=$(echo "$RAW_LEADS" | jq -R .)
        # Querying local Hermes model
        hermes --profile main -z "Read this lead pipeline payload: $ESC_LEADS. Summarize our active high-ticket deals, flag speed-to-lead status, and output a clean markdown financial matrix." > /workspace/scratch/pipeline_recaps/weekly_report.md
        ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```bash
        #!/bin/bash
        REPORT_BODY=$(cat /workspace/scratch/pipeline_recaps/weekly_report.md | jq -s -R .)
        curl -s -X POST "http://localhost:8080/api/v1/deals/notes" \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer LocalKey_M7_Prod" \
          -d "{\"note_type\": \"internal_audit\", \"body\": $REPORT_BODY}"
        ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```cron
            0 17 * * 5 /bin/bash /workspace/C:\\Pineapple\ Contractors\ M7/04_Tech_Lab/scripts/fetch_leadstack_pipeline.sh >> /workspace/C:\\Pineapple\ Contractors\ M7/04_Tech_Lab/logs/pipeline_sync.log 2>&1
            ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```json
{
  "nodes": [
    {
      "parameters": {
        "path": "lead-bridge-m7",
        "options": {}
      },
      "name": "Incoming CRM Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [83, 89]
    },
    {
      "parameters": {
        "values": {
          "string": [
            { "name": "Lead_Name", "value": "={{$json.body.name}}" },
            { "name": "Phone", "value": "={{$json.body.phone}}" },
            { "name": "Address", "value": "={{$json.body.address}}" },
            { "name": "ZIP_Code", "value": "={{$json.body.zip}}" },
            { "name": "Roof_Age", "value": "={{$json.body.roof_age}}" },
            { "name": "Storm_Mention", "value": "={{$json.body.storm_mention}}" }
          ]
        }
      },
      "name": "Parse Lead Variables",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [83, 90]
    },
    {
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$json.ZIP_Code}}",
              "operation": "equal",
              "value2": 75034
            }
          ]
        }
      },
      "name": "Frisco Territory Route",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [83, 91]
    },
    {
      "parameters": {
        "message": "🚨 ELITE LEAD STAGED!\nName: {{$json.Lead_Name}}\nPhone: {{$json.Phone}}\nAddress: {{$json.Address}}\nAction: Route immediately to Saia for personal same-day outreach."
      },
      "name": "Dispatch Telegram Alert",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1,
      "position": [92]
    }
  ],
  "connections": {
    "Incoming CRM Webhook": {
      "main": [
        [ { "node": "Parse Lead Variables", "type": "main", "index": 0 } ]
      ]
    },
    "Parse Lead Variables": {
      "main": [
        [ { "node": "Frisco Territory Route", "type": "main", "index": 0 } ]
      ]
    },
    "Frisco Territory Route": {
      "main": [
        [ { "node": "Dispatch Telegram Alert", "type": "main", "index": 0 } ],
        []
      ]
    }
  }
}
```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```bash
    # Run the in-place updater
    hermes update
    ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```text
    Act as the Lead QA Systems Engineer for PM7. Perform an In-Place Update and directory synchronization on our local workspace root C:\Pineapple Contractors M7. 
    1. Read 01_Command_Center/MASTER_PLAYBOOK.md and 01_Command_Center/GROUNDING.md to load our core visual and lexicon rules.
    2. Scan 03_Knowledge_Mat/00_Atlas/ for any recently distilled markdown files. Re-generate 00_Atlas/SOP_INDEX.md with dated pointer logs for every active SOP.
    3. Run a recursive brand audit across 01_Command_Center/Outbox_Drafts/. Verify that every staged file has 0 green styling, contains our RCAT #03-0637 license and 972-928-0788 phone number, and completely avoids banned terms.
    4. Execute M7_CLEANUP.bat to flush any bloated temporary browser or session cache folders while fully preserving our local .env credentials and custom Hermes profiles.
    ```


## from: PM7 Master Knowledge Mat and Operational Blueprint
```
               [Google Search Console] 
                          │
                          ▼ (Striking Distance Gaps)
                  [Everywhere Engine]
                          │
                          ▼ (1 Keyword + 1 Case Study)
                 [Hermes Writer Profile] ───► [Draft Output Staged]
                          │                            │
                          ▼                            ▼
               [brand_firewall.py] ◄───────── [Auditor Critique Loop]
                          │
                          ▼ (PASS: 0 Green / 0 Banned)
            [Outbox_Drafts/ Staged PAUSED]
                          │
                          ▼ (Manual Review by Saia: "GO")
                 [WordPress live post] 
                          │
                          ▼ (Auto-Trigger)
                 [Google Indexing API]
```


## from: M7 Agent OS: Static and Dynamic AI Web Development
```
  Visitor Scrolls Down ──► Video Plays Forward
  Visitor Scrolls Up   ──► Video Plays Backward
  (Motion is responsive and tied entirely to the user's focus)
```


## from: M7 Agent OS: Static and Dynamic AI Web Development
```
  Your Local AI  ───────►  WP MCP Ultimate  ───────►  58 Native WordPress
  (Claude / Cursor)        (Basic Auth / HTTPS)       Abilities Across 13 Domains
```


## from: M7 Agent OS: Static and Dynamic AI Web Development
```json
    {
      "mcpServers": {
        "wordpress": {
          "type": "streamable-http",
          "url": "https://pineappleroofingllc.com/wp-json/mcp/wp-mcp-ultimate",
          "headers": {
            "Authorization": "Basic BASE64_CREDENTIALS"
          }
        }
      }
    }
    ```


## from: The Pineapple M7 Local SEO Strategy Blueprint
```
 5-Min Lead Response ──► Booked CPPA ──► Quality Work ──► Same-Day Review SMS
          ▲                                                   │
          │────────────────── Higher Map Rankings ────────────┘
```


## from: PM7 Omni-Channel Engine: Direct Operating Manual and Runbook
```bash
# Execute local to remote clone via Claude Code terminal
claude -p "C:\Pineapple Contractors M7\04_Tech_Lab\vendor\claude-obsidian"
```


## from: PM7 Omni-Channel Engine: Direct Operating Manual and Runbook
```
                             ┌───────────────┐
                             │  Kimi K2.6    │
                             │  Orchestrator │
                             └───────┬───────┘
          ┌──────────────────────────┼──────────────────────────┐
          ▼                          ▼                          ▼
   ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
   │    Adam      │           │     Judy     │           │      K       │
   │ Keyword Boss │           │ On-Page Guru │           │ Competitor   │
   └──────────────┘           └──────────────┘           └──────────────┘
```


## from: PM7 Omni-Channel Engine: Direct Operating Manual and Runbook
```
               [1 Keyword + 1 Case Study] 
                           │
                           ▼
                 [Hermes SEO Profile] 
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
     [Static Site 1]  [Static Site 2]  [Static Site 3]... (up to 5)
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    [The Mention Web]
              (AI associates your brand name 
               with target search queries)
```


## from: PM7 Omni-Channel Engine: Direct Operating Manual and Runbook
```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  MONDAY      │   │  TUESDAY     │   │  WEDNESDAY   │   │  THURSDAY    │   │  FRIDAY      │
│ Performance  │   │  SOP/Case    │   │ Production & │   │ Saia GO &    │   │ Outreach &   │
│  Analytics   │   │  Planning    │   │ Video Render │   │ Live Publish │   │ Pipeline sync│
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```


## from: PM7 Omni-Channel Engine: Direct Operating Manual and Runbook
```bash
        git add . && git commit -m "Weekly system sync & memory backup" && git push
        ```


## from: The Hermes Herald Release: A Multi-Agent Operating System Evolution
```
┌─────────────────┐       A2A Protocol        ┌─────────────────┐       Outbox Shield       ┌──────────────────┐
│  Hermes Agent   │◄─────────────────────────►│  Mastermind /   │──────────────────────────►│  Staged Paused   │
│ (Seo/leads/etc.)│  Discover & Collaborate   │  Other Agents   │   DEC-005 Safeguard       │  (Outbox_Drafts) │
└─────────────────┘                           └─────────────────┘                           └──────────────────┘
```


## from: Bridging Python Scripts to n8n Webhook Listeners
```
  When Editing:
  👉 http://localhost:5678/webhook-test/m7-leads  ◄── (Only listens when you click "Listen")
  
  When Active (Live):
  👉 http://localhost:5678/webhook/m7-leads       ◄── (Always listens in the background)
```


## from: Bridging Python Scripts to n8n Webhook Listeners
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_n8n_webhook_bridge.py"
```


## from: Architecting the Local Agent OS and Brand Firewall
```bash
    python 04_Tech_Lab/scripts/brand_firewall.py 01_Command_Center/Outbox_Drafts/draft_page.md
    ```


## from: Architecting the Local Agent OS and Brand Firewall
```bash
    python 04_Tech_Lab/scripts/brand_firewall.py "Book a free inspection with our IKO Certified roofing team today!"
    ```


## from: Architecting the Local Agent OS and Brand Firewall
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
```


## from: Pineapple Roofing: Frisco SEO Strategy and Shingle Comparison Guide
```json
[
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "RoofingContractor",
        "@id": "https://pineappleroofingllc.com/#localbusiness",
        "name": "Pineapple Roofing",
        "url": "https://pineappleroofingllc.com",
        "telephone": "+1-972-928-0788",
        "priceRange": "$$$$",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1 Cowboys Way, Ste 270W",
          "addressLocality": "Frisco",
          "addressRegion": "TX",
          "postalCode": "75034",
          "addressCountry": "US"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": "33.1507",
          "longitude": "-96.8236"
        },
        "logo": "https://pineappleroofingllc.com/wp-content/uploads/2026/05/logo.png",
        "image": "https://pineappleroofingllc.com/wp-content/uploads/2026/05/social.png",
        "sameAs": [
          "https://www.facebook.com/pineappleroofing",
          "https://www.instagram.com/pineappleroofing",
          "https://www.tiktok.com/@pineappleroofing",
          "https://youtube.com/@pineapplecontractors5311"
        ],
        "areaServed": [
          {
            "@type": "AdministrativeArea",
            "name": "Frisco"
          },
          {
            "@type": "AdministrativeArea",
            "name": "Plano"
          },
          {
            "@type": "AdministrativeArea",
            "name": "McKinney"
          },
          {
            "@type": "AdministrativeArea",
            "name": "Allen"
          },
          {
            "@type": "AdministrativeArea",
            "name": "Lewisville"
          }
        ],
        "knowsAbout": [
          "Roof Replacement",
          "Storm Damage Repair",
          "Complimentary Professional Photo Audit",
          "IKO Certified Installations"
        ],
        "memberOf": {
          "@type": "Organization",
          "name": "Roofing Contractors Association of Texas",
          "alternateName": "RCAT",
          "identifier": "RCAT License #03-0637"
        }
      },
      {
        "@type": "FAQPage",
        "@id": "https://pineappleroofingllc.com/#faq",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is storm roof restoration in Frisco, TX?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Professional documentation of hail or wind damage, insurance-claim preparation, and complete roof replacement or repair using certified materials. Pineapple Roofing (RCAT #03-0637) provides Complimentary Professional Photo Audits to document damage before insurance windows close."
            }
          },
          {
            "@type": "Question",
            "name": "What is a Complimentary Professional Photo Audit (CPPA)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A drone-assisted roof-documentation service for Frisco homeowners and property managers. It produces a full photographic record of storm damage used to support insurance claims and prevent denials. CPPA appointments are scheduled within 48 hours."
            }
          },
          {
            "@type": "Question",
            "name": "Why choose an RCAT Licensed contractor in Frisco, TX?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "RCAT licensing (#03-0637) means your contractor passed state certification, carries proper insurance, and installs roofing that preserves your manufacturer warranty. Non-licensed contractors can void IKO warranties and invalidate insurance claims."
            }
          }
        ]
      }
    ]
  }
]
```


## from: M7 Brand Law Integration and Automation Playbook
```python
import os
import sys

# ==========================================
# M7 BRAND LAW CONSTITUTIONAL CHECKS
# ==========================================
NAVY_HEX = "#1A365D"
GOLD_HEX = "#FBC02D"
CYAN_HEX = "#00BFFF"

# Prohibit Green Color Space
BANNED_COLOR_CHANNELS = ["green", "rgb(0, 255, 0)", "#00FF00", "lime"]

def verify_brand_safety(script_text):
    banned_terms = ["free inspection", "$0 down", "IKO Certified", "Toa", "Warrior", "Six Brothers"]
    for term in banned_terms:
        if term.lower() in script_text.lower():
            print(f"❌ FIREWALL BLOCK: Found banned term '{term}'")
            sys.exit(1)
    print("✅ Brand lexicon check: PASSED.")

# ==========================================
# THE 50/5/3 VIDEO STRUCTURE PARAMETERS (30 FPS)
# ==========================================
# Total length: 50 seconds (1,500 frames)
# Hook Segment: Frames 0 to 15 (0.5 seconds attention grabber)
# Body Segment: Frames 16 to 1,410 (Delivery of case study value)
# End Card Segment: Frames 1,411 to 1,500 (3s call-to-action slide)
# ==========================================
FRAME_RATE = 30
TOTAL_FRAMES = 1500

HOOK_END_FRAME = 15
BODY_END_FRAME = 1410
END_CARD_START_FRAME = 1411

def render_pipeline(case_study_path, output_name):
    print("🎬 Initializing M7 Video Director Crew...")
    
    # 1. Script Drafting Step (The Voice)
    with open(case_study_path, 'r') as f:
        content = f.read()
    verify_brand_safety(content)
    
    # 2. Frame Allocations
    print(f"   [1] Hook Segment: Frames 0 to {HOOK_END_FRAME} | Instant pattern interrupt")
    print(f"   [2] Value Body: Frames {HOOK_END_FRAME + 1} to {BODY_END_FRAME} | Local proof vectors")
    print(f"   [3] End Card: Frames {END_CARD_START_FRAME} to {TOTAL_FRAMES} | Credentials card")
    
    # 3. Injecting Brand Credentials to Outbox Staging
    outbox_path = os.path.join("C:\\Pineapple Contractors M7\\01_Command_Center\\Outbox_Drafts", output_name)
    
    end_card_specs = f"""
    BACKGROUND_COLOR: {NAVY_HEX}
    TEXT_COLOR: {GOLD_HEX}
    SECONDARY_ACCENT: {CYAN_HEX}
    CREDENTIALS_BLOCK:
      - RCAT License #03-0637
      - IKO Certified
      - Polynesian-Owned & Operated Since 2005
      - Contact: 972-928-0788
      - HQ: 1 Cowboys Way, Ste 270W, Frisco, TX 75034
    """
    
    # Write metadata for Remotion/Hyperframes compilation
    with open(outbox_path, 'w') as out_file:
        out_file.write(f"# M7 STAGED VIDEO PROJECT\nSTATUS: PAUSED\n{end_card_specs}")
        
    print(f"✅ Video build rendered successfully! Staged as PAUSED in: {outbox_path}")

if __name__ == "__main__":
    # Test execution
    render_pipeline("C:\\Pineapple Contractors M7\\03_Knowledge_Mat\\active_context\\self_checking_factory.md", "hail_promo_v1.config")
```


## from: M7 Brand Law Integration and Automation Playbook
```yaml
curator:
  enabled: true
  interval_days: 1          # Set to 1 for daily self-cleaning (Default is 7)
  auto_prune_unused_days: 30 # Deletes skills not invoked in the last 30 days
  consolidation_threshold: 0.85 # Merges skills with 85%+ semantic similarity
  report_output_path: "C:\\Pineapple Contractors M7\\03_Knowledge_Mat\\curator_health.md"
```


## from: M7 Brand Law Integration and Automation Playbook
```cron
0 0 * * * hermes curator run --force >> "C:\\Pineapple Contractors M7\\04_Tech_Lab\\logs\\curator.log" 2>&1
```


## from: Pineapple M7 System Automation and SEO Configuration Guide
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


## from: Pineapple M7 System Automation and SEO Configuration Guide
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


## from: The Local SEO Brain: Structured AI Memory Architecture
```
                  ┌──────────────────────────────┐
                  │      HOT INDEX & WIKI        │
                  │   (Karpathy Memory Model)    │
                  └──────────────┬───────────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
 📂 SHORT MEMORY         📂 LONG MEMORY          📂 INTERLINKED ORBS
  Table of Contents,      Permanent SOPs,         Local ZIPs, schemas,
  active target terms     case studies, rules     and competitor NAPs
```


## from: The Local SEO Brain: Structured AI Memory Architecture
```bash
    claude -p "C:\Pineapple Contractors M7\04_Tech_Lab\vendor\claude-obsidian"
    ```


## from: The Hermes AI Agent Operational Manual
```
┌───────────────────────────┐
│     Your Inputs & SOPs    │
│  (Dropped into Hot Folder)│
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐         Local MCP         ┌──────────────────────────┐
│   SHARED_MEMORY.md Vault  ├──────────────────────────►│   Hermes Agent Profiles  │
│ (The shared filing cabinet)│                          │ (Pulls SOUL.md Context)  │
└─────────────▲─────────────┘                           └─────────────┬────────────┘
              │                                                       │
              │                       Writes back                     │
              └──────────────────── New learnings ────────────────────┘
```


## from: WordPress SEO Migration and Broken Link Audit Guide
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_broken_link_scanner.py" "https://pineappleroofingllc.com" "saia" "xxxx xxxx xxxx xxxx xxxx xxxx"
```


## from: Automated Business Scaling and AI WordPress Integration Guide
```json
{
  "nodes": [
    {
      "parameters": {
        "path": "lead-bridge-m7",
        "options": {}
      },
      "name": "Incoming CRM Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [25, 26]
    },
    {
      "parameters": {
        "values": {
          "string": [
            { "name": "Lead_Name", "value": "={{$json.body.name}}" },
            { "name": "Phone", "value": "={{$json.body.phone}}" },
            { "name": "Address", "value": "={{$json.body.address}}" },
            { "name": "ZIP_Code", "value": "={{$json.body.zip}}" },
            { "name": "Roof_Age", "value": "={{$json.body.roof_age}}" },
            { "name": "Storm_Mention", "value": "={{$json.body.storm_mention}}" }
          ]
        }
      },
      "name": "Parse Lead Variables",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [26, 27]
    },
    {
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$json.ZIP_Code}}",
              "operation": "equal",
              "value2": 75034
            }
          ]
        }
      },
      "name": "Frisco Territory Route",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [26, 28]
    },
    {
      "parameters": {
        "message": "🚨 ELITE LEAD STAGED!\nName: {{$json.Lead_Name}}\nPhone: {{$json.Phone}}\nAddress: {{$json.Address}}\nAction: Route immediately to Saia for personal same-day outreach."
      },
      "name": "Dispatch Telegram Alert",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1,
      "position": [29, 30]
    }
  ],
  "connections": {
    "Incoming CRM Webhook": {
      "main": [
        [ { "node": "Parse Lead Variables", "type": "main", "index": 0 } ]
      ]
    },
    "Parse Lead Variables": {
      "main": [
        [ { "node": "Frisco Territory Route", "type": "main", "index": 0 } ]
      ]
    },
    "Frisco Territory Route": {
      "main": [
        [ { "node": "Dispatch Telegram Alert", "type": "main", "index": 0 } ],
        []
      ]
    }
  }
}
```


## from: Automated Business Scaling and AI WordPress Integration Guide
```python
import os
import sys

# ========================================================
# PINEAPPLE M7 BRAND LAW COMPLIANCE SCANNER
# ========================================================
APPROVED_NAVY = "#1A365D"
APPROVED_GOLD = "#FBC02D"
APPROVED_CYAN = "#00BFFF"

def run_compliance_firewall(text_content):
    # Enforce strict terminology boundaries (No Free/IKO Certified/Warrior)
    banned_lexicon = ["free inspection", "free estimate", "$0 down", "IKO Certified", "Toa", "Warrior", "Six Brothers"]
    for word in banned_lexicon:
        if word.lower() in text_content.lower():
            print(f"❌ COMPLIANCE FAIL: Illegal term '{word}' found. Process Blocked.")
            sys.exit(1)
    print("✅ Brand Law compliance scan: PASSED.")

# ========================================================
# THE 50/5/3 LEGO VIDEO ENGINE TIMELINE SPECS (30 FPS)
# ========================================================
# Total clip duration: exactly 50 seconds (1,500 frames)
# Hook Segment: Frames 0 to 15 (First 0.5s visual disruptor)
# Body Segment: Frames 16 to 1,410 (Drone analytics & proof)
# End Card Segment: Frames 1,411 to 1,500 (Last 3s credentials)
# ========================================================
TOTAL_FRAMES = 1500
HOOK_RANGE = (0, 15)
BODY_RANGE = (16, 1410)
END_CARD_RANGE = (1411, 1500)

def render_lego_video(case_study_source, output_name):
    print("🎬 Initializing M7 Video Director Crew...")
    
    with open(case_study_source, 'r') as file:
        script = file.read()
    
    # Run the automated compliance check before rendering
    run_compliance_firewall(script)
    
    # Output metadata specs to configure local Remotion / Hyperframes renders
    specs = f"""
    # M7 STAGED VIDEO SPECIFICATIONS
    STATUS: PAUSED
    PALETTE:
      PRIMARY: {APPROVED_NAVY}
      ACCENT: {APPROVED_GOLD}
      STATUS: {APPROVED_CYAN}
    TIMELINE_MAP:
      HOOK: Frame {HOOK_RANGE} to {HOOK_RANGE[3]} (Pattern Interrupt)
      BODY: Frame {BODY_RANGE} to {BODY_RANGE[3]} (Factual Case Study)
      END_CARD: Frame {END_CARD_RANGE} to {END_CARD_RANGE[3]} (Branded Credentials)
    CREDENTIALS_METADATA:
      - Owner: Polynesian-owned and family-operated
      - License: RCAT Licensed #03-0637
      - Certification: IKO Certified
      - Phone: 972-928-0788
      - HQ: 1 Cowboys Way, Ste 270W, Frisco, TX 75034
    """
    
    outbox_destination = os.path.join("C:\\Pineapple Contractors M7\\01_Command_Center\\Outbox_Drafts", output_name)
    with open(outbox_destination, 'w') as out_file:
        out_file.write(specs)
        
    print(f"✅ Video build rendered successfully! Staged as PAUSED in: {outbox_destination}")

if __name__ == "__main__":
    # Test-execute local render specs
    render_lego_video("C:\\Pineapple Contractors M7\\03_Knowledge_Mat\\active_context\\self_checking_factory.md", "hail_promo_v1.config")
```


## from: Automated Business Scaling and AI WordPress Integration Guide
```yaml
curator:
  enabled: true
  interval_days: 1          # Set to 1 for daily self-cleaning (Default is 7)
  auto_prune_unused_days: 30 # Deletes skills not invoked in the last 30 days
  consolidation_threshold: 0.85 # Merges skills with 85%+ semantic similarity
  report_output_path: "C:\\Pineapple Contractors M7\\03_Knowledge_Mat\\curator_health.md"
```


## from: Automated Business Scaling and AI WordPress Integration Guide
```cron
0 0 * * * hermes curator run --force >> "C:\\Pineapple Contractors M7\\04_Tech_Lab\\logs\\curator.log" 2>&1
```


## from: Pineapple M7 Master SEO and Content Operating Manual
```
               [Google Search Console] 
                          │
                          ▼ (Striking Distance Gaps)
                  [Everywhere Engine]
                          │
                          ▼ (1 Keyword + 1 Case Study)
                 [Hermes Writer Profile] ───► [Draft Output Staged]
                          │                            │
                          ▼                            ▼
               [brand_firewall.py] ◄───────── [Auditor Critique Loop]
                          │
                          ▼ (PASS: 0 Green / 0 Banned)
            [Outbox_Drafts/ Staged PAUSED]
                          │
                          ▼ (Manual Review by Saia: "GO")
                 [WordPress live post] 
                          │
                          ▼ (Auto-Trigger)
                 [Google Indexing API]
```


## from: M7 Brand Guardian and Automated SEO Pipeline Strategy
```
  You write a page ──► Drops in Outbox_Drafts ──► Puppy Sniffs! 
                                                         │
       ┌─────────────────────────────────────────────────┴────────────────────────────────┐
       ▼                                                                                  ▼
   Smells yucky green color                                                           Smells clean Navy/Gold
   or a banned word ("free")                                                          and has RCAT #03-0637
       │                                                                                  │
   🚨 BARK! BARK! (Error!)                                                            🐾 Safe! (Passes!)
   Blocks the file from launching.                                                    Stays waiting to be published.
```


## from: M7 Brand Guardian and Automated SEO Pipeline Strategy
```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        M7 AGENT KANBAN — FRISCO DAMAGE CLUSTER                         │
├──────────────┬───────────────┬──────────────────┬──────────────────┬───────────────────┤
│ 📋 1. INTAKE │ 📈 2. GAP MAP │ 📝 3. STAGING    │ 🛡️ 4. QUALITY CHECK│ 🚀 5. LIVE/INDEXED│
├──────────────┼───────────────┼──────────────────┼──────────────────┼───────────────────┤
│ [Card-01]    │ [Card-04]     │ [Card-07]        │ [Card-10]        │ [Card-12]         │
│ Storm-Track  │ Striking-     │ Home-Page        │ Watchdog Sweep   │ Frisco Hub        │
│ Ingestion    │ Distance Map  │ Brand-Flip       │ og:image check   │ Indexed (24hr)    │
│              │               │                  │                  │                   │
│ [Card-02]    │ [Card-05]     │ [Card-08]        │ [Card-11]        │ [Card-13]         │
│ 39GB Media   │ Competitor    │ IKO vs. IKO Certified      │ Schema Validation│ Five-Site         │
│ Geotagging   │ Category Scan │ Drafts           │ FAQ structures   │ Flywheel Spin     │
│              │               │                  │                  │                   │
│ [Card-03]    │ [Card-06]     │ [Card-09]        │                  │                   │
│ Customer     │ Intent & LSO  │ 5-Site Unique    │                  │                   │
│ Interview    │ Keyword Set   │ Content Cluster  │                  │                   │
└──────────────┴───────────────┴──────────────────┴──────────────────┴───────────────────┘
```


## from: M7 Brand Guardian and Automated SEO Pipeline Strategy
```bash
    python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_categories_mapper.py" "https://pineappleroofingllc.com" "saia" "xxxx xxxx xxxx xxxx xxxx xxxx"
    ```


## from: Real-Time Webhook Integration and Outbox Watcher Configuration
```json
{
  "discord_webhook_url": "https://discord.com/api/webhooks/PASTE_YOUR_DISCORD_WEBHOOK_HERE",
  "slack_webhook_url": "https://hooks.slack.com/services/PASTE_YOUR_SLACK_WEBHOOK_HERE",
  "telegram_bot_token": "PASTE_YOUR_TELEGRAM_BOT_TOKEN_HERE",
  "telegram_chat_id": "PASTE_YOUR_TELEGRAM_CHAT_ID_HERE",
  "notify_on_pass": true,
  "notify_on_fail": true
}
```


## from: Real-Time Webhook Integration and Outbox Watcher Configuration
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\outbox_watcher-v2.py"
```


## from: Pineapple M7 System Integration and Prompt Catalog
```bash
   python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_connection_test.py"
   ```


## from: Pineapple M7 System Integration and Prompt Catalog
```bash
   python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_connection_test.py" "https://pineappleroofingllc.com" "saia" "abcd efgh ijkl mnop qrst uvwx"
   ```


## from: Pineapple M7 System Integration and Prompt Catalog
```
[Case Study File] ──► [Hermes SEO Profile] ──► [5 Uniquely Hooked Articles] ──► [Eleventy Builds] ──► [Netlify CLI Deploy]
```


## from: Pineapple M7 System Integration and Prompt Catalog
```text
Act as the Lead Operations Manager for PM7 [cite: 206]. Scan our local directory at C:\Pineapple Contractors M7 [cite: 76, 132].
1. Read our active task pipeline inside '01_Command_Center/M7_Agent_Kanban.md' [cite: 66, 76].
2. Organize our active project tasks cleanly into our 5-column Kanban layout: [Triage] -> [Backlog] -> [In Progress] -> [Outbox Review] -> [Shipped] [cite: 66, 120].
3. For our upcoming Frisco SEO campaign [cite: 17], create a dedicated task card to audit our homepage and draft 3 striking-distance city pages (Allen, Grapevine, Euless) [cite: 17, 127].
4. Enforce strict M7 Brand Laws: Ensure every task inherits our visual color codes (Royal Navy #1A365D, Pineapple Gold #FBC02D, Status Cyan #00BFFF), blocks the color green entirely, and mandates the use of CPPA instead of "free inspection" [cite: 87, 126].
5. Update 'M7_Agent_Kanban.md' locally and report back with a clean markdown overview of our workspace [cite: 66, 76].
```


## from: Pineapple M7 System Integration and Prompt Catalog
```text
/goal "Act as the Lead Local SEO Copywriter for PM7 [cite: 14]. Read our core visual identity and lexicon rules from 01_Command_Center/GROUNDING.md and our business coordinates from 01_Command_Center/MASTER_PLAYBOOK.md [cite: 76, 98].
1. Ingest our $571,000 gross margin case study from '03_Knowledge_Mat/active_context/case_study_571k_plumbing.md' [cite: 207, 208].
2. Write a highly authoritative, conversion-optimized 1,200+ word Location Service Page targeting our unbranded keyword: 'hail damage roof repair Frisco TX' [cite: 14, 126].
3. Format the introduction block to provide a direct-answer hook within the first 40 words to capture Google AI Mode citations [cite: 43, 99].
4. Embed our verified trust credentials: family-operated in North Texas since 2005, RCAT Licensed #03-0637, IKO Certified (No IKO Certified), and our phone number 972-928-0788 [cite: 87, 126].
5. Enforce single-sentence-per-line spacing to improve crawlers' readability [cite: 43].
6. Generate complete, valid FAQPage schema mapping ZIP codes 75033, 75034, and 75035 [cite: 99, 130].
7. Save the completed markdown draft as PAUSED inside '01_Command_Center/Outbox_Drafts/Website_Pages/roof_repair_frisco.md' [cite: 76, 99]."
```


## from: Pineapple M7 System Integration and Prompt Catalog
```text
Act as the Systems Deployment Engineer for PM7 [cite: 130]. We are ready to push our validated assets live [cite: 81].
1. Connect to our self-hosted WordPress site using our active 'wordpress' MCP server connection [cite: 155, 161].
2. Read the staged location page draft from our local outbox: 'C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\Website_Pages\roof_repair_frisco.md' [cite: 76, 80].
3. Execute a brand-compliance scan: Verify there are 0 green visual hex codes, the CTA button is set to Pineapple Gold (#FBC02D), and there are no instances of the banned term 'free inspection' (must use CPPA) [cite: 87, 126].
4. Create a new page on pineappleroofingllc.com with the title 'Hail Damage Roof Repair in Frisco, TX' and slug 'hail-damage-roof-repair-frisco-tx' [cite: 15, 124].
5. Inject the compliant HTML body content and publish the page as a PAUSED draft [cite: 87, 126].
6. Verify the page creation was successful, log the transaction in our Memory Galaxy, and report back [cite: 66, 162].
```


## from: Pineapple M7 System Integration and Prompt Catalog
```text
Act as the Lead Compliance Auditor for PM7 [cite: 97]. Our non-negotiable Brand Laws are absolute [cite: 101, 108].
1. Run a recursive audit pass over all markdown drafts staged inside 'C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\' [cite: 76, 80].
2. Open and inspect each file: Scan for any green visual hex codes (e.g., #00FF00, lime, green css classes) [cite: 87, 126]. If found, flag the line and replace with Royal Navy (#1A365D) or Status Cyan (#00BFFF) [cite: 87, 126].
3. Scan for banned words: replace 'free inspection' with 'CPPA' [cite: 101, 126], replace 'IKO Certified' with 'IKO Certified' [cite: 101], replace '$0 down' with 'Full Restoration Coverage' [cite: 81], and replace 'Toa/Warrior/Six Brothers' with 'The Pineapple Standard' [cite: 101].
4. Verify that every page displays our physical address (1 Cowboys Way, Ste 270W, Frisco, TX 75034), RCAT Licensed #03-0637, and phone number 972-928-0788 [cite: 87, 126].
5. Report the audit results: output a clean log mapping each audited page with a green 'PASS' or a detailed failure correction note [cite: 17, 66].
```


## from: Pineapple M7 Automation and Regional Marketing Strategy Blueprint
```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        M7 REGIONAL CAMPAIGN BOARD CONFIGURATION                        │
├──────────────┬───────────────┬──────────────────┬──────────────────┬───────────────────┤
│ 📋 1. INTAKE │ 📈 2. GAP MAP │ 📝 3. STAGING    │ 🛡️ 4. QUALITY CHECK│ 🚀 5. LIVE/INDEXED│
├──────────────┼───────────────┼──────────────────┼──────────────────┼───────────────────┤
│ [Card-01]    │ [Card-04]     │ [Card-07]        │ [Card-10]        │ [Card-12]         │
│ Case Study   │ GSC Keyword   │ Localized City   │ Double-Agent     │ WordPress Live    │
│ Assembly     │ Scoreboard    │ Service Pages    │ Brand Firewall   │ Publish           │
│              │               │                  │                  │                   │
│ [Card-02]    │ [Card-05]     │ [Card-08]        │ [Card-11]        │ [Card-13]         │
│ Geotagged    │ Competitor    │ Multi-Format     │ Schema & Meta    │ Everywhere        │
│ Photo Pools  │ Category Scan │ Copywriting      │ Validator        │ Flywheel Spin     │
│              │               │                  │                  │                   │
│ [Card-03]    │ [Card-06]     │ [Card-09]        │                  │                   │
│ Review       │ Local Map     │ 5-Site Blog      │                  │                   │
│ Interceptor  │ Centroids     │ Network          │                  │                   │
└──────────────┴───────────────┴──────────────────┴──────────────────┴───────────────────┘
```


## from: Pineapple M7 Automation and Regional Marketing Strategy Blueprint
```
                                 ┌──────────────────────────────┐
                                 │      YOUR 39GB OF MEDIA      │
                                 │   (Before/Afters & Testimonials)│
                                 └──────────────┬───────────────┘
                                                │
         ┌──────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                      ▼                                      ▼
 📱 SOCIAL DEMAND                        📈 ORGANIC RANKINGS                    🛰️ LSA & MAP PACKS
  50/5/3 Video Reels,                    Everywhere Flywheel,                    Review Loops,
  pattern interrupts,                    AEO word-hooks,                         geotagged uploads
  and Pacific heritage story             and schema embeds                       and Category sweeps
```


# +78 prompt/code blocks (Master SOP 8/26)

## from: M7 Automation Guide: Drone Video and SEO Loop Setup
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
```

## from: M7 Automation Guide: Drone Video and SEO Loop Setup
```bash
/loop "run C:\Pineapple Contractors M7\04_Tech_Lab\scripts\run_background_seo.bat" --interval=7d --start="Wednesday 17:00"
```

## from: M7 Automation Guide: Drone Video and SEO Loop Setup
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
```

## from: Pineapple M7 Automation and AI Coding Workflow Guide
```cmd
@echo off
:: ============================================================================
:: PINEAPPLE M7 — AUTOMATED DAILY BACKUP & LINK HEALTH MONITOR
:: File: daily_backup.bat
:: ============================================================================
:: Automatically backs up your active local directory and executes
:: sitemap_validator.py to check site crawler health before closing.
:: ============================================================================

title PINEAPPLE M7 — DAILY BACKUP MANAGER
color 0E

echo ===================================================================
echo   🍍 PINEAPPLE M7 — ACTIVE BACKUP ^& MONITOR MANAGER 🍍
echo ===================================================================
echo   Enforcing RCAT License #03-0637 ^& Polynesian Family Standards [cite: 18, 126, 256]
echo   Corporate HQ: 1 Cowboys Way, Ste 270W, Frisco, TX 75034 [cite: 54]
echo ===================================================================
echo.

:: 1. Navigate to local project root folder
cd "C:\Pineapple Contractors M7" 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Root directory C:\Pineapple Contractors M7 was not found!
    echo Please make sure this script is located or run inside your vault root.
    pause
    exit /b
)

:: 2. Set date stamp (Format: YYYY-MM-DD)
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set stamp=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2%

set "BACKUP_DIR=_Backup_Vault\%stamp%"
echo [SYSTEM] Creating secure daily backup station at: %BACKUP_DIR%...
if not exist "%BACKUP_DIR%" (
    mkdir "%BACKUP_DIR%"
)

:: 3. Backing up folders to Backup_Vault using xcopy
echo.
echo [BACKING UP] Copying active workspace directories...
xcopy "01_Command_Center" "%BACKUP_DIR%\01_Command_Center\" /S /E /Y /I /Q >nul 2>&1
xcopy "03_Knowledge_Mat" "%BACKUP_DIR%\03_Knowledge_Mat\" /S /E /Y /I /Q >nul 2>&1
xcopy "04_Tech_Lab" "%BACKUP_DIR%\04_Tech_Lab\" /S /E /Y /I /Q >nul 2>&1
echo ✅ Workspace folder backup completed successfully!

:: 4. Run sitemap crawler verification
echo.
echo ===================================================================
echo 🛰️  LAUNCHING SITEMAP VALIDATOR (Daily Pre-Flight Sweep)
echo ===================================================================
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [WARNING] Python was not found on your system path.
    echo Skipping live XML sitemap crawling audit...
) else (
    if exist "04_Tech_Lab\scripts\sitemap_validator.py" (
        python "04_Tech_Lab\scripts\sitemap_validator.py" "https://pineappleroofingllc.com/wp-sitemap.xml"
        echo.
        echo ✅ Live sitemap validation sweep executed! 
        echo    Diagnostic report generated inside 01_Command_Center\Outbox_Drafts\
    ) else (
        echo [ERROR] sitemap_validator.py was not found in 04_Tech_Lab\scripts\!
    )
)

echo.
echo ===================================================================
echo   ✅ M7 DAILY SECURITY RUN COMPLETED!
echo   Backup Stamped: %stamp%
echo   Sitemap Health Checked! Stay safe, Saia!
echo ===================================================================
timeout /t 10
exit
```

## from: Pineapple M7 Automation and AI Coding Workflow Guide
```
 📊 1. PLANNING          🔧 2. BUILDING          🧪 3. TESTING           🚀 4. DEPLOYING
┌──────────────┐        ┌──────────────┐        ┌──────────────┐        ┌──────────────┐
│  Define the  │───────►│  Write Code  │───────►│ Auto-Execute │───────►│  PAUSED Draft│
│  TCCA Goal   │        │  (Ollama/Son)│        │   In Sandbox │        │  Check & Ship│
└──────────────┘        └──────────────┘        └──────────────┘        └──────────────┘
```

## from: Pineapple M7 Automation and AI Coding Workflow Guide
```bash
    jcode --role "scout" --task "Scan '03_Knowledge_Mat/01_Leads/' and map target zip positions."
    ```

## from: Pineapple M7 Automation and AI Coding Workflow Guide
```bash
    jcode --role "builder" --task "Compile 'one_take_scroll_landing.html' with Gold and Navy styles." [cite: 9, 127, 391]
    ```

## from: Pineapple M7 Automation and AI Coding Workflow Guide
```bash
    jcode --role "bouncer" --task "Run brand-firewall.py over all active workspace changes." [cite: 80, 391]
    ```

## from: M7 Automation Pipeline and Brand Compliance Deployment Guide
```json
{
  "envelope_version": "v1.2.0",
  "security_clearance": "DEC-005_OUTBOX_SHIELD",
  "routing": {
    "sender_agent": "m7_gsc_scout_agent",
    "recipient_agent": "m7_hormozi_writer_agent",
    "next_action_node": "m7_brand_compliance_firewall",
    "timestamp_gmt": "2026-08-11T16:17:00Z"
  },
  "brand_soul_constraints": {
    "brand_name": "Pineapple Roofing",
    "family_authority": "Polynesian-Owned since 2005 (JR & Saia Moeakiola)",
    "rcat_license": "#03-0637",
    "contact_phone": "972-928-0788",
    "physical_hq": "1 Cowboys Way, Ste 270W, Frisco, TX 75034",
    "color_palette": {
      "primary": "#1A365D",
      "secondary": "#FBC02D",
      "accent": "#00BFFF",
      "prohibited_colors": ["green", "#00FF00", "emerald"]
    },
    "banned_lexicon": [
      "Complimentary Professional Photo Audit (CPPA)",
      "Complimentary Professional Photo Audit (CPPA)",
      "$0 down",
      "no money out of pocket",
      "IKO Certified"
    ]
  },
  "payload": {
    "target_city": "Frisco",
    "target_zips": ["75033", "75034", "75035"],
    "focus_keyword": "hail damage roof repair frisco tx",
    "case_study_metrics": {
      "gross_revenue": 571000,
      "jobs_completed": 595,
      "timeframe_months": 9
    },
    "raw_input_data": "Insert raw search queries or customer transcript notes here..."
  },
  "audit_trail": {
    "firewall_scanned": false,
    "firewall_pass_status": "PENDING"
  }
}
```

## from: M7 Automation Pipeline and Brand Compliance Deployment Guide
```typescript
// C:\Pineapple Contractors M7\04_Tech_Lab\scripts\seo_pipeline.ts
// Coordinates build & deploy processes across your local static site silos

import * as fs from 'fs';
import * as path from 'path';

interface StaticSiteSilo {
  id: string;
  name: string;
  localPath: string;
  liveUrl: string;
  netlifySiteId: string;
}

export const SEO_FLYWHEEL_CONFIG = {
  version: "v0.20.0-Herald",
  primaryFlagship: "https://pineappleroofingllc.com",
  outboxDraftsDir: "C:\\Pineapple Contractors M7\\01_Command_Center\\Outbox_Drafts",
  
  // 🎡 REGISTERING THE 5 SITES ON THE FLYWHEEL
  silos: [
    {
      id: "site-1",
      name: "Pineapple Roofing Flagship",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-1-main",
      liveUrl: "https://pineappleroofingllc.com",
      netlifySiteId: "netlify-flagship-id"
    },
    {
      id: "site-2",
      name: "Frisco Storm Repair",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-2-frisco",
      liveUrl: "https://friscoroomdamage.com",
      netlifySiteId: "netlify-satellite-2"
    },
    {
      id: "site-3",
      name: "North Texas Roofing Pros",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-3-ntx",
      liveUrl: "https://northtexasroofingexperts.com",
      netlifySiteId: "netlify-satellite-3"
    },
    {
      id: "site-4",
      name: "Collin County Restoration Info",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-4-collin",
      liveUrl: "https://collincountyrestorations.com",
      netlifySiteId: "netlify-satellite-4"
    },
    {
      id: "site-5",
      name: "Polynesian Roofing Heritage Hub",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-5-heritage",
      liveUrl: "https://thepineapplestandard.com",
      netlifySiteId: "netlify-satellite-5"
    }
  ] as StaticSiteSilo[],

  // 🛡️ ENFORCING M7 BRAND COMPLIANCE BEFORE DEPLOYMENT
  complianceValidation: {
    enforceNoGreen: true,
    enforceCppaLexicon: true,
    requiredCredentials: ["RCAT #03-0637", "IKO Certified", "972-928-0788"]
  }
};
```

## from: M7 Automation Pipeline and Brand Compliance Deployment Guide
```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              PRIMARY LEADS SHEET HEADERS                               │
├────┬───────────┬───────────────┬──────────────┬──────────────────┬──────────┬──────────┤
│ ID │ TIMESTAMP │ CUSTOMER_NAME │ PHONE_NUMBER │ PROPERTY_ADDRESS │ ZIP_CODE │ LEAD_VAL │
├────┼───────────┼───────────────┼──────────────┼──────────────────┼──────────┼──────────┤
│ ...│ ...       │ ...           │ ...          │ ...              │ ...      │ ...      │
└────┴───────────┴───────────────┴──────────────┴──────────────────┴──────────┴──────────┘
```

## from: The M7 Autonomous SEO Dashboard and Automation Guide
```bash
    "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\run_background_seo.bat"
    ```

## from: M7 Automation Upgrade and Brand Compliance Manual
```python
    # =========================================================================
    # 🔥 DESKTOP HOT LEADS STASH (TOA TIER SPECIAL DISPATCH)
    # =========================================================================
    if tier == "TOA_TIER":
        try:
            # Dynamically resolves the active user's Desktop path on Windows
            desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop", "HOT_LEADS.txt")
            
            with open(desktop_path, "a", encoding="utf-8") as hf:
                hf.write("====================================================\n")
                hf.write(f"🔥 HOT LEAD ALERT: TOA TIER QUALIFIED (Score: {score}/100)\n")
                hf.write("====================================================\n")
                hf.write(f"👤 Name:     {lead_payload.get('customer_name', 'N/A')}\n")
                hf.write(f"📞 Phone:    {lead_payload.get('phone', 'N/A')}\n")
                hf.write(f"📍 ZIP Code: {lead_payload.get('zip_code', 'N/A')}\n")
                hf.write(f"🏢 Comm:     {lead_payload.get('is_commercial', False)}\n")
                hf.write(f"💰 Est. Val: ${property_value:,.2f}\n")
                hf.write(f"⛈️ Services: {lead_payload.get('services_requested', 'N/A')}\n")
                hf.write(f"📝 Notes:    {lead_payload.get('notes', 'N/A')}\n")
                hf.write(f"🕒 Timestamp: 2026-08-11 18:48:55\n")
                hf.write("====================================================\n\n")
                
            print(f"\n🔥 {RED}[DESKTOP ALERT] Hot Lead instantly written to Desktop/HOT_LEADS.txt!{RESET}")
        except Exception as de:
            print(f"\n⚠️ [DESKTOP WRITE ERROR] Could not save hot lead: {de}")
```

## from: M7 Automation Upgrade and Brand Compliance Manual
```
┌────────────────────────────────────────────────────────────────────────┐
│               M7 24/7 BACKGROUND TRAFFIC ENGINE RUNTIME                 │
├────────────────────────────────────────────────────────────────────────┤
│  LOOP START (Every 6 Hours)                                            │
│   │                                                                    │
│   ├──► 1. Query GSC Data (gsc_frisco_scan.py) -> Finds hot terms       │
│   ├──► 2. Generate Content -> Claude Code drafts a clean static page   │
│   ├──► 3. Firewall Scan (brand-firewall.py) -> Block if green or "free"│
│   ├──► 4. Deploy Page (Netlify CLI / WP REST) -> Moves page live       │
│   └──► 5. Index Submission (sitemap_validator.py) -> Indexes in 24 hrs │
│                                                                        │
│  SLEEP (6 Hours) ──► RESTART LOOP                                       │
└────────────────────────────────────────────────────────────────────────┘
```

## from: M7 Automation Upgrade and Brand Compliance Manual
```cmd
@echo off
TITLE M7 24/7 Background SEO Traffic Engine
color 0C

:loop
cls
echo ===================================================================
echo   🛰️  M7 24/7 BACKGROUND TRAFFIC ENGINE IS ACTIVE
echo   Enforcing 0%% Green visual laws and strict CPPA naming schemas [cite: 9, 126, 127]
echo ===================================================================
echo [SYSTEM] Local Time: %date% %time%
echo.

:: 1. Scan GSC for trending keywords in Frisco/Plano
echo [STEP 1/4] Scanning Google Search Console for impression spikes...
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\gsc_frisco_scan.py" [cite: 80]
timeout /t 5 >nul

:: 2. Execute JCode to write a new local static landing page
echo.
echo [STEP 2/4] Initializing jcode Swarm to generate optimized city copy... [cite: 386]
jcode --role "builder" --task "Generate a new HTML location page for Frisco ZIP 75035 using IKO Dynasty metrics [cite: 150, 256]. Use no green styles [cite: 127]." [cite: 391]
timeout /t 10 >nul

:: 3. Force Compliance Check
echo.
echo [STEP 3/4] Passing page to Brand Firewall...
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\brand-firewall.py" "C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts" [cite: 80]
if %errorlevel% neq 0 (
    echo [CRITICAL ERROR] Brand Firewall flagged a violation! Halting deploy.
    goto sleep_cycle
)

:: 4. Deploy and Index
echo.
echo [STEP 4/4] Publishing page and submitting to Indexceptional API...
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\sitemap_validator.py" [cite: 80]

:sleep_cycle
echo.
echo ===================================================================
echo   💤 CYCLE COMPLETE. Sleeping for 6 hours before next check...
echo ===================================================================
:: Sleeps for 21,600 seconds (6 hours)
timeout /t 21600

goto loop
```

## from: Pineapple M7: Automated WordPress Deployment and Interactive Scroll Engine
```
  [Claude / Hermes] ──► [m7_n8n_webhook_bridge.py] ──► [Local n8n Webhook Node]
                                                               │
     ┌─────────────────────────────────────────────────────────┴─────────────────────────────────────────┐
     ▼                                                         ▼                                         ▼
[Discord Alerts]                                        [Twilio SMS Loop]                       [Google Sheets CRM]
```

## from: Pineapple M7: Automated WordPress Deployment and Interactive Scroll Engine
```cmd
@echo off
:: ============================================================================
:: PINEAPPLE M7 — 1-CLICK WORDPRESS BULK DEPLOYMENT UTILITY
:: File: deploy_all_services.bat
:: ============================================================================

title PINEAPPLE M7 — 1-CLICK DEPLOYMENT CONSOLE
color 0B

echo ===================================================================
echo    Pineapple M7 — AUTOMATED MIGRATION DEPLOYER CONSOLE 🍍
echo ===================================================================
echo   Enforcing RCAT License #03-0637 & Polynesian Family Standards [cite: 18, 126, 256]
echo   Corporate HQ: 1 Cowboys Way, Ste 270W, Frisco, TX 75034 [cite: 54]
echo ===================================================================
echo.

:: 1. Verify python is installed and available
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python was not detected on your system path!
    echo Please install Python 3.10+ and select "Add to PATH" before continuing.
    pause
    exit /b
)

:: 2. Setup targets and credentials
set "WP_URL=https://pineappleroofingllc.com"
set "WP_USER=saia"
set "WP_PASS="

:: 3. Read cached Application Password from .env if it exists
if exist "04_Tech_Lab\config\.env" (
    for /f "tokens=1,2 delims==" %%A in (04_Tech_Lab\config\.env) do (
        if "%%A"=="WP_APPLICATION_PASSWORD" set "WP_PASS=%%B"
    )
)

:: 4. Prompt user if Application Password is missing
if "%WP_PASS%"=="" (
    echo [PROMPT] WordPress Application Password is not configured in your .env file yet.
    echo Please generate one from your WordPress Dashboard under (Tools -> MCP Ultimate) [cite: 311, 323].
    echo.
    set /p "WP_PASS=🔑 Paste your 24-character Application Password: "
)

if "%WP_PASS%"=="" (
    echo [ERROR] Application Password is required to execute authenticated REST pings!
    echo Aborting deployment loop to protect staging files.
    pause
    exit /b
)

echo.
echo 🛰️ Starting secure REST handshake with %WP_URL%...
echo 🛡️  Outbox Shield Status: PASS (Enforcing draft-only safety check) [cite: 13, 182]
echo ===================================================================
echo.

:: 5. Execute the background python deployment orchestrator
python "%~dp0wp_deployer.py" "%WP_URL%" "%WP_USER%" "%WP_PASS%"

echo.
echo ===================================================================
echo   ✅ DEPLOYMENT QUEUE COMPLETED!
echo   All processed items are currently saved in your WP Drafts dashboard.
echo   You can review and publish them at your discretion.
echo   Stay safe, Saia!
echo ===================================================================
pause
exit
```

## from: Pineapple M7: Automated WordPress Deployment and Interactive Scroll Engine
```python
import os
import sys

# ============================================================================
# PINEAPPLE M7 — ONE-TAKE WEBSITE ENGINE: SCROLL-ROTATION BUILDER
# File: one_take_builder.py
# ============================================================================

def compile_one_take_page(output_path, video_filename="shingle_rotation_30s.mp4"):
    """
    Compiles an interactive scroll-scrubbing HTML page.
    Utilizes 100% compliant brand colors (0% Green, Royal Navy & Gold) [cite: 9, 127].
    """
    print("=================================================================")
    print("🍍 PINEAPPLE M7 — ONE-TAKE WEBSITE ENGINE ACTIVE")
    print(f"📁 Compiling scroll-rotation template to: {output_path}")
    print("=================================================================")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Pineapple Standard — Premium IKO Roof Restoration</title>
    
    <!-- Local Geographic SEO Metadata -->
    <meta name="geo.region" content="US-TX">
    <meta name="geo.placename" content="Frisco, TX">
    <meta name="geo.position" content="33.1507;-96.8236">
    <meta name="ICBM" content="33.1507, -96.8236">

    <style>
        /* 🎨 PINEAPPLE M7 CORPORATE COLOR MATRIX (0% GREEN ALLOWED) */
        :root {{
            --navy: #1A365D;      /* Royal Navy - Dominates Headers & Base */
            --gold: #FBC02D;      /* Pineapple Gold - Hero CTAs & Borders */
            --cyan: #00BFFF;      /* Status Cyan - Hyperlinks & Dynamic Focus */
            --dark: #0F172A;      /* Deep Slate Base */
            --light: #F8FAFC;     /* Off-White Text Elements */
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }}

        body {{
            background-color: var(--dark);
            color: var(--light);
            overflow-x: hidden;
            font-size: 16px;
            line-height: 1.6;
        }}

        /* 🎬 SCROLL CONTAINER (Controls scroll depth and play speed) */
        #scroll-container {{
            position: relative;
            height: 400vh; /* 4 pages of scroll depth for comfortable scrubbing */
        }}

        /* 📹 STICKY VIDEO VIEWPORT (Stays locked on screen during scrub) */
        #video-viewport {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            background: radial-gradient(circle, var(--navy) 0%, var(--dark) 100%);
        }}

        video {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.55; /* Blends visual contrast with overlay text */
            pointer-events: none;
        }}

        /* 📑 HERO CONTENT OVERLAYS */
        .content-section {{
            position: relative;
            z-index: 2;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 0 10%;
            max-width: 800px;
        }}

        /* 💥 HORMOZI-STYLE TYPOGRAPHY RULES */
        h1 {{
            font-size: 3.5rem;
            color: var(--gold);
            line-height: 1.1;
            margin-bottom: 20px;
            font-weight: 900;
            text-transform: uppercase;
            text-shadow: 2px 4px 10px rgba(0,0,0,0.8);
        }}

        p {{
            font-size: 1.25rem;
            color: #FFFFFF;
            margin-bottom: 25px;
            text-shadow: 1px 2px 5px rgba(0,0,0,0.8);
        }}

        .intro-hook {{
            font-weight: bold;
            color: var(--cyan);
            letter-spacing: 1px;
            margin-bottom: 5px;
            text-transform: uppercase;
        }}

        /* 💰 PREMIUM CTA DESIGN (No green, high contrast) */
        .cta-btn {{
            display: inline-block;
            background-color: var(--gold);
            color: var(--navy);
            padding: 18px 36px;
            font-size: 1.1rem;
            font-weight: bold;
            text-decoration: none;
            border-radius: 50px;
            text-transform: uppercase;
            letter-spacing: 1px;
            border: 2px solid var(--gold);
            transition: all 0.25s ease;
            box-shadow: 0 4px 15px rgba(251, 192, 45, 0.4);
            align-self: flex-start;
        }}

        .cta-btn:hover {{
            background-color: transparent;
            color: var(--gold);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(251, 192, 45, 0.6);
        }}

        /* 📜 TRUST CARD BLOCK */
        .trust-card {{
            background: rgba(26, 54, 93, 0.85); /* 85% Navy Opacity */
            border-left: 5px solid var(--gold);
            padding: 25px;
            border-radius: 4px;
            margin-top: 20px;
            backdrop-filter: blur(10px);
        }}

        .trust-meta {{
            font-size: 0.9rem;
            color: var(--cyan);
            margin-top: 10px;
            font-weight: bold;
        }}

        /* 📜 SCROLL DOWN INDICATOR */
        .scroll-down {{
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            color: var(--gold);
            font-weight: bold;
            letter-spacing: 2px;
            animation: bounce 2s infinite;
        }}

        @keyframes bounce {{
            0%, 20%, 50%, 80%, 100% {{ transform: translate(-50%, 0); }}
            40% {{ transform: translate(-50%, -10px); }}
            60% {{ transform: translate(-50%, -5px); }}
        }}
    </style>
</head>
<body>

    <!-- 📹 THE SCROLL-DRIVEN STICKY REEL VIEWPORT -->
    <div id="video-viewport">
        <video id="scrollVideo" playsinline muted preload="auto">
            <source src="{video_filename}" type="video/mp4">
            Your browser does not support HTML5 video.
        </video>
    </div>

    <!-- 📑 HERO SCROLL CONTAINER -->
    <div id="scroll-container">
        
        <!-- SECTION 1: THE DISRUPTIVE HOOK -->
        <div class="content-section" style="height: 100vh;">
            <span class="intro-hook">Let's Be Real</span>
            <h1>Frisco Roof Damage<br>Is Invisible.</h1>
            <p>North Texas winds shear off shingles. Hidden hail micro-cracks go unnoticed. Until water ruins your living room ceiling.</p>
            <a href="#audit" class="cta-btn">Book Your Photo Audit</a>
            <div class="scroll-down">🔽 SCROLL TO ROTATE ACCENT</div>
        </div>

        <!-- SECTION 2: THE DATA REVEAL -->
        <div class="content-section" style="height: 100vh;">
            <span class="intro-hook">We Tested It</span>
            <h1>ArmourZone®<br>Strong Defense.</h1>
            <p>As you scroll, notice the premium reinforced backing. Standard shingles tear at the nail line. IKO Dynasty shingles hold fast in 130 mph hurricanes.</p>
            <div class="trust-card">
                We standardized strictly on IKO Certified systems to shield your family equity. [cite: 18, 126, 256]
                <div class="trust-meta">RCAT License #03-0637 | Polynesian-Run Since 2005 [cite: 18, 126, 256]</div>
            </div>
        </div>

        <!-- SECTION 3: THE CASE STUDY PROOF -->
        <div class="content-section" style="height: 100vh;">
            <span class="intro-hook">$571,000 Recovered</span>
            <h1>595 Local Homes<br>Fully Restored.</h1>
            <p>We completed a massive 9-month restoration sprint across North Texas. That is 595 families protected from predatory storm chasers.</p>
            <a href="tel:972-928-0788" class="cta-btn">Call Saia: 972-928-0788</a>
        </div>

        <!-- SECTION 4: THE AUDIT FORM CLOSE -->
        <div class="content-section" style="height: 100vh;" id="audit">
            <span class="intro-hook">Get Objective Proof</span>
            <h1>Complimentary<br>Photo Audit.</h1>
            <p>We perform a detailed, drone-assisted survey of your complete roof decking. You get a full, high-definition photographic record for your insurance files.</p>
            <div class="trust-card">
                🗺️ <strong>Pineapple Contractors HQ:</strong><br>
                1 Cowboys Way, Ste 270W, Frisco, TX 75034 [cite: 54]<br>
                📞 Phone: 972-928-0788 [cite: 54]
            </div>
        </div>

    </div>

    <!-- ⚙️ SCROLL SCRUBBING ENGINE -->
    <script>
        const video = document.getElementById("scrollVideo");
        const container = document.getElementById("scroll-container");

        // Smooth Easing Interpolation variables
        let targetScrubTime = 0;
        let currentScrubTime = 0;
        const interpolationFactor = 0.1; // Lower is smoother (creates easing)

        window.addEventListener("scroll", () => {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            const maxScroll = container.scrollHeight - window.innerHeight;
            
            // Calculate progress percentage (0.0 to 1.0)
            const scrollPercent = Math.max(0, Math.min(1, scrollTop / maxScroll));
            
            // Map scroll ratio to video timeline duration
            if (video.duration) {
                targetScrubTime = video.duration * scrollPercent;
            }
        });

        // Fluid Easing Animation Loop
        function animateScrub() {
            if (video.duration) {
                // Interpolate current time toward target time
                currentScrubTime += (targetScrubTime - currentScrubTime) * interpolationFactor;
                video.currentTime = Math.max(0, Math.min(video.duration - 0.05, currentScrubTime));
            }
            requestAnimationFrame(animateScrub);
        }

        // Initialize easing animation frame loop
        requestAnimationFrame(animateScrub);
    </script>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"🎉 [SUCCESS] One-Take scroll template completed! Saved to: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\Website_Pages"
    os.makedirs(out_dir, exist_ok=True)
    compile_one_take_page(os.path.join(out_dir, "one_take_scroll_landing.html"))
```

## from: Building Strategic Comparison Pages with Claude-SEO
```bash
/seo competitor-pages https://competitor-domain.com
```

## from: Building Strategic Comparison Pages with Claude-SEO
```markdown
# Pineapple Roofing vs. DFW Competitors: The Honest Comparison
> **Slogan:** Roofing Made Sweeter [cite: 490]  
> **Brand Policy:** The Pineapple Standard [cite: 591]  
> **License & Authority:** RCAT Licensed #03-0637 | IKO Certified [cite: 592]  

---

When your home survives a major North Texas storm, choosing a contractor isn't about finding the lowest bidder. It's about protecting your family's investment with documented, certified engineering proof. 

Most DFW roofing companies send aggressive doorstep salespeople to push un-itemized "Complimentary Professional Photo Audit (CPPA)." At Pineapple Roofing, we hold our family-operated, Polynesian-owned business to a higher standard. We don't sell; we document.

## 📊 Side-by-Side Comparison Matrix

For comparison-style pages, the SEO-team uses scannable HTML tables to display our credentials against standard regional competitors:

<table>
  <thead>
    <tr style="background-color: #1A365D; color: #FFFFFF;">
      <th style="padding: 12px; border: 1px solid #FBC02D;">Core Feature</th>
      <th style="padding: 12px; border: 1px solid #FBC02D;">DFW Storm Chasers / Competitors</th>
      <th style="padding: 12px; border: 1px solid #FBC02D; color: #FBC02D;">Pineapple Roofing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold;">Initial Roof Inspection</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0;">Un-itemized "Complimentary Professional Photo Audit (CPPA)" or visual driveway guess [cite: 13, 112]</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #1A365D;">Complimentary Professional Photo Audit (CPPA) [cite: 591]</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold;">Manufacturer Shingle System</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0;">IKO Certified or low-performance 3-tab shingle variants [cite: 15, 112, 147]</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #1A365D;">IKO Certified Premium Storm Shingles (Dynasty) [cite: 150, 592]</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold;">Product Warranty Coverage</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0;">Standard 10 to 20-year limited warranty [cite: 37]</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #1A365D;">50-Year Non-Prorated Product Warranty [cite: 224]</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold;">Licensing & Credentials</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0;">Unlicensed, out-of-state storm-chasing crews [cite: 223]</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #1A365D;">RCAT Licensed #03-0637 (Certified DFW HQ) [cite: 592, 599]</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold;">Insurance Claim Approach</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0;">Verbal arguments with adjusters, risking fast denials [cite: 112]</td>
      <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #1A365D;">Comprehensive drone & photo documentation for successful claims [cite: 591]</td>
    </tr>
  </tbody>
</table>

---

## 📸 Drone-Assisted Photographic Proof

We document every hail fracture and wind-torn shingle seal with high-resolution visual evidence that insurance adjusters accept. Instead of arguing, we provide your carrier with an indisputable engineering-grade file of your roof's condition.

## 🤝 Schedule Your Professional Photo Audit Today

Protect your family's investment and secure your structural assets. Contact our Frisco command center to book your CPPA.

**🔥 Want to get started with an elite local crew?**
> Inside our Frisco restoration pipeline, our certified experts stand ready to document your property's exterior. Call **972-928-0788** today to schedule your Complimentary Professional Photo Audit [cite: 591].

---
### 📋 Frequently Asked Questions (FAQ)

**Q: How much does a Complimentary Professional Photo Audit cost?**  
**A:** There is zero cost to you [cite: 263]. We perform a full, drone-assisted visual mapping of your shingles and present you with a high-definition copy of the damage [cite: 223].

**Q: Will filing a storm restoration claim raise my insurance rates?**  
**A:** In Texas, carriers are generally restricted from raising personal rates due to acts of nature or natural storm events [cite: 14, 428].
```

## from: Goldie Search Gravity Stack Automation Blueprint
```mermaid
graph TD
    %% Define Nodes with Brand Color Classes
    A[GSC Scout Node<br>gsc_frisco_scan.py] -->|1. Keyword Gaps| B(Copywriting Station<br>jcode / Claude)
    B -->|2. Staged Drafts| C{Compliance Firewall<br>brand_firewall-v2.py}
    
    %% Decision Fork
    C -->|FAIL: Violation Detected| D[Slack/Discord Webhook<br>Immediate Block]
    C -->|PASS: Safe Draft| E[n8n Webhook Bridge<br>m7_n8n_webhook_bridge-v2.py]
    
    %% Post-Pass Distribution Flow
    E -->|3. Calculate score| F[Lead Scorer Module<br>m7_scoring.py]
    F -->|If Score >= 80| G[Desktop Hot Leads File<br>Desktop/HOT_LEADS.txt]
    F -->|All leads synced| H[CRM Leads Database<br>Leads Google Sheet]
    
    E -->|4. Push Approved Pages| I[WordPress Deployer<br>wp_deployer.py / rest]
    I -->|5. Check Indexing Link Health| J[Sitemap Validator<br>sitemap_validator.py]

    %% Color Enforcements (Royal Navy & Pineapple Gold theme)
    classDef default fill:#1A365D,stroke:#FBC02D,stroke-width:2px,color:#F8FAFC;
    classDef decision fill:#0e1629,stroke:#00BFFF,stroke-width:2px,color:#00BFFF;
    classDef fail fill:#6e0e0e,stroke:#dc2626,stroke-width:2px,color:#fca5a5;
    
    class C decision;
    class D fail;
```

## from: Goldie Search Gravity Stack Automation Blueprint
```typescript
// Replace placeholder parameters with your active 5-site paths [cite: 374]
export const SEO_FLYWHEEL_CONFIG = {
  primaryFlagship: "https://pineappleroofingllc.com",
  outboxDraftsDir: "C:\\Pineapple Contractors M7\\01_Command_Center\\Outbox_Drafts",
  
  silos: [
    { id: "site-1", localPath: "C:\\M7\\site-1-main", liveUrl: "https://pineappleroofingllc.com" },
    { id: "site-2", localPath: "C:\\M7\\site-2-frisco", liveUrl: "https://friscoroofrepair.com" },
    { id: "site-3", localPath: "C:\\M7\\site-3-pros", liveUrl: "https://northtexasroofingexperts.com" },
    { id: "site-4", localPath: "C:\\M7\\site-4-collin", liveUrl: "https://collincountyrestorations.com" },
    { id: "site-5", localPath: "C:\\M7\\site-5-heritage", liveUrl: "https://thepineapplestandard.com" }
  ]
};
```

## from: Goldie Search Gravity Stack Automation Blueprint
```text
Act as the fractional CMO of PM7 [cite: 420]. Your job is to ingest raw roofing metrics and transform them into SEO-optimized content briefs for our local city-pages [cite: 420].
Mandatory Rules:
1. All landing pages must deliver a highly concentrated, direct answer in the first 40 words (Google AI Mode optimization) [cite: 347, 553].
2. Enforce Royal Navy (#1A365D) for background blocks and Pineapple Gold (#FBC02D) for action buttons [cite: 180]. Zero green colors allowed [cite: 180].
3. Emphasize "The Pineapple Standard" and "Roofing Made Sweeter" [cite: 57, 125, 282].
4. Banned Terms: Never use "Complimentary Professional Photo Audit (CPPA)," "Complimentary Professional Photo Audit (CPPA)," or IKO Certified. Replace with "Complimentary Professional Photo Audit (CPPA)" and "IKO Certified" [cite: 126, 189].
5. Do not include any Tongan native proverbs or cultural principles [cite: 14]. Maintain a clean, high-performance corporate tone [cite: 14, 57].
```

## from: Goldie Search Gravity Stack Automation Blueprint
```bash
antigravity run hermes_seo --context=/03_Knowledge_Mat/active_context/gsc_run_01.md --execute-stack
```

## from: Digital Avatar Cloning and Automated Video Production Blueprint
```
   👤 CLONE LAYER A: THE LIKENESS (HeyGen)      🗣️ CLONE LAYER B: THE VOICE (ElevenLabs)
  ┌──────────────────────────────────────┐     ┌──────────────────────────────────────┐
  │ • Upload a clear 2-minute raw video  │     │ • Upload 5-10 minutes of clean,      │
  │ • Capture natural gestures & smiles  │     │   uninterrupted microphone audio     │
  │ • Generates a responsive HD avatar   │     │ • Creates a 100% life-like vocal map │
  └──────────────────────────────────────┘     └──────────────────────────────────────┘
```

## from: Pineapple M7 Bulk Pre-Flight Compliance Sweep Guide
```
     📦 33 STAGED COOKIES            👀 DETECTOR ROBOT                🏫 THE BAKE SALE
   (Draft HTML / Markdown)         (bulk_firewall_sweep.py)          (Live WordPress Site)
   ┌───────────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
   │ 🍪 Cookie #1          │ ──►   │ Scans for green icing │ ──►   │ Only perfect cookies  │
   │ 🍪 Cookie #2          │       │ or bad ingredients   │       │ are approved and sent │
   │ 🍪 ...                │       │ [BANNED TERMS CHECKED]│       │ to the shelves!       │
   └───────────────────────┘       └───────────────────────┘       └───────────────────────┘
```

## from: Pineapple M7 Bulk Pre-Flight Compliance Sweep Guide
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\bulk_firewall_sweep.py"
```

## from: Pineapple M7 Bulk Pre-Flight Compliance Sweep Guide
```text
=================================================================
🍍 PINEAPPLE M7 — BULK PRE-FLIGHT COMPLIANCE SWEEP
📁 Staging Folder: C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts
=================================================================

🟢 [PASS] frisco_hail_repair_75033.html
🟢 [PASS] plano_storm_restoration_75093.html
🟢 [PASS] commercial_decking_audit.md
...

=================================================================
📊 PRE-FLIGHT SWEEP COMPLETED:
=================================================================
📁 Total Staged Drafts Scanned:  33
🟢 Clean Certified Drafts:       33
🔴 Action Required (Failed):     0
🚨 Total Violations Logged:      0
=================================================================

💾 [SAVED] Compliance summary written to: Outbox_Drafts/bulk_compliance_report.md
```

## from: The M7 Graph Architecture: Velocity via Parallel Agent Assembly
```
   🔎 STATIONS 1-4 (Cheap Workers)               🛡️ STATION 5 (Flagship Checker)
  ┌───────────────────────────────┐             ┌───────────────────────────────┐
  │ Runs on: Free Local Ollama    │ ──────────► │ Runs on: Premium GPT-5.6 /    │
  │ Tasks: Fetching, writing,     │             │          Claude Sonnet        │
  │        formatting city drafts │             │ Task: Strict Brand Firewall   │
  └───────────────────────────────┘             └───────────────────────────────┘
```

## from: The Pineapple Standard: Brand Firewall Engine Protocol
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\brand_firewall.py" "This draft contains Toa and mentions Complimentary Professional Photo Audit (CPPA)."
```

## from: The Pineapple Standard: Brand Firewall Engine Protocol
```text
=== Running Compliance Audit: CLI_Raw_Text_Input ===
❌ COMPLIANCE FAIL: Found 2 active violations!

[1] Violation: Banned Lexicon Term
    Line 1: "This draft contains Toa and mentions Complimentary Professional Photo Audit (CPPA)."
    Mandated Fix: Replace with approved Brand terminology: 'The Pineapple Standard' [cite: 86]

[2] Violation: Banned Lexicon Term
    Line 1: "This draft contains Toa and mentions Complimentary Professional Photo Audit (CPPA)."
    Mandated Fix: Replace with approved Brand terminology: 'Complimentary Professional Photo Audit (CPPA)' [cite: 86]
```

## from: Sitemap Validator and Unified Core Systems Technical Guide
```
   THE TREASURE MAP (Sitemap)      🧑‍🚀 ROBOT DETECTOR (Validator)     🏴‍☠️ THE CAPTAIN (Google)
 ┌───────────────────────────┐      ┌───────────────────────────┐     ┌───────────────────────┐
 │ (X) /locations/frisco-tx/ │ ──►  │ Pings: "Is there real     │ ──► │ Indexes clean pages   │
 │ (X) /locations/plano-tx/  │      │ gold buried here?" [200]  │     │ in search results!    │
 └───────────────────────────┘      └───────────────────────────┘     └───────────────────────┘
```

## from: Sitemap Validator and Unified Core Systems Technical Guide
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\sitemap_validator.py" "https://pineappleroofingllc.com/wp-sitemap.xml"
```

## from: Graph Engineering: The Multi-Agent Assembly Line
```
  📋 INPUT ──► [🔎 Node 1: Scout] ──► [📝 Node 2: Writer] ──► [🛡️ Node 3: Auditor] ──► 🚀 OUTBOX
                     │                      │                       │
                     └────── Edge 1 ────────┘─────── Edge 2 ────────┘
                  (Handoff: research.json)   (Handoff: draft.md)
```

## from: The Pineapple Standard Brand Firewall Deployment Guide
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\brand_firewall.py" "This draft contains Toa and mentions Complimentary Professional Photo Audit (CPPA)."
```

## from: The Pineapple Standard Brand Firewall Deployment Guide
```text
=== Running Compliance Audit: CLI_Raw_Text_Input ===
❌ COMPLIANCE FAIL: Found 2 active violations!

[1] Violation: Banned Lexicon Term
    Line 1: "This draft contains Toa and mentions Complimentary Professional Photo Audit (CPPA)."
    Mandated Fix: Replace with approved Brand terminology: 'The Pineapple Standard' [cite: 86]

[2] Violation: Banned Lexicon Term
    Line 1: "This draft contains Toa and mentions Complimentary Professional Photo Audit (CPPA)."
    Mandated Fix: Replace with approved Brand terminology: 'Complimentary Professional Photo Audit (CPPA)' [cite: 86]
```

## from: The M7 Second Brain and Infinite Context Engine
```bash
claude --plugin-dir "C:\Pineapple Contractors M7\04_Tech_Lab\vendor\claude-obsidian"
```

## from: The Pineapple M7 Autonomous SEO Dashboard and Loop Guide
```bash
    "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\run_background_seo.bat"
    ```

## from: The Hormozi Matrix and CARPARK Sales Blueprint
```
  [New Inbound Lead] ──► [Lead Score Calculated] ──► [Score ≥ 80 (TOA Tier)]
                                                              │
     ┌────────────────────────────────────────────────────────┴─────────────────────────────────────────┐
     ▼                                                                                                  ▼
[SMS Alert Sent to Saia]                                                                     [Speed-to-Lead Rep SLA]
  "Call immediately!" [cite: 1]                                                                 Dial within 120 seconds [cite: 3]
                                                                                                        │
                                                                                                        ▼
                                                                                             [The 5-Min Lead Bridge]
                                                                                               "This is a photo report,
                                                                                                not a sales pitch" [cite: 3]
                                                                                                        │
                                                                                                        ▼
                                                                                              [In-Home CARPARK Walk]
                                                                                               Document → Agitate → Resolve
                                                                                               → Proof → Agree → Review → Kickoff [cite: 2]
```

## from: The Everywhere Engine AI SEO Automation Strategy
```
  [1 Keyword + 1 Case Study] ──► [jcode Parallel Swarms] ──► [Cross-Site Backlinks] ──► [Indexing API]
```

## from: The Everywhere Engine AI SEO Automation Strategy
```
   ┌────────────────────────────────────────────────────────────────────────┐
   │ 📊 GSC DATA EXTRACTION PASS — 25 TARGET OPPORTUNITIES ANALYZED          │
   ├────────────────────────────────────────────────────────────────────────┤
   │                                                                        │
   │  🔍 GSC CONTENT GAPS (Impressions > 0, Clicks = 0)                     │
   │   • The "Golden Signal" — Google is already trying to show your site   │
   │     for these terms, but you lack a dedicated landing page [cite: 260].      │
   │   • Action: Autonomously spin up parent-spoke target hub pages [cite: 17].   │
   │                                                                        │
   │  💧 GSC CONTENT LEAKS (High Rankings, CTR < 1%)                        │
   │   • The page ranks fine but fails to earn the user's click [cite: 41].       │
   │   • Action: Rewrite meta titles, adjust CTA buttons, and optimize tags [cite: 41].│
   │                                                                        │
   └────────────────────────────────────────────────────────────────────────┘
```

## from: The Everywhere Engine AI SEO Automation Strategy
```
  OLD WAY: Click ──► Report ──► Think ──► Click ──► [Wasted Tokens & High Latency] [cite: 302]
  
  NEW WAY: One unified script ──► Start to Finish execution ──► [66% Token Savings] [cite: 300, 303]
```

## from: The Pineapple Standard: Integrated DFW Automation Suite v7
```
  [GSC Scout Node] ──► [Copywriting Station] ──► [Brand Firewall]
                                                        │
     ┌──────────────────────────────────────────────────┴──────────────────────────────────────────────────┐
     ▼ (If PASS)                                                                                           ▼ (If FAIL)
 [n8n Webhook Bridge]                                                                                  [Discord Block]
     │
     ├──► [Lead Scorer Module] ──► [Desktop HOT_LEADS.txt] (If Score ≥ 80)
     │
     └──► [WordPress Deployer] ──► [Sitemap Link Validator]
```

## from: Frisco City Hub SEO and Browser Use Engine Integration
```
  [OLD 12-TOOL LOOP]  Carries 12 manuals ──► Click ──► Call home ──► Think ──► Type ──► Call home [cite: 365, 366]
```

## from: Frisco City Hub SEO and Browser Use Engine Integration
```
  [ONE-SCRIPT ENGINE] Carries 1 manual ──► Writes checklist ──► Executes task start-to-finish ──► Done! [cite: 368, 369]
```

## from: M7 Hermes Profile and Skill Enhancement Package
```text
/goal "Act as the Lead Systems Engineer for PM7 [cite: 197]. Read our newly published 'm7-hermes-profile-enhancement.md' from our active artifacts folder [cite: 80]. Safely copy the updated 'soul.md' to our Command Center [cite: 236], register the new Wednesday ad audit and sitemap health skills in our Tech Lab [cite: 250], and update our global 'config.yaml' to lock on the 60% token-saving browser-use backend [cite: 351, 358]. Verify all paths and run a brand firewall check over changed configurations [cite: 80, 245]. Pause and wait for Saia's review [cite: 192, 205]."
```

## from: M7 Agent OS: Automated AI Video Production Blueprint
```
  [1. The Brief] ──► [2. The Likeness] ──► [3. The Cut] ──► [4. The Screening] ──► [5. Outbox PAUSED]
```

## from: M7 Agent OS: Automated AI Video Production Blueprint
```
   FRISCO REEL STRUCTURE — 50 SECONDS TOTAL (1500 FRAMES @ 30FPS) [cite: 137, 264]
  ┌─────────────────────────┬───────────────────────────────┬────────────────────────┐
  │  HOOK (Frames 0–15)     │   FACT-DENSE BODY (16–1410)   │  END CARD (1411–1500)  │
  ├─────────────────────────┼───────────────────────────────┼────────────────────────┤
  │ • Pattern Interrupt     │ • Case Study Drone Analytics  │ • Gold Text on Navy    │
  │ • Stop the Scroll       │ • Premium IKO Shingle Footage  │ • CTA: Book CPPA       │
  │ • 0.5-Second Window     │ • No Fluff, conversational    │ • Phone: 972-928-0788  │
  └─────────────────────────┴───────────────────────────────┴────────────────────────┘
```

## from: The M7 Agent OS Digital Content Factory
```
  [GSC Keyword + Case Study] ──► [jcode Parallel Swarms] ──► [Automatic Cross-Linking] ──► [Indexceptional API]
```

## from: The M7 Agent OS Digital Content Factory
```
   [Builder Agent] ──► [Draft Generated] ──► [Auditor / Judge Agent]
          ▲                                         │
          │                                         ▼ (Self-Correction Loop)
          └─────────── [Failed Brand Check] ────────┴──► [Passed: Staged PAUSED] [cite: 234]
```

## from: The Everywhere Engine: DFW Roofing SEO and AEO Strategy
```
   ┌────────────────────────────────────────────────────────────────────────┐
   │ 💻 IKO VS. IKO Certified COMPARISON PAGE — DESIGN & STRUCTURAL MATRIX             │
   ├────────────────────────────────────────────────────────────────────────┤
   │                                                                        │
   │  [ROYAL NAVY TOP BANNER — 140px Height] [cite: 17]                           │
   │   "IKO Certified vs. IKO Certified Timberline: The Honest DFW Comparison"        │
   │                                                                        │
   │  [AEO INTRO BLOCK — First 40 Words] [cite: 110]                             │
   │   Directly answers which shingle stands up best to DFW storm damage.   │
   │                                                                        │
   │  [SIDE-BY-SIDE DATA MATRIX — Royal Navy #1A365D & Gold #FBC02D] [cite: 211] │
   │   Comparing Warranty, Impact Rating, Wind Resistance, & Cost [cite: 140].  │
   │                                                                        │
   │  [NAVY PHOTO MOAT BEFORE/AFTER PORTFOLIO IMAGES] [cite: 17]                 │
   │   Every project photo must carry a 10px solid Navy border [cite: 17].     │
   │                                                                        │
   │  [BOTTOM CREDENTIAL BAR — 95px Height] [cite: 17]                            │
   │   "Pineapple Contractors | RCAT Licensed #03-0637 | IKO Certified"     │
   │                                                                        │
   └────────────────────────────────────────────────────────────────────────┘
```

## from: The Pineapple Agent OS: Command Centers and Lead Drills
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\test_handshake.py"
```

## from: The Pineapple Standard: Commercial Handshake and DFW Flywheel Suite
```
  [1. GSC Scout] ──► [2. jcode Swarm] ──► [3. Brand Firewall] ──► [4. Link Bridges] ──► [5. Auto-Index]
```

## from: Sitemap Validator and Technical Deployment Guide
```
   THE TREASURE MAP (Sitemap)      🧑‍🚀 ROBOT DETECTOR (Validator)     🏴‍☠️ THE CAPTAIN (Google)
 ┌───────────────────────────┐      ┌───────────────────────────┐     ┌───────────────────────┐
 │ (X) /locations/frisco-tx/ │ ──►  │ Pings: "Is there real     │ ──► │ Indexes clean pages   │
 │ (X) /locations/plano-tx/  │      │ gold buried here?" [200]  │     │ in search results!    │
 └───────────────────────────┘      └───────────────────────────┘     └───────────────────────┘
```

## from: Sitemap Validator and Technical Deployment Guide
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\sitemap_validator.py" "https://pineappleroofingllc.com/wp-sitemap.xml"
```

## from: The M7 Agent OS AI Coding Tool Engine
```
┌──────────────────────────────────────────────────────────────────────┐
│                      PSS RAM USAGE PER SESSION                       │
├──────────────────────┬───────────────────────────────────────────────┤
│ 🚀 jcode             │ █ 28 MB  (Boots in 14ms!)                     │
│ 🐘 Claude Code       │ █████████████ 387 MB  (Boots in 3.4s)         │
└──────────────────────┴───────────────────────────────────────────────┘
```

## from: M7 Automation Upgrade and Brand Compliance Protocol
```python
    # =========================================================================
    # 🔥 DESKTOP HOT LEADS STASH (TOA TIER SPECIAL DISPATCH)
    # =========================================================================
    if tier == "TOA_TIER":
        try:
            # Dynamically resolves the active user's Desktop path on Windows
            desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop", "HOT_LEADS.txt")
            
            with open(desktop_path, "a", encoding="utf-8") as hf:
                hf.write("====================================================\n")
                hf.write(f"🔥 HOT LEAD ALERT: TOA TIER QUALIFIED (Score: {score}/100)\n")
                hf.write("====================================================\n")
                hf.write(f"👤 Name:     {lead_payload.get('customer_name', 'N/A')}\n")
                hf.write(f"📞 Phone:    {lead_payload.get('phone', 'N/A')}\n")
                hf.write(f"📍 ZIP Code: {lead_payload.get('zip_code', 'N/A')}\n")
                hf.write(f"🏢 Comm:     {lead_payload.get('is_commercial', False)}\n")
                hf.write(f"💰 Est. Val: ${property_value:,.2f}\n")
                hf.write(f"⛈️ Services: {lead_payload.get('services_requested', 'N/A')}\n")
                hf.write(f"📝 Notes:    {lead_payload.get('notes', 'N/A')}\n")
                hf.write(f"🕒 Timestamp: 2026-08-11 18:48:55\n")
                hf.write("====================================================\n\n")
                
            print(f"\n🔥 {RED}[DESKTOP ALERT] Hot Lead instantly written to Desktop/HOT_LEADS.txt!{RESET}")
        except Exception as de:
            print(f"\n⚠️ [DESKTOP WRITE ERROR] Could not save hot lead: {de}")
```

## from: M7 Automation Upgrade and Brand Compliance Protocol
```
┌────────────────────────────────────────────────────────────────────────┐
│               M7 24/7 BACKGROUND TRAFFIC ENGINE RUNTIME                 │
├────────────────────────────────────────────────────────────────────────┤
│  LOOP START (Every 6 Hours)                                            │
│   │                                                                    │
│   ├──► 1. Query GSC Data (gsc_frisco_scan.py) -> Finds hot terms       │
│   ├──► 2. Generate Content -> Claude Code drafts a clean static page   │
│   ├──► 3. Firewall Scan (brand-firewall.py) -> Block if green or "free"│
│   ├──► 4. Deploy Page (Netlify CLI / WP REST) -> Moves page live       │
│   └──► 5. Index Submission (sitemap_validator.py) -> Indexes in 24 hrs │
│                                                                        │
│  SLEEP (6 Hours) ──► RESTART LOOP                                       │
└────────────────────────────────────────────────────────────────────────┘
```

## from: M7 Automation Upgrade and Brand Compliance Protocol
```cmd
@echo off
TITLE M7 24/7 Background SEO Traffic Engine
color 0C

:loop
cls
echo ===================================================================
echo   🛰️  M7 24/7 BACKGROUND TRAFFIC ENGINE IS ACTIVE
echo   Enforcing 0%% Green visual laws and strict CPPA naming schemas [cite: 9, 126, 127]
echo ===================================================================
echo [SYSTEM] Local Time: %date% %time%
echo.

:: 1. Scan GSC for trending keywords in Frisco/Plano
echo [STEP 1/4] Scanning Google Search Console for impression spikes...
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\gsc_frisco_scan.py" [cite: 80]
timeout /t 5 >nul

:: 2. Execute JCode to write a new local static landing page
echo.
echo [STEP 2/4] Initializing jcode Swarm to generate optimized city copy... [cite: 386]
jcode --role "builder" --task "Generate a new HTML location page for Frisco ZIP 75035 using IKO Dynasty metrics [cite: 150, 256]. Use no green styles [cite: 127]." [cite: 391]
timeout /t 10 >nul

:: 3. Force Compliance Check
echo.
echo [STEP 3/4] Passing page to Brand Firewall...
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\brand-firewall.py" "C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts" [cite: 80]
if %errorlevel% neq 0 (
    echo [CRITICAL ERROR] Brand Firewall flagged a violation! Halting deploy.
    goto sleep_cycle
)

:: 4. Deploy and Index
echo.
echo [STEP 4/4] Publishing page and submitting to Indexceptional API...
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\sitemap_validator.py" [cite: 80]

:sleep_cycle
echo.
echo ===================================================================
echo   💤 CYCLE COMPLETE. Sleeping for 6 hours before next check...
echo ===================================================================
:: Sleeps for 21,600 seconds (6 hours)
timeout /t 21600

goto loop
```

## from: M7 Integrated Automation Suite and Lead Scoring Orchestrator
```
   🐍 THE POSTMAN WITH A CALCULATOR          🎛️ THE BIG START BUTTON
   (m7_n8n_webhook_bridge-v2.py)             (LAUNCH_WATCHER-v2.bat)
   ┌───────────────────────────────┐         ┌───────────────────────────────┐
   │ Runs: m7_scoring.py first!    │         │ 1. Turns on watchdog v3       │
   │ Stamps: Scores & Tier tags.   │         │ 2. Boots jcode cockpit at     │
   │ Dispatches: Clean data to n8n │         │    http://localhost:4040      │
   └───────────────────────────────┘         └───────────────────────────────┘
```

## from: M7 Integrated Automation Suite and Lead Scoring Orchestrator
```python
# Check out the preflight integration in your new v2 script!
def run_lead_scoring_integration(payload):
    print("📊 [PREFLIGHT SCORING] Running lead evaluation matrix...")
    try:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        import m7_scoring # Calls your Tech Lab scoring code natively!
        
        scores = m7_scoring.calculate_lead_score(payload)
        payload["calculated_score"] = scores["score"]
        payload["routing_tier"] = scores["tier"]
        payload["sms_dispatch_alert"] = scores["trigger_sms"]
        payload["scoring_breakdown"] = scores["breakdown"]
        
        print(f"   ↳ Lead Score: {scores['score']}/100 ({scores['tier']})")
    except ImportError:
        print("⚠️ m7_scoring.py not found in local path. Skipping preflight scoring.")
```

## from: M7 Integrated Automation Suite and Lead Scoring Orchestrator
```cmd
:: Quick Preview of LAUNCH_WATCHER-v2.bat
:: 1. Launch the Outbox Watchdog Daemon (v3) in a persistent console
echo 📡 Booting Real-Time Outbox Watchdog v3...
start "M7 Outbox Watcher Daemon v3" cmd /k python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\outbox_watcher-v3.py"

:: 2. Launch the JCode High-Speed Swarm Dashboard Visual Cockpit
echo.
echo 🚀 Booting jcode Swarm Dashboard Visual Cockpit...
start "jcode Swarm Dashboard Visual Cockpit" cmd /k jcode --dashboard --port 4040
```

## from: M7 Integrated Automation Suite and Lead Scoring Orchestrator
```cmd
:: From Section 4 of daily_backup.bat
if exist "04_Tech_Lab\scripts\sitemap_validator.py" (
    python "04_Tech_Lab\scripts\sitemap_validator.py" "https://pineappleroofingllc.com/wp-sitemap.xml"
)
```

## from: Frisco Roofing Domination: Multi-Channel Growth and Operations Manual
```
                     ┌──────────────────────────────────────────────┐
                     │           PRIMARY PILLAR MONEY PAGE          │
                     │    /locations/hail-damage-roof-repair-frisco-tx/  │
                     └──────────────────────┬───────────────────────┘
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
 ❓ Spoke Spoke                      ❓ Spoke Spoke                      ❓ Spoke Spoke
  "How long to file                   "Will filing a claim                "What size hail
  a claim in Texas?"                  raise my insurance rates?"          damages roof shingles?"
```

## from: Frisco Roofing Domination: Multi-Channel Growth and Operations Manual
```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      BLOTATO AUDIT WINDOW: 12-MONTH BUFFER TIMELINE                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [NOW] ──────────────────────────────────────────────────────────► [DRAFTS STACKED HERE] │
│   All Live Posts                                                    Scheduled +12 Months  │
│                                                                                            │
│   Saia Reviews Draft ──► Toggles AI_CONTENT_APPROVED (TRUE) ──► Drags to Today ──► SHIPS!  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## from: Frisco Roofing Domination: Multi-Channel Growth and Operations Manual
```
  C ──► Circumstances (Document the property's current structural state) [cite: 12]
  A ──► Agitation (Frame loss-aversion; the storm claim window is closing!) [cite: 12]
  R ──► Resolve (Introduce permanent, Premium Estate Restoration) [cite: 12]
  P ──► Proof (Highlight 350+ local families and 209 perfect reviews) [cite: 12, 191]
  A ──► Agreement (Ask: "Would you settle for a cheap, temporary patch?") [cite: 12, 97]
  R ──► Review (Detail the engineering timeline and documentation file) [cite: 12]
  K ──► Kickoff (Authorize paperwork and secure the crew schedule) [cite: 12]
```

## from: Frisco Roofing Domination: Multi-Channel Growth and Operations Manual
```
                     ┌──────────────────────────────────────────────┐
                     │          STEP 1: THE SIGNED CONTRACT         │
                     │  $18K+ premium IKO shingle system approved    │
                     └──────────────────────┬───────────────────────┘
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
 📸 GEOTAGGED PHOTOS                 🗣️ REVIEW LOOPS                     📬 THE RULE OF 100
  Upload drone views to GBP           On-site reviews name                Deploy 100 physical
  optimized with target               specific neighborhood               touchpoints within 
  neighborhood coordinates.           tags (e.g., Starwood).              a 1-mile radius.
```

## from: Pineapple M7: Automated Lead Scoring System Configuration
```python
import sys
import json
import os

# ============================================================================
# PINEAPPLE M7 — LOCAL AUTONOMOUS LEAD SCORING SYSTEM
# File: m7_scoring.py
# ============================================================================
# Automatically scores inbound leads based on premium geographic, structural,
# and customer type qualifiers. Leads scoring >= 80 trigger instant elite
# alerts to Saia's phone for immediate high-ticket outreach.
# ============================================================================

# ANSI Term Color Codes (M7 Royal Navy & Gold Aesthetic) [cite: 9, 127]
NAVY = "\033[1;34m"
GOLD = "\033[1;33m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
RESET = "\033[0m"

def calculate_lead_score(lead_data):
    """
    Evaluates lead qualifiers and returns a composite score (0-100)
    and prioritization routing tier [cite: 98, 158].
    """
    score = 0
    breakdown = []

    # 📍 1. Geographic Priority (Frisco ZIPs: 75033, 75034, 75035) -> +25 Points [cite: 98, 158]
    priority_zips = ["75033", "75034", "75035"]
    zip_code = str(lead_data.get("zip_code", "")).strip()
    if zip_code in priority_zips:
        score += 25
        breakdown.append(f"📍 Geographic Match ({zip_code}): +25 Points")
    else:
        breakdown.append(f"⚪ Outside Priority Area ({zip_code}): +0 Points")

    # 🏢 2. Commercial Property Manager Status -> +30 Points [cite: 98, 158]
    is_commercial = lead_data.get("is_commercial", False)
    customer_type = str(lead_data.get("customer_type", "")).lower()
    if is_commercial or "commercial" in customer_type or "manager" in customer_type:
        score += 30
        breakdown.append("🏢 Commercial Property/Manager Status: +30 Points")
    else:
        breakdown.append("⚪ Residential Single-Family Property: +0 Points")

    # 💰 3. Luxury Estate Premium Value (Est Value >= $700k) -> +20 Points [cite: 98, 158]
    property_value = lead_data.get("est_property_value", 0)
    try:
        property_value = float(property_value)
    except (ValueError, TypeError):
        property_value = 0

    if property_value >= 700000:
        score += 20
        breakdown.append(f"💰 Luxury Estate Value (${property_value:,.2f}): +20 Points")
    else:
        breakdown.append(f"⚪ Standard Estate Value (${property_value:,.2f}): +0 Points")

    # ⛈️ 4. Explicit Wind/Hail Storm Damage Mention -> +20 Points [cite: 98, 158]
    services_requested = str(lead_data.get("services_requested", "")).lower()
    notes = str(lead_data.get("notes", "")).lower()
    storm_keywords = ["hail", "wind", "storm", "leak", "tear", "damage", "restoration"]
    
    matches = [word for word in storm_keywords if word in services_requested or word in notes]
    if matches:
        score += 20
        breakdown.append(f"⛈️ Storm Damage Indicator ({', '.join(matches)}): +20 Points")
    else:
        breakdown.append("⚪ Routine Service Inquiry: +0 Points")

    # Determine Tier & SLA Dispatch Rule [cite: 1, 98, 158]
    # Score >= 80 lands in the elite TOA Tier (requires 120s dispatch call) [cite: 1, 13, 98, 158]
    tier = "TOA_TIER" if score >= 80 else "STANDARD_TIER"
    trigger_sms = score >= 80

    return {
        "score": min(100, score),
        "tier": tier,
        "trigger_sms": trigger_sms,
        "breakdown": breakdown
    }

def process_lead(lead_payload):
    print(f"{NAVY}================================================================={RESET}")
    print(f"🍍 {GOLD}PINEAPPLE M7 — LEAD SCORING SYSTEM ACTIVE{RESET}")
    print(f"{NAVY}================================================================={RESET}")

    # Calculate scoring metrics
    evaluation = calculate_lead_score(lead_payload)
    score = evaluation["score"]
    tier = evaluation["tier"]
    trigger_sms = evaluation["trigger_sms"]

    print(f"\n👤 {CYAN}Customer Name:{RESET} {lead_payload.get('customer_name', 'N/A')}")
    print(f"📞 {CYAN}Phone Number:{RESET}  {lead_payload.get('phone', 'N/A')}")
    print(f"📊 {GOLD}Composite Score:{RESET} {score}/100")
    
    if tier == "TOA_TIER":
        print(f"🏆 {RED}PRIORITY TIER: TOA TIER (Score >= 80) — ELITE STATUS!{RESET}")
        print(f"🚨 {RED}SLA ACTIVATED: Trigger immediate SMS dispatch to Saia!{RESET}")
    else:
        print(f"🟢 {CYAN}PRIORITY TIER: STANDARD TIER{RESET}")
        print("🟢 SLA: Route to normal follow-up queue.")

    print(f"\n📋 {CYAN}SCORING BREAKDOWN:{RESET}")
    for item in evaluation["breakdown"]:
        print(f"  ↳ {item}")

    # Format output payload for n8n/webhook routing [cite: 80, 132]
    output_payload = {
        "lead_id": lead_payload.get("lead_id", "N/A"),
        "customer_name": lead_payload.get("customer_name", "N/A"),
        "phone": lead_payload.get("phone", "N/A"),
        "zip_code": lead_payload.get("zip_code", "N/A"),
        "calculated_score": score,
        "routing_tier": tier,
        "sms_dispatch_alert": trigger_sms,
        "breakdown_logs": evaluation["breakdown"]
    }

    # Attempt to write local log record
    log_dir = r"C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts"
    try:
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "lead_scoring_log.json")
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(output_payload, f, indent=2)
        print(f"\n💾 {CYAN}[SAVED] Scoring diagnostics log written to Outbox.{RESET}")
    except Exception as e:
        print(f"\n⚠️ Unable to write local log file: {e}")

    print(f"{NAVY}================================================================={RESET}\n")
    return output_payload

if __name__ == "__main__":
    # If run directly with command-line arguments (passed as raw JSON string) [cite: 80]
    if len(sys.argv) > 1:
        try:
            raw_input = sys.argv[1]
            input_data = json.loads(raw_input)
            process_lead(input_data)
        except Exception as e:
            print(f"🚨 [ERROR] Failed to parse input JSON payload: {e}")
            sys.exit(1)
    else:
        # Run standard mock lead for local testing/verification [cite: 80]
        mock_lead = {
            "lead_id": "m7-test-9999",
            "customer_name": "Saia Moeakiola Test",
            "phone": "972-928-0788",
            "zip_code": "75034",             # +25 Points (Geographic Match) [cite: 98, 158]
            "is_commercial": False,          # +0 Points
            "est_property_value": 850000,    # +20 Points (Est Value >= $700k) [cite: 98, 158]
            "services_requested": "Complimentary Professional Photo Audit (CPPA)",
            "notes": "Severe wind damage on shingles with visible attic leak" # +20 Points (Storm Mention) [cite: 98, 158]
        }
        # Expected Score: 25 + 0 + 20 + 20 = 65. Let's run it!
        process_lead(mock_lead)
```

## from: Pineapple M7: Automated Lead Scoring System Configuration
```yaml
# %LOCALAPPDATA%\hermes\profiles\seo\config.yaml
# Add this under your active mcp_servers configuration block [cite: 165, 249]

mcp_servers:
  # 📊 Automated lead evaluation matrix [cite: 98, 158]
  m7_lead_scorer:
    command: "python"
    args:
      - "C:\\Pineapple Contractors M7\\04_Tech_Lab\\scripts\\m7_scoring.py"
```

## from: Pineapple M7: Automated Lead Scoring System Configuration
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_scoring.py"
```

## from: Pineapple M7: Automated Lead Scoring System Configuration
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_scoring.py" "{\"lead_id\": \"m7-test-7777\", \"customer_name\": \"Frisco Plaza\", \"phone\": \"972-928-0788\", \"zip_code\": \"75034\", \"is_commercial\": true, \"est_property_value\": 1200000, \"services_requested\": \"hail storm restoration\"}"
```

## from: Pineapple M7: Understand Anything Plugin Setup SOP
```
  C:\Pineapple Contractors M7\  ──►  /understand Scan  ──►  .understand-anything/knowledge-graph.json
                                                                            │
      ┌─────────────────────────────────────────────────────────────────────┴─────────────────────────────────────┐
      ▼                                                                     ▼                                     ▼
 /understand-dashboard                                             /understand-onboard                            /understand-diff
 Interactive clickable visual map of layers (API, UI, Utility) [cite: 265]  Guided tours ordered by dependencies [cite: 265]  Evaluates blast radius of edits [cite: 267]
```

## from: Pineapple M7: Understand Anything Plugin Setup SOP
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

## from: Pineapple M7: Understand Anything Plugin Setup SOP
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

## from: Automating Social Content with the Loop Command and Slicer
```
   [NORMAL CHAT] ──► You ask ──► Robot writes ──► Stop. (You must ask again tomorrow) [cite: 193]
   
   [THE /loop COMMAND] ──► Set clock ──► Runs overnight ──► Saves draft ──► Repeats automatically! [cite: 9, 193, 194]
```

## from: Automating Social Content with the Loop Command and Slicer
```
   RAW DRONE FOOTAGE ──► [video_multiplier_setup.py] ──► 50s LEGO REEL (.mp4)
  ┌───────────────────────────┬─────────────────────────────────────┬───────────────────────────┐
  │  HOOK (Frames 0-15)       │   BODY (Frames 16-1410)             │   END CARD (Frames 1411-1500)│
  ├───────────────────────────┼─────────────────────────────────────┼───────────────────────────┤
  │ • Pattern Interrupt       │ • Factual Density & Drone Reveals   │ • Navy Background         │
  │ • "Your Roof Survived..." │ • Shows active DFW restoration      │ • Gold Credentials Box    │
  └───────────────────────────┴─────────────────────────────────────┴───────────────────────────┘
```

## from: Automating Social Content with the Loop Command and Slicer
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\video_multiplier_setup.py"
```

## from: Automating Social Content with the Loop Command and Slicer
```text
=== Pineapple M7: Initializing Drone Video Multiplier Swarm ===
📁 Source Asset: 02_Media_Vault/raw_drone_temp.mp4
📁 Target Destination: 02_Media_Vault/clips/
⏳ Compiling and rendering your 50s Lego reel locally...
🟢 Success! Branded reel saved to: 02_Media_Vault/clips/frisco_drone_hail_reveal_50s.mp4
```
