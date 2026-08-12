---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: c1f73e37-04f8-4e8b-a441-cca587e22e34
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW free?,green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# Hermes OS: Voice Control and Autonomous Agent Workflows

### 🎙️ 1. Swapping Between Hermes Profiles Using Voice Commands

Inside your local studio build, swapping between profiles is completely hands-free and handled on-device using the **Sherpa** open-vocabulary voice engine [1]. 

Instead of typing in your terminal or clicking through tabs in your command center, **your microphone acts as a voice-addressable team router** [2]. The Sherpa engine is configured with a micro-vocabulary that assigns a unique spoken wake word to each independent directory profile inside `~/.hermes/profiles/` [2]:

*   **"Hey Hermes"** → Wakes your **Default Profile** (configured via `localhost:20128` to run free keyword research and storm-tracking models) [2].
*   **"Hey Coder"** → Wakes your **Coder Profile** (Sol, configured to run local write-run-fix scripting loops and Python automation) [2].
*   **"Hey Oracle"** → Wakes your **Oracle Profile** (configured via GPT-5.6 Sol or Luna for high-conversion brand copy and competitor watch sweeps) [2].

#### How the Hot-Swap Loop Executes:
1.  **The Always-On Listener:** A lightweight, local ONNX model listens to your microphone [3, 4]. No audio ever leaves your local machine until a wake word is matched [3].
2.  **The Wake Match:** When you say **"Hey Oracle"** from across the room, the Sherpa engine fuzzy-matches the speech [2, 5]. It instantly pauses its idle state, loads the Oracle profile's YAML configuration, and sets the Oracle's `soul.md` file as the system's unshakeable guiding instructions [2, 4].
3.  **Spoken Confirmation:** The model switches context in under a second and announces its active state out loud: *"Oracle listening. What is the mission?"*
4.  **Hands-Free Command:** Speak your request naturally (e.g., *"Write an Alex Hormozi 'so that' landing page headline for Plano"*). The command is captured, run through your local brand firewall check (`brand_firewall.py`), and staged as a **PAUSED** file in your Outbox folder.
5.  **Spoken Interruption:** If Oracle starts reading back a draft that is too wordy, you can shout **"Stop!"** mid-turn [4]. The voice engine immediately flushes its speech buffer, stops generating, and opens the microphone for your redirect (e.g., *"Keep it under two sentences and emphasize our RCAT #03-0637 license"*), preventing token waste [4, 6].

---

### 🏛️ 2. Inside the Goldie Infinite Knowledge Engine Loop

Most users interact with AI as a single-turn chatbot—typing a prompt, copying the answer, closing the tab, and starting from scratch tomorrow [7]. The **Goldie Infinite Knowledge Engine** replaces this manual copy-paste grind with a closed-loop system where your research, memory, and media production compound automatically [8]:

```
┌────────────────────────────────────────────────────────┐
│             THE INFINITE KNOWLEDGE ENGINE              │
├────────────────────────────────────────────────────────┤
│                                                        │
│   [ Layer 1: GEMINI NOTEBOOK (The Knowledge Vault) ]   │
│   • Ingests Collin/Denton building codes, GSC data,    │
│     and OMI voice-notes.                               │
│                        │                               │
│                        ▼ (Connected via MCP Bridge)    │
│                                                        │
│   [ Layer 2: HERMES / AGENT OS (The Operating Core) ]  │
│   • Runs unmetered local & cloud models (Sol/Luna).   │
│   • Triggers and pulls reports, audios, and layouts.   │
│                        │                               │
│                        ▼                               │
│                                                        │
│   [ Layer 3: OBSIDIAN VAULT (The Long-Term Memory) ]   │
│   • Shared database where every output is logged.      │
│   • Feeds fresh context back into the Knowledge Vault.  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

#### Layer 1: The Knowledge Vault (Gemini Notebook)
You drop all of your raw, unstructured target files (such as local storm damage coordinates, drone thermal camera logs, Collin County roofing ordinances, or competitor transcripts) into your Google-secure cloud container [9, 10]. Gemini Notebook reads all of it together as your single source of truth [9, 10].

#### Layer 2: The Agent Operating Core (Hermes / Agent OS)
Your local workspace connects directly to your cloud notebooks using the **NotebookLM Model Context Protocol (MCP) Bridge** [10, 11]. This means your hands-free local agents (Claude Code, Hermes, or Codex Sol) can read your cloud sources [11]. Your agent can command the cloud notebook's secure computer to write and execute code, analyze spreadsheets, and compile assets—generating up to 12 distinct formats (including Audio Overviews, infographics, or slide decks) [12-14]. Hermes then programmatically downloads these files directly to your local computer's media folders with **zero browser clicking** [11, 15].

#### Layer 3: The Infinite Loop (Obsidian shared brain)
Every completed asset, report, and video script is automatically logged as plain Markdown files in your local **Obsidian vault** [11, 16]. When you capture new work decisions or field notes using your OMI device, those transcripts sync directly into Obsidian as well [16, 17]. Your background agents read this growing memory vault, identify new keyword opportunities, and push updated briefs back up into your Gemini Notebook [16, 18]. This closes the loop: **what one agent builds, your entire local-cloud system instantly knows, compounding your local authority forever** [11].

---

### 🎯 3. Running the Claude Gauntlet Loop in Your Business

The **Claude Gauntlet Loop** (originated by Matt Schumer) is a brutal self-correcting workflow that completely replaces human review of AI drafts [19]. 

Instead of you reading a draft, correcting it, and typing back-and-forth 20 times to get it right, **you write the standard once, and a wall of "blind, cold critics" runs a gauntlet against the builder agent until the output is flawless** [20-22]. 

#### How the Gauntlet Loop Operates Natively on Your PM7 Build:
1.  **The Goal Split:** You drop a goal on your Kanban board (e.g., *"Write an optimized, high-converting McKinney storm-restoration landing page"*). The lead agent breaks the goal down and spawns parallel sub-agents (one for the headline, one for local code citations, one for review-social proof) [21, 22].
2.  **The Blind Critic Wall:** Each sub-agent is assigned its own "blind critic" [22]. The critics never see the builder's prompt or reasoning; they only look at the finished text or rendered screenshots of the output and judge it directly against your gold-standard benchmark [22].
3.  **The Unforgiving Stop Condition:** The critics will reject drafts repeatedly (even 100+ times) with zero fatigue or politeness [23]. The loop refuses to complete until the output perfectly matches the benchmark [23, 24].

#### The Perfect Gauntlet Loop Prompt for Your Roofing Pages:
You can paste this exact prompt into your unmetered **Codex / Sol (BUILD Lane)** or **Claude Code (ORCHESTRATE Lane)** session to run a full landing page copy gauntlet:

```text
Act as the Lead Systems Architect running an autonomous Claude Gauntlet Loop. 
Our target goal is: [Draft a hyper-local, high-converting storm-restoration service page for our Plano, TX campaign].

GAUNTLET CONSTRAINTS:
1. Spawn specialized builder sub-agents in parallel to draft separate sections: the Hero block, the Local Building Code block, the IKO Certified shingle proof block, and the FAQ section.
2. Spawn blind critic sub-agents to evaluate each section. The benchmark for evaluation is Alex Hormozi's Value Equation: Dream Outcome (articulated using the "so that" headline formula), maximum Perceived Likelihood of Success, minimal Time Delay, and zero friction.
3. Apply our Brand Compliance Firewall: Convert all instances of "Complimentary Professional Photo Audit (CPPA)" to "Complimentary Professional Photo Audit (CPPA)", map "$0 down" to "Full Restoration Coverage", specify shingles as "IKO Certified RoofPro" or "IKO Certified Roofing Contractor", completely prohibit green colors, and embed the trust footer: Polynesian-owned · RCAT #03-0637 · IKO Certified · since 2005 · (972) 928-0788 · Frisco, TX.
4. Run the feedback loops autonomously. Builder agents must edit and refine their outputs. The critics must reject any draft that falls short of 9.5/10 against the benchmark.
5. Do not terminate the loop or write the output to our local C:/Pineapple Contractors M7/01_Command_Center/Outbox_Drafts/ folder until the critics are utterly wowed by the quality and our brand_firewall.py compliance script returns 0 errors. Mark the final compiled file status as STATUS: PAUSED.
```

***

⭐ **Next Step:** You can double-click your master launcher **`launch-all-studio-v3.bat`** and run **Option 4** to turn on your hands-free voice wake-word engine. Do you want me to write the automated script that lets you shout *"Hey Coder - build the Plano page"* to instantly launch your first live Gauntlet Loop on your desktop?