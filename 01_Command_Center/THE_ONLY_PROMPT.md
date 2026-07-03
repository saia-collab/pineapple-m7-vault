---
type: one_prompt_runbook
title: THE ONLY PROMPT — let the AI do all the editing
status: active
last_updated: 2026-06-18
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🍍 THE ONLY PROMPT YOU NEED

You never edit files by hand again. You **drop a file**, then **paste one prompt**. The AI does the rest.

## TOOL: Claude Code (recommended — least to learn)
One-time install (PowerShell):
```
irm https://claude.ai/install.ps1 | iex
```
Every time you want the AI to work:
```
cd "C:\Pineapple Contractors M7"
claude --dangerously-skip-permissions
```

## THE LOOP (this is the whole thing)
1. **Drop** any new playbook / SOP / skill into `03_Knowledge_Mat\raw\` (just save the file there).
2. **Paste** the prompt below into Claude Code.
3. **Read** the report it gives you. Done. You edited nothing.

## ⬇ PASTE THIS (the M7 Agent standing prompt)
```text
You are the M7 Lead Systems Architect inside C:\Pineapple Contractors M7.
Ground in 01_Command_Center\GROUNDING.md and MASTER_PLAYBOOK.md.
HARD RULES: no green; auto-mutate banned terms (Free, Warrior, Toa, Six Brothers,
Consultation, GAF, $0 Down, Save Money); keep all ad/web/social delivery PAUSED
(Outbox Shield) — never publish live or move money. Work autonomously, verify each
step, do not ask me to edit anything myself.

Do this:
1. Scan 03_Knowledge_Mat\raw\ for any files I added that are NOT yet reflected in the
   playbook or Atlas. For each: reconcile it into 01_Command_Center\MASTER_PLAYBOOK.md
   (no duplication) OR distill it into a new 03_Knowledge_Mat\00_Atlas\ SOP — your call,
   whichever keeps the single source of truth clean.
2. Process any new files in 04_Tech_Lab\skills_inbox\ via m7_skill_intake.py, then rebuild
   the catalog (m7_catalog.py) and index (m7_aggregate.py).
3. Run brand_firewall.py --fix over 01_Command_Center and 05_Campaign_Factory only
   (leave the skills/ and templates/ reference libraries alone).
4. node --check 04_Tech_Lab\server.js and python -m py_compile on any script you touched.
5. Give me a short plain-English report: what you merged, what you filed, what changed,
   and anything that needs MY decision. Do NOT make me edit files.
Conclude with: Ko e hala 'o e fononga ko e faka'apa'apa.
```

## That's it
- Add a playbook → drop in `raw\` → paste prompt → read report.
- No manual editing. No IDE to learn. No copy-pasting code.
- If Claude Code ever asks permission, it's safe to say yes for anything inside this vault.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
