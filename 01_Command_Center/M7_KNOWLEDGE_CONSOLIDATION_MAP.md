---
title: M7 KNOWLEDGE CONSOLIDATION MAP — One Brain Across Two Accounts
status: active reference
date: 2026-07-24
---

# 🧠 M7 KNOWLEDGE CONSOLIDATION MAP

## THE PRINCIPLE (the answer to "how do I work with all this collectively")
You have valuable SOPs scattered across **NotebookLM (2 Google accounts) + Gemini Gems**. Trying to
*work across* two clouds is the trap — context gets lost, and only the agent logged into that
account can see it.

> **The fix: the VAULT is the one brain. NotebookLM + Gems are SOURCES, not the home.**
> You distill each notebook/Gem down to a markdown SOP in the vault. Once it's markdown here,
> **it doesn't matter which Google account it came from** — Hermes, Claude, and Codex all read the
> vault, not the cloud. Two accounts become irrelevant.

This is your own system's law: *the local filesystem is the single source of truth.*

## THE 4 HUBS → VAULT HOMES
Your Gemini Gems are already organized as 4 HUBS. Mirror each one as a vault SOP so it's permanent:

| HUB (Gemini Gem) | Purpose | Vault home |
|---|---|---|
| **HUB 1 — PM7 SEO Playbook** (Traffic Engine) | GSC analytics, keyword→page engine | `03_Knowledge_Mat/active_context/M7_SEO_DAILY_SOP.md` ✅ done |
| **HUB 2 — PM7 Brand & Content** (Cultural Soul) | Brand law, Goldie Omnipresence, voice | `00_Atlas/2026-07-24_SOP_Goldie_Omnipresence_Stack.md` ✅ done |
| **HUB 3 — PM7 Ops & SOP** (Mission Control) | Operating manual, agent orchestration | `01_Command_Center/MASTER_PLAYBOOK.md` (already here) |
| **HUB 4 — PM7 SEO Mastery Library** (Nico + Goldie + Skool) | The deep SEO source library | → distill to `00_Atlas/` (pending) |
| Custom Gems: Frisco SEO Architect · Sandcastles Hook Analyst | Specialist prompt personas | → `03_Knowledge_Mat/00_Atlas/gems/` (pending) |

## THE NOTEBOOKS (both accounts) → treat as SOURCE LIBRARIES
NotebookLM = your research/source layer (300+ sources in PM7 SEO Mastery alone). You don't move all
sources into the vault — you pull the **distilled outputs** (reports, playbooks, the SOP text) down.
Two ways:
1. **The Agentic OS "Notebook" module** — already downloads notebook assets to
   `AGENTIC OS/notebooks/_assets/` (41 saved). Use its Assets → Save to keep the good ones.
2. **The NotebookLM MCP / `nlm` CLI** — switches between your two accounts:
   - `nlm login switch business` → pull from the 108-notebook account
   - `nlm login switch personal` → pull from the 22-notebook account
   - Then query/export each notebook's report → save as markdown in `00_Atlas/`.

Keep `NOTEBOOKLM_INDEX.md` (already in vault) as the master list of every notebook, which account
it's on, and its purpose.

## THE WORKFLOW (repeat for each notebook/Gem worth keeping)
1. Open the notebook/Gem → generate its best summary/SOP output.
2. Copy it (or export via the OS Notebook module / nlm).
3. Save as a dated markdown SOP in `03_Knowledge_Mat/00_Atlas/` (permanent) or `active_context/` (Hermes-learnable).
4. Add a one-line pointer in `00_Atlas/SOP_INDEX.md`.
5. In Hermes: `/learn <that file>` so it enters the shared brain.

Once distilled, **retire the "which account" problem** — the vault is the single place all agents read.

## WHAT'S DONE vs PENDING
| ✅ Captured to vault | ⏳ Still to distill |
|---|---|
| HUB 1 → M7_SEO_DAILY_SOP.md | HUB 4 (SEO Mastery Library, 300 sources) |
| HUB 2 → Goldie Omnipresence Stack | Frisco SEO Architect + Sandcastles gems |
| HUB 3 → MASTER_PLAYBOOK.md | Personal-account notebooks (22) sweep |

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
