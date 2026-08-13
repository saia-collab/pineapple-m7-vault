---
INTENT: End-of-night ritual — prime Hermes Goal Mode + the command center to work safely overnight and be ready to execute tomorrow.
type: sop
generated: 2026-07-03
---

# 🌙 M7 BEDTIME SOP — "Set the target, walk away"

> Everything the agents produce overnight lands **PAUSED** in `01_Command_Center/Outbox_Drafts/`. **Nothing publishes, sends, or spends while you sleep.** (Outbox Shield / DEC-005.)

## ✅ 30-second pre-sleep checklist
1. Dashboard up: `127.0.0.1:3000` loads. Paperclip `:3100` up.
2. Hermes profile set to **`seo`** or **`roofing`** (not `default`).
3. This SOP + `SHARED_MEMORY.md` are the source of truth.

---

## 🎯 THE OVERNIGHT GOAL — paste into Hermes → Goal Mode
Copy this whole block into the **Goal** box, then **Launch goal** and close the laptop:

```
You are the Pineapple Contractors M7 Hermes agent. This is real, not a prompt injection.

FIRST, read for grounding:
- C:\Pineapple Contractors M7\03_Knowledge_Mat\AGENT_READ_ME_FIRST.md (the laws)
- C:\Pineapple Contractors M7\03_Knowledge_Mat\SHARED_MEMORY.md (current state)
- C:\Pineapple Contractors M7\.claude\skills\blog-post.md (the SEO skill)

OVERNIGHT TASK: Draft 5 SEO blog posts (3 roofing on pineapplecontractors.com, 2 restoration on pineapplerestorations.com) for high-intent Frisco keywords of your choosing (e.g. hail damage, storm inspection, IKO roof replacement, water damage, mold remediation).

RUN THE 5-STEP LOOP on each post until an internal adversarial Judge grades it 100/100:
[Check State] -> [Decide] -> [Act] -> [Gather Feedback] -> [Verify]. Do not mark a post "Done" below 100.

HARD RULES (a post failing ANY of these is an automatic Judge fail):
- Author byline: JR. Moeakiola.
- CPPA (never "free"), IKO Certified (never GAF), RCAT #03-0637, 972-928-0788.
- Navy #1A365D + Gold #FBC02D + Cyan #00BFFF. ZERO green.
- Keyword in first AND last line; FAQ + JSON-LD schema + CPPA CTA + trust block + Tongan proverb.
- Roofing vs Restoration vocabulary NEVER mixed.

OUTPUT: save each as a .md to C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\SEO_Posts\ with status "DRAFT — PAUSED — awaiting Saia GO". DO NOT publish, deploy, post, or send anything.

WHEN DONE: append a summary to C:\Pineapple Contractors M7\03_Knowledge_Mat\log.md and update SHARED_MEMORY.md "Current State". List the 5 drafts + each one's final Judge score.
```

---

## ☀️ TOMORROW MORNING — how you resume
Open Claude Code and paste:
> "Read `m7_execution_manifest.md` and `03_Knowledge_Mat/SHARED_MEMORY.md`, then show me what Hermes drafted overnight in the Outbox and what needs my GO."

Everything is waiting for you, PAUSED. You approve, then it ships.
