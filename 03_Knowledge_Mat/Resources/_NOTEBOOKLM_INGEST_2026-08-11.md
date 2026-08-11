---
title: NotebookLM Ingest — 2026-08-11 (2 notebooks → vault)
type: ingest_summary
status: active
date: 2026-08-11
brand_lock: CPPA not "free" · IKO Certified not GAF · zero green · Roofing Made Sweeter · no proverbs
---

# 📥 NotebookLM → Vault Ingest — 2026-08-11

Pulled **both notebooks directly** (via the NotebookLM connection), scrubbed, and structured into PARA **Resources**. **63 notes total.** Everything is a **DRAFT** — nothing publishes or runs until you say GO (Outbox Shield).

## What landed & where

| Notebook | Notes | Folder |
|---|---|---|
| **PM7 SEO Mastery (Nico + Skool)** | 20 | [`Resources/NotebookLM_SEO_Mastery_2026-08-11/`](NotebookLM_SEO_Mastery_2026-08-11/_INDEX.md) |
| **Pineapple M7 Agent OS Master SOP 8/26** | 43 | [`Resources/NotebookLM_MasterSOP_2026-08-11/`](NotebookLM_MasterSOP_2026-08-11/_INDEX.md) |

Each folder has an **`_INDEX.md`** (table of every note + review flags) and a **`_PROMPTS_LIBRARY.md`** (the extracted prompt/code blocks — 56 + 117 = **173 blocks** saved for reuse).

## The scrub I applied (safe + automatic)
- **Removed** every Tongan-proverb line.
- **GAF → IKO Certified** (unambiguous, auto-replaced).
- **Flagged (not blind-replaced)** any note containing **"free"** or **"green"** — 56 notes flagged — because these are internal SOPs and "free tool"/"green light" shouldn't be mangled. Review those before anything customer-facing ships.

## The high-value assets now in your vault
**Operating manuals & architecture:** PM7 Master Knowledge Mat & Operational Blueprint · PM7 Agentic OS Master Operational Manual · Hermes Command Desk (Architecture, Soul, Agent Ops) · Hermes AI Agent Operational Manual · PM7 Omni-Channel Engine Runbook · Compound Employee Configuration Matrix · Architecting the Local Agent OS & Brand Firewall.

**SEO / GEO strategy:** 2026 Generative Engine Optimization (GEO) Framework · Five-Site Flywheel Strategy · Goldie Search Gravity Stack · Local SEO Brain (structured AI memory) · SEO Architecture & Siloing · Frisco SEO + Shingle Comparison · GBP Audit & WordPress Migration.

**Automation SOPs:** M7 → n8n Webhook Bridge Setup · Outbox Watcher config · WordPress Category Mapping & Migration · Broken-Link Audit · Agent-to-Agent Protocol · System Integration & Prompt Catalog.

## ⚠️ Two honest notes
1. **Raw code files** (`m7_n8n_webhook_bridge.py`, `LAUNCH_WATCHER.bat`, `outbox_watcher-v3.py`, `wp_broken_link_scanner.py`, `cppa-calculator-code.md`) are **"download-only" Studio artifacts**, not text notes — they did **not** come through this pass. I can fetch them separately, but they're AI-generated code and must be **reviewed before running** (verify-don't-hallucinate + Outbox Shield).
2. A few notes are **near-duplicates** (e.g., 3 copies of the Master Knowledge Mat) — kept as-is; say the word and I'll dedupe.

## ✅ Next steps (your call)
1. **Review the ~56 flagged notes** (or tell me to auto-convert "free"→CPPA across them).
2. **`/wiki-ingest`** these two folders so your agents can answer grounded questions from them.
3. **Pull the raw code artifacts** into a `04_Tech_Lab` staging area for review.
4. **Promote the best prompts** from the two `_PROMPTS_LIBRARY.md` files into your [Prompt Control Panel](../../01_Command_Center/M7_PROMPT_CONTROL_PANEL.md).

<!-- M7-FIREWALL-EXEMPT: governance-reference (ingest summary; "free"/"green" named only as the terms being reviewed) -->
