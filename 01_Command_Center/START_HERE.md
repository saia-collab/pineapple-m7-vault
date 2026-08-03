---
type: operator_runbook
status: active
last_updated: 2026-07-30
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
supersedes: "THE_ONLY_PROMPT.md, M7_QUICK_CARD.md, FINISH_LINE.md, EXECUTE_EVERYTHING_CLAUDE_CODE.md"
---

# 🍍 START HERE — the only file you need to open

**Pineapple Contractors** · RCAT #03-0637 · IKO Certified · 5-Star Rated · Since 2005 · 972-928-0788

> **If you read one thing, read §1.** Everything below it is reference.
> You do **not** need to configure anything to start working today.

---

## 1. EXECUTE NOW — pick one, paste it, done

Open Claude Code in the vault and paste one of these. All three work **today**,
with zero setup, using only what is already online.

| # | You want… | Paste this |
|---|-----------|-----------|
| 1 | **Content** — turn footage/notes into posts | `Run M7_CONTENT_FACTORY.md. Draft this week's posts. Stage PAUSED in Outbox_Drafts/.` |
| 2 | **Leads** — speed-to-lead + review requests | `Run M7_LEAD_ENGINE.md. Draft today's follow-ups and review asks. Stage PAUSED in Outbox_Drafts/.` |
| 3 | **Campaign** — social + LSA + SEO together | `Run M7_INTEGRATED_CAMPAIGN.md. Build this week's campaign. Stage PAUSED in Outbox_Drafts/.` |

Every output lands **PAUSED** in `01_Command_Center/Outbox_Drafts/`.
Nothing publishes, sends, or spends until you say **GO**. That is the Outbox Shield.

**That is the whole job.** If you are doing anything other than the above, you are
configuring, not executing — and configuring is what has been eating your time.

---

## 2. WHY YOU KEPT GETTING STUCK (read once, then move on)

You were not doing anything wrong. Four things were quietly working against you:

1. **No single entry point.** `01_Command_Center/` holds **61 markdown files**, and
   **20** of them read like the master doc — `MASTER_PLAYBOOK`, `M7_MASTER_SOP`,
   `M7_MASTER_SOP_Command_Deck`, `M7_MASTER_RUNBOOK`, `M7_EXECUTE`,
   `M7_EXECUTION_CHEATSHEET`, `EXECUTE_EVERYTHING_CLAUDE_CODE`, `THE_ONLY_PROMPT`,
   `FINISH_LINE`, `M7_QUICK_CARD`… Every session began by re-deciding which one was
   real. **This file is now the answer. Start here, always.**

2. **This very file was stale.** Until today `START_HERE.md` told you to double-click
   `RUN_M7_DASHBOARD.bat` — *a launcher that does not exist* — and to open port 8787,
   *where nothing runs*. Following the start file could not possibly work.

3. **A port collision made a whole tab unfixable.** The Agentic OS was running on
   port 3000, but 3000 is hardcoded as **SEO Office's** port. The SEO tab was pinging
   the Agentic OS itself, getting a 404, and reporting "not responding." No amount of
   API keys would ever have fixed that. See `PORT_MAP.md`.

4. **You were maintaining ~40 services to run a 3-service business.** The Agent OS
   pack ships 43 tabs and 36 install guides. Every tab you don't need still shows a
   red/disconnected badge, and a red badge *reads* like a broken thing to go fix.
   **They are optional. Ignore them.** You need Claude, Hermes, and the vault.

**The rule going forward:** a red badge on a tab you don't use is not a problem.
Execute first. Configure only when a task you actually need is blocked.

---

## 3. WHAT IS ACTUALLY ONLINE (as of this file)

| Status | Service | Notes |
|--------|---------|-------|
| 🟦 Online | **Claude** | your builder — this is the one you use |
| 🟦 Online | **Hermes** | orchestrator, dashboard on :9119 |
| 🟦 Live | **Free Claude Code** | via OmniRoute |
| 🟦 Wired | **Obsidian vault** | filesystem-first memory |
| ⬜ Idle | OpenClaw | 0 agents — optional, ignore until needed |
| ⬜ Optional | Paperclip · OpenSEO · SEO Office · OpenDesign | each needs its own service running |

You have **more working than you think.** The four 🟦 rows are everything the
three workflows in §1 require.

---

## 4. THE 5 RULES THAT NEVER CHANGE

1. **Outbox Shield** — every output lands PAUSED in `Outbox_Drafts/`. Never publish,
   post, send, or spend without an explicit **GO**.
2. **Never restructure folders** or delete files unless told to.
3. **Brand lexicon** — never "free" → **CPPA** (Complimentary Professional Photo
   Audit); never "GAF" → **IKO Certified**; never green.
4. **Run the brand firewall** before staging content:
   `python 04_Tech_Lab/scripts/brand_firewall.py --report`
5. **Verify, don't hallucinate** — flag anything unverified.

## Visual identity

| Swatch | Colour | Use |
|--------|--------|-----|
| ■ | Royal Navy `#1A365D` | structural authority |
| ■ | Pineapple Gold `#FBC02D` | action markers |
| ■ | Status Cyan `#00BFFF` | live status |

**The colour green is prohibited everywhere** — including status indicators.
Use Status Cyan for "good/online" instead.

---

## 5. LAUNCHERS THAT ACTUALLY EXIST

| Double-click | What it does |
|--------------|--------------|
| `RUN_AGENT_OS.bat` | M7 Command Center → `http://localhost:3939` |
| `LAUNCH_ALL.bat` | Command Center (3939) + Agentic OS (3737) + FCC + Paperclip |
| `M7_DOCTOR.bat` | connection health check |
| `M7_CLEANUP.bat` | tidy the vault |

Ports are documented once, in **`PORT_MAP.md`**. Do not re-derive them.

> ⚠️ `LAUNCH_ALL.bat` starts the Agentic OS from a **dated pack folder**. When you
> unzip a newer pack, update that path or you will keep booting the old build.

---

## 6. KEYS — where they actually go

Not in the vault `.env`. The Agentic OS reads them from the Hermes profile:

```
%LOCALAPPDATA%\hermes\profiles\main\.env      →      OPENROUTER_API_KEY=...
```

(That is `C:\Users\<you>\AppData\Local\hermes\…` — **not** `~/.hermes\…`.
`sync_hermes_m7.ps1` and `update_agent_os.ps1` both resolve it from
`$env:LOCALAPPDATA`, which is authoritative.)

One key feeds Hermes, Fusion, Loop and Hy3-Coder. Don't repeat it per-tab.
To have an agent wire everything for you, point it at the pack's `SETUP-WITH-AI.md`.

> ⚠️ **Never create a `.env.local` with an empty `ANTHROPIC_API_KEY=`.** An empty
> value overrides `claude login` and breaks the Claude tab. The Claude tab uses
> subscription OAuth (`claude login`), not an API key.

> 🔐 **Obsidian Local REST API** runs at `http://127.0.0.1:27123`. Its key lives in
> `.obsidian/plugins/obsidian-local-rest-api/data.json` — **local config only.**
> This repo is public: never paste key material into a tracked markdown file.
> Rotate the key from the plugin settings if it is ever exposed.

---

Ko e hala 'o e fononga ko e faka'apa'apa.
