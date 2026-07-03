---
type: workflow
status: active
trigger: /closeday
last_verified: "2026-05-01"
tags: [workflow, eod, daily]
---

# Workflow - /closeday

End-of-day workflow. Close today's note using the compiled closeday prompt plus the actual state of the day.

## Step 1 - Read compiled closeday prompt
Read `Machine/Personalization/closeday-prompt.md` first.
This is the only personalization file `/closeday` should need by default.

## Step 2 - Read today's daily note
Open `00 Human/10 Daily Notes/YYYY-MM-DD.md`.
If it does not exist, create it from the daily template.

## Step 3 - Find carry-overs
Pull unchecked items from:
- `## 🐸 Frogs to Eat`
- `## ✅ Today's Tasks`
- `## ⚡ Quick Wins`

## Step 4 - Ask the end-of-day questions
Ask one question at a time.
Always ask:
1. "What got done today that you're glad about?"
2. "What got in the way or is still stuck?"
3. "One sentence on how today felt overall."

If the compiled closeday prompt says metrics matter, ask only the relevant metric follow-up.

## Step 5 - Update today's note
Fill in `## 🧠 End of Day` and, if relevant, `## 📈 Metrics Snapshot`.
Append to Activity Log:
`- [HH:MM] /closeday - day closed and carry-overs staged.`

## Step 6 - Stage tomorrow
Create tomorrow's note if needed and pre-populate `## ✅ Today's Tasks` with carry-overs.

## Step 7 - Close
Report back with:
- wins logged
- carry-overs staged
- tomorrow note ready
