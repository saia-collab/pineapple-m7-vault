---
type: workflow
status: active
trigger: /meeting-notes
last_verified: "2026-05-01"
tags: [workflow, meeting]
---

# Workflow - /meeting-notes

Turn a meeting transcript or rough notes into a clean meeting record, action items, and person updates.

## Step 1 - Read context
Read `Machine/Personalization/meeting-notes-prompt.md`.

## Step 2 - Parse the meeting
Extract:
- date
- meeting name
- attendees
- decisions
- action items
- open questions

## Step 3 - Update people notes
Create or update person notes in `00 Human/50 People/`.

## Step 4 - Create tasks
Create one task file per action item in `00 Human/20 Tasks/`.

## Step 5 - Create the meeting note
Save to `00 Human/40 Resources/Meetings/YYYY-MM-DD - [meeting name].md`.

## Step 6 - Log it
Append to today's Activity Log with the number of tasks and people updated.
