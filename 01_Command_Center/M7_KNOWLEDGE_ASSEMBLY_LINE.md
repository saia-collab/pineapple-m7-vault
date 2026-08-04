---
title: M7 KNOWLEDGE ASSEMBLY LINE — Skool → Gem → Vault → Hermes
status: active reference
date: 2026-07-24
---

# 🏭 M7 KNOWLEDGE ASSEMBLY LINE

The repeatable pipeline for turning any course lesson, video, or SOP into something Hermes runs.
**Your instinct was right — this replaces juggling a separate NotebookLM notebook per SOP.**

## THE 5 STATIONS
```
1. CAPTURE        2. DISTILL         3. DEPOSIT        4. COMPILE        5. EXECUTE
   (Skool)    →    (Gemini Gem)  →    (Vault)      →   (Claude/me)   →   (Hermes + OS)
 video + link      add sources        markdown          master SOP        /learn + run
 + SOP text        → clean .md        into 00_Atlas      + workflow        → Outbox PAUSED
```

### 1. CAPTURE — Skool is your SOURCE
Julian Goldie's AI SEO course (Kimi swarms, Hermes Agent OS, Claude AI SEO, etc.) = raw material.
Grab the lesson **link + video URL + any pasted SOP text**.

### 2. DISTILL — Gemini Gem (this is your shortcut)
Instead of a notebook per SOP: **one Gem per HUB**. Drop the Skool link + video + SOP in as sources,
then prompt: *"Extract this into a clean M7 markdown SOP + step-by-step workflow under M7 Brand Law
(CPPA, IKO, RCAT #03-0637, zero green, Outbox Shield). Output only the markdown."* → you get final markdown.

### 3. DEPOSIT — drop the markdown in the Vault
Save each Gem's output to `03_Knowledge_Mat/00_Atlas/` (permanent SOP) or `active_context/`
(Hermes-learnable). One line in `SOP_INDEX.md`.

### 4. COMPILE — Claude (me) builds the master
You hand me the distilled markdowns → I merge them into ONE master SOP + workflow, de-duplicated,
brand-checked, formatted for Hermes. (Like I just did with the Goldie Omnipresence Stack.)

### 5. EXECUTE — Hermes + the Agentic OS
`/learn <master SOP>` → Hermes runs it in Goal Mode → the Kanban orchestrates the swarm →
output lands PAUSED in `Outbox_Drafts/` → you give the GO.

---

## WHICH GOOGLE TOOL FOR WHAT (stop mixing them up)
| Tool | Best at | Role in M7 |
|---|---|---|
| **NotebookLM** | Ingesting 100s of sources, deep Q&A, audio/reports | Research library — grounding, not execution |
| **Gemini Gems** | A persistent persona + a few key sources → clean output | **The distiller** — turns a lesson into a markdown SOP |
| **Gemini Spark** (new) | Scheduled tasks, connected apps (Gmail/Drive), digests | **Google-side research + scheduling** — feeds the vault, does NOT execute |

## WHERE SPARK FITS (and its one limit)
Spark is Google's new agent layer — "describe a task," it schedules + runs it with your connected apps.
**Use it for the GATHERING side:** a daily brief, a weekly "new roofing SEO trends" digest, pulling
Google data on a schedule → output to Drive/markdown → into the vault.

⚠️ **Do NOT make Spark the executor.** It lives in one Google account's cloud and can't honor your
Outbox Shield or brand firewall. **Execution stays LOCAL** (Hermes + Agentic OS) so the vault stays
the single source of truth. Spark researches; Hermes executes; you approve.

## DIVISION OF LABOR (who does what)
| You (in Google) | Me (Claude Code) | Can't be automated |
|---|---|---|
| Distill lessons in Gems → markdown | Compile master SOP + workflow | I can't watch videos or log into your Gemini/Skool |
| Run Spark for scheduled digests | Wire it into Hermes + the vault | The Gem-distill step is yours (your login) |
| Approve the Outbox | Keep the brand firewall + index | — |

## THE HABIT
Every new lesson → Gem distills → drop the markdown in the vault → tell me "compile this in" →
I fold it into the master → Hermes runs it. That's the whole loop.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
