---
type: workflow
status: active
trigger: /interview
last_verified: "2026-05-01"
tags: [workflow, interview, context]
---

# Workflow - /interview

Conversational personalization workflow. Capture how the user works, what matters right now, and what `/today` and `/closeday` should optimize for.

## Step 1 - Load current state
Read:
- `00 Human/70 Context/business-profile.md`
- `00 Human/70 Context/audience-profile.md`
- `00 Human/70 Context/writing-style.md`
- `Machine/Personalization/operator-profile.md`
- `Machine/Personalization/today-prompt.md`
- `Machine/Personalization/closeday-prompt.md`
- the last 2 daily notes in `00 Human/10 Daily Notes/` if they exist
- project notes in `00 Human/30 Projects/` if they exist

Tell the user you are going to personalize the vault and regenerate the compiled prompts used by `/today` and `/closeday`.

## Step 2 - Ask about current reality
Ask one question at a time:
1. "What are you actually working on right now?"
2. "What matters most over the next 30 days?"
3. "What projects or responsibilities should this vault keep in view?"

## Step 3 - Ask about planning style
Ask one question at a time:
1. "How do you want `/today` to plan your days — focused, balanced, or aggressive?"
2. "How many true priorities do you want in a normal day?"
3. "Do you want suggested time blocks, or just a priority list?"
4. "What counts as a frog for you — overdue tasks, avoided tasks, admin, or something else?"

## Step 4 - Ask about metrics and closeout
Ask one question at a time:
1. "Do you want this vault to track any metrics at all?"
2. "If yes, which ones actually matter?"
3. "What should `/closeday` ask every day besides wins and blockers, if anything?"
4. "Do you want `/closeday` to be quick, reflective, or performance-oriented?"

## Step 5 - Update vault notes
Create or update project notes in `00 Human/30 Projects/` for any active project surfaced.
Update these files so the user can read them directly:
- `00 Human/70 Context/business-profile.md`
- `00 Human/70 Context/audience-profile.md`
- `00 Human/70 Context/writing-style.md` if relevant
- `Machine/Personalization/operator-profile.md`

## Step 6 - Regenerate compiled prompts
Rewrite these files fully based on the interview answers:
- `Machine/Personalization/today-prompt.md`
- `Machine/Personalization/closeday-prompt.md`
- `Machine/Personalization/meeting-notes-prompt.md`

The point is to compile the user's preferences into prompt-ready instructions so `/today` and `/closeday` do not need to read a pile of separate preference files each run.

## Step 7 - Log it
Append to today's daily note Activity Log:
`- [HH:MM] /interview - personalization updated.`

## Step 8 - Close
Summarize what changed and recommend `/today` as the next step.
