---
name: m7-doctor
description: >-
  Read-only health check for the Pineapple M7 Agentic OS. Verifies the 4-Fala folders and key
  files exist, which studio/model ports are online (Studio 3737, Free Claude Code 8082, Ollama
  11434, OmniRoute 20128, Hermes 9119), that all Hermes profiles are proverb-clean (brand rule),
  scans Outbox drafts for real brand violations (green hex, "free <offer>" wording), and reports
  git status. Use when Saia asks "is my setup configured right?", "is everything working/online?",
  "run a health check / doctor", "did the config apply?", or at the start of a work session. It
  CHANGES NOTHING — pure inspection.
---

# m7-doctor — "is my studio configured right?" in one command

Saia is non-technical and often unsure whether the OS is set up correctly. This answers that in
one read-only sweep. It never edits, publishes, starts, or stops anything.

## When to use
- "Is everything working?" / "is my setup configured?" / "is X online?"
- "Did the [config / profile / brand] change actually apply?"
- Before starting a work session, or after any setup change.

## How to run
```bash
python ".claude/skills/m7-doctor/m7_doctor.py"
```
(Exit code 0 = healthy or warnings only; 1 = at least one hard FAIL.)

## What it checks (6 sections)
1. **4-Fala folders** — 01_Command_Center, 02_Media_Vault, 03_Knowledge_Mat, 04_Tech_Lab.
2. **Key files** — playbook, prompt panel, study guide, clean Hermes soul.md, brand_firewall.py, CLAUDE.md.
3. **Ports** — Studio/dashboard/fcc/ollama/omniroute/hermes. *Offline = just not started, not an error (warn).*
4. **Hermes profiles** — counts them and confirms **none still contain a Tongan proverb** (fails if any do).
5. **Outbox brand scan** — real violations only: green hex codes + "free inspection/estimate/quote" wording (should be CPPA). *(Green = fail; free-offer = warn to review.)*
6. **Git** — clean tree? anything unpushed? last commit.

## How to read the result
- **✅ pass** — good.
- **⚠️ warn** — worth a look, not broken (an offline optional service, drafts to review, unpushed commits).
- **❌ fail** — needs attention (a missing folder/file, or a profile that still has a proverb).
- The last line is the TL;DR verdict + counts.

## Guardrail
100% read-only. If the report shows something to fix (e.g., unpushed commits, a proverb that crept
back, an offline service), tell Saia plainly and offer to fix it — never auto-fix from inside the doctor.

## Optional: one-click desktop launcher
A `RUN_M7_DOCTOR.bat` can wrap this so Saia double-clicks it:
`@echo off` / `python "C:\Pineapple Contractors M7\.claude\skills\m7-doctor\m7_doctor.py"` / `pause`
