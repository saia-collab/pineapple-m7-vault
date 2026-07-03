### Master SOP: Building the 6-Agent Hermes Student Companion & Mission Control Dashboard

#### 1\. System Architecture Overview

The Hermes Student Companion is a decentralized multi-agent system engineered to automate the academic lifecycle—from raw document ingestion to interactive assessment and long-term retention. The system is built upon the  **7-Layer Blueprint** , ensuring a modular, "local-first" operating environment that eliminates vendor lock-in.

##### The 7-Layer Structural Basis

1. **Layer I: Foundation:**  The infrastructure layer, comprising a Linux VPS and the Hermes development environment.  
2. **Layer II: Memory:**  Persistent context stored in Markdown (Obsidian/Vault), ensuring agent continuity across sessions.  
3. **Layer III: Brain:**  Large Language Models (LLMs). This build utilizes  **GPT-5.5 via the OpenAI Codex provider**  to leverage existing subscriptions.  
4. **Layer IV: Agents:**  Specialized personas (Bill, Vault, Scholar, Quizmaster, Planner, Dev) with distinct operating parameters.  
5. **Layer V: Command:**  The Mission Control dashboard, serving as the centralized "Single Pane of Glass."  
6. **Layer VI: Production:**  Functional surfaces, including the PDF.js reader, Research Workspace, and Quiz Center.  
7. **Layer VII: Loop:**  The feedback flywheel, where all agent outputs are written back to Layer II to compound system intelligence.

##### Messaging Distribution

The fleet is distributed across Telegram (for coordination) and Discord (for execution/specialization) to ensure operational isolation.| Agent | Platform | Primary Role || \------ | \------ | \------ || **Bill** | Telegram | System Coordinator, Pipeline Narrator, & Router || **Vault** | Discord | File Librarian & Inventory Logger || **Scholar** | Discord | Markdown Extractor & Research Specialist || **Quizmaster** | Discord | Assessment & Flashcard Generator || **Planner** | Discord | Academic Schedule & Deadline Strategist || **Dev** | Discord | Backend Architect & Dashboard Engineer |

#### 2\. Prerequisites and Infrastructure Deployment

##### Hardware and Environment Specifications

* **Linux VPS:**  Root access on  **Ubuntu 22.04+**  (Recommended: Contabo or RackNerd).  
* **Hermes Agent venv:**  The environment must be initialized at /usr/local/lib/hermes-agent/venv.  
* **Web Search:**  DuckDuckGo/Brave backend (No search API keys required).

##### API and Token Checklist

Configure the following in your \~/.hermes/.env file:

*   **TELEGRAM\_BOT\_TOKEN:**  Generated via @BotFather.  
*   **TELEGRAM\_CHAT\_ID:**  Numeric ID via @userinfobot to restrict access to the administrator.  
*   **DISCORD\_BOT\_TOKEN:**  From the Discord Developer Portal (Enable all Gateway Intents).  
*   **OPENAI\_CODEX:**  Authenticated session to utilize a standard ChatGPT subscription for agent inference.

#### 3\. Phase 1: Establishing the Specialist Agent Personas

##### Agent Identity and "Souls"

Each agent is provisioned with a specific soul.md file located in \~/.hermes/profiles/.

* **Bill (The Coordinator):**  The primary Telegram interface. Bill provides "narrative updates" on pipeline status and routes user intent to specialized sub-agents.  
* **Vault (The Librarian):**  Manages secure file storage. He logs every PDF upload into a subject.md inventory and maintains the file system integrity.  
* **Scholar (The Specialist):**  Extends from Markdown extraction to web-based research. He converts complex PDFs into structured notes and gathers external academic data.  
* **Quizmaster (The Assessor):**  Analyzes Scholar’s notes to generate interactive quizzes and swipe-through flashcard decks in parseable JSON/Markdown formats.  
* **Planner (The Strategist):**  Scans documents for deadlines, exams, and lecture times to populate the timetable.  
* **Dev (The Engineer):**  The dashboard architect. Dev is responsible for scanning the design template as the "Source of Truth" to generate code iteratively.

##### Operating Rules and Shared Team Awareness

To prevent task overstepping, use a  **Natural Language Routing Table** . Agents are configured with "Shared Awareness" protocols—every agent understands the capabilities of their peers (e.g., Quizmaster knows Scholar provides the input text). Use the AGENT\_LOG\_DB environment variable to ensure all agents log to the shared system database.

#### 4\. Phase 2: Messaging Integration and Channel Binding

##### CLI-Driven Integration

Instead of manual GUI configuration, use the Hermes CLI for robust initialization:

1. **Initialize Setup:**  Run hermes setup in the terminal.  
2. **Provider Selection:**  Choose Discord and enter the  **Discord Bot Token** .  
3. **Channel Provisioning:**  Use hermes channel create to generate channels for \#vault, \#scholar, \#quizmaster, \#planner, and \#dev.

##### Strict Isolation Binding

To lock agents to specific channels:

1. Capture the  **Channel ID**  for each Discord channel.  
2. Map the Agent ID to the Channel ID within the agent's profile config or via the hermes bind AgentName ChannelID command.  
3. This ensures that messages in \#scholar only trigger the Scholar agent, preventing cross-agent interference.

#### 5\. Phase 3: Building the Agent Logging and Activity System

##### Shared SQLite Framework

The system utilizes a central SQLite database. Ensure the AGENT\_LOG\_DB environment variable points to the global system log file. Every agent must execute a logging script upon task completion:

* **Schema:**  Name, Task, Model (GPT-5.5), Status (Success/Fail), Timestamp.  
* **Dashboard Feed:**  This database powers the live activity cards and success gauges.

##### Maintenance and Performance

To maintain VPS performance, implement a cron job executing the  **Maintenance Protocol** :

* Flush all log entries older than  **30 days** .  
* Verify database integrity weekly to prevent corruption during high-concurrency agent swarms.

#### 6\. Phase 4: Mission Control Dashboard Development

##### FastAPI Backend Scaffolding

The  **Dev Agent**  must scaffold a FastAPI application running on  **port 51763** .

* **Architecture:**  The dashboard serves a single-page application (SPA). Use FastAPI.staticfiles to mount the /assets directory.  
* **Static Serving:**  Dev must serve index.html as a static file through a StaticFiles mount point.  
* **Execution:**  Run via uvicorn main:app \--host 127.0.0.1 \--port 51763\.

##### Iterative Build Protocol

Dev must scan the provided  **Glassmorphism Design Template**  as the visual source of truth before generating any UI components.

* **Versioning:**  Before every code injection to index.html, Dev is required to save a copy in the /backups directory (e.g., index\_v1.2.html).  
* **Visual Integrity:**  All components must adhere to the semi-transparent, dark-mode aesthetic defined in the design truth.

#### 7\. Phase 5: Dashboard Tab Layouts and Functionality

The dashboard is partitioned into nine specialized production surfaces:

* **Overview:**  Hero section, mission stats strip, agent activity heatmap, and a 30-day activity trend chart.  
* **Agents Page:**  Live agent cards with glowing status indicators, success gauges, and model usage stats.  
* **Chat Workspace:**  In-browser messaging interface mirrored to Discord and Telegram in real-time.  
* **Library/Notes:**  A rendered Markdown viewer displaying Scholar’s extracted study notes, organized by subject.  
* **Lecture Notes (PDF.js):**  An integrated PDF.js reader that allows for inline document viewing and the saving of annotations back to the vault.  
* **Upload → Pipeline:**  Drag-and-drop entry point for PDF injection that triggers the automated multi-agent chain.  
* **Research Workspace:**  Scholar’s web-research interface for gathering external academic data with hand-off to Quizmaster.  
* **Quiz Center:**  Interactive quiz player with instant feedback, practice history, and score tracking.  
* **Planner (Schedule):**  Read-only view of today’s classes, weekly timetable, and exam dates.  
* **Tasks & Focus:**  A dedicated workspace featuring a  **Kanban board**  for task triage and a  **Pomodoro focus timer**  with sticky notes.

#### 8\. Phase 6: The Document Pipeline Workflow

##### The Core Chain Reaction

The Student Companion executes an automated sequence upon any document upload:

1. **Ingestion:**  User drops a PDF into the dashboard "Upload" zone.  
2. **Coordination:**   **Bill**  receives the file and initiates the narrative on Telegram.  
3. **Storage:**   **Vault**  moves the PDF to the correct subject directory and updates the inventory log.  
4. **Extraction:**   **Scholar**  reads the PDF and generates structured Markdown notes.  
5. **Assessment:**   **Quizmaster**  parses the Markdown notes to generate a practice quiz and flashcard deck.  
6. **Scheduling:**   **Planner**  extracts dates (deadlines/exams) and injects them into the Planner calendar.

##### Real-Time Transparency

Bill provides  **narrative Telegram updates**  at every transition (e.g.,  *"Vault has secured the file; Scholar is now extracting lecture notes..."* ).

#### 9\. Phase 7: Secure Access and Automation

##### Secure Remote Access

The dashboard is private by design. Do not expose port 51763 to the public web.

* **Tailscale:**  Install Tailscale on the VPS and client machine. Access the dashboard via the Tailnet IP.  
* **SSH Tunneling:**  For manual access, use: ssh \-L 51763:localhost:51763 root@VPS\_IP.

##### Morning Brief Automation

Configure a cron job to trigger Bill’s "Morning Brief" via Telegram at 08:00 AM daily.

* **Payload:**  A summary of today's classes, imminent deadlines, and local weather data.

#### 10\. System Validation and Quality Control

##### Final End-to-End Test Checklist

The system is considered "Live" only when these 5 outcomes are verified in a single pipeline run:

1.   **Bill Orchestration:**  Telegram notifications confirmed at every stage of the pipeline.  
2.   **Markdown Production:**  Structured notes for the new subject appear in the Library.  
3.   **Assessment Integrity:**  A practice quiz generated from the PDF is playable in the Quiz Center.  
4.   **Visual Accuracy:**  The dashboard reflects the Glassmorphism design and displays the new data.  
5.   **Activity Logged:**  The Agents page shows a 100% success rate for the specific pipeline run.

