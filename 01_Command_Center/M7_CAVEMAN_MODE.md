---
type: token_efficiency_sop
title: M7 CAVEMAN MODE — cut agent output tokens ~75%
status: active
last_updated: 2026-07-06
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🪓 M7 CAVEMAN MODE — spend fewer tokens, keep the work

> **What it is:** a terse OUTPUT style (not a downloaded tool). The agent strips conversational
> padding and returns only what's needed — byte-exact paths, code, commands, results. ~75% fewer
> output tokens on routine work. Implemented as an M7 rule = $0, no install, no security risk.
> (We deliberately did NOT run the `curl | bash` installer — never pipe unreviewed remote scripts.)

## HOW TO TURN IT ON
Prefix any request with **`caveman:`** — e.g. `caveman: draft 8 captions`. The agent replies terse:
no preamble, no "Here's…", no recap, just the deliverable + a 1-line status. Say `full:` to switch back.

## THE RULE (what caveman mode does)
- Output ONLY: the artifact, the file path, the command, the result. Drop greetings, restatements, "as you can see", options-you-won't-take.
- Keep code/CLI/paths **exact**. Never abbreviate a real command or path.
- Status = one line max (e.g. `✓ 8 captions → Outbox/Content · firewall OK · PAUSED`).

## 🛡️ GUARDRAILS — when caveman mode AUTO-REVERTS to full sentences
Never compress these (safety over brevity):
1. **Destructive commands** — delete/overwrite/rm/reset/drop. Explain fully + confirm first.
2. **Multi-step data mutations** — anything touching many files, the CRM, or memory.
3. **Security-sensitive ops** — keys, auth, credentials, anything leaving the machine.
4. **Confirmations & briefings to Saia** — the morning Jarvis briefing is always plain English.

## 🍍 WHERE M7 USES IT (fits the Playbook)
- ✅ **Use caveman:** execution logs, status updates, file drops, in-progress drafts, agent-to-agent handoffs, code/CLI.
- ❌ **Never caveman (full brand voice):** customer-facing copy (captions, ads, website, SEO, review texts). Brand voice + the M7 lexicon (CPPA/IKO/proverb) is never compressed. Marketing quality > token saving.

## HOW THE FLEET USES IT
- Hermes Goal Mode / Kanban: agents log terse, draft customer copy in full brand voice → Outbox.
- Claude Code / Cowork: prefix `caveman:` for setup/fix/status turns to save your session tokens.
- Result: the *volume* (logs, builds, execution) costs 75% less; the *quality* (your marketing) stays full.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
