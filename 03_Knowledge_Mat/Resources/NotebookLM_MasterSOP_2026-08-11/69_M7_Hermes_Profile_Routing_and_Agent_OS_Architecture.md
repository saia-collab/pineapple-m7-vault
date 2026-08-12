---
source: "NotebookLM - Master SOP 8/26"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 99801658-b7ba-40d9-aa9b-fe65e0d98953
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW free?,green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# M7 Hermes Profile Routing and Agent OS Architecture

### 🧠 MASTERING THE M7 HERMES PROFILES

Inside your **M7 Agent OS**, your AI agents do not run as one giant, generic chatbot [cite: 121, 244]. Instead, you have **specialized, profile-driven personas** [cite: 121, 245]. 

Each profile functions like a dedicated team member in your digital office—pre-loaded with its own custom system prompt (its "SOUL"), specific folder boundaries, and targeted tools [cite: 121, 245].

By dividing your workflow across these profiles, you prevent **"Context Inflation"** (where an agent gets confused by trying to hold too much unrelated information in its active memory) [cite: 98, 235] and guarantee absolute brand compliance under **The Pineapple Standard** [cite: 176].

---

### 🏛️ THE PROFILE SELECTION ROUTING MATRIX

Your profiles are selectable directly from the **Profile Bar** at the top of your Hermes interface [cite: 152, 178]. By default, they run on the fast and free **`gpt-5.6-sol` model via Codex** [cite: 173, 178], though you can easily scale up to premium engines when running complex tasks [cite: 173]:

| Profile Name | Operational Role & Job Description | Active Context Hook & Memory Link |
| :--- | :--- | :--- |
| **`main` / `default`** [cite: 173, 178] | **The General Daily Operator & Orchestrator** [cite: 173, 178] <br>Coordinates vault-wide maintenance, file refactoring, and directory cleanups [cite: 246]. | Reads `m7_core_rules.config` and runs standard system tools [cite: 246]. |
| **`seo` / `seo-lead`** [cite: 173, 178] | **The SEO Page & Keyword Machine** [cite: 173, 178] <br>Generates high-intent location service pages and SEO clusters [cite: 173]. | Integrates GSC metrics and maps keyword gaps from `active_context/` [cite: 246]. |
| **`marketing`** [cite: 173, 178] | **The Campaign Strategist** [cite: 173] <br>Drafts high-converting landing page hooks and campaign briefs [cite: 246]. | Built around direct-response frameworks [cite: 172, 246]. |
| **`content`** [cite: 173, 178] | **The Digital Repurposer** [cite: 173, 178] <br>Writes blogs, email funnels, and scripts for video reels [cite: 173, 194]. | Monitors your media vault and drives active short-form scripts [cite: 246]. |
| **`roofing`** [cite: 173, 178] | **The Technical Roofing Expert** [cite: 173, 178] <br>Drafts highly technical roof replacement and claim copies [cite: 173]. | Restricted strictly to roofing and claim lexicon [cite: 178]. |
| **`restoration`** [cite: 173, 178] | **The Rapid Mitigation Specialist** [cite: 173, 178] <br>Handles water, fire, mold, and storm emergency damage briefs [cite: 178]. | Strictly isolated to emergency response rules (never cross-mixes with roofing) [cite: 178]. |
| **`leads`** [cite: 173, 178] | **The Speed-to-Lead CRM Agent** [cite: 173, 178] <br>Performs prospect enrichment and drafts outbound follow-ups [cite: 173, 246]. | Reads your local Leadstack CRM databases [cite: 246]. |
| **`notebook-obsidian`** [cite: 152, 173] | **The Knowledge Synthesizer** [cite: 173] <br>Extracts structured research from your local vault files and NotebookLM [cite: 173]. | Connects directly to local folders and NotebookLM via MCP [cite: 152]. |

---

### 🛡️ THE COGNITIVE GROUNDING SYSTEM (THE SECURE WRAPPER)

No matter which profile you select, **they all share the exact same long-term memory vault (`C:\Pineapple Contractors M7`)** [cite: 174, 229]. This means your core business facts, physical HQ address, and operational guidelines are instantly visible to every agent [cite: 37, 229]:

*   **Shared Obsidian Substrate:** When you update an SOP or add a new customer review in Obsidian, the changes are automatically read by every profile [cite: 93, 229]. You explain your business once, and every worker in the office instantly remembers it [cite: 227, 229].
*   **The Outbox Shield (DEC-005):** Profiles are strictly gated [cite: 37, 176]. No agent possesses the write privileges to post to social media, deploy live website edits, or spend advertising dollars autonomously [cite: 37, 163, 172]. **All outputs land in a PAUSED state inside your `01_Command_Center/Outbox_Drafts/` folder for your manual review and approval** [cite: 172, 176].
*   **Immutable Brand Guidelines:** Every profile is hardcoded to respect your strict design standards:
    *   **Colors:** Strictly **0% Green** (relying on Royal Navy `#1A365D`, Pineapple Gold `#FBC02D`, and Status Cyan `#00BFFF`) [cite: 37, 288].
    *   **Lexicon:** Enforces **Complimentary Professional Photo Audit (CPPA)** (never *"Complimentary Professional Photo Audit (CPPA)"*), **IKO Certified** (never *"IKO Certified"*), and **Full Restoration Coverage** (never *"0 down"*) [cite: 288].
    *   **Tone:** Highly professional, objective, clean, and optimized to deliver immediate, direct answers to capture Google AI search visibility [cite: 29, 31].

---

### ⚡ SWAPPING AND MODEL FAILOVERS

Within the **Hermes Cockpit**, managing your active brains is effortless [cite: 266, 268]:
1.  **To Switch Personas:** Simply select your desired profile pill from the profile bar at the top of the interface [cite: 152, 178].
2.  **To Switch Models:** If your current API route experiences latency or hits rate limits, you can swap the underlying model in the top-right dropdown [cite: 158, 231]. It will immediately fall back to your **free local Ollama models (`qwen2.5-coder` or `gemma2`)** so your work never halts mid-run [cite: 155, 191, 266].

📂 **Next Step Suggestion:**  
I can prepare a specialized **`profile_health_check.py`** script inside your `04_Tech_Lab/scripts/` directory to verify that all 7 local Hermes profiles are perfectly synced with your latest brand firewall rules [cite: 80, 245]. Would you like me to map out this diagnostic profile auditor? [cite: 80]