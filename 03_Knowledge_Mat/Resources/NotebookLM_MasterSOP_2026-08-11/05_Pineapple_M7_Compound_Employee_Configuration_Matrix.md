---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 146e0f2e-a4c6-4525-b7ac-17a53a95dde7
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Pineapple M7 Compound Employee Configuration Matrix

### 🛰️ COUPLING YOUR PERSISTENT BRAND SOUL WITH SWAPPABLE AI BRAINS

To configure a specialized profile (such as `seo`, `marketing`, `content`, or `leads`) so it behaves as a true **"Compound Employee"** [cite: 133], you configure two files inside your profile directory [cite: 148, 239]:
1.  📁 **`soul.md`:** The permanent "identity chip" that enforces your brand guidelines [cite: 239].
2.  📁 **`config.yaml`:** The "brain wiring" that binds specific AI models, MCP servers, and tool permissions [cite: 165, 249].

These profiles reside on your local machine at:  
📂 **`%LOCALAPPDATA%\hermes\profiles\<profile_name>\`** [cite: 311]  
*(Alternatively mirrored in your vault at `C:\Pineapple Contractors M7\04_Tech_Lab\hermes_profiles\`)* [cite: 311]

---

## 💾 SECTION 1: THE BRAND CONSTITUTION (`soul.md`)
Every time an agent in your profile starts a task [cite: 231], it is hardcoded to parse **`soul.md`** first [cite: 231]. This prevents **context drift** and ensures absolute alignment with your strict business parameters [cite: 54, 220]. 

Save this exact code block as **`soul.md`** inside your active profile folder:

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

---

## ⚙️ SECTION 2: BINDING THE AI MODELS (`config.yaml`)

This configuration sheet manages the **effort-to-token ratio** [cite: 10, 220]. It maps complex strategic planning to your cloud reasoning engines, routes high-volume work to fast local models [cite: 12, 114], and enables the **One-Script Browser Engine** [cite: 269].

Save this file as **`config.yaml`** inside the same profile directory:

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

---

## 🗂️ SECTION 3: SYSTEM PROFILE ROUTING MATRIX
When launching Hermes tasks from your terminal, choose the correct persona profile based on your task category [cite: 236]:

| Task / Deliverable | Hermes Run Profile | Shared Memory Hook |
| :--- | :--- | :--- |
| **GSC Data, OpenSEO SERP, Schema Injections** | `hermes --profile seo` [cite: 237] | Isolate positions 5–20 page-2 leaks [cite: 29]. |
| **IKO Comparative Pages, Storm Damage Landing Pages** | `hermes --profile roofing` [cite: 237] | Ingests `MASTER_PLAYBOOK.md` + storm codes [cite: 237]. |
| **Social Captions, 50/5/3 Video Multiplier Scripts** | `hermes --profile content` [cite: 237] | Pulls from `02_Media_Vault/` directory [cite: 237]. |
| **Offers, Facebook UGC Ads, Hormozi Pricing Hooks** | `hermes --profile marketing` [cite: 237] | Maps onto your `M7_INTEGRATED_CAMPAIGN.md` [cite: 237]. |
| **Speed-to-Lead, Review-Request SMS, CRM Sync** | `hermes --profile leads` [cite: 237] | Reads local `Pineapple_Mana_Master_CRM_M7.xlsx` [cite: 237]. |

---


📂 **Next Step Suggestion:**  
I can configure your **`leads` profile** to automatically parse your incoming Meta Ads webhook and output a fully mapped payload directly to your messaging channels. Would you like me to map out this n8n automation webhook? [cite: 124, 237]