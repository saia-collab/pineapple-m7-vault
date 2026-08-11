---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: bd9c68fd-fac7-4144-8450-6ac96e75cdaa
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# The Hermes AI Agent Operational Manual

### 🛰️ THE OPERATIONAL MANUAL FOR THE HERMES AI AGENT

The **Hermes AI Agent** (originally released by Nous Research under the open-source MIT license) is one of the most powerful sovereign agent frameworks [cite: 141, 160]. Unlike standard chatbots that trap you in a single tab and start every session from zero [cite: 161, 326], Hermes functions as a true **"Compound Employee"** designed to live locally on your computer, integrate with your business systems, and execute complex workflows autonomously [cite: 141, 161, 345].

Behind Hermes’ capability is a three-layer architecture [cite: 362]: **The Brain** (swappable cloud or local models) [cite: 365, 367], **The Cockpit** (your visual dashboard on `localhost:3000` or `:3737`) [cite: 266, 365], and **The Memory** (your private Obsidian vault) [cite: 168, 365].

---

### 🧠 1. THE FIVE PILLARS OF HERMES CAPABILITIES

#### 🎯 Pillar A: Goal Mode & Autonomous Execution [cite: 85]
Instead of prompting Hermes step-by-step [cite: 383], you toggle **Goal Mode** and give it a single finished outcome [cite: 177, 429]. Hermes then autonomously plans the tasks, writes code, drafts content, and runs background loops until the objective is fully met [cite: 85, 177].
*   **Smart Approvals & Guardrails:** Hermes is designed with custom fence permissions [cite: 163]. If a task is risky (such as deleting files or processing ad payments), it stops and requests a human **"smart approval"** before proceeding [cite: 79, 127, 330].
*   **Self-Healing Recovery:** If your local machine crashes or the power cuts out mid-task, Hermes will automatically clean up the environment and resume the job exactly where it left off [cite: 86].

#### 🧹 Pillar B: The Curator (The Built-In Janitor) [cite: 143]
When agents execute long-term tasks, they often generate loose files, duplicate skills, and bloated memory logs [cite: 142]. This context inflation slows down the agent and spikes your API bills [cite: 142]. 
*   **Automatic Maintenance:** Every 7 days, a background agent called **The Curator** wakes up, reviews your entire local skill library, and prunes unused tools or merges redundant prompts [cite: 143, 144]. This keeps your local Agent OS running fast and cost-effective [cite: 142, 143].

#### 🌐 Pillar C: The One-Script Engine (Unified Browser Use) [cite: 401, 407]
Before recent updates, browser-use agents had to make separate API calls for every micro-action (navigate, click, scroll, scrape), resulting in high latency and expensive token fees [cite: 403, 404].
*   **Unifying Browser Tasks:** Powered by the **Browser Use CLI 3.0** backend, the **One-Script Engine** writes a single consolidated script to execute the entire browsing task upfront [cite: 401, 405, 410]. This achieves the exact same execution accuracy while cutting your API token expenses by **48% to 66%** [cite: 401, 406].

#### 🎙️ Pillar D: Hands-Free Control ("Hey Hermes" Wake Word) [cite: 185]
Hermes includes native, local-first voice activation [cite: 185, 186].
*   **Local Processing:** Using lightweight, on-device ONNX engines like **openWakeWord** or **sherpa**, the listener runs entirely offline and never sends ambient home audio to the cloud [cite: 187, 188].
*   **Profile Voice Routing:** If you have multiple custom profiles configured, you can assign different wake-words to them [cite: 189]. Saying *"Hey Hermes"* boots your standard operations persona [cite: 189], while saying *"Hey coder"* instantly switches your local dashboard to your terminal development profile [cite: 189, 190].

#### 🔌 Pillar E: Gateway, Buzz, & MCP Integrations [cite: 132, 134, 178]
You can extend the reach of your local command desk to control your systems on the go [cite: 136, 178]:
*   **The 19-Channel Gateway:** Hermes connects directly to 19 chat surfaces, including **Telegram, iMessage, and WhatsApp** [cite: 146, 148, 163]. You can send a voice note to your agent while out in the field; Hermes transcribes the audio, logs the details to your Obsidian vault, and replies in your own cloned text-to-speech voice [cite: 124, 179].
*   **Buzz Integration:** Hermes natively bridges into **Buzz** (the AI-powered, Slack-style workspace) [cite: 132, 134]. It can join channels, answer your team's direct messages, and execute scheduled tasks with its local second-brain context fully intact [cite: 132, 138].

---

### 📂 2. HOW THE SHARED MEMORY MATRIX COMPUNDS [cite: 337]

The secret to running Hermes successfully inside your local **M7 Agent OS** is ensuring that **all your AI tools share one single source of truth** [cite: 168, 337, 342]. 

If your AI agents start every session from blank chat boxes, they will continually hallucinate and repeat the same mistakes [cite: 159, 337]. By hooking your local system to your **Obsidian vault (`03_Knowledge_Mat`)** [cite: 168, 281], memory is compiled bidirectionally [cite: 342, 343]:

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
``` [cite: 167, 168, 281, 337]

Every time you give Hermes feedback (e.g., *"replace 'free' with 'CPPA' and use Navy `#1A365D` styling"*), Hermes saves that correction directly back to `SHARED_MEMORY.md` [cite: 111, 126, 170]. The next morning, when you boot up your dashboard, **every agent in the room—including Claude Code and your Kimi swarms—instantly inherits the new rules** [cite: 198, 328, 337].

---

### 🛠️ 3. ESSENTIAL HERMES CLI SHEET FOR QUICK CHECKS [cite: 17, 149]

When driving your agent from your terminal, execute these rapid command utilities:

*   **Update Hermes:**  
    `hermes update` [cite: 149]
*   **Test Model Connection:**  
    `hermes model` [cite: 150]
*   **Run a One-Shot Task:**  
    `hermes -z "Check 01_Command_Center/Outbox_Drafts/ for any instances of the word 'free'"` [cite: 158, 246]
*   **Trigger a Skill Learn Command:**  
    `/learn 03_Knowledge_Mat/00_Atlas/SOP_M7_Everywhere_Flywheel_and_Rhythms.md` [cite: 145, 170]
*   **Force a Curator Skill Clean:**  
    `hermes curator run --force` [cite: 142]
*   **Check Wake-Word Hardware Diagnostics:**  
    `/wake status` [cite: 193]

---


📂 **Next Step Suggestion:**  
I can write a custom **`M7_TEST_VOICE.bat`** file to quickly run a local diagnostic test on your microphone, ensuring your speech-to-text engines and wake-word listeners are armed and ready on your machine [cite: 185, 187, 258]. Would you like me to output this script code?