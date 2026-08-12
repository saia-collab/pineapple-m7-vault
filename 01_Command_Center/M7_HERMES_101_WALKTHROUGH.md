---
type: walkthrough
title: HERMES 101 — a 6-part walkthrough (do one per sitting)
status: active
date: 2026-08-11
pairs_with: M7_STUDIO_STUDY_GUIDE.md · M7_PROMPT_CONTROL_PANEL.md · Brand_DNA/M7_HERMES_SOUL.md
note: ADHD mode — 6 short episodes, ONE action each. Grounded in the Hermes manuals NotebookLM wrote you.
---

# 🛰️ HERMES 101 — the 6-part walkthrough
**You've avoided Hermes because of config. This walks you in, one small win at a time. Do ONE episode, then stop. Six sittings and you'll run it daily.** Nothing here publishes — drafts land PAUSED.

> **Hermes in one breath:** it's not a chatbot that forgets you tomorrow. It's a **"Compound Employee"** — a swappable **Brain** (AI models) + a **Cockpit** (your dashboard at `localhost:3737`) + a **Memory Vault** (your markdown files). It reads your business every turn, so you never re-explain it.

---

## 🎬 EPISODE 1 — What Hermes actually is
**10-year-old version:** Hermes is a robot employee. Its *brain* you can swap (cheap or smart), its *desk* is your dashboard, and its *notebook* is your vault folder — so it remembers everything about Pineapple Roofing.

**▶️ DO THIS:** Open `localhost:3737` → click **Hermes** → **Chat**. Type:
```
In one paragraph, what do you know about Pineapple Roofing from my vault? List our license, phone, and slogan.
```
If it answers with RCAT #03-0637, (972) 928-0788, and "Roofing Made Sweeter" — its memory is working.

**💡 Why it matters:** proves Hermes already *knows your business*. That's the whole point — no re-explaining.
**✅ Got it when:** it recites your real credentials back.

---

## 🎬 EPISODE 2 — Profiles & the soul.md (its personality chip)
**10-year-old version:** Hermes has different *employees* (profiles) — a roofing writer, a coder, a researcher. Each keeps its own **`soul.md`** (its rulebook + your brand law) so the roofing one never writes restoration copy by accident.

Your profiles live at `%LOCALAPPDATA%\hermes\profiles\<name>\` — each holds `config.yaml` (which model), `soul.md` (brand rules), `auth.json` (keys). **Your clean master soul.md is done:** `01_Command_Center/Brand_DNA/M7_HERMES_SOUL.md`.

**▶️ DO THIS:** In **Hermes → Manage** (or Control Room), look at your profile list. You don't need to edit anything — just see that profiles exist. When you're ready, I apply the clean soul.md to each for you (back-up first).

**💡 Why it matters:** the soul.md is *why* Hermes stays on-brand. Get this right once and every output obeys brand law.
**✅ Got it when:** you can name 2 of your profiles.

---

## 🎬 EPISODE 3 — The model sockets (how you save money)
**10-year-old version:** the brain is a *swappable socket*. Plug in a **free** model for easy stuff, a **smart paid** model only for hard stuff. Never pay for what a free model can do.

Simple routing:
- **Free workhorse** (Ollama local / Free Claude Code) → drafts, cleanups, bulk. **$0.**
- **Smart/paid** (Claude, GPT-5.6) → hard strategy, tricky pages. **Only when needed.**

**▶️ DO THIS:** In **Hermes → Chat**, find the **model dropdown** (top-right). Switch it to a free/local model, ask it to "summarize my Prompt Control Panel in 5 bullets." Watch it run at $0.

**💡 Why it matters:** this one habit is the difference between a $0 month and a $200 month.
**✅ Got it when:** you've swapped the model once.

---

## 🎬 EPISODE 4 — Chat & Goal Mode (your daily driver)
**10-year-old version:** **Chat** = ask one thing. **Goal Mode** = give a whole *goal* and it runs all the steps by itself until done.

**▶️ DO THIS:** Go to **Hermes → Goal Mode** and paste:
```
/goal "Write a Frisco 'hail damage roof repair' location page for Pineapple Roofing. 1,000+ words, direct-answer hook in the first 40 words, our credentials (RCAT #03-0637, IKO Certified, since 2005, (972) 928-0788), a CPPA call-to-action, an FAQ, and a LocalBusiness JSON-LD block. Brand-lock: CPPA not free, IKO not GAF, zero green, Roofing Made Sweeter, no proverbs. Save PAUSED to 01_Command_Center/Outbox_Drafts/SEO/."
```
Watch it research → write → save. Then review it in `Outbox_Drafts/`.

**💡 Why it matters:** this is 80% of your daily use. One goal = one finished draft.
**✅ Got it when:** a PAUSED page draft appears in your Outbox.

---

## 🎬 EPISODE 5 — Kanban (the multi-agent team)
**10-year-old version:** drop a big job on a board; Hermes splits it into cards and sends *several* worker agents to do them at once. You already have this running — your **Collin County roofing cluster** (McKinney, Allen, Plano, Frisco, Prosper) is on the board.

**▶️ DO THIS:** Open **Hermes → Kanban**. Add one card:
```
Build the McKinney roofing service page (roof replacement + hail). 900 words, CPPA CTA, LocalBusiness schema, our credentials. Navy/gold/cyan, zero green. Save PAUSED to Outbox_Drafts/SEO/.
```
Watch it move Triage → Todo → Running → Done, built by a worker agent.

**💡 Why it matters:** this is how you build 5 pages in the time one used to take.
**✅ Got it when:** a card reaches **Done** and a draft is in your Outbox.

---

## 🎬 EPISODE 6 — The power tabs (when to reach for each)
Now you know the daily driver. Here's when to grab the rest:

| Tab | Reach for it when… | One-liner to try |
|---|---|---|
| **Muse** | You need content ideas | *"10 saveable Reel ideas for DFW roofing this week, each with a hook + CPPA CTA."* |
| **Mixture** | It's a big decision | *"Best $500/mo marketing move for Frisco roofing — argue 3 options, pick 1."* |
| **Oracle** | "What did we decide about ___?" | *"From my vault: what's our NAP and target ZIPs?"* |
| **Apollo (voice)** | Hands full on a jobsite | Say *"Hey Hermes"* → ask your question out loud |
| **Outreach** | Follow-ups / review asks | *"Draft a 3-touch Google review request for a finished job."* (PAUSED) |

**▶️ DO THIS:** Pick the ONE that excites you most and run its one-liner.
**💡 Why it matters:** you now have a tool for ideas, decisions, memory, voice, and outreach — not just writing.
**✅ Got it when:** you've tried one power tab.

---

## 🎓 GRADUATION — you can now:
- Ask Hermes anything (it knows your business).
- Run a **Goal** to get a finished page.
- Drop a **Kanban** card and let agents build.
- Swap to a **free model** to save money.
- Grab **Muse/Mixture/Oracle** for ideas, decisions, and memory.

**Then always:** review the Outbox → say **GO** on what's ready → tell me *"commit and push."*

> Full Hermes manuals (deeper): `03_Knowledge_Mat/Resources/NotebookLM_MasterSOP_2026-08-11/` (Command Desk, Operational Manual, Agent Skills). Clean config: `Brand_DNA/M7_HERMES_SOUL.md`.

<!-- M7-FIREWALL-EXEMPT: governance-reference (training doc; "free" = free AI models, not marketing copy) -->
