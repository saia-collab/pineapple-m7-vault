---
type: master_sop
title: M7 MASTER SOP — the one file Claude Code reads to run the whole Agent OS
status: active
version: "1.0 — consolidated 2026-06-27"
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🛰️ PINEAPPLE M7 — MASTER SOP (read this, run anything)

**Claude Code / Hermes / any agent:** this is the single map of the Pineapple Contractors M7 Agent OS.
Read this file first. It tells you what exists, where it lives, how to run each part, and the rules you
never break. When Saia gives a job, find the matching SOP below and execute it. **You draft and build;
Saia is the only one who publishes, posts, sends, or spends.**

---

## 0. THE 5 RULES THAT NEVER CHANGE (Outbox Shield + Brand Law)

1. **Outbox Shield:** every output lands **PAUSED** in `01_Command_Center/Outbox_Drafts/`. Never publish,
   post, send, schedule, or spend (ad budget, Higgsfield credits) without Saia's explicit "GO."
2. **Never restructure folders** or delete files unless Saia says so. Move/clean only via the launchers.
3. **Brand lexicon:** never "free" → **CPPA** (Complimentary Professional Photo Audit); never "$0 down" →
   **Full Restoration Coverage**; never "GAF" → **IKO Certified**; never "Toa/Warrior/Six Brothers" →
   **The Pineapple Standard**.
4. **No green** anywhere. Palette: Royal Navy `#1A365D`, Pineapple Gold `#FBC02D`, Status Cyan `#00BFFF`.
5. **Verify, don't hallucinate.** Run `brand_firewall.py --check` before staging. If a fact isn't sourced,
   flag it — never invent. Identity: Polynesian-owned, RCAT #03-0637, IKO Certified, since 2005, 972-928-0788.

---

## 1. THE SYSTEM IN ONE PICTURE

```
  SAIA (voice / click / type)
        │
        ▼
  COMMAND CENTER  ── M7_COMMAND_CENTER.html (served by server.js @ localhost:3737)
        │            tabs: Mission Control · Pipeline · Shared Memory · Execute · Skills · Studio · Jarvis
        ▼
  AGENTS  ── Claude Code (builder) · Hermes (orchestrator) · NotebookLM (research) ·
            Paperclip (content team) · Higgsfield (creative/clone) · OpenClaw (gateway) · Ollama (local)
        │   all read shared memory + the vault as context
        ▼
  PIPELINE  ── 5-column Kanban: Idea Input → Agent Planning → ⛔ Human Approval (PAUSED) → Implementation → Shipped
        │
        ▼
  OUTPUT  ── PAUSED drafts in Outbox_Drafts/ → Saia reviews → Saia publishes
        │
        ▼
  MEMORY  ── vault files are the memory (filesystem-first) + SHARED_MEMORY.md + Obsidian + GitHub history
```

---

## 2. FILE MAP — where everything lives (vault root: `C:\Pineapple Contractors M7`)

| File                                                                           | What it is                                                                      |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| `server.js` + `package.json` + `.env.example`                                  | Local Agent OS server (Node, zero-dep) → serves dashboard + APIs on :3737       |
| `01_Command_Center/M7_COMMAND_CENTER.html`                                     | The live command center (Mission Control + Jarvis voice)                        |
| `01_Command_Center/M7_NOTEBOOK_BAY.html`                                       | Local PDF reader + notes (no server)                                            |
| `01_Command_Center/GROUNDING.md`                                               | Brand constitution (the law)                                                    |
| `01_Command_Center/MASTER_PLAYBOOK.md`                                         | Single source of truth for the business                                         |
| `01_Command_Center/M7_EXECUTE.md`                                              | The "hand to an agent, it executes" playbook                                    |
| `01_Command_Center/M7_INTEGRATED_CAMPAIGN.md`                                  | Social + LSA + SEO/AEO campaign                                                 |
| `01_Command_Center/M7_CONTENT_FACTORY.md`                                      | 39GB media → viral cuts → ads                                                   |
| `01_Command_Center/M7_LEAD_ENGINE.md`                                          | Speed-to-lead + reviews                                                         |
| `01_Command_Center/M7_AGENT_LOOPS.md`                                          | Every automation loop                                                           |
| `01_Command_Center/M7_LOCAL_MODEL_PLAYBOOK.md`                                 | Workload tiers + free local models (token strategy)                             |
| `01_Command_Center/M7_CLOUD_DEPLOYMENT_CHEATSHEET.md` + `M7_MASTER_RUNBOOK.md` | GCP + Docker deploy + GitHub                                                    |
| `01_Command_Center/M7_SKILLS_CATALOG.md`                                       | Your 48 kits + how to fire each                                                 |
| `01_Command_Center/M7_Agent_Kanban.md`                                         | The live 5-column board                                                         |
| `01_Command_Center/Outbox_Drafts/`                                             | Where all PAUSED drafts land                                                    |
| `02_Workspaces/Pineapple_Mana_Master_CRM_M7.xlsx`                              | The CRM (Airtable retired)                                                      |
| `03_Knowledge_Mat/SHARED_MEMORY.md`                                            | The shared brain every agent reads                                              |
| `03_Knowledge_Mat/00_Atlas/`                                                   | SOP library (see §11)                                                           |
| `04_Tech_Lab/scripts/brand_firewall.py`                                        | Compliance firewall (lexicon + green)                                           |
| `04_Tech_Lab/server_m7.py`                                                     | Python backend (alt to server.js)                                               |
| `04_Tech_Lab/m7_doctor.py`                                                     | Connection health checker                                                       |
| `04_Tech_Lab/skills_inbox/`                                                    | 48 downloaded skill kits                                                        |
| Launchers (root .bat)                                                          | `RUN_AGENT_OS.bat` · `M7_DOCTOR.bat` · `M7_CLEANUP.bat` · `START_M7_SERVER.bat` |

---

## 3. HOW TO RUN IT (the only commands you need)

| Goal                         | Do this                                                             |
| ---------------------------- | ------------------------------------------------------------------- |
| Start the command center     | Double-click **`RUN_AGENT_OS.bat`** → opens `http://localhost:3737` |
| Check everything's connected | Double-click **`M7_DOCTOR.bat`** (green/red checklist)              |
| Tidy the vault               | Double-click **`M7_CLEANUP.bat`**                                   |
| Run on the cloud (24/7)      | Follow **`M7_MASTER_RUNBOOK.md`** (GitHub → GCP → Docker)           |
| Read a PDF / take notes      | Open **`M7_NOTEBOOK_BAY.html`**                                     |

---

## 4. THE SOPs (find the job, run the command)

### SOP-A · Execute a week of content (the money engine)

Paste into Hermes/Claude Code:

> `Read 01_Command_Center/M7_EXECUTE.md and execute this week's content: 8–12 branded captions (Authority/Proof/Heritage), repurpose 1 video into 6 cuts, 2 GBP posts, testimonial money-quotes. Draft PAUSED to Outbox_Drafts, run brand_firewall.py --check. No folder changes.`

### SOP-B · NotebookLM research → sourced brief

> `Act as the NotebookLM Core Research Node. Ingest [sources]. Summarize each, map gaps, extract stats with sources. Save a sourced brief to 05_Campaign_Factory/10_Research_Stage/ (PAUSED). Never invent a fact.`

### SOP-C · Brand firewall check (always before staging)

> `Run python 04_Tech_Lab/scripts/brand_firewall.py --check "<text>"` — must return 0 green / 0 banned. On any flag, fix and re-run.

### SOP-D · Fire a skill from the 48 kits

> `Read everything in 04_Tech_Lab/skills_inbox/<KIT NAME>/ and apply it to <task>. CPPA/IKO/no green. Draft PAUSED to Outbox.` *(First make the folder "Available offline" in Google Drive so the files are local — see M7_SKILLS_CATALOG.md.)*

### SOP-E · Deploy to the cloud (free the laptop, 24/7)

> Open Google Cloud Shell, attach `M7_MASTER_RUNBOOK.md` + `M7_CLOUD_DEPLOYMENT_CHEATSHEET.md`, paste THE ONE PROMPT in the runbook. It provisions the VM, git-clones the vault, runs Docker, sets Tailscale. Keep the persistent volume + `HERMES_ALLOW_*_WRITE=false`, never expose ports.

### SOP-F · Back up to GitHub (your undo button)

> In `C:\Pineapple Contractors M7`: `git add . && git commit -m "update" && git push` (repo: saia-collab/Roofing-Marketing-System; .gitignore already excludes media + secrets; make the repo Private).

### SOP-G · Shared memory (so agents never need re-explaining)

> Append a note via the dashboard Shared Memory tab, or: every agent reads `03_Knowledge_Mat/SHARED_MEMORY.md` before a task. Log what was built after.

### SOP-H · Model/token strategy (when Hermes stalls)

> Follow `M7_LOCAL_MODEL_PLAYBOOK.md`: route heavy/multi-agent work to a cloud flagship (OpenRouter/owl), small drafts to local (gemma2:2b / qwen2.5-coder:7b). Never run the swarm on a starved local box.

### SOP-I · CRM + speed-to-lead

> CRM = `02_Workspaces/Pineapple_Mana_Master_CRM_M7.xlsx` (Google_LSA_Leads, Master_Lead_Tracker, Attribution, Meta_Ads, Assets). Answer every lead in 5 min; ask every finished job for a review (`M7_LEAD_ENGINE.md`).

### SOP-J · Campaign / ads (human-gated)

> Draft per `M7_INTEGRATED_CAMPAIGN.md`; stage PAUSED. Saia launches in Meta ($250/wk CBO, 1% Kill / 1.5% Scale). Agents never spend.

---

## 5. WEEKLY OPERATING RHYTHM

- **Mon** — performance brief; plan the week; NotebookLM ingests fresh storm/SERP data.
- **Tue** — asset planning; pull case studies; build sourced briefs.
- **Wed** — production: content + Pomelli + Higgsfield + video → Quality Gate → PAUSED.
- **Thu** — Human Approval: review, approve, publish the winners.
- **Fri** — outreach + reviews.
- **Weekend** — rank checks, analytics, memory sync, `git push`.
- **Daily reflexes:** answer leads in 5 min · ask for reviews · ship one thing.

---

## 6. TROUBLESHOOTING (the things that bit us — and the fix)

| Symptom                                    | Fix                                                                                                                                                                                      |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Disk full / freezes**                    | Media is in Google Cloud now — keep `02_Media_Vault` OFF the local disk. Keep 15GB+ free.                                                                                                |
| **localhost refused**                      | The server isn't running — double-click `RUN_AGENT_OS.bat` (or `START_M7_SERVER.bat`).                                                                                                   |
| **Hermes "install didn't finish"**         | That's the local Desktop app — **don't use it** (eats RAM). Hermes runs on the cloud VM.                                                                                                 |
| **Hermes workspace :3000 login fails**     | Cookie bug on HTTP. Use the gateway dashboard at **:9119**; log in with AUTH_USER/AUTH_PASS from the cloud `.env`; keep `AUTH_COOKIE_SECURE=false`; use the same Tailscale IP each time. |
| **Skills folders empty**                   | Drive Stream placeholders — right-click `skills_inbox` → "Available offline," then `INGEST_AND_INDEX.bat`.                                                                               |
| **Obsidian MCP missing in Claude**         | Add the `obsidian` block from `04_Tech_Lab/config/claude_desktop_obsidian_mcp.json` to Claude Desktop config; restart.                                                                   |
| **Model keeps dropping to gemma (stalls)** | Route to OpenRouter/owl (token wall = Ollama free weekly cap). See M7_LOCAL_MODEL_PLAYBOOK.md.                                                                                           |

---

## 7. ONE-PROMPT HAND-OFF (paste into Claude Code to run the OS)

```
Read 01_Command_Center/M7_MASTER_SOP.md and treat it as your operating manual for Pineapple Contractors M7.
Then do what I ask, matching the SOP. Always: draft PAUSED to Outbox_Drafts, run brand_firewall.py --check,
keep CPPA/IKO/no-green/972-928-0788, never restructure folders, never publish or spend. Confirm you've read
it and list the SOPs you can run.
```

---

## 8. SOP LIBRARY INDEX (other SOPs in the vault — read on demand)

In `03_Knowledge_Mat/00_Atlas/`: Omnichannel SEO Everywhere · Dynamic Review Velocity · Meta Offensive
Guardrails · GCP/Docker Persistence · NotebookLM + Obsidian Infinite Memory Loop · Paperclip + Hermes
One-Person Empire · Local Memory & Execution Bridge · Agent OS Contractor Playbook · Building AI Systems
with Gemini & NotebookLM. Plus the 48 kits in `04_Tech_Lab/skills_inbox/` (catalogued in M7_SKILLS_CATALOG.md).
If Saia references an SOP not here, search the vault for it before saying it's missing.


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
