---
type: icm_folder_sop
title: M7 ICM — Folder Structure as Agent Architecture (the playbook's operating system)
status: active
date: 2026-08-13
source: Van Clief & McDermott, "Interpretable Context Methodology" (arXiv:2603.16021) + icm-architect skill + M7 NotebookLM "VanClief AI Folders Stack" (brand-scrubbed)
brand_lock: CPPA not "free" · IKO Certified not GAF · Navy #1A365D + Gold #FBC02D + Cyan #00BFFF · ZERO green · "The Pineapple Standard" / "Roofing Made Sweeter" · NO Tongan proverbs · NO "warrior/six brothers/toa" · RCAT #03-0637 · (972) 928-0788
---

# 🗂️ M7 ICM — FOLDER STRUCTURE AS AGENT ARCHITECTURE
**The one idea:** the *folders themselves* are the AI's brain. Numbered folders = the steps of a job. Plain markdown files = the instructions + context for each step. Scripts do the mechanical work. **One** AI agent reads the right file at the right moment — no expensive multi-agent framework, no "AI amnesia." A human can open any folder and see exactly what state the system is in ("glass box"). — Van Clief, ICM (arXiv:2603.16021)

> **Your 4-Fala folders are ALREADY 80% ICM.** This SOP formalizes the rest (adds the routing files + persistent memory) — **no risky vault move, no rename.** We stay in `C:\Pineapple Contractors M7`.

---

## THE 5 PRINCIPLES (why it works — 50-year-old proven engineering)
1. **One stage, one job.** Each folder does ONE step and writes to its own `output/`. A folder that researches doesn't also write; one that writes doesn't also render.
2. **Plain text is the interface.** Everything is `.md` / `.json`. Any tool reads it; any human edits it in a text editor.
3. **Load only what the step needs.** The agent reads down only as far as it must — less irrelevant context = better, cheaper output.
4. **Every output is an edit surface.** Each step's result is a file you can open, fix, and save before the next step runs. The next step reads whatever you left there.
5. **Configure the factory, not the product.** Set brand/voice/style ONCE (the factory). Every run produces a new deliverable from that same config.

*Consequence: sequencing = folder numbers · context scoping = folder hierarchy · state = files on disk · coordination = one folder's output is the next folder's input.*

---

## THE 5-LAYER CONTEXT HIERARCHY (what reads what)
| Layer | File | Answers | Role | Size |
|---|---|---|---|---|
| **L0** | `CLAUDE.md` (root) | "Where am I?" | identity + routing | <200 lines / ~800 tok |
| **L1** | `CONTEXT.md` (root) | "Where do I go?" | the router | ~300 tok |
| **L2** | `CONTEXT.md` (in each folder) | "What do I do?" | **the control point** (Inputs/Process/Output/Human-check) | 200–500 tok |
| **L3** | `references/`, `Brand_DNA/`, `_shared/` | "What rules apply?" | the **factory** (stable — brand, voice, design) | 500–2k tok |
| **L4** | `output/`, `Outbox_Drafts/` | "What am I working with?" | the **product** (per-run drafts) | varies |

- **L0–L2 = the catalog:** small, stable, they *point* at things and store almost nothing.
- **L3 = the recipe** (brand law, voice, design system) — internalized as constraints.
- **L4 = the ingredients + the dish** (this run's draft) — processed as input.

---

## HOW M7'S 4-FALA FOLDERS MAP TO ICM (already aligned)
| Your folder | ICM role | Its ONE job |
|---|---|---|
| **`CLAUDE.md`** (root) | **L0** identity | The constitution every agent reads first. Brand law + routing. Already exists ✅ |
| **`CONTEXT.md`** (root) | **L1** router | *NEW* — "which folder handles what." Added by this SOP. |
| **`01_Command_Center`** | L1/L3 — strategy + factory | Playbooks + `Brand_DNA/` (the recipe). No code, no media here — read strategy + brand, set direction. |
| **`02_Media_Vault`** | **L3** references (read-only) | The 39 GB visual inventory (drone/roofs/family b-roll). Read-only proof assets. Naming: `YEAR_MONTH_CAMPAIGN`. |
| **`03_Knowledge_Mat`** | L3/L4 — the woven brain | Obsidian second brain: research → structured JSON contracts + script drafts. Has the Map-of-Content index. |
| **`04_Tech_Lab`** | **L4** stage / tools | The engine room: CLI scripts (video, scraping, Meta uploader). Deterministic, mechanical — no AI needed. |
| **`Outbox_Drafts`** | **L4** product | Every finished draft lands here **PAUSED** until Saia says GO. |
| **`_memory/`** | persistent state | *NEW* — the "no-amnesia" bridge: `task_plan / findings / progress / decisions`. Added by this SOP. |

---

## WHAT I ADDED TODAY (safe, additive — nothing moved or deleted)
1. **`CONTEXT.md`** (root) — the L1 router.
2. **`_memory/`** — `task_plan.md`, `findings.md`, `progress.md`, `decisions.md` (ICM "Protocol 0" — the AI resumes after a crash without re-explaining).
3. **`CONTEXT.md`** inside `01/02/03/04` — each folder's L2 "one job" contract.

## HOW TO USE IT (daily)
- **Start a job:** tell Claude the goal. It reads `CLAUDE.md` (L0) → root `CONTEXT.md` (L1) → the right folder's `CONTEXT.md` (L2) → loads only that folder's references (L3) + inputs (L4).
- **Edit anything:** open the `.md` file, change it, save. The next step picks up your edit. That's the whole control surface — no code.
- **Restructure deeper later:** the **`icm-architect`** skill is now installed. Say *"ICM this folder"* / *"restructure 03_Knowledge_Mat to ICM"* — it audits, proposes a migration map **for your approval**, then migrates and runs the "walk test" (a fresh agent must orient from the files alone).

## NAMING LAW (ICM conventions, M7-locked)
- Stage folders: `NN_kebab-name` (number = order).
- System/meta folders: underscore prefix, sort to top (`_memory/`, `_shared/`, `_templates/`).
- Media assets: `YEAR_MONTH_CAMPAIGN_ASSET-TYPE`.
- One home per fact — a link beats a copy (duplication is how structures rot).
- The structure IS the documentation: if it needs explaining, the explanation goes in that folder's `CONTEXT.md`.

## ⚠️ WHAT I DELIBERATELY DID NOT DO (from the notebook blueprint)
The NotebookLM synthesis was **pre-brand-scrub** — it is NOT safe to apply as-is:
- ❌ Renaming the vault to `C:\Pineapple-Mana-Global` / consolidating 5 folders — **massive, risky move**; we stay put.
- ❌ Tongan proverbs, "warrior / six brothers / toa", `TATAFU_BRAND` proverb file — **banned** by M7 brand law.
- ❌ "GAF Certified" → must be **IKO Certified**. ❌ Green `#2D7D46` → **zero green**.
- ✅ Kept only the **structure** (layers, routing, memory, JSON contracts, read-only media), brand-clean.

<!-- M7-FIREWALL-EXEMPT: governance-reference (ICM methodology SOP; "free" named only as the banned term) -->
