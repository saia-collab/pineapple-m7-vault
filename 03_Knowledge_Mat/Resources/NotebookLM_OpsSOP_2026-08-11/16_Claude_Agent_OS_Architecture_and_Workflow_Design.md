---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: aa890f4d-4813-45b3-87c3-9a327636672d
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW free?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# Claude Agent OS: Architecture and Workflow Design

### The Claude Agent OS Architecture

The **Claude Agent OS** is a self-hosted, private agentic operating system designed to run 24/7 [1, 2]. Instead of relying on fragmented SaaS platforms or expensive agencies, it consolidates your local command center, AI tools, and business data into a single, unified environment [1, 3]. 

The system operates under a clear, hierarchical flow [4]:

```
  HUMAN OPERATOR (Saia)
         │
         ▼
  COMMAND CENTER (Dashboard on Port 3737/3000)
         │  (Tabs: Mission Control, Pipeline, Shared Memory, Execute, Skills, Studio, Jarvis)
         ▼
  AI AGENTS (Claude Code, Hermes, NotebookLM, Paperclip, Higgsfield)
         │  (All read Shared Memory & local vault files as context)
         ▼
  PIPELINE (5-Column Kanban: Idea → Plan → Human Approval (PAUSED) → Implement → Shipped)
         │
         ▼
  OUTPUT (Staged as PAUSED drafts in Outbox_Drafts/ to protect the brand)
         │
         ▼
  MEMORY (Obsidian, SHARED_MEMORY.md, and local markdown files)
```

---

### The Three-Lane Division of Labor (AI Agent Design)

A key design principle of the Agent OS is the **Three-Lane Division of Labor** [5]. By allocating specific types of tasks to the most optimized model in your stack, you achieve elite-level results while keeping operating costs virtually at zero [5-7].

| Lane | Assigned Agent | Core Ownership | Design Philosophy |
| :--- | :--- | :--- | :--- |
| **BUILD** *(Code)* [5] | **Codex / GPT 5.6** *(ChatGPT OAuth)* [5] | Automation scripts, WordPress integrations, custom dashboards, schema/JSON-LD, and technical SEO [5]. | **Unmetered & highly technical.** Point this frontier coder at your codebase and vault files to execute engineering tasks without token limits [5, 8]. |
| **ORCHESTRATE + VOICE** [5] | **Claude Code** [5] | Brand-voice copywriting, high-priority landing pages, review replies, workflow planning, and running the brand compliance firewall [5]. | **Quality-critical seat.** This agent is trained to know your brand guidelines cold to prevent compliance errors or halluncinations [5]. |
| **RESEARCH / IDEATE** [5] | **ChatGPT** *(Plus, web)* [5] | Keyword brainstorming, local competitor analysis, and generating creative angles or first-draft concepts [5]. | **Fast and conversational.** Designed for rapid-fire search and discovery. Its raw outputs are fed back to Claude or Codex to be finalized and firewalled [5]. |

---

### Cost-Smart Overflow and Model Routing

Because commercial API costs can spiral quickly, the Agent OS is designed with an **automated fallback chain** that maximizes free and unmetered resources [6, 9]:

1. **The content workhorse is Hermes (Goal Mode)** [10]: It runs on your cloud VM or a local setup [10, 11], reading your local files and drafting bulk landing pages or social media posts directly into your draft folders [10, 12].
2. **OmniRoute provides infinite scale** [9, 10]: When a primary model hits a rate limit, OmniRoute acts as an intelligent gateway, giving the system access to **90+ free models** with automatic failover [9, 10].
3. **Claude Fable 5 is strictly rationed** [6, 13]: Expensive frontier models are never used for high-volume drafting. Fable 5 is only brought in for **one or two prompts to perform a "hero polish"** on critical pages, such as your primary homepages [6, 7].
4. **Local models serve as the final safety net** [9]: Unlimited, offline models (like gemma2:2b or qwen2.5-coder:7b) handle basic drafting tasks on your local machine if cloud endpoints are temporarily unavailable [9, 11, 14].

---

### Filesystem-First Memory Management

Traditional AI systems rely on complex, brittle vector databases that require constant upkeep. The Claude Agent OS uses a **filesystem-first memory design** [15]:

* **Shared Brain File (`SHARED_MEMORY.md`)** [15]: Every agent is programmed to read this file before starting any task [14]. At the end of a session, agents log what they built directly back into this file, creating a continuous feedback loop [14].
* **Active Context Folder (`03_Knowledge_Mat/active_context/`)** [16]: This is a single, local directory where you drop GSC exports, customer testimonials, and storm reports [16]. Because the agents monitor this folder directly, updating your system's "live brain" is as simple as adding or updating a markdown file [16].
* **Obsidian Integration** [15]: The workspace maps directly to an Obsidian vault [15]. This allows you to visually map, link, and review the markdown notes and files that the agents generate and read [15, 17].

---

### The Outbox Shield and Brand Firewall

To ensure that autonomous agents never damage your business reputation or make unapproved changes, the OS implements a strict **defense-in-depth security model**:

* **The Outbox Shield** [18]: Under no circumstances are agents permitted to publish content, post to social media, or spend ad budget on their own [2, 18, 19]. All outputs land in `01_Command_Center/Outbox_Drafts/` in a **PAUSED** state, waiting for human approval [2, 18, 20].
* **Programmatic Brand Firewall (`brand_firewall.py --check`)** [18, 21]: Before any file is staged for your review, a local script automatically scans the draft [18, 20]. It instantly flags and rejects any text that violates brand rules (e.g., using banned terms like "free" instead of "CPPA", or failing to list required credentials like RCAT #03-0637) [18].

---

🛠️ Would you like to map out how to set up the **Shared Memory** file and connect your local workspace to Obsidian so you can start viewing your agent logs in real time?