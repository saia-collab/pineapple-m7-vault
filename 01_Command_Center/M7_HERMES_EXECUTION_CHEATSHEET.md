---
title: Hermes Execution Cheat Sheet — Chat vs Goal Mode (copy-paste ready)
status: active — Hermes now runs qwen2.5-coder:latest (local, free, uncapped)
last_updated: 2026-07-22
brand_check: CPPA · IKO Certified · RCAT #03-0637 · zero green
---

# ⚕️ HERMES CHEAT SHEET — what to run, where

## 🚦 THE GOLDEN RULES (read once)
1. **Chat = short jobs (under ~2 min).** Hermes chat **kills any task at 360 seconds.**
2. **Goal Mode = long, multi-step jobs.** ONE bounded objective per run — never "run the whole pipeline."
3. **Hermes now runs a LOCAL model** (`qwen2.5-coder:latest`) — **free, no cap, private**… but it's a **coder** model.
4. **Play to its strength.** ⬇️

| Give Hermes ✅ | Give Claude (me) ✅ |
|---|---|
| Reading/scanning vault files | Brand copy, captions, pages |
| Building indexes + checklists | Anything customer-facing |
| Structured data, JSON, schema | Strategy + validation |
| File moves, renames, cleanup | Firewall / brand law calls |
| Research summaries | Final approval of copy |

> **Why:** a coder model writes great structure and lousy marketing. Don't ask Hermes for a hook — ask it to organize, scan, and build.

---

## 1️⃣ YOUR FIRST CHAT TASK (do this first — 30 seconds)
Proves Hermes can read your vault and obeys brand law. Paste into **Hermes → Chat**:

```
Read 01_Command_Center/M7_MASTER_SOP.md and list the 5 rules that never change,
one line each. No preamble. Then confirm you can see 01_Command_Center/Outbox_Drafts/.
```

✅ **Pass =** it lists your 5 rules and confirms the Outbox. Now you know it's wired to the vault.

---

## 2️⃣ YOUR FIRST GOAL MODE TASK (highest value — solves your "too many files" pain)
Paste into **Hermes → Goal Mode**:

```
GOAL: Build a master index of every SOP and playbook in this vault.

Steps:
1. Scan 01_Command_Center/ and 03_Knowledge_Mat/ for all .md files.
2. For each file, write ONE line: filename — what it's for (from its title/frontmatter).
3. Group them under headings: SEO · Brand & Content · Operations · Media · Agents/Tech.
4. Save the result to 03_Knowledge_Mat/active_context/SOP_INDEX.md
5. Mark it STATUS: PAUSED at the top.

RULES: do not edit or delete any existing file. Do not publish anything.
Never write "free" (use CPPA), never "GAF" (use IKO Certified), never the color green.
Stop when SOP_INDEX.md is written and tell me how many files you indexed.
```

**Why this first:** it's a *file* job (its strength), it's bounded (won't time out), it needs zero keys, and it hands you the one thing you've been missing — **a single map of every SOP you own.**

---

## 3️⃣ THE TASK MENU (after the first two work)

### ✅ Good CHAT tasks (short)
- `Summarize 01_Command_Center/M7_LEAD_ENGINE_GBP_LSA_FOR_BROTHER.md in 5 bullets.`
- `List every file in 01_Command_Center/Outbox_Drafts/Content/ with a one-line purpose.`
- `Check 01_Command_Center/Outbox_Drafts/ for any file containing the word "free" and list them.`

### ✅ Good GOAL MODE tasks (bounded, multi-step)
- **Brand audit:** `Scan every .md in Outbox_Drafts/. Flag any file containing free, GAF, warrior, toa, cheap, or green. Write findings to active_context/brand_audit.md. Fix nothing — just report.`
- **Media index:** `Scan 02_Media_Vault/. Build an index of every video/photo with folder + filename, grouped by city/service. Save to active_context/media_index.md.`
- **Schema check:** `Read 01_Command_Center/Outbox_Drafts/schema/ALL_12_PAGES_JSONLD.md and verify each block has telephone, address, areaServed, and aggregateRating. Report any missing field.`
- **Keyword sort:** `Read the GSC export I paste, group keywords into Transactional vs Informational, sort by impressions, output a markdown table.`

### ❌ DON'T give Hermes
- "Write me a reel caption / landing page / ad" → **that's mine** (brand voice)
- "Run the whole SEO pipeline" → too big, it will time out
- Anything that publishes, posts, or spends → **Outbox Shield**

---

## 4️⃣ YOUR HERMES SOP LIBRARY (found in Google Drive)
Feed any of these to Hermes as context when you want it to follow a specific workflow:
- **HERMES AGENTIC SOP: "Near Me" Domination Pipeline** ← the SEO one
- SOP: How To Use The Hermes Desktop App As A Self-Learning AI Agent
- SOP: How to Set Up and Use Hermes Agent to Automate Your Business
- SOP: Use Hermes + Agent OS to Build Agents That Remember and Run 24/7
- SOP: How To Use NotebookLM And Hermes To Build A Free AI Content Workflow
- SOP: Hermes MCP Catalog Update · Hermes Agent v0 update · Local Voice AI
- EXTRACT 23rd May: Hermes Agent SEO SOP (the Goldie Ranking Stack)

---

## 5️⃣ SWITCHING MODELS IN CHAT
- **Agent OS Hermes tab** → the **PROFILE pills** (default · marketing · content · roofing) = different agent personalities.
- **Hermes dashboard** (`localhost:9119`) → the **MODEL dropdown** (top-right) = switch the actual model.
- **For 237 models:** open OmniRoute (`localhost:20128`) → Endpoints → copy key → paste into `~/.hermes/config.yaml` where it says `REPLACE_WITH_OMNIROUTE_KEY`, then pick `auto`.

---

## 🍍 THE ONE RULE
**Hermes organizes. Claude writes. Saia approves.**


<!-- M7-FIREWALL-EXEMPT: cheatsheet -->
