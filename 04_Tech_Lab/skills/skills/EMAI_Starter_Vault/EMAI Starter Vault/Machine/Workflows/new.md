---
type: workflow
status: active
trigger: /new
last_verified: "2026-05-01"
tags: [workflow, capture, routing]
---

# Workflow - /new

Capture and route a raw input into the right notes with as little friction as possible.

## Step 1 - Accept the dump
Do not ask clarifying questions first.

## Step 2 - Classify the pieces
Split the input into any mix of:
- task
- frog
- project update
- person update
- resource
- idea/inbox
- general log entry

## Step 3 - Route each piece
- Tasks -> `00 Human/20 Tasks/`
- Frogs -> today's daily note `## 🐸 Frogs to Eat`
- Project updates -> project note log
- People -> `00 Human/50 People/`
- Resources -> `00 Human/40 Resources/`
- Ideas -> `00 Human/00 Inbox/`

## Step 4 - Add links where obvious
Link to the projects or people you just created or found.

## Step 5 - Log the run
Append a timestamped note to today's Activity Log summarizing what was routed.

## Step 6 - Report back
Tell the user what was created, updated, or left ambiguous.
