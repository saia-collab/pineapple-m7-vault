# CLAUDE.md

This repository is an **Obsidian vault operating system** packaged for community use.

## What this vault is
- `00 Human/` = user-owned notes and source-of-truth information
- `Machine/` = workflows, templates, personalization files, scripts, and outputs
- `System/` = onboarding and operating docs

## This package
- This is the **starter edition**.
- It is sanitized for distribution.
- `emai-command-center` is intentionally excluded.
- Commands are written to work from the vault root using relative paths.

## Included commands
- `/start`
- `/interview`
- `/today`
- `/new`
- `/closeday`
- `/meeting-notes`

## Personalization model
`/interview` updates these files:
- `00 Human/70 Context/business-profile.md`
- `00 Human/70 Context/audience-profile.md`
- `00 Human/70 Context/writing-style.md`
- `Machine/Personalization/operator-profile.md`
- `Machine/Personalization/today-prompt.md`
- `Machine/Personalization/closeday-prompt.md`
- `Machine/Personalization/meeting-notes-prompt.md`

`/today` should read `Machine/Personalization/today-prompt.md` rather than loading multiple preference notes.
`/closeday` should read `Machine/Personalization/closeday-prompt.md` rather than loading multiple preference notes.

## Working rules
1. Respect the Human/Machine boundary.
2. Use templates when creating new notes.
3. Log activity into the daily note when a workflow calls for it.
4. Keep file paths vault-relative.
5. Prefer updating compiled personalization files in `Machine/Personalization/` through `/interview` instead of making `/today` or `/closeday` read many separate preference files every run.
