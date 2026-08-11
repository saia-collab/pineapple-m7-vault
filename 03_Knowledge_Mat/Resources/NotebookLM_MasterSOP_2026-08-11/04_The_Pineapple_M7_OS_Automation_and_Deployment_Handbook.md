---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 0616af45-82d3-4451-bbdb-e5b45c97de28
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# The Pineapple M7 OS Automation and Deployment Handbook

Building directly on our established system design and local **Pineapple M7 Agent OS** configurations, here is your comprehensive, zero-error guide to setting up the Friday pipeline automation, prompting design gauntlets, and deploying your static Everywhere Engine sites to Netlify [cite: 924].

---

## 📅 1. AUTOMATING THE FRIDAY PIPELINE UPDATE IN HERMES

By running this routine, your local machine will autonomously query your self-hosted CRM, generate a strategic financial matrix using your **`main` profile**, and write that analysis directly back into the CRM as an internal note—completely bypassing third-party cloud aggregators and recurring licensing costs [cite: 840, 843, 844].

### Step 1: Create the Ingestion & Proxy Script
Create a shell script on your local computer at this exact path [cite: 919]:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\fetch_leadstack_pipeline.sh` [cite: 915, 919]

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
``` [cite: 888, 919]

### Step 2: Configure the Auto-Post Script
Append this section to the script to automatically post the generated markdown summary back into the CRM deal notes for your project managers [cite: 843, 844]:

```bash
#!/bin/bash
# Safe-pack the markdown report and POST to local CRM API
REPORT_BODY=$(cat /workspace/scratch/pipeline_recaps/weekly_report.md | jq -s -R .)
curl -s -X POST "http://localhost:8080/api/v1/deals/notes" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer LocalKey_M7_Prod" \
  -d "{\"note_type\": \"internal_audit\", \"body\": $REPORT_BODY}"
``` [cite: 919]

### Step 3: Set Up the Friday 5:00 PM Cron Job
To run this script automatically without human error or manual terminal entry [cite: 846]:
1. Open your terminal and access your system cron scheduler [cite: 920]:
   ```bash
   crontab -e
   ```
2. Paste this absolute path crontab entry [cite: 920]:
   ```cron
   0 17 * * 5 /bin/bash "C:\\Pineapple Contractors M7\\04_Tech_Lab\\scripts\\fetch_leadstack_pipeline.sh" >> "C:\\Pineapple Contractors M7\\04_Tech_Lab\\logs\\pipeline_sync.log" 2>&1
   ``` [cite: 915, 920]

Your OS is now self-reporting [cite: 848]. Every Friday at 5:00 PM, the system will wake up, compile your pipelines, and write a secure, compliant update to your records [cite: 848].

---

## 🧠 2. THE THREE-SENTENCE DESIGN GAUNTLET LOOP PROMPT

The **Gauntlet Loop (Infinite Critic Engine)** replaces manual back-and-forth review with a self-healing, multi-agent evaluation hierarchy [cite: 44, 49]. Instead of reviewing every rough draft yourself, you set the standard once, let the AI run checks recursively, and only look at the finished asset after it has survived multiple rounds of rejection [cite: 62, 72].

### The Core Prompt Template
Copy and paste this exact prompt structure into **Claude Code** or your **AI Agent Mastermind** tab [cite: 641, 885]:

> **TASK:** Build me [State exactly what you are building, e.g., a Frisco storm restoration landing page] matching the visual styles and guidelines in the attached benchmark file [Attach your reference screenshot / text guide] [cite: 70].
> 
> **METHOD:** Fan out specialized subagents to construct each component (design, layout, and copy), and pass their drafts behind a blind wall to a harsh auditor agent that judges only the rendered screenshots [cite: 51, 70].
> 
> **BAR:** Do not stop until every blind critic is utterly wowed compared to my reference, returning a perfect 10/10 compliance score [cite: 52, 71].

### The Strict Non-Negotiable Rules of the Gauntlet:
*   **The Power of the Benchmark:** "Make it look amazing" is not a checkable metric [cite: 68]. If you do not attach a high-quality visual reference or text guide up front, the critics will drift and begin agreeing with the builder, generating bad layouts [cite: 68, 71].
*   **Set a Hard Cap:** AI has unlimited stamina and will grade its own work recursively forever [cite: 54, 67]. Always set a hard limit (e.g., `/loop max 10 rounds`) so you can step in as the final human gatekeeper [cite: 62, 67].
*   **Enforce the M7 Brand Law:** Add these strict criteria to the prompt so the auditor agent instantly flags violations [cite: 940]:
    *   **Palette:** Headings must be **Royal Navy (`#1A365D`)** and calls-to-action **Pineapple Gold (`#FBC02D`)** [cite: 940]. Strictly **NO GREEN** colors allowed [cite: 940].
    *   **Lexicon:** Force the regex compliance check to replace banned terms: never say "free inspection" (use **CPPA**), never say "\$0 down" (use **Full Restoration Coverage**), and never say "IKO Certified" (use **IKO Certified**) [cite: 874].
    *   **Staging:** Ensure all code outputs land **PAUSED** inside `01_Command_Center/Outbox_Drafts/` [cite: 126, 884].

---

## 🚀 3. HOW TO DEPLOY A FIVE-SITE FLYWHEEL TO NETLIFY

To bypass the slow, bloated management overhead of standard WordPress databases and plugins, deploy the **five-site Everywhere Engine** as high-speed static builds on Netlify [cite: 605, 606]. 

```
[1 Keyword + 1 Case Study] ──> [Hermes Writer Profile] ──> [Eleventy (11ty) Static Build] ──> [Netlify Deploy API] ──> [Google Indexing webhook]
``` [cite: 603, 605, 607]

### Step-by-Step Deployment Workflow:

### Phase 1: Initialize Your Static Sites Locally
1. Initialize your project folders inside your root workspace using **Eleventy (11ty)**, which acts as a lightweight static site generator [cite: 605]:
   ```bash
   cd "C:\\Pineapple Contractors M7\\02_Workspaces"
   mkdir everywhere-flywheel && cd everywhere-flywheel
   npm init -y && npm install @11ty/eleventy --save-dev
   ``` [cite: 605, 915]
2. Scaffolding your directory: Build five subfolders (`site1`, `site2`, `site3`, `site4`, `site5`), keeping them cleanly segregated to prevent **context contamination** [cite: 602, 888].

### Phase 2: Connect Netlify CLI and Authorize Your Agents
To let your autonomous coding agents (Codex or Claude Code) publish updates in the background without you having to log in manually [cite: 704]:
1. Install the Netlify command-line utility globally:
   ```bash
   npm install netlify-cli -g
   ```
2. Log in and link your local workspace directory to your Netlify billing account [cite: 704]:
   ```bash
   netlify login
   ```
   *(A browser window will pop up asking for your authorization. Your API access token will save locally under `~/.config/netlify`.)* [cite: 294]

### Phase 3: Trigger the Content & Auto-Deploy Prompt
When you have a new keyword and a local case study ready to publish, switch to your **`seo` profile** in Hermes Chat and run this goal mode command [cite: 885, 888]:

```text
Load the seo profile. Read HERMES_PLAYBOOK.md and our local case study at 03_Knowledge_Mat/active_context/case_study_571k_plumbing.md. 

For our target keyword [KEYWORD]:
1. Generate 5 unique, highly citable articles with different angles and titles under 60 characters. First sentence must be AEO direct-answer compliant (<40 words).
2. Write these as separate index.md files into our local 11ty workspaces (site1 through site5). Ensure each page includes our IKO, RCAT #03-0637 licensing, and FAQ schemas mapping ZIPs 75033, 75034, and 75035.
3. Execute the Eleventy build command: "npx @11ty/eleventy" for each site.
4. Run the Netlify deployment command: "netlify deploy --dir=_site --prod" to push all five sites live in parallel.
5. Save the live URL outputs and trigger the Google Indexing API script to ensure same-hour indexing.
``` [cite: 604, 607, 608, 885]

Your AI agent will write the static pages, compile the static build, deploy them to production Netlify nodes under your custom domains, and ping Google crawlers—**all from one single, plain-English command** [cite: 604, 704, 1115].

---


📂 **Next Step Suggestion:**  
We can write a custom gatekeeper script (`netlify_gate.py`) to run a mandatory brand firewall check over your Eleventy builds *before* the Netlify CLI commands are triggered. This ensures that a green hex code or "free" reference can never accidentally go live on your custom domains. Would you like me to map out this pre-deployment check?