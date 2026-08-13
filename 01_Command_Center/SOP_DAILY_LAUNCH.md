# 🍍 Daily Launch SOP — Pineapple M7 Command Center

## Every morning when you sit down — do these in order

---

### STEP 1 — Start the Agent OS Dashboard (30 seconds)
Double-click this file:
```
C:\Pineapple Contractors M7\RUN_AGENT_OS.bat
```
> If that bat isn't working yet, open PowerShell and paste:
> ```
> cd "C:\Users\estim\Downloads\agent-os-pack-extracted\agent-os\source"
> npm run dev
> ```
Wait ~20 seconds, then open Chrome → **http://127.0.0.1:3000**

---

### STEP 2 — Start the Complimentary Claude Code Proxy (10 seconds)
Open a second PowerShell window and paste:
```
fcc-server --port 8082
```
Leave it running in the background. This makes the Complimentary Claude Code tab go green.

---

### STEP 3 — Open Claude Code (your AI builder)
Open a third PowerShell window and paste:
```
cd "C:\Pineapple Contractors M7"
claude
```
Then paste this one-liner to load your entire OS into Claude's memory:
```
Read 01_Command_Center/M7_MASTER_SOP.md and treat it as your operating manual. Confirm you've read it and list the SOPs you can run.
```

---

### STEP 4 — Check All Systems (Mission Control)
In the browser at **http://127.0.0.1:3000** → click **Mission Control**

| What you see | Means |
|---|---|
| Claude — green/degraded | ✅ Connected via API key |
| Hermes — any color | ✅ Installed |
| NotebookLM — authenticated | ✅ 100 notebooks live |
| fcc panel — green | ✅ Complimentary Claude Code proxy live |

---

### STEP 5 — Pick your Hermes profile for the day
Click **Hermes** in the sidebar → **Chat** tab
At the top you'll see profile pills: **main · roofing · marketing · content**

- Working on leads/CRM → pick **roofing**
- Creating content/ads → pick **marketing**
- Repurposing video → pick **content**
- General AI work → pick **main**

---

### STEP 6 — Check your Outbox (30 seconds)
Go to **http://127.0.0.1:3737** (your M7 Command Center) → **Pipeline (Kanban)**
Review anything sitting in "⛔ Human Approval (PAUSED)" — those are ready for your GO.

---

## Your 3 browser tabs to always have open
1. **http://127.0.0.1:3000** — Agentic OS (Hermes, NotebookLM, Kanban, Paperclip)
2. **http://127.0.0.1:3737** — M7 Command Center (Execute Playbook, Outbox, Memory)
3. **http://127.0.0.1:8082/admin** — Complimentary Claude Code Admin (provider status)

---

## Quick commands for common jobs (paste into Claude Code or Hermes)

**Week of content:**
```
Read 01_Command_Center/M7_EXECUTE.md — execute this week's content: 8-12 branded captions, 2 GBP posts, 1 video repurposed into 6 cuts. CPPA CTA, IKO, RCAT #03-0637, 972-928-0788. Draft PAUSED to Outbox_Drafts.
```

**Research a topic:**
```
Act as the NotebookLM research node. Research [TOPIC] using my vault. Save a sourced brief to 05_Campaign_Factory/10_Research_Stage/ (PAUSED).
```

**Firewall check before publishing:**
```
python 04_Tech_Lab/scripts/brand_firewall.py --check "[paste your text]"
```

**Morning briefing from Hermes-Jarvis:**
Go to Hermes → Hermes-Jarvis → click the mic → say "Give me my daily briefing"

---

*Outbox Shield is always ON. You publish. Agents draft. Nothing goes live without your GO.*
