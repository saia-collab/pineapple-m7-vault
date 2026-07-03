---
type: operator_prompt
status: active
last_updated: 2026-06-17
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# HOW TO DRIVE THE M7 OS WITH CLAUDE CODE

## Do you need Cursor or an IDE?
No. Three ways to run things, easiest first:

1. **Double-click the `.bat` files** — no IDE, no terminal. `RUN_M7_DASHBOARD.bat` (start everything) and `INGEST_SKILLS.bat` (process zips). This covers 90% of daily use.
2. **Claude Code (CLI)** — best for "execute the rest of the playbook autonomously." Your `.claude/settings.json` is already set so it won't stop to ask permission inside this vault. Install once, then run from the vault.
3. **Cursor / VS Code** — optional. Works as an editor, but Cursor's agent is separate from Claude Code and won't use this vault's `.claude/settings.json` permission profile. Use it only if you prefer a GUI; it's not required.

## One-time Claude Code install
```
npm install -g @anthropic-ai/claude-code
cd "C:\Pineapple Contractors M7"
claude
```
(If you want zero prompts: `claude --dangerously-skip-permissions`)

## MASTER PROMPT — paste this into Claude Code
```
You are the M7 Lead Systems Architect operating inside C:\Pineapple Contractors M7.
Ground every action in 01_Command_Center\GROUNDING.md and 01_Command_Center\MASTER_PLAYBOOK.md.
Hard rules: never use banned terms (Free, Warrior, Toa, Six Brothers, Consultation, GAF, $0 Down,
Save Money); never output the color green; keep all ad/web/social delivery PAUSED in
01_Command_Center\Outbox_Drafts\ (Outbox Shield) — never publish live or move money.

Execute autonomously, in order, fixing any error you hit:
1. Run: python 04_Tech_Lab\Scripts\setup_m7.ps1   (verify the 4-Fala topography, zero drift)
2. Run: python 04_Tech_Lab\Scripts\brand_firewall.py --fix   (sweep the whole vault)
3. Run: python 04_Tech_Lab\Scripts\m7_aggregate.py   (flatten raw -> 00_Atlas)
4. Run: python 04_Tech_Lab\Scripts\m7_factory.py --demo   (build PAUSED drafts to Outbox)
5. Ingest any zips: python 04_Tech_Lab\Scripts\m7_skill_intake.py
6. Start the engine: node 04_Tech_Lab\server.js   (dashboard + APIs on :3000)
7. Print the final folder tree and a summary of what changed.
Conclude with: Ko e hala 'o e fononga ko e faka'apa'apa.
```

## To ADD a new playbook (from a Claude chat, a doc, or a paste)
```
Read the file I just added at 03_Knowledge_Mat\raw\<NEW_PLAYBOOK>.md.
Reconcile it into 01_Command_Center\MASTER_PLAYBOOK.md WITHOUT duplicating existing
sections. Apply the brand firewall lexicon + green ban. Preserve the 4-section structure
(Core Architecture, File Spec Table, Stage-Contract Contexts, Automation Ready Content).
Then run brand_firewall.py --fix and report what merged.
```

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
