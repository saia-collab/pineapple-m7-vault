---
source: "NotebookLM - Master SOP 8/26"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: c37da178-accd-4342-b78e-bfb57f82e9b1
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW free?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# The M7 Agent OS AI Coding Tool Engine

### 🛠️ THE AI CODING TOOL ENGINE: CLAUDE CODE, JCODE, & THE LOCAL SWARMS

In your local **M7 Agent OS**, your AI coding tools are not just smart chatbots—they are **fully autonomous terminal agents** that can read your files, write code, run commands, and test themselves until a task is completed [cite: 11, 392]. 

If we look at your local vault (`C:\Pineapple Contractors M7`) [cite: 203], you have access to a suite of elite developer utilities [cite: 191, 386]. Here is the ultimate operational guide to your AI coding stack, explained simply so you know exactly which "digital builder" to dispatch [cite: 188, 231].

---

### 🥊 1. THE HEAVYWEIGHT CLASH: CLAUDE CODE VS. jcode

```
┌──────────────────────────────────────────────────────────────────────┐
│                      PSS RAM USAGE PER SESSION                       │
├──────────────────────┬───────────────────────────────────────────────┤
│ 🚀 jcode             │ █ 28 MB  (Boots in 14ms!)                     │
│ 🐘 Claude Code       │ █████████████ 387 MB  (Boots in 3.4s)         │
└──────────────────────┴───────────────────────────────────────────────┘
``` [cite: 386, 387, 393]

#### 🐘 Claude Code: The Executive Architect
*   **What it is:** The official terminal developer CLI built directly by Anthropic [cite: 50, 392].
*   **What it does best:** Complex planning, structural edits, writing brand check scripts, and running advanced "dynamic workflows" [cite: 231, 309].
*   **The Blueprint Metaphor:** Claude Code is like your **Master Architect** [cite: 59]. It is incredibly smart but carries a lot of weight [cite: 63, 390]. A single session eats **~387MB of RAM** and takes **3.4 seconds to boot** [cite: 386]. If you try to run ten Claude Code agents at once to work on different files, your computer's fans will start spinning like a jet engine (**2.3GB of RAM** used) [cite: 388, 390].
*   **When to use it:** Use it for the **heavy, high-stakes structural decisions**—like connecting your local databases, managing Git repositories, and writing major operational scripts [cite: 189, 231].

#### 🚀 jcode: The High-Speed Swarm Coder
*   **What it is:** A lightweight, open-source (MIT licensed) coding agent written in **Rust** [cite: 386, 392]. It uses the exact same Claude subscription you already pay for but wraps it in a race-car body [cite: 386, 392, 397].
*   **What it does best:** Running lightning-fast parallel coding swarms [cite: 391, 395].
*   **The Blueprint Metaphor:** jcode is your **Elite Bricklaying Crew** [cite: 59, 391]. It boots in a blistering **14 milliseconds** (245x faster than Claude Code) and idles at only **~28MB of RAM** [cite: 386, 387, 393]. You can run **ten jcode sessions at once for only 117MB of RAM** [cite: 391]! 
*   **Two Killer Features:**
    1.  **The Memory Graph:** It automatically converts past conversations into semantic vectors [cite: 394]. It recalls what you did last session naturally, without burning your monthly API tokens on long recap summaries [cite: 394].
    2.  **Swarm Mode:** If you open multiple jcode agents in your repo, they talk to each other [cite: 395, 406]. If Agent A edits a file that Agent B has open, Agent B instantly gets a notification and reads the code diff, preventing them from overwriting each other's work [cite: 395, 406].
*   **When to use it:** Use it for **everyday volume coding**, generating interactive calculators, and running multi-agent swarms [cite: 236, 391].

---

### 🔌 2. THE META-BUILDERS & VISUALIZERS

Your coding agents get even stronger when you equip them with these specialized plugin "backpacks" [cite: 20, 372]:

#### 🔨 skill-forge: The Tool Maker
*   **What it is:** A meta-tool created by Agrici Daniel [cite: 20]. It is literally **an AI skill that builds other AI skills** [cite: 21].
*   **What it does:** It scaffolds the complex manifest files, command inputs, error handle patterns, and directory rules that Claude Code expects when installing a new command [cite: 23, 24].
*   **When to use it:** Whenever you think, *"I wish there was a custom command to automate this boring, repetitive task."* [cite: 26] Instead of taking hours copy-pasting code folders, you run `/skill-forge` and have a working, custom skill built in 5 minutes [cite: 22, 24].

#### 🗺️ Understand Anything: The Code Map
*   **What it is:** A visual codebase inspector plugin (`Egonex-AI/Understand-Anything`) [cite: 372].
*   **What it does:** Running `/understand` scans your entire folder, maps class/function dependencies, and outputs a **clickable, color-coded interactive knowledge graph** of your codebase [cite: 372].
*   **When to use it:** Use it when onboarding onto a large, messy, or undocumented folder [cite: 374]. It tells your agents exactly where the "entry points" are and alerts you to the "blast radius" (the files that will break) before you commit code changes [cite: 372, 374].

---

### 💳 3. THE TOKEN SAVING FORMULA: CODING FOR \$0

Running continuous loops on paid enterprise models can exhaust your API limits quickly [cite: 17, 308]. Your system is hardcoded to bypass this using **Free Claude Code (FCC)** [cite: 191]:

1.  **The Switchboard (fcc-server):** Running on local port `127.0.0.1:3737/admin` [cite: 191], this proxy intercepts developer requests and routes them away from expensive models [cite: 191].
2.  **Deploy Free Coder Models:** Point your configurations to **`open_router/qwen/qwen3-coder:free`** (a frontier-level open-source coder) [cite: 193] or run **`ollama/gemma2`** completely offline on your own machine's graphics card for **unlimited, free coding runs** [cite: 193, 195].
3.  **Context Compaction (`/compact`):** When coding sessions get long, type `/compact` [cite: 63, 64]. The agent will summarize the current progress into a 5-line handoff note, execute a `/clear` command to wipe the bloated memory log, and paste the handoff note back in [cite: 64]—**cutting your token usage by up to 80% to 95%** [cite: 21, 64, 85].

---


📂 **Next Step Suggestion:**  
I can prepare a custom local configuration template to install **`Understand Anything`** inside your active **`config.yaml`** so your workspace is ready to visualize page dependencies automatically [cite: 372]. Would you like me to map out this plugin installation prompt? [cite: 372]