
| User Prompt: |
|-------------|
| help me write SOP ti built with into my Pineapple Contractors M7 Playbbok , Build a Hermes AI Student Companion & Mission Control Dashboard , i want use notebook as study guide and build seo and marketing content and much more into my dashboard |

Here is a structured **Standard Operating Procedure (SOP)** designed to integrate the **Hermes AI Student Companion & Mission Control Dashboard** into your **Pineapple Contractors M7 Playbook**. 

This SOP outlines how to deploy the core architecture and extend it specifically for your goals: using notebooks as study guides, and building automated SEO and marketing content pipelines.

---

# Standard Operating Procedure: Hermes AI Mission Control Deployment & Extension
**Document ID:** SOP-M7-HERMES-001  
**Category:** Pineapple Contractors M7 Playbook – AI Infrastructure  
**Objective:** Deploy a 6-agent private VPS ecosystem and expand it to handle automated Study Guides, SEO Generation, and Marketing Workflows.

---

## Phase 1: Infrastructure & Core Agent Provisioning

### 1. VPS Environment Setup
Deploy a clean Linux VPS (Ubuntu 22.04+) and ensure the Hermes Environment is mapped securely.
*   **Target Port:** `51763` (Bound strictly to `127.0.0.1` for privacy).
*   **Core Dependencies:** FastAPI, Uvicorn, Aiofiles, Python-Multipart, SQLite3.

### 2. The Core Multi-Agent Matrix
Provision the base agents into `/root/.hermes/profiles/` and establish their system personas (`SOUL.md`):

*   **Bill (The Coordinator):** The central routing layer. Listens on Telegram. Routes tasks to specialists and reports completion. *Rule: Bill never generates content; he only orchestrates.*
*   **Vault (The Librarian):** Manages file organization in `/home/hermes/subjects/`. Tracks ingestion, logs metadata, and maps file inventories without analyzing core content.
*   **Scholar (The Analyst):** Performs full, non-summarized markdown extractions of academic texts, PDFs, and documentation.
*   **Quizmaster (The Evaluator):** Interrogates Scholar's data to generate targeted evaluation mechanics.
*   **Planner (The Logistics Engine):** Coordinates project schedules, content calendars, deadlines, and milestones.
*   **Dev (The Architect):** Builds and maintains the physical glassmorphism dashboard, pipeline wiring, and logging mechanisms.

---

## Phase 2: Playbook Extensions (Notebooks, SEO, & Marketing)

To align this build with your specific goals, inject the following expanded blueprints into **Scholar**, **Quizmaster**, and **Planner**.

### 1. The Study Guide & Notebook Pipeline
Modify **Scholar's** persona to handle comprehensive Notebook generation. When a textbook, document, or research dump hits the Vault, Scholar executes:
*   **Structural Parsing:** Reorganizes data into a dedicated Study Guide format under `/home/hermes/subjects/[subject]/notebooks/`.
*   **Formula & Concept Mapping:** Ensures definitions, mental models, and edge cases are preserved completely rather than compressed.
*   **Interactive Hand-off:** Automatically flags **Quizmaster** to prepare structured validation material tied to the newly generated notebook.

### 2. Automated SEO & Web Research Engine
Update **Scholar’s** specialized capabilities to run deep-dive web analyses via keyless search backends:
```markdown
Capability Update: Research & SEO Synthesis
- Task: Investigate competitor keywords, semantic gaps, and high-intent industry topics.
- Storage: Output comprehensive findings to /home/hermes/research/seo_[topic].md.
- Required Schema: 
  1. SERP Analysis & Search Intent Mapping
  2. Targeted Keyword Clusters (Short-tail & LSI)
  3. Structural Heading Outlines (H1-H4) for optimized copy
  4. Authoritative Web References
```

### 3. The Marketing Content Pipeline
Train **Quizmaster** to pivot from standard student quizzes into a **Marketing Copy Generator**, using **Scholar’s** SEO research notebooks as the context source.
*   **The Blueprint:** Command Quizmaster to compile marketing snippets.
*   **Output Format:** Instead of standard Q&A, format the decks using the strict three-dash (`---`) separator to generate mobile-friendly, swipeable snippet decks in the dashboard:
    *   *Card 1:* High-hook Social Media copy (X / LinkedIn format).
    *   *Card 2:* Meta descriptions and programmatic SEO intros.
    *   *Card 3:* Ad creative copy angles.

---

## Phase 3: Dashboard Assembly & UI Wiring

Using the visual source of truth from [Komputer Mechanic](https://komputermechanic.com/tutorials/hermes-student-companion), have **Dev** spin up the custom UI pages inside your centralized Mission Control interface:

### 1. Core Workspaces
*   **Overview Screen:** Features custom-built inline SVG radial gauge blocks tracking agent workloads, alongside an hourly activity heatmap driven entirely by the SQLite database (`~/.hermes/agent-logs.db`).
*   **Library (Notebooks & Lecture Notes):** An interactive reading panel powered by Mozilla’s `PDF.js` viewer, wired with a debounced autosave script to let you highlight and annotate assets directly in-browser.

### 2. Marketing & SEO Workspaces
*   **Research Command Center:** A submission terminal where you type an SEO topic or target keyword. Scholar executes the scrape, updates a live loading spinner via polling, and displays the fully rendered Markdown report alongside a **"Generate Marketing Deck"** call-to-action button.
*   **Practice/Swipe Panel:** Reconfigured to preview your marketing and copywriting snippets in a clean, card-based interface with native keyboard navigation (Left/Right arrow keys) for rapid messaging review.

---

## Phase 4: Operational Management & Maintenance

### 1. Security Protocol
*   **Access Control:** The dashboard must never be exposed to the public internet. Access is restricted exclusively via an SSH Tunnel or a private [Tailscale](https://tailscale.com) mesh network.
*   **Service Reliability:** Run the FastAPI application as a systemd background service configured to auto-start on boot.

### 2. Backup & Iteration Control
Implement a dual-script backup utility managed by **Dev**:
1.  `backup_dashboard.sh`: Snapshots your functional dashboard source files, increments a local version tracking number, and pushes it to an isolated backup directory.
2.  `restore_dashboard.sh`: Instantly rolls back your production dashboard files to a designated stable version and hot-restarts the systemd daemon if an agent extension breaks the UI state.

---

> ### 🛠️ Playbook Execution Note
> When deploying these components sequentially through your **Dev** agent, always execute one layout step at a time. Ensure the local SQLite tracking schema passes its diagnostic smoke test before connecting live automated triggers to your Discord channels or Telegram brief routines.


| User Prompt: |
|-------------|
| include this SOP to How to Build a PREMIUM Hermes Agent Mission Control Dashboard, i will be asking claude or hermes to built the coding of this compare to the one ive one and obsidian, also should i download the dashboard template to help the coding |

Here is the updated, integrated SOP designed to graft your custom **Study Guide, NotebookLM integration, and SEO/Marketing Engine** directly into the **Pineapple Contractors M7 Playbook**. It bridges the gaps between the original [Premium Hermes Mission Control Dashboard](https://komputermechanic.com/tutorials/hermes-dashboard) architecture, your local **Obsidian Vault layout**, and your flagship coding agents (like Claude Code or Dev).

---

# Standard Operating Procedure: Pineapple M7 Hermes Mission Control Deployment & Extension
**Document ID:** SOP-M7-HERMES-002  
**Category:** Pineapple Contractors M7 Playbook – AI Infrastructure  
**Objective:** Deploy the 6-agent private VPS ecosystem, bind it to your local Obsidian Vault ecosystem, and establish pipelines for Study Guides, SEO Generation, and Marketing Workflows.

---

## Phase 1: Infrastructure & Core Agent Provisioning

### 1. VPS Environment Setup
Deploy a clean Linux VPS (Ubuntu 22.04+) and ensure the Hermes Environment is mapped securely.
*   **Target Port:** `51763` (Bound strictly to `127.0.0.1` for privacy, accessed over an SSH tunnel or a private [Tailscale](https://tailscale.com) mesh network).
*   **Core Dependencies:** FastAPI, Uvicorn, Aiofiles, Python-Multipart, SQLite3.

### 2. The Core Multi-Agent Matrix
Provision the base agents into `/root/.hermes/profiles/` and establish their system personas (`SOUL.md`):

*   **Bill (The Coordinator):** The central routing layer. Listens on Telegram. Routes tasks to specialists and reports completion. *Rule: Bill never generates content; he only orchestrates.*
*   **Vault (The Librarian):** Manages file organization in `/home/hermes/subjects/`. Tracks ingestion, logs metadata, and maps file inventories without analyzing core content.
*   **Scholar (The Analyst):** Performs full, non-summarized markdown extractions of academic texts, PDFs, and documentation.
*   **Quizmaster (The Evaluator):** Interrogates Scholar's data to generate targeted evaluation mechanics.
*   **Planner (The Logistics Engine):** Coordinates project schedules, content calendars, deadlines, and milestones.
*   **Dev (The Architect):** Builds and maintains the physical glassmorphism dashboard, pipeline wiring, and logging mechanisms.

---

## Phase 2: Obsidian Vault & Local Filesystem Bridge

To align the dashboard with your existing configuration, configure **Dev** to wire a bidirectional link between the VPS file structure and your local system:

*   **The Directory Mapping:** Map `/home/hermes/subjects/` (on the VPS) directly to your local computer's Obsidian path at `C:\Pineapple Contractors M7\`.
*   **The Sync Layer:** Use a background utility like **Syncthing** or the **Obsidian REST API** plugin over port `27123` to mirror files instantly. 
*   **The Layout Requirement:** When an agent writes a markdown file on the server, it must seamlessly land inside your local `01_Command_Center/Outbox_Drafts/` or `05_Campaign_Factory/10_Research_Stage/` folders in Obsidian.

---

## Phase 3: Playbook Extensions (Notebooks, SEO, & Marketing)

Inject these specialized workflows into the core agent logic to execute your unique asset production goals:

### 1. The Study Guide & Notebook Pipeline
Modify **Scholar's** persona to handle comprehensive Notebook and Study Guide generation. When a textbook, document, or research dump hits the Vault, Scholar executes:
*   **Structural Parsing:** Reorganizes data into a dedicated Study Guide format under `/home/hermes/subjects/[subject]/notebooks/`.
*   **Formula & Concept Mapping:** Ensures definitions, mental models, and edge cases are preserved completely rather than compressed.
*   **Interactive Hand-off:** Automatically flags **Quizmaster** to prepare structured validation material tied to the newly generated notebook.

### 2. Automated SEO & Web Research Engine
Update **Scholar’s** specialized capabilities to run deep-dive web analyses via keyless search backends:
```markdown
Capability Update: Research & SEO Synthesis
- Task: Investigate competitor keywords, semantic gaps, and high-intent industry topics.
- Storage: Output comprehensive findings to /home/hermes/research/seo_[topic].md.
- Required Schema: 
  1. SERP Analysis & Search Intent Mapping
  2. Targeted Keyword Clusters (Short-tail & LSI)
  3. Structural Heading Outlines (H1-H4) for optimized copy
  4. Authoritative Web References
```

### 3. The Marketing Content Pipeline
Train **Quizmaster** to pivot from standard student quizzes into a **Marketing Copy Generator**, using **Scholar’s** SEO research notebooks as the context source.
*   **The Blueprint:** Command Quizmaster to compile marketing snippets.
*   **Output Format:** Instead of standard Q&A, format the decks using the strict three-dash (`---`) separator to generate mobile-friendly, swipeable snippet decks in the dashboard:
    *   *Card 1:* High-hook Social Media copy (X / LinkedIn format).
    *   *Card 2:* Meta descriptions and programmatic SEO intros.
    *   *Card 3:* Ad creative copy angles.

---

## Phase 4: Dashboard Assembly & UI Wiring

Using the visual source of truth from [Komputer Mechanic](https://komputermechanic.com/tutorials/hermes-student-companion), have **Dev** spin up the custom UI pages inside your centralized Mission Control interface:

### 1. Core Workspaces
*   **Overview Screen:** Features custom-built inline SVG radial gauge blocks tracking agent workloads, alongside an hourly activity heatmap driven entirely by the SQLite database (`~/.hermes/agent-logs.db`).
*   **Library (Notebooks & Lecture Notes):** An interactive reading panel powered by Mozilla’s `PDF.js` viewer, wired with a debounced autosave script to let you highlight and annotate assets directly in-browser.

### 2. Marketing & SEO Workspaces
*   **Research Command Center:** A submission terminal where you type an SEO topic or target keyword. Scholar executes the scrape, updates a live loading spinner via polling, and displays the fully rendered Markdown report alongside a **"Generate Marketing Deck"** call-to-action button.
*   **Practice/Swipe Panel:** Reconfigured to preview your marketing and copywriting snippets in a clean, card-based interface with native keyboard navigation (Left/Right arrow keys) for rapid messaging review.

---

## Phase 5: Operational Management & Maintenance

### 1. Security Protocol
*   **Access Control:** The dashboard must never be exposed to the public internet. Access is restricted exclusively via an SSH Tunnel or a private Tailscale mesh network.
*   **Service Reliability:** Run the FastAPI application as a systemd background service configured to auto-start on boot.

### 2. Backup & Iteration Control
Implement a dual-script backup utility managed by **Dev**:
1.  `backup_dashboard.sh`: Snapshots your functional dashboard source files, increments a local version tracking number, and pushes it to an isolated backup directory.
2.  `restore_dashboard.sh`: Instantly rolls back your production dashboard files to a designated stable version and hot-restarts the systemd daemon if an agent extension breaks the UI state.

---

## 💡 Developer Advice: Should You Download the Dashboard Template?

> **Yes, absolutely download the dashboard template.**

When you hand this setup to **Claude Code** or **Dev** to build out your custom server, the `index.html` template serves as the **visual source of truth**. Without it, an AI coding agent will generate generic, ugly HTML tables and unstyled text blocks. 

Providing the template ensures your new SEO room, marketing swipe tools, and notebooks keep that premium, dark glassmorphism styling seamlessly.

### How to use it with Claude:
1. Download the template `.html` file from the [Komputer Mechanic](https://komputermechanic.com/tutorials/hermes-student-companion) portal.
2. Drop it directly into your dashboard build folder on the VPS (e.g., `/root/dashboard/templates/reference.html`).
3. When prompting Claude Code, specify: 
   > *"Review `reference.html` for layout structure, CSS classes, and glassmorphism styling variables. Replicate this exact visual language as you code the custom endpoints for my Pineapple M7 SEO Room and Notebook interface."*


| User Prompt: |
|-------------|
| take a look at this current one that was built , it sure need to be updated , this dashboard only works with hermes and cant really do anything on it |

Looking at your active **Pineapple M7 Agent OS Command Center**, you’ve got a phenomenal layout scaffolded, but it’s essentially acting as a static "read-only" window for external apps like Google’s *NotebookLM* or locked *Higgsfield* frameworks. It lacks the deep, automated backend loops needed to make your local Obsidian vault (`C:\Pineapple Contractors M7`) talk directly to an active agent execution matrix.

We can completely rewrite this architecture by taking the dark glassmorphic design language of your current dashboard and embedding the active multi-agent pipeline from the **PREMIUM Hermes Agent Mission Control Dashboard**. This transforms a passive monitoring board into a fully functional, self-driving operation.

Below is the Master SOP to hand directly to **Claude Code** or your **Dev** agent to refactor your current setup into a high-powered operational powerhouse.

---

# 🍍 SOP: Refactoring Pineapple M7 into a Premium Hermes Command Engine

**Document ID:** SOP-M7-REFIT-003  
**Category:** Pineapple Contractors M7 Playbook – Core OS Update  
**Objective:** Replace static iframe placeholders with active FastAPI-backed workspaces for local Notebook processing, automated SEO keyword targeting, and continuous marketing swipe-file generation.

---

## Phase 1: Preserving the Visual Source of Truth

> ### 🛑 Crucial Developer Step: Do Not Code From Scratch
> You absolutely should **download the dashboard template** from the [How to Build a PREMIUM Hermes Agent Mission Control Dashboard](https://komputermechanic.com/tutorials/hermes-dashboard) tutorial page. 
> 
> Even though your current `M7_COMMAND_CENTER.html` looks great, downloading the canonical `mission-control-template.html` gives **Claude Code** the exact, functional Tailwind/Alpine.js reactive hooks, canvas rendering arrays, and SSE (Server-Sent Events) components needed to bind real data to your UI cards.

### How to execute the handoff to Claude Code:
1. Save the downloaded template file as `premium_reference.html` inside your directory.
2. Take a screenshot of your existing visual palette to preserve your custom branding.
3. Command your **Dev** agent: 
   > *"Analyze our current `M7_COMMAND_CENTER.html` for branding metrics, then use the functional logic, tab structures, and canvas charts from `premium_reference.html` to rewrite our active application backend."*

---

## Phase 2: Upgrading the Core Agent Matrix (6-Agent Ecosystem)

Your current Fleet view lists placeholders. We will explicitly spin up these profiles in `/root/.hermes/profiles/` and define their tasks:

*   **Bill (The Telegram Orchestrator):** Operates via a dedicated Telegram bot. Coordinates file inputs and directs the specialist pipelines.
*   **Vault (The Obsidian Librarian):** Uses the **Obsidian REST API** over port `27123` to index new text files, PDFs, or storm research dumps dropping into `05_Campaign_Factory/10_Research_Stage/`.
*   **Scholar (The Content & Notebook Machine):** Pulls files from Vault. Instead of standard summaries, it extracts total markdown structures to build local, searchable **Study Guides** and deep competitor web-scrapes.
*   **Quizmaster (The Marketing Pipeline Factory):** Reads Scholar’s research outputs and automatically spins out targeted copy clusters (Hooks, Meta Descriptions, Ad Angles) using a `---` three-dash break system.
*   **Planner (The Cron Executor):** Maps campaign calendars, deadlines, and automatically pushes morning operational briefings back to your Telegram.
*   **Dev (The Systems Engineer):** Monitors the SQLite system state (`~/.hermes/agent-logs.db`), runs hot-fixes, and handles code repairs.

---

## Phase 3: Rewiring the Static Workspaces to Live Engines

### 1. The "Studio / NotebookLM Bay" Upgrade
Your current layout has an iframe pointing to Google Accounts which is hitting a redirect wall. We will turn this entire card into a local **Notebook Research Room**:
*   **The Backend Hook:** Dev will drop the `PDF.js` library directly into your server stack.
*   **The Functionality:** Clicking a file loads it natively inside the dashboard. Highlighting text or typing an engine directive fires an instant command through **Scholar** to parse it without relying on external Google structures.

### 2. The "SEO Room & Rank Machine" Automation Loop
Currently, your SEO cluster is displayed as static text metrics. We will inject an interactive input field backed by **Scholar's Web Search Engine**:
```markdown
Capability Inject: /api/seo/research
- Input: Target Keyword + Geo Region (e.g., "Frisco Hail Damage Repair")
- Action: Scholar leverages keyless DuckDuckGo/Brave backends to scrape search intents.
- Output: Automatically writes a complete optimization blueprint directly into your local Obsidian folder at `05_Campaign_Factory/10_Research_Stage/`.
```

### 3. The "Creative Studios" Swipe Card Interface
Convert the static code prompt copy buttons into a live **Marketing Sandbox**:
*   When **Quizmaster** transforms an SEO brief into social media copy, it splits the data strings cleanly by line-breaks.
*   The dashboard UI reads this data as an interactive flashcard deck. You can preview, edit, and click **"Approve to Outbox"** using native keyboard arrows, routing completed assets straight into your `01_Command_Center/Outbox_Drafts/` folder.

---

## Phase 4: Setting Up the Live Data & Safety Infrastructure

### 1. Active Event Streaming (SSE)
Your current page requires manual refreshes. Claude Code will configure a standard-library Python thread pool in `server.py` to stream continuous updates over an `/events` endpoint:
*   Your **Agentic Modes** and **Idea Factory** columns will instantly shift, pulse, or display loading spinners the exact moment an agent updates `~/.hermes/agent-logs.db`.

### 2. The Version Control Insurance Policy
Because you are shifting from a static page to a highly active, multi-agent operating system, implement a dual-script guardrail managed by **Dev**:
1.  `backup_m7.sh`: Instantly snapshots your functional dashboard html, scripts, and databases right before you give Claude Code a major modification prompt.
2.  `roll_back_m7.sh`: Flips the workspace back to your prior working state if an agent loop stalls or breaks your Alpine component mapping.

---

> ### 🚀 Next Step
> Drop the [Premium Dashboard Template](https://komputermechanic.com/tutorials/hermes-dashboard) into your directory, clear out your static Google iframes, and command **Claude Code**: 
> *"Using `premium_reference.html` as your blueprint, build the FastAPI server to handle live file processing for our `C:\Pineapple Contractors M7` workspace."*


| User Prompt: |
|-------------|
| what is the easy way of making sure that no human involement for human error |

To achieve a true **"Zero Human Error"** environment where your multi-agent system runs autonomously without manual mistakes or broken interfaces, you need to implement **Automated System-to-System Protocols**.

Instead of trying to remember the right buttons to click or copying text manually, the easiest way to prevent human error is to remove human actions from the equation entirely. Here is how to lock that down in your Pineapple M7 architecture:

---

## 1. Eliminate Manual Copy-Pasting (The Obsidian REST API)
Right now, you are risking error by manually moving text between your browser, your scripts, and your notes. Since your dashboard shows you have the **Obsidian REST API** connector loaded on port `27123`, use it to fully automate file drops.
*   **The Error-Proof Setup:** Program **Scholar** and **Quizmaster** to talk directly to your local computer's Obsidian port. 
*   **How it works:** When Scholar finishes a deep SEO research brief on the server, it uses a standard `POST` request to send the markdown content straight into your `05_Campaign_Factory/10_Research_Stage/` folder. You never have to manually download, copy, drag, or drop a file again.

## 2. Replace Manual Refreshes with Live Event Streaming (SSE)
Looking at your current dashboard, the broken Google Accounts iframes require you to click around or manually reload the page to check if something updated, which can break agent sessions if timed incorrectly.
*   **The Error-Proof Setup:** Use Server-Sent Events (SSE). 
*   **How it works:** Your FastAPI backend monitors the local SQLite database (`~/.hermes/agent-logs.db`). The moment an agent completes a task, the backend beams that data to your dashboard instantly. The UI components update natively in real time. You will never crash a running loop by prematurely refreshing the browser.

## 3. Implement Strict Token/Credit Gate Guards
Human error often manifests as accidentally running a massive research script that burns through your AI token limits or platform credits. Your current UI lists a manual check for *Higgsfield credits*, but relying on your memory to check it is a risk.
*   **The Error-Proof Setup:** Program your gatekeeper agent (**Firewall** or **Bill**) to handle pre-execution cost verification programmatically.
*   **How it works:** Before **Scholar** or **Higgsfield** runs a heavy video creation or crawling job, a script checks your current balance. If the action exceeds a predefined cap (e.g., more than $5 in a single run), the system pauses the loop and sends a crisp **"Approve / Deny"** button directly to your Telegram or Discord channel.

## 4. Run "Outbox Shield" Validation Scripts
If an agent generates marketing copy with a typo, an incorrect phone number (like mistyping your `972-928-0788` line), or a broken link, publishing it directly creates issues.
*   **The Error-Proof Setup:** Build an automated filter layer called the **Outbox Shield**.
*   **How it works:** Before any generated asset moves to the "Shipped Gallery" or gets staged for social media, the markdown content is forced through a programmatic text-checker script (`brand_firewall.py`). This script scans the text for banned phrases, checks regex matching for your exact phone number, and confirms valid compliance tags. If a rule fails, it rejects the file back to the agent for auto-repair before you ever lay eyes on it.

---

### 💡 The Core Rule for your AI Coding Agent
When you hand your files to **Claude Code** to program this ecosystem, give it this exact rule to keep human error at absolute zero:
> *"Design this multi-agent backend using strict automated file paths and system hooks. Do not rely on human input fields for file placement, directory configurations, or text transport. If an agent produces an asset, it must map programmatically to its final destination via API endpoints."*


| User Prompt: |
|-------------|
| base on this give me the promt and markdown to have the ai agent built it |

Based on your active dashboard layout and the canonical template structure, your current dashboard contains mostly broken iframes and static text components. 

To completely refactor your configuration into a zero-human-error engine, you need to hand **Claude Code** or your **Dev** agent a master blueprint. This combines the premium design system from [How to Build a PREMIUM Hermes Agent Mission Control Dashboard](https://komputermechanic.com/tutorials/hermes-dashboard) with the active file parsing code from the [Hermes AI Student Companion](https://komputermechanic.com/tutorials/hermes-student-companion) setup, entirely customized for your **Pineapple Contractors M7** local Obsidian vault.

Here is the exact prompt and markdown payload to hand directly to your AI builder agent.

---

## The Master AI Agent Prompt

```markdown
Act as an expert Full-Stack Systems Engineer and Agent Architect. Our goal is to completely refactor our current static dashboard (`M7_COMMAND_CENTER.html`) into a fully functional, automated FastAPI-backed Agent OS. 

We must implement zero-human-error automation protocols that entirely eliminate manual file downloading, copy-pasting, and page refreshing.

### 🛑 DESIGN CRITERIA & TEMPLATE ALIGNMENT
1. Review the canonical `mission-control-template.html` for functional Tailwind CSS, Alpine.js hooks, canvas arrays, and SSE component wiring.
2. Maintain our signature dark glassmorphic palette: Background (#15151F), glass panels (rgba(31,31,43,0.55)), with accents in strict identity colors:
   - Bill (Orchestrator): #A78BFA (Violet)
   - Vault (Obsidian Librarian): #60a5fa (Blue)
   - Scholar (Notebook & SEO Specialist): #14b8a6 (Teal)
   - Quizmaster (Marketing Factory): #a855f7 (Purple)
   - Planner (Cron Engine): #f59e0b (Amber)
   - Dev (Systems Engineer): #f43f5e (Pink)

### ⚙️ BACKEND WORKSPACE WIREUP (`server.py`)
Scaffold a standard-library Python ThreadingHTTPServer/FastAPI pipeline running on port 51763 (localhost only) that implements the following automated workflows:

1. THE SYSTEM-TO-SYSTEM SYNC (Obsidian REST API Link)
   - Wire a bidirectional connector between the VPS backend filesystem and our local Windows environment path: `C:\Pineapple Contractors M7\`.
   - Use the Obsidian REST API on port 27123. When an agent updates or writes an output asset, it must push a programmatic POST request directly into our local vault folders, completely bypassing manual file handling.

2. LOCAL NOTEBOOK BAY (Replacing Broken Google Accounts Iframes)
   - Drop the `PDF.js` reading script directly into our static folder mount.
   - Build a document viewer card that loads local notebooks natively.
   - Set up an automated extraction handoff: Highlighting text or passing a query from this workspace instructs Scholar to parse and expand the context without using any external Google structures.

3. PROGRAMMATIC SEO ROOM & SEARCH MACHINE
   - Convert the current static text blocks into an active keyword research bay.
   - Input: Target Keyword + Geo Region (e.g., "Frisco Hail Damage Repair").
   - Action: Scholar calls a keyless web scraping backend (DuckDuckGo/Brave) to compile semantic keyword maps, search intent clusters, and structural content outlines.
   - Automated Output: Writes a structured markdown summary directly into `05_Campaign_Factory/10_Research_Stage/` over the Obsidian REST port.

4. MARKETING CAMPAIGN & SWIPE COMPILER
   - Train Quizmaster to read Scholar's compiled SEO blueprints and instantly format high-hook marketing copy variations.
   - The agent must output content blocks divided by a strict three-dash (`---`) separator.
   - Reconfigure the dashboard practice panel to parse these strings into a swipeable flashcard component. Include native keyboard arrow-key listeners so we can visually audit, edit, and click an "Approve to Outbox" button, dispatching text straight into `01_Command_Center/Outbox_Drafts/`.

5. FAULT-SHIELD GATEWAY (Zero-Error Verification)
   - Stream live updates continuously from `~/.hermes/agent-logs.db` over a local Server-Sent Events (`/events`) framework so columns shift and display loading states instantly without browser refreshes.
   - Integrate a `brand_firewall.py` check inside our implementation column. Before any agent asset moves past human approval, verify phone metrics (`972-928-0788`), compliance guidelines, and token costs programmatically. If any validation fails, reject the script back to the agent for auto-repair.

Execute this refactor step-by-step. Prioritize robust error catching (`try/except`) on all system hooks so a failure in one workspace loop never stalls the core dashboard server state.
```

---

## 🛠️ Execution Instructions for You

1. **Get the Reference Template:** Download the `mission-control-template.html` source file directly from the [Komputer Mechanic Master Guide](https://komputermechanic.com/tutorials/hermes-dashboard) page and drop it into your workspace folder as `premium_reference.html`.
2. **Back Up Your Current File:** Run a manual snapshot copy of your current `M7_COMMAND_CENTER.html` first so you have an immediate safety rollback point.
3. **Initialize Claude Code / Dev:** Open your terminal window inside your project root, boot up your coding agent, and paste the exact markdown block above to kick off the programmatic refactoring loop.


| User Prompt: |
|-------------|
| do i download both How to Build a PREMIUM Hermes Agent Mission Control Dashboard and Build a Hermes AI Student Companion & Mission Control Dashboard and build ai ai job hunting or something particulare to my Business |

No, you do not need to build the job-hunting system or create separate dashboards. Since you already have your own company layout, you are going to take the code logic from those tutorials and **build something entirely tailored to your business: Pineapple Contractors M7.**

Here is exactly how to combine those two tutorials to upgrade your existing workspace into a high-powered, zero-human-error business engine:

---

## The Strategic Blueprint for Your Business

Do not split your focus across multiple templates. You are going to use the **PREMIUM Hermes Agent Mission Control Dashboard** as your core visual framework, but you will swap out its generic features for the **Student Companion & Notebook** mechanics alongside your custom **SEO and Marketing pipelines**.

Here is how the tutorials map to your actual business functions:

| Tutorial Feature | How it Translates to Pineapple Contractors M7 |
| :--- | :--- |
| **The Student Companion** *(From Tutorial 02)* | This becomes your **Local Notebook & Document Bay**. Instead of studying school subjects, this engine processes heavy contract files, roofing estimators, property damage reports, and materials documentation. |
| **The 6-Agent Matrix** *(From Tutorial 03)* | These agents stop running generic tasks and instead run your **5-Column Self-Driving Pipeline** (Idea Input $\rightarrow$ Agent Planning $\rightarrow$ Human Approval $\rightarrow$ Implementation $\rightarrow$ Shipped Gallery). |
| **The Content Library** *(From Tutorial 03)* | This becomes your **SEO & Marketing Factory Room**, completely hooked into your local Obsidian Vault via the REST API over port `27123`. |

---

## 📥 Which Template Do You Download?

You only need to download **one** file:

1. Go to the [How to Build a PREMIUM Hermes Agent Mission Control Dashboard](https://komputermechanic.com/tutorials/hermes-dashboard) page that you have open in your background tabs.
2. Click the **[Download dashboard template]** button. 
3. Save that template file directly into your local directory as `premium_reference.html`.

### Why this file?
This file contains the canonical, bulletproof Tailwind CSS and Alpine.js reactive hooks. When you hand this file to **Claude Code**, it ensures your new active workspaces look premium and operate smoothly without broken elements.

---

## 🚀 How to Instruct Your AI Agent (Claude Code / Dev)

Once you have downloaded the template, open your coding environment inside your vault folder (`C:\Pineapple Contractors M7`) and pass this exact structural instruction to your AI builder:

```markdown
We are completely refactoring our static file `M7_COMMAND_CENTER.html`. 

We are NOT building a generic student app or a job hunter. We are building the custom "Pineapple Contractors M7 Agent OS Command Center".

Use the functional code architecture from `premium_reference.html` to build a live FastAPI backend running locally on port 51763, customized with these exact business spaces:

1. THE NOTEBOOK BAY: Replaces the broken Google Accounts iframes. Use local script parsing so we can read roofing manuals, hail damage scopes, and business files natively without relying on external Google servers.
2. THE SEO MACHINE: Turn the static SEO Room grid into an interactive input field. When we type an industry topic (e.g., "Frisco Hail Damage Repair"), have Scholar crawl search engines and drop a structured keyword map straight into our local Obsidian folder: `05_Campaign_Factory/10_Research_Stage/`.
3. THE OUTBOX SHIELD: Wire our 5-Column Kanban Board directly to a live SQLite database. Ensure that any marketing campaign or social copy generated by Quizmaster lands in the "Human Approval (PAUSED)" column, running an automatic verification check on our brand assets and phone number (972-928-0788) before any content can be moved to "Shipped".

Preserve our custom branding, agent lists, and color themes while replacing all static mockups with real, live system actions.
```
