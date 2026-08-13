---
type: master_runbook
title: M7 MASTER RUNBOOK — attach + paste once. Zero human error.
status: active
last_updated: 2026-06-27
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# ▶️ M7 MASTER RUNBOOK — DO THIS IN ORDER

**The plan in one line:** GitHub backs up your vault → the cloud VM pulls it → Docker runs the agents
24/7 → you reach the dashboard from anywhere → you hand the agent the playbook and it executes.
**You copy-paste. The agent does the work. GitHub lets you undo any mistake.**

> **YES — you can attach this + `M7_CLOUD_DEPLOYMENT_CHEATSHEET.md` to Claude Code / Codex and have it
> execute the whole thing.** The exact attach-and-go prompt is at the bottom (THE ONE PROMPT).

---

## 🛑 BEFORE ANYTHING — 2 safety facts (so nothing leaks or breaks)
1. **Your GitHub repo is PUBLIC.** The `.gitignore` I set excludes your `.env`, API keys, and the 28 GB
   media — so those never upload. **Even safer: make the repo Private** (GitHub → repo → Settings → change
   visibility → Private). Do that and you can relax completely.
2. **GitHub = your undo button.** Every push is a restore point. If an agent ever scrambles your files
   again, you `git revert` and it's back. This is the safety net you were missing.

---

## STEP 1 — Back up the vault to GitHub (one time, then repeat anytime)
Open a terminal in `C:\Pineapple Contractors M7` and paste:
```bash
git init
git add .gitignore
git commit -m "add gitignore (exclude media + secrets)"
git add .
git commit -m "M7 vault — playbooks, dashboards, scripts, SOPs"
git branch -M main
git remote add origin https://github.com/saia-collab/Roofing-Marketing-System.git
git push -u origin main
```
*(If it says the remote already exists, skip the `remote add` line. To save again later, just:
`git add . && git commit -m "update" && git push`.)*

✅ Your whole system is now backed up and versioned. Verify on github.com — you should NOT see `.env` or
`02_Media_Vault` (good — those are excluded).

---

## STEP 2 — Stand up the cloud (Claude Code / Codex does this for you)
Open **Google Cloud Shell**, then paste **THE ONE PROMPT** (bottom of this file) into Claude Code/Codex.
It will run the cloud cheat sheet step by step, pausing for you to confirm. In short, it:
1. Provisions the `e2-standard-4` Ubuntu VM (Docker pre-installed).
2. Pulls your vault onto the VM: `git clone https://github.com/saia-collab/Roofing-Marketing-System.git`
3. Writes the `.env` + `docker-compose.yml` (keeps the persistent volume + no public ports).
4. `docker compose up -d` → the 3 containers run.
5. Sets up the `systemd` service so it never dies + Tailscale so you reach it from your phone.

*(All commands live in `M7_CLOUD_DEPLOYMENT_CHEATSHEET.md` — the agent reads them from there.)*

---

## STEP 3 — Reach your command center (private, from anywhere)
After Tailscale is up (Step 5 of the cheat sheet), open on your laptop or phone:
- **Workspace / Mission Control** → `http://localhost:3000` (or the Tailscale IP)
- **Hermes dashboard** → `http://localhost:9119`
- **Your branded command center** → open `01_Command_Center/M7_COMMAND_CENTER.html` (works with Obsidian).

---

## STEP 4 — Execute the playbook (you never code)
In Hermes or Claude on the VM, paste:
```
Read 01_Command_Center/M7_EXECUTE.md, GROUNDING.md, MASTER_PLAYBOOK.md, and
03_Knowledge_Mat/SHARED_MEMORY.md. Execute this week's content: branded social captions, repurposed
video cuts, GBP posts, testimonial money-quotes. Draft everything PAUSED to 01_Command_Center/Outbox_Drafts/,
run brand_firewall.py --check, never restructure folders. Saia is the only publisher. Summarize what you made.
```

---

## STEP 5 — Save your progress back to GitHub (end of each session)
On the VM (or locally):
```bash
git add . && git commit -m "session: drafts + updates" && git push
```
That snapshots everything the agents produced. Roll back anytime with `git log` → `git revert <id>`.

---

# 🚀 THE ONE PROMPT — attach this file + the cloud cheat sheet, paste this into Claude Code / Codex
```
Act as my DevOps + Systems engineer for Pineapple Contractors M7. I've attached M7_MASTER_RUNBOOK.md and
M7_CLOUD_DEPLOYMENT_CHEATSHEET.md. Execute the full deployment END TO END, but PAUSE after each step and
tell me exactly what to paste into Google Cloud Shell, then wait for me to confirm before the next step.

Non-negotiable rules:
- Pull my vault onto the VM by git-cloning https://github.com/saia-collab/Roofing-Marketing-System.git
- Keep the Docker persistent volume map (/opt/m7-agentos/data:/opt/data) — never drop it.
- Keep HERMES_ALLOW_POLICY_WRITE / CRON_WRITE / WORKSPACE_WRITE = false.
- NEVER expose ports 3000 / 8642 / 9119 to the public internet — use Tailscale or SSH tunnel only.
- Do not invent my secrets — leave the placeholder lines for me to fill in.
- After the stack is up, point the agent at my vault as memory (read GROUNDING.md, MASTER_PLAYBOOK.md,
  M7_EXECUTE.md, SHARED_MEMORY.md) and confirm everything is running.

Go one step at a time. Verify each step succeeded before moving on. If anything fails, stop and show me the error.
```


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
