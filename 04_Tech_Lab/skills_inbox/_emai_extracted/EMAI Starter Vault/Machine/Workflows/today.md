---
type: workflow
status: active
trigger: /today
last_verified: "2026-05-01"
tags: [workflow, planning, daily]
---

# Workflow - /today

Morning planning workflow. Build today's plan using live vault state plus the compiled personalization file.

## Step 1 - Get today's date
Use `YYYY-MM-DD`.

## Step 2 - Read compiled today prompt
Read `Machine/Personalization/today-prompt.md` first.
This is the only personalization file `/today` should need by default.

## Step 3 - Check or create today's note
Look for `00 Human/10 Daily Notes/YYYY-MM-DD.md`.
- If it exists, read it.
- If not, create it from `00 Human/80 Templates/Daily Template.md`.

## Step 4 - Read recent execution state
Read the last 3 daily notes before today and pull forward:
- unchecked tasks
- unchecked frogs
- blockers worth carrying

## Step 5 - Read open work
Read:
- pending task files in `00 Human/20 Tasks/`
- active project notes in `00 Human/30 Projects/`

## Step 6 - Build the plan
Use the compiled today prompt plus the real vault state to determine:
- The ONE Thing
- Top priorities
- Frogs
- Today's tasks
- Quick wins
- Time blocks if the compiled prompt says to use them
- Watch-outs or drift warnings

## Step 7 - Present the plan
Use this format:

```
## Today's Plan - [Day, Date]

### The ONE Thing
> ...

### Top Priorities
1. ...
2. ...
3. ...

### Frogs to Eat
- [ ] ...

### Today's Tasks
- [ ] ...

### Quick Wins
- [ ] ...

### Watch Out
- ...

### Time Blocks
| Time | Block | Why |
|------|-------|-----|
```

## Step 8 - Write to today's note
After presenting the plan, ask whether to write it into today's note.
If yes, update:
- `## 🎯 Today's Focus`
- `## 🐸 Frogs to Eat`
- `## ✅ Today's Tasks`
- `## ⚡ Quick Wins`
- `## 📅 Calendar` if blocks were created

Append to Activity Log:
`- [HH:MM] /today - plan written.`
