---
type: parallel_execution_runbook
status: active
last_updated: 2026-06-17
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# M7 — MAX-OUT PARALLEL EXECUTION PLAN

Run these four tracks at the same time while the 47 Gumroad products download. Golden rule to avoid collisions: **only ONE agent edits code/files at a time.** The others do read-only research, environment setup, or work in separate folders.

## TRACK ASSIGNMENTS (who does what, in parallel)

| Track | Tool | Job | Touches |
| :--- | :--- | :--- | :--- |
| A | **You (terminal/CLI)** | Environment setup only a human can do | installs, plugins, services |
| B | **Claude Code (CLI)** | Autonomous file/script execution + verification | the vault (owns edits) |
| C | **Cursor (Agent mode)** | Visual feature build / review | one feature branch/file |
| D | **Antigravity / NotebookLM** | Research + content drafts (read-only → Outbox PAUSED) | research stage only |

> Run Track B **or** Track C as the "code editor" at a given moment — not both on the same file. Easiest: let Claude Code own edits today; use Cursor only to review.

---

## TRACK A — YOU (CLI / terminal): ~15 min of setup
These unblock everything else and only you can do them:
```powershell
# 1. Install Claude Code
irm https://claude.ai/install.ps1 | iex

# 2. Local model runtime
ollama serve
ollama pull gemma4-pineapple        # (or: ollama pull qwen2.5-coder:14b)

# 3. One-time git backup of the vault (safety net before agents edit)
cd "C:\Pineapple Contractors M7"
git init && git add -A && git commit -m "M7 baseline before parallel run"
```
Then in Obsidian: enable **Local REST API** + **MCP Tools** (key already wired), confirm `http://127.0.0.1:27124`.

---

## TRACK B — CLAUDE CODE (CLI): autonomous execution
Open a terminal in the vault (`cd "C:\Pineapple Contractors M7"` → `claude`) and paste:
```text
Ground in 01_Command_Center/GROUNDING.md and MASTER_PLAYBOOK.md. Keep Outbox Shield
(all delivery PAUSED). Execute sequentially, verifying after each step:
1. python 04_Tech_Lab/Scripts/brand_firewall.py --fix      (sweep whole vault)
2. python 04_Tech_Lab/Scripts/m7_aggregate.py              (flatten raw -> 00_Atlas, rebuild INDEX)
3. python 04_Tech_Lab/Scripts/m7_cleanup.py                (dry-run dupes; report only)
4. python 04_Tech_Lab/Scripts/m7_factory.py --demo         (sample PAUSED drafts to Outbox)
5. node --check 04_Tech_Lab/server.js && python -m py_compile 04_Tech_Lab/Scripts/*.py
6. Print the folder tree + a status matrix of every file (EXISTS/COMPLIANT).
Then create a root CLAUDE.md that pins: Outbox Shield = PAUSED, no green, banned-lexicon
auto-mutate, and "syntax-check before done."
```
Leave this running too (auto-files zips as they land):
```powershell
python 04_Tech_Lab\Scripts\m7_skill_intake.py --watch
```

---

## TRACK C — CURSOR (Agent mode): build/review one feature
Open the vault folder in Cursor, `Ctrl+I`, set **Agent**, paste ONE of:
```text
@04_Tech_Lab/server.js Add an /api/obsidian-health route that GETs
http://127.0.0.1:27124/vault/ with the bearer token from config/.env and returns
{online:true/false}. Then add a "Vault / MCP" health card to
@01_Command_Center/OS_Dashboard.html next to the model fleet. Run node --check after.
```
or (lower risk, read-only):
```text
Review @04_Tech_Lab/server.js and @01_Command_Center/OS_Dashboard.html for bugs,
dead code, and missing error handling. List findings as a checklist. Do not edit yet.
```

---

## TRACK D — ANTIGRAVITY / NOTEBOOKLM: research + drafts (no code)
These are model endpoints, not editors — use them for content that lands PAUSED in the Outbox:
- **NotebookLM:** upload the new template/SOP sources, run "Based ONLY on these sources, extract the 5 highest-intent Frisco roofing content gaps with citations."
- **Antigravity/Gemini:** draft 3 GEO landing-page outlines (Heritage / CPPA Value / Premium Durability angles) using the PACT framework — save as drafts for human review, never publish.

---

## THE DOWNLOAD LOOP (as Gumroad finishes, in batches of ~10)
1. Drop downloaded files (zip / loose / folder — all fine) into `04_Tech_Lab\skills_inbox\`.
2. If the `--watch` from Track B is running, it auto-processes. Otherwise double-click `INGEST_SKILLS.bat`.
3. After all 47: `python 04_Tech_Lab\Scripts\m7_aggregate.py` to index everything into `00_Atlas\INDEX.md`.

---

## GUARDRAIL (all tracks)
No agent flips `delivery_status` off PAUSED. No agent holds payment/ad API keys. You click publish — that's the only manual gate, by design.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
