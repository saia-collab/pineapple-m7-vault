---
title: M7 Folder Cleanup — DRY RUN (nothing moved yet)
type: cleanup_plan
status: PAUSED — approve buckets, then I (or a Hermes goal) execute
date: 2026-08-06
rule: nothing is deleted; "delete-candidates" go to _Archive first, kept 30 days
---

# 🧹 M7 FOLDER CLEANUP — DRY RUN

Scan of the vault ROOT (`C:\Pineapple Contractors M7`). Three buckets. **Nothing has moved.**
Reply with which buckets to run (e.g. "run ARCHIVE + tidy MD"), or hand the whole thing to a Hermes goal (prompt at bottom).

## ✅ KEEP (do not touch — active system)
- `01_Command_Center` `02_Media_Vault` `02_Workspaces` `03_Knowledge_Mat` `04_Tech_Lab` `05_Campaign_Factory` — the 4-Fala + factory
- `Agentic OS/` — the OS/Hermes memory output (Memory tab reads this). Active.
- `.obsidian` `.claude` `.claudian` `.git` `.gitignore` — system
- `Launcher_Archive/` — where old launchers already went
- Desktop **LAUNCH_ALL.bat** stays your one master launcher

## 📦 ARCHIVE → move to a new `_Archive/2026-08-06/` (reversible, frees ~30MB)
Old install packs + redundant zips — the 08-06 build is live, these are superseded:
- `agent-os-pack-2026-07-03.zip` (11MB), `agent-os-pack-2026-07-05.zip` (16MB)
- `mobbin-sample-pack-100.zip` (2MB), `seo-pack.zip`, `CLAUDE MOBILE.zip`
- zip'd launchers: `AM_STARTUP.zip`, `AM_STARTUP (2).zip`, `LAUNCH_CLAUDE_CODE.zip`, `M7_CLEANUP.zip`, `M7_DOCTOR.zip`, `ORGANIZE_MEDIA.zip`
- empty/broken root launchers (0KB, superseded by Desktop master): `RUN_AGENT_OS.bat`, `RUN_AGENT_OS.bat - Shortcut.lnk`, `START_LOCAL_STUDIO.bat`, `START_PAPERCLIP.bat`, `UPDATE_AGENT_OS.bat`

## 🗂️ TIDY LOOSE .MD → move into `03_Knowledge_Mat/00_Atlas/` (or 01_Command_Center)
These SOP/reference notes are loose at root; they belong in the knowledge mat:
- `How to Dominate _Near Me_ Searches PM7.md` (3.3MB), `HERMES AGENTIC SOP_ _Near Me_ Domination Pipeline.md`
- `EXCTRACT 23rd May_ Hermes Agent SEO SOP AND THE.md`, `Accessing and Editing WordPress Website.md`
- `ElevenLabs_ Spoken Voice Output Choice.md`, `Understand Anything_ Turn Any Codebase...md`, `USER.md`, `LAUNCHERS_README.md`
- KEEP at root (tools expect them there): `CLAUDE.md`, `m7_execution_manifest.md`, `GSC_Connect.bat`

## 🔍 REVIEW-THEN-ARCHIVE (older duplicated folders — you confirm each)
- `knowledge-base/` (6/12, the old Karpathy meta-layer — superseded by 03_Knowledge_Mat?)
- `legacy_backup/` (6/25), `Omi/` (6/12), `_Inbox_Cleanup/` (7/16), `Scheduled/` (6/22)
- `Projects/` (6/16) — confirm it's not active

## Duplicate content to dedupe (same SOP in 2 places)
- The "Near Me" pipeline exists both at root AND in 03_Knowledge_Mat — keep the 03_Knowledge_Mat copy, archive the root one.
- Multiple `agent-os-pack-*` copies exist in Downloads AND 03_Knowledge_Mat/00_Atlas/templates — keep one canonical.

---

## Hand it to an AI agent instead (if you'd rather)
Paste into **Hermes → Goal Mode**:
```
Read 01_Command_Center/Outbox_Drafts/M7_FOLDER_CLEANUP_DRYRUN.md.
Execute ONLY the ARCHIVE and TIDY LOOSE .MD buckets:
- Create _Archive/2026-08-06/ and MOVE (never delete) the listed files there.
- Move the listed loose .md files into 03_Knowledge_Mat/00_Atlas/.
- Do NOT touch the KEEP list or the REVIEW list.
- After moving, write a receipt of every file moved to Outbox_Drafts/, and git add+commit "folder cleanup 2026-08-06".
Stop and show me the receipt. Change nothing else.
```

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
