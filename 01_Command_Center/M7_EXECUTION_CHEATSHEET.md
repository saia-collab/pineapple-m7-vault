---
type: execution_cheatsheet
status: active
last_updated: 2026-06-17
classification: M7_Command_Level_1
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# M7 AGENTIC OS — EXECUTION CHEAT SHEET

A single-glance map of what has been executed, what **you** need to do, and what **Claude Code** can execute for you. Tracks the original M7 Agentic OS Execution Plan (Phases 1–4) plus the Command Center build-out.

**Legend:** ✅ Done · 🟡 Your action · ⬜ Claude Code can run

---

## PHASE STATUS (vs. the original Execution Plan)

| Phase | Objective | Status |
| :--- | :--- | :--- |
| **1. Local File Scaffolding** | Build the immutable 4-Fala topography | ✅ Done |
| **2. Brand Constitution & Firewall** | MASTER_PLAYBOOK + `brand_firewall.py` + GROUNDING | ✅ Mostly (see 🟡 GROUNDING) |
| **3. Dashboard Rebuild & Integrations** | Local `OS_Dashboard.html` + Drive + MCP | ✅ Done |
| **4. Recursive Completion / Verification** | Run firewall, verify zero drift | ✅ Done |
| **5. AI Model Fleet (added)** | Ollama, Hermes, Antigravity, NotebookLM on one panel | ✅ Done |
| **6. Live Execution (added)** | Task runner, Hermes goals, trend sparklines | ✅ Done |

---

## ✅ WHAT HAS BEEN EXECUTED

**Command Center (`01_Command_Center/`)**

- `MASTER_PLAYBOOK.md` — single source of truth (4 sections, brand-compliant, closing mandate)
- `ARCHITECTURE_MCP_MAP.md` — line-by-line tree + Drive mirror + `.obsidian` patch
- `CROSS_AGENT_PROTOCOL.md` — universal JSON envelope for Claude/Hermes/OpenClaw/NotebookLM
- `START_HERE.md` — operator runbook
- `OS_Dashboard.html` — live command center (fleet, task runner, firewall terminal, sparklines)
- `avatar_telemetry.json` — live 1-3-12 telemetry feed
- `CONTEXT.md` — stage-contract gates (8 total across rooms + factory stages)

**Tech Lab (`04_Tech_Lab/`)**

- `Scripts/brand_firewall.py` — banned-term mutation, green block (exit 1), `--fix/--report/--watch`
- `Scripts/m7_scoring.py` — Elite Lead Matrix + 1-3-12 kill/scale engine
- `Scripts/setup_m7.ps1` — scaffolder / pre-flight
- `server.js` — engine: `/api/metrics`, `/api/models`, `/api/execute`, `/api/ollama`, `/api/hermes`, `/api/history`, `/api/telemetry`
- `config/models.json` — AI fleet endpoints
- `config/claude_desktop_config.json` + `antigravity_mcp.json` + `.env` — MCP wiring (local-only)
- `logs/telemetry_history.json` — rolling trend history

**Vault wiring**

- `.obsidian/plugins/obsidian-local-rest-api/data.json` — API key + HTTP port **27124**
- `.obsidian/plugins/mcp-tools/data.json`, `community-plugins.json`, `appearance.json` (gold accent)
- `.claude/settings.json` — non-interactive execution allow-list (live ad publishing stays denied)
- `RUN_AGENT_OS.bat` — one-click launcher
- Full 4-Fala folder topography scaffolded; configs JSON-validated; firewall + scoring tested live

---

## 🟡 WHAT YOU NEED TO DO (one-time, ~10 min)

1. **Let Google Drive finish syncing** — watch for the green check in the Drive tray before launching (the files are saved; Drive just needs to settle).
2. **Launch:** double-click **`RUN_AGENT_OS.bat`** → opens `http://localhost:3939/OS_Dashboard.html`.
3. **Obsidian plugins:** open the vault → Settings → Community plugins → enable **Local REST API** and **MCP Tools** (key already wired). Confirm `http://127.0.0.1:27124` is live.
4. **Connect agents:** copy the MCP configs into place, then restart the apps:
   - `04_Tech_Lab\config\claude_desktop_config.json` → `%APPDATA%\Claude\claude_desktop_config.json`
   - `04_Tech_Lab\config\antigravity_mcp.json` → `%APPDATA%\antigravity\mcp.json`
5. **Bring the fleet online:** `ollama serve` then `ollama pull gemma4-pineapple` (Ollama card flips to ONLINE).
6. **Set real ports** in `04_Tech_Lab\config\models.json` for Hermes (`command_url`), Antigravity, NotebookLM so their cards light up.
7. **Rotate the API key** if this chat was shared — the key is in local configs and the transcript.
8. **(Recommended)** move from HTTP 27124 to HTTPS 27123 once wiring works (install the cert).

---

## ✅ NOW EXECUTED (was the ⬜ list)

1. **`GROUNDING.md`** — brand constitution deployed to root + `03_Knowledge_Mat/`. ✅
2. **Support scripts** — `m7_fetch.py`, `m7_cleanup.py`, `m7_aggregate.py` built + tested. ✅
3. **Full factory pipeline** — `m7_factory.py` runs 10→20→30 and writes `approved.json` + PAUSED drafts into `Outbox_Drafts/`. ✅
4. **Skill / Template intake** — `m7_skill_intake.py` + `INGEST_AND_INDEX.bat` + `04_Tech_Lab/skills_inbox/`. ✅

### 📥 TOMORROW — the 15 skill/template zips (drag-drop, no manual filing)

1. Drop all 15 `.zip` files into **`04_Tech_Lab\skills_inbox\`**.
2. Double-click **`INGEST_AND_INDEX.bat`** (vault root).
3. Each zip is auto-classified (Skill → `04_Tech_Lab\skills\`, Template → `03_Knowledge_Mat\00_Atlas\templates\`), firewall-scanned + mutated, and logged to `04_Tech_Lab\logs\skill_intake_log.json`.
4. Tested live: skill vs template detection, filing, and banned-term mutation all confirmed working.

### ⬜ Optional polish (only if you want it)

- Obsidian MCP health card on the dashboard (ping `127.0.0.1:27124/vault/`).
- `--watch` mode for hands-free intake: `python 04_Tech_Lab\Scripts\m7_skill_intake.py --watch`.

---

## QUICK REFERENCE

**Commands**

```bash
# Launch everything
RUN_AGENT_OS.bat

# Engine only
node 04_Tech_Lab\server.js                         # http://localhost:3939

# Brand firewall
python 04_Tech_Lab\Scripts\brand_firewall.py --report   # scan
python 04_Tech_Lab\Scripts\brand_firewall.py --fix      # auto-mutate
python 04_Tech_Lab\Scripts\brand_firewall.py --watch    # live listener

# Scoring / telemetry
python 04_Tech_Lab\Scripts\m7_scoring.py --demo

# Scaffold / verify
powershell -ExecutionPolicy Bypass -File 04_Tech_Lab\Scripts\setup_m7.ps1

# Factory pipeline (writes PAUSED drafts to Outbox_Drafts)
python 04_Tech_Lab\Scripts\m7_factory.py --demo

# Knowledge_Mat: flatten raw -> 00_Atlas
python 04_Tech_Lab\Scripts\m7_aggregate.py

# Housekeeping: dedupe (dry-run, then --apply)
python 04_Tech_Lab\Scripts\m7_cleanup.py
python 04_Tech_Lab\Scripts\m7_cleanup.py --apply

# Research capture
python 04_Tech_Lab\Scripts\m7_fetch.py --url https://example.com

# Skill / Template intake (the 15 zips)
INGEST_AND_INDEX.bat
python 04_Tech_Lab\Scripts\m7_skill_intake.py --watch
```

**Ports**

| Port | URL | Use |
| :--- | :--- | :--- |
| 3939 | `http://localhost:3939` | M7 Engine + dashboard + APIs |
| 27124 | `http://127.0.0.1:27124` | Obsidian REST API (initial wiring) |
| 27123 | `https://127.0.0.1:27123` | Obsidian REST API (secure) |
| 11434 | `http://localhost:11434` | Ollama |

**Dashboard APIs:** `/api/metrics` · `/api/models` · `/api/execute` · `/api/ollama` · `/api/hermes` · `/api/history` · `/api/telemetry`

**Guardrails (always on):** banned terms auto-mutated · green = build fail · all ad delivery PAUSED (Outbox Shield) · human authorization required to go live.

---

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
