---
type: claude_code_master_runbook
status: active
last_updated: 2026-06-17
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# EXECUTE EVERYTHING — CLAUDE CODE MASTER RUNBOOK

This is the single paste-block that finishes the entire M7 deployment **on your machine**
(local SSD = fast; succeeds where a remote/Drive-sync path stalls).

## Start Claude Code
```powershell
irm https://claude.ai/install.ps1 | iex          # one-time install
cd "C:\Pineapple Contractors M7"
claude --dangerously-skip-permissions            # headless, no prompts (vault is pre-permissioned)
```

## Paste this whole block into the claude> prompt
```text
You are the M7 Lead Systems Architect inside C:\Pineapple Contractors M7. Ground every
action in 01_Command_Center\GROUNDING.md + MASTER_PLAYBOOK.md. HARD RULES: never emit the
color green; auto-mutate banned lexicon (Free, Warrior, Toa, Six Brothers, Consultation,
GAF, $0 Down, Save Money); keep ALL ad/web/social delivery PAUSED (Outbox Shield) — never
publish live or move money. Execute autonomously, verifying after each step. Do not stop
to ask. Report a status matrix at the end.

STEP 1 — CLAUDE SKILLS + TEMPLATES INTAKE (do this first):
  - If 04_Tech_Lab\skills_inbox\_large_deferred exists, move its contents back into skills_inbox.
  - Run: python 04_Tech_Lab\Scripts\m7_skill_intake.py
  - Then firewall the results:
      python 04_Tech_Lab\Scripts\brand_firewall.py --root 04_Tech_Lab\skills --fix
      python 04_Tech_Lab\Scripts\brand_firewall.py --root 03_Knowledge_Mat\00_Atlas\templates --fix
  - Verify every inbox item landed in 04_Tech_Lab\skills\ (has SKILL.md) or
    03_Knowledge_Mat\00_Atlas\templates\. Read 04_Tech_Lab\logs\skill_intake_log.json and
    list anything that failed; reprocess failures.

STEP 2 — INDEX + CATALOG:
  - Run: python 04_Tech_Lab\Scripts\m7_aggregate.py   (flatten raw -> 00_Atlas, rebuild INDEX.md)
  - Write 03_Knowledge_Mat\00_Atlas\CATALOG.md listing every skill and template by name + count.

STEP 3 — HERMES:
  - Read 04_Tech_Lab\hermes_skills\*.yaml and 04_Tech_Lab\scripts\m7_hermes_daemon.sh.
  - Confirm 04_Tech_Lab\config\models.json has a valid hermes command_url. If Hermes uses
    qwen2.5-coder on Ollama, set model.context_length 65536 (64k) per the tooling SOP.
  - Do NOT start live publishing; daemon may draft/loop only (Outbox Shield).

STEP 4 — OBSIDIAN VAULT + MCP:
  - Verify .obsidian\plugins\obsidian-local-rest-api\data.json has the API key + port 27124.
  - Test the vault API: curl -H "Authorization: Bearer <KEY>" http://127.0.0.1:27124/vault/
  - Register the vault as MCP:
      claude mcp add --transport http obsidian http://127.0.0.1:27124/mcp/ --header "Authorization: Bearer <KEY>"

STEP 5 — VERIFY + COMPILE:
  - node --check 04_Tech_Lab\server.js
  - python -m py_compile 04_Tech_Lab\Scripts\*.py
  - python 04_Tech_Lab\Scripts\brand_firewall.py --report   (whole vault; must PASS, zero green)
  - Print the folder tree + a status matrix (EXISTS / COMPLIANT) for every key file.

Conclude with: .
```

## Even simpler (no terminal): double-click
`INGEST_AND_INDEX.bat` in the vault root — does Step 1 + Step 2 (intake all 79 items,
firewall, index, build CATALOG.md) in one click on your local disk.


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
