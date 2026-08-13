---
type: icm_restructure_audit
title: M7 ICM Restructure — Audit + Migration Map (icm-architect, Restructure mode)
status: active
date: 2026-08-13
note: Produced by the icm-architect skill. Safe moves = DONE. Risky moves = need Saia's approval.
---

# 🧭 M7 ICM RESTRUCTURE — AUDIT + MIGRATION MAP

## ✅ DONE (safe consolidations — loose standalone docs, no code touched)
| Moved | → | Role |
|---|---|---|
| HERMES AGENTIC SOP, How to Dominate Near Me, EXTRACT Hermes SEO SOP, Accessing WordPress | `01_Command_Center/Playbooks/` | Factory (reference SOPs) |
| ElevenLabs Voice, Understand-Anything (codebase graph) | `03_Knowledge_Mat/Resources/` | Factory (reference) |
| RUN_AGENT_OS.bat - Shortcut.lnk | `_Archive/` | Dead (superseded launcher) |

Root went from 19 loose files → 15. The root now reads as a catalog.

## ✅ KEEP AT ROOT (catalog / system / referenced by path — do NOT move)
`CLAUDE.md` (L0) · `CONTEXT.md` (L1) · `_memory/` (state) · `m7_core_rules.config` (scripts read it) · `m7_execution_manifest.md` (engineering-log convention) · `package.json` / `package-lock.json` / `server.js` (root Node server) · `START_PAPERCLIP.bat` (a Startup task points here) · `USER.md` · `LAUNCHERS_README.md` · the `.gdoc` pointers (Google-Drive-synced) · `.env` / `.gitignore` / `.claude` / `.obsidian`.

## ⚠️ NEEDS YOUR APPROVAL (structural — could break references; I did NOT touch these)
| Item | Issue | Proposed ICM move |
|---|---|---|
| **`02_Workspaces/`** | **Numbering collision** — two `02_` folders (with `02_Media_Vault`) | Renumber to `06_Workspaces/` OR fold `_SITE_BACKUPS` into `_Archive` |
| **`knowledge-base/`** | Duplicate of `03_Knowledge_Mat` | Merge unique files into `03_Knowledge_Mat/`, then `_Archive` the shell |
| **`legacy_backup/`** | Dead (old backup) | → `_Archive/legacy_backup/` |
| **`Gemini Chats/`** | Raw chat exports | → `03_Knowledge_Mat/raw/gemini-chats/` |
| **`_Inbox_Cleanup/`** | Inbox of loose files | Sort contents into rooms, then `_Archive` |
| **`Launcher_Archive/`** | Already archival | Rename → merge into `_Archive/launchers/` |
| **`Omi/`** | Omi wearable memory dump | Keep, or → `03_Knowledge_Mat/raw/omi/` |
| root `package.json` / `server.js` | Code at root | Move to `04_Tech_Lab/` **only if** nothing runs `npm start` from root (verify first) |
| `.tmp.drivedownload` / `.tmp.driveupload` | Google Drive temp junk | Leave — Drive manages them (already gitignored) |

**Why I didn't just do these:** ICM is a human-gated method, and these are folder-level moves that scripts/tasks may reference by path. Deletion is also blocked by a safety guard, so "dead" items get **archived, not deleted**. Say **"do the approved moves"** (or pick specific ones) and I'll execute them.

## 🚶 WALK TEST (passed)
- Open root → `CLAUDE.md` answers *where am I* + routes to `CONTEXT.md` → `CONTEXT.md` routes to the right room by job. ✅ (≤2 reads)
- Each room `01/02/03/04/05` has a `CONTEXT.md` stating its one job, inputs, output, human check. ✅
- Pipeline state = scan `Outbox_Drafts/` + stage `output/` folders. ✅
- Persistent state = `_memory/`. ✅
- No routing file carries content payload; brand law lives in `CLAUDE.md`, not duplicated. ✅

**Verdict:** M7 is a valid ICM workspace. The approved moves above are polish, not blockers.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
