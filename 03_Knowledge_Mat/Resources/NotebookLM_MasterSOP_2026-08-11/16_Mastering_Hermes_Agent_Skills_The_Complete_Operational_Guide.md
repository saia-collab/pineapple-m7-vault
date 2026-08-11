---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 70cd8d9b-f158-4174-a2cf-1f0941722716
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Mastering Hermes Agent Skills: The Complete Operational Guide

### 🧰 THE OPERATIONAL GUIDE TO HERMES AGENT SKILLS

In standard AI setups, you are trapped in a loop of repeating your instructions, pasting your brand parameters, and correcting the same mistakes session after session [cite: 114]. **Hermes Agent Skills** completely break this cycle [cite: 114]. 

If memory is what your agent knows, **skills are what your agent can do** [cite: 121]. A skill is essentially a **procedural "recipe"**—a step-by-step executable instruction sheet for a specific task [cite: 121]. Once you teach Hermes how you want a job completed, it packages those instructions into a runnable program that it keeps forever [cite: 114, 122, 293]. The next time you call that skill, the agent executes it perfectly on the first try, allowing your work to compound over time [cite: 114, 122].

---

### 🍳 1. HOW SKILLS ARE CREATED: RECIPES & THE `/learn` ENGINE

Hermes allows you to build its capabilities library in two ways:

#### A. The Organic Training Loop
You can train Hermes directly in your chat [cite: 122]. If you ask the agent to perform a task (such as auditing local competitor sites) and give it feedback over a few turns (e.g., *"keep it short, compare their warranties, prioritize Frisco ZIPs"*), Hermes detects the pattern [cite: 122]. It will ask: **"Should I save this as a skill?"** [cite: 122] Once you confirm, those exact feedback parameters are baked into its local files forever [cite: 122].

#### B. The Instant `/learn` Command (The Golden Shortcut)
If you find a new SEO guide, a Julian Goldie video transcript, or third-party tool documentation, you do not have to write code to teach it to your agent [cite: 122]. 
1. Open your **Hermes Console** [cite: 191] and type:  
   `/learn <path_to_document_or_url>` [cite: 122, 176]
2. Hermes will read the guide, extract the exact step-by-step logic, and autonomously author its own permanent, structured **`.md` skill file** inside your workspace [cite: 122]:  
   📁 `C:\Pineapple Contractors M7\04_Tech_Lab\skills_inbox\` [cite: 169, 180]
3. Every training manual on the internet immediately becomes a functional skill in your local studio [cite: 123].

---

### 🏛️ 2. THE 0.16.0 SKILLS HUB & GOLDIE SKILL VAULT™ REHAUL

Before the recent **Skills Hub rehaul**, managing local agent capabilities was a blind guessing game [cite: 326]. You had to click install, hope the third-party script worked, and uninstall it if it crashed your terminal [cite: 326, 333]. 

With the launch of **Hermes 0.16.0+**, your **Manage → Skills** tab inside your Agent OS dashboard has been upgraded to the **Goldie Skill Vault™** [cite: 325, 332]:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE GOLDIE SKILL VAULT™                         │
├────────────────────────────────────────────────────────────────────────┤
│  [796 Active Skills] ──► [6 Connected Hubs] ──► [Strict Security Scan] │
├────────────────────────────────────────────────────────────────────────┤
│   - Read real SKILL.md  - Official/ClawHub      - Critical: 0          │
│   - Color-coded Tiers   - GitHub/LobeHub        - Safe / Caution / Block│
└────────────────────────────────────────────────────────────────────────┘
``` [cite: 325, 326, 330, 331, 333, 342]

*   **796 Skills Across 6 Hubs:** A single search box now queries all six major open-source agent repositories simultaneously: *Official, Hermes Index, skills.sh, GitHub, ClawHub, and LobeHub* [cite: 325, 330, 333].
*   **Source Code Previews:** Before a single file is downloaded to your machine, you can click **Preview** to read the exact `SKILL.md` layout, the tools it uses, and its execution steps [cite: 327, 330, 333].
*   **Visual Security Scanning:** The hub runs background scans on every package and displays a clear security status—flagging **Critical, High, or Medium** risk factors so you never install malicious code [cite: 327, 330, 331].
*   **Color-Coded Trust Tiers:** Skills are visually labeled on your dashboard as **Trusted**, **Built-In**, or **Community** so you know who wrote the script at a glance [cite: 331].

---

### 🌐 3. THE AUGUST 11, 2026 "ONE-SCRIPT ENGINE" UPGRADE

On August 11, 2026, Nous Research dropped a major update that fundamentally changed how local agents interact with the web [cite: 344].

#### The Old Way:
Previously, Hermes had to carry **twelve separate browser tools** (*browser_navigate, browser_click, browser_scroll, etc.*) in its active memory [cite: 346]. To complete a simple form, the agent had to carry twelve separate instruction manuals, execute a tool call, pause to re-think, request permission, and execute the next tool call [cite: 346, 347]. A single web-browsing run could easily consume **50,000 to 64,000 API tokens** [cite: 347].

#### The New Way (The One-Script Engine):
Powered by the **Browser Use CLI 3.0** backend, the agent replaces all twelve tools with **one single script-writing capability** [cite: 345, 347]. 
1. You provide a plain-English instruction (e.g., *"Check our competitors' pricing and save the details"* [cite: 353].
2. Hermes writes **one comprehensive Python script** for the entire browsing sequence upfront [cite: 348].
3. It launches your local browser, navigates, clicks, types, and scrapes in one unbroken sequence without stopping to ask for permission between steps [cite: 348, 352].
4. **The Benefit:** It achieves the exact same execution accuracy while **cutting your API token expenses by 48% to 66%** [cite: 344, 347].

---

### 📦 4. THE SKILLS WORTH GRABING FIRST FOR YOUR STUDIO

To maximize your local workflow speed, open your **Agent OS → Hermes → Manage → Skills** tab, search these exact names, and install them [cite: 332, 335, 339]:

1.  **`obsidian`:** The core engine of your memory loop [cite: 336]. It allows Hermes to read, update, and organize your local notes so your agent sessions never start cold [cite: 305, 336].
2.  **`youtube-content`:** Instantly performs competitor research, extracts transcripts, and drafts AEO-optimized video summaries [cite: 336].
3.  **`kanban-orchestrator` & `kanban-worker`:** The skill pair that drives your **Idea Factory** [cite: 203, 338]. It allows your main agent to break a high-ticket campaign card into tasks and delegate them to parallel sub-agents [cite: 125, 205, 338].
4.  **`webhook-subscriptions`:** The ultimate integration glue [cite: 338]. It allows Hermes to listen for external triggers (like a new inbound CRM lead) and autonomously launch background loops [cite: 214, 338].

---


📂 **Next Step Suggestion:**  
I can configure the **`youtube-content`** and **`obsidian`** skills inside your local profile's `config.yaml` to ensure your agent can pull video notes from Julian Goldie's channels and write them straight into your vault as linked notes [cite: 120, 165, 336]. Would you like me to map out this YAML configuration block? [cite: 165]