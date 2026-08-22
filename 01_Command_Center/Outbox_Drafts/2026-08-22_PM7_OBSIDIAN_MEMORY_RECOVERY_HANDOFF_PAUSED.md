---
title: PM7 Obsidian and Shared Memory Recovery Handoff
status: PAUSED
date: 2026-08-22
owner: Saia
branch: codex/pm7-omniroute-recovery-20260822
pull_request: 2
---

# PM7 Obsidian and shared-memory recovery handoff

## Executive result

The repository recovery is prepared and statically tested. The physical Windows runtime is **not yet verified**. Do not describe Obsidian, Memory Galaxy, Local Studio, Hermes, OmniRoute, or model routes as working until the two new desktop receipts record their results.

## What Codex prepared

- Added `PM7_OBSIDIAN_RECOVER.bat` as the single Obsidian recovery launcher.
- Added `PM7_OBSIDIAN_MEMORY_RECOVERY.ps1` to terminate Obsidian, back up `workspace.json`, verify the Local REST plugin without reading its secret, focus Local Studio on `03_Knowledge_Mat`, restart Obsidian, probe `:27124`, and write a receipt.
- Added `Obsidian_Memory_Recovery_Playbook.md` with architecture, security, Codex/Hermes/Claude boundaries, rollback, and acceptance tests.
- Added `03_Knowledge_Mat/OBSIDIAN_MEMORY_CONTRACT.md` as the focused recovery authority. Republishing the broader legacy `SHARED_MEMORY.md` was blocked pending explicit public-disclosure approval.
- Replaced the obsolete hard-coded `sync_memory.py` behavior with the root-relative `memory_sync.py` compiler.
- Extended `PM7_REPAIR_AND_VERIFY.bat` verification to check Agentic OS `vaultRoot`, `SHARED_MEMORY.md`, the Markdown corpus, and Local REST HTTPS.
- Added Windows PowerShell parsing and dependency-free tests to GitHub Actions.
- Reviewed the supplied Codex and Hermes/Memory Galaxy notes. Useful workflow ideas were retained; unsafe privacy, autonomy, unlimited-token, and installation claims were corrected.

## What Claude Code must do on the physical desktop

Work read-first. Do not overwrite Saia's dirty `main`, `CLAUDE.md`, or launcher changes.

1. Pause Google Drive sync for `C:\Pineapple Contractors M7` or move the Git working copy outside the synchronized folder.
2. Inspect `.git\refs` and remove only confirmed `desktop.ini` junk. Do not delete legitimate refs. Prove `git fetch --prune origin` succeeds.
3. Preserve the existing dirty work before any merge. Show Saia the preservation method and file list.
4. Merge PR #2 only after the Git/Drive gate is clean and Saia gives merge approval.
5. Double-click `PM7_OBSIDIAN_RECOVER.bat`.
6. Open the newest `PM7_OBSIDIAN_MEMORY_RECOVERY_*.md` receipt. Resolve failed rows and rerun until there are no failures.
7. In Obsidian Local REST API settings, Saia selects **Reset all cryptography**, confirms **Reset all crypto**, and stores the replacement credential only in an approved local secret mechanism.
8. Double-click `LAUNCH_PM7_STUDIO.bat`, then `CONFIGURE_PM7_AI_CLIENTS.bat`.
9. Complete Cursor's in-app endpoint settings and any Google/Antigravity owner OAuth prompts. Do not enable MITM, stealth, forced-credit, or automatic paid overages.
10. Double-click `PM7_REPAIR_AND_VERIFY.bat` and rerun until required checks pass or the receipt names a genuine owner/authentication blocker.
11. In Local Studio, open Memory and confirm linked notes from `03_Knowledge_Mat` appear. Ask Jarvis/Hermes for one fact from `SHARED_MEMORY.md` and require the source note name.

## Owner-only actions

Saia must personally:

- rotate the compromised Obsidian Local REST, OpenAI, Google, and Omega Indexer credentials;
- complete provider OAuth/login or add replacement provider keys through approved secret storage;
- approve the merge after dirty work is preserved;
- approve any WordPress publishing, outbound message, social post, email, ad spend, or live customer action.

No key value belongs in a screenshot, chat message, Markdown file, Git commit, launcher, or verification receipt.

## Acceptance evidence

Required receipts on the real Windows computer:

1. `01_Command_Center\Outbox_Drafts\PM7_OBSIDIAN_MEMORY_RECOVERY_*.md`
2. `01_Command_Center\Outbox_Drafts\PM7_LOCAL_VERIFY_*.md`

The first proves the workspace reset, plugin presence, focused memory scope, restart, and local port state. The second proves commands, Studio `:3737`, Hermes `:9119`, OmniRoute `:20128`, the memory corpus, and live automatic model routes. GitHub CI proves source syntax and static safety only.

## Current decision

**PAUSED — PR update and CI may proceed. Merge and physical Windows execution remain gated by the Drive/Git repair, credential rotation, and local receipts.**

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
