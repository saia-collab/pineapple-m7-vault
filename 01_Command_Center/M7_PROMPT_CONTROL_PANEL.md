---
type: prompt_control_panel
title: M7 PROMPT CONTROL PANEL — copy-paste prompts + which AI to paste into
status: active
date: 2026-08-11
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
note: ADHD-friendly single-glance panel. Nothing here publishes. Every output lands PAUSED in Outbox_Drafts until you say GO.
---

# 🍍 M7 PROMPT CONTROL PANEL
**Stop opening folders. This one file has every prompt + tells you which AI tab to paste it into.**

Slogan lock: **"Roofing Made Sweeter" · "The Pineapple Standard."** No Tongan proverbs. No "free" (→ CPPA). No green. No GAF (→ IKO Certified).

---

## ⚡ 10-SECOND ROUTER — "I want to ___"

| I want to… | Paste into this tab | Prompt # |
|---|---|---|
| Audit my website page for SEO problems | **Claude Code** (or Hermes Goal) | **#1** |
| Write a city / location page (Frisco, Allen…) | **Hermes → Goal Mode** | **#2** |
| Write a service page (roof replacement, hail…) | **Hermes → Goal Mode** | **#3** |
| Fix my Google map/schema (the "Mosso" bug) | **Claude Code** | **#4** |
| See what keywords I can win this week | **Claude Code** (claude-seo) | **#5** |
| Turn a job photo into a Reel/short script | **Hermes → Goal Mode** | **#6** |
| Get a week of social captions | **Hermes → Goal Mode** | **#7** |
| Ask a customer for a Google review | **Hermes → Goal Mode** | **#8** |
| Research a storm / competitor before I act | **Hermes → Goal Mode** | **#9** |
| Save a good AI answer into my brain (vault) | **Claude Code** (`/save`) | **#10** |
| File a document into my Second Brain | **Claude Code** (`/wiki-ingest`) | **#11** |
| Ask my Second Brain a question | **Claude Code** (`/wiki-query`) | **#12** |
| Build a tool/calculator (no code by me) | **Hermes → Agent Kanban → Hy3** | **#13** |
| Do a coding job for FREE (no Claude tokens) | **Free Claude Code / opencode** | **#14** |
| Check content is brand-safe before staging | **Claude Code** | **#15** |
| Save today's work so cloud-me remembers | **Claude Code** | **#16** |

---

## 🟦 THE 4 TABS THAT ACTUALLY WORK (ignore the rest for now)

1. **Hermes → Goal Mode** = your autopilot writer/researcher. Give it a goal, it runs the steps. *Best for words: pages, captions, research, review asks.*
2. **Hermes → Agent Kanban (Hy3 coder)** = drag a card, an agent builds it. *Best for tools/calculators/pages that need code.*
3. **Claude Code** (this window) = the boss/orchestrator + skills (`/seo-team`, `/watch`, `/wiki`, brand firewall, git). *Best for judgment, audits, knowledge, shipping.*
4. **Free Claude Code / opencode** = coding on **free models** so you don't burn paid tokens. *Best for cheap builds & edits.* (Set Model Config → `open_router/qwen/qwen3-coder:free` or `ollama/gemma2`; make sure **fcc-server** is running.)

> If a fancy tab (Muse, Astros, etc.) throws "401 / user not found / needs key" — **skip it.** It just needs a login/API key. The 4 above are all you need to ship.

---

## 📋 THE PROMPT LIBRARY (copy the whole gray block)

> Every content prompt already bakes in the brand lock. You don't add anything — just paste.

### — SEO —

**#1 · On-page SEO audit** — *When: before you touch any website page. Where: Claude Code (or Hermes Goal).*
```
Act as my SEO auditor for Pineapple Roofing (pineappleroofingllc.com), Frisco/DFW.
Audit THIS page for on-page SEO: [paste the URL or the page text].
Check: title tag, meta description, H1/H2 structure, keyword targeting, internal links,
image alt text, LocalBusiness/RoofingContractor schema, NAP consistency (name/address/phone),
and any "free"/GAF/green violations. Flag the single biggest problem first (P0), then P1/P2.
Output a fix-list I can hand to a builder. Brand lock: CPPA not "free", IKO Certified not GAF,
"Roofing Made Sweeter", no green, phone (972) 928-0788, RCAT #03-0637. Save PAUSED to Outbox_Drafts.
```

**#2 · City / location page** — *When: building out DFW city pages. Where: Hermes Goal Mode.*
```
Goal: Write a location page for Pineapple Roofing targeting "[CITY] roofing company" (e.g. Frisco, Allen,
McKinney). 700–900 words. Include: local hook, storm/hail context for that city, our services,
why us (RCAT #03-0637, IKO Certified, 5-star, since 2005, Polynesian family-owned), a CPPA call-to-action,
FAQ (3 Q&A), and a LocalBusiness schema block. Brand lock: never "free" (use CPPA — Complimentary
Professional Photo Audit), never GAF (IKO Certified), no green, slogan "Roofing Made Sweeter",
phone (972) 928-0788. Save the draft PAUSED in 01_Command_Center/Outbox_Drafts/SEO/.
```

**#3 · Service page** — *When: a service needs its own page. Where: Hermes Goal Mode.*
```
Goal: Write a service page for "[SERVICE]" (e.g. roof replacement, hail damage repair, storm restoration)
for Pineapple Roofing, Frisco/DFW. 700–900 words: problem the homeowner feels, our process step-by-step,
materials (IKO Dynasty/Cambridge, the 50-Year Edge), trust signals, CPPA offer, FAQ, and RoofingContractor
schema. Brand lock: CPPA not "free", IKO Certified not GAF, no green, "Roofing Made Sweeter",
(972) 928-0788, RCAT #03-0637. Save PAUSED to Outbox_Drafts/SEO/.
```

**#4 · Fix Google/schema identity** — *When: your map/schema shows wrong info. Where: Claude Code.*
```
My site's schema/Google Business info is wrong or inconsistent. Here's what shows: [paste it].
Truth: Pineapple Roofing LLC, Frisco HQ (1 Cowboys Way, Frisco, TX 75034), (972) 928-0788,
RCAT #03-0637, IKO Certified, since 2005. Generate corrected JSON-LD (RoofingContractor +
LocalBusiness), fix NAP so name/address/phone match everywhere, and list every place I need to
update it. Flag any leftover wrong business name or old address. Save PAUSED to Outbox_Drafts/SEO/.
```

**#5 · Keyword / opportunity scan** — *When: deciding what to write next. Where: Claude Code (claude-seo / OpenSEO).*
```
Scan my Search Console + target market (Frisco/DFW roofing) and give me the top 10 keyword
opportunities I can realistically rank for in 90 days. For each: the keyword, why it's winnable,
the page type to build (city/service/FAQ), and the intent. Prioritize storm/hail/replacement money
terms. Output a ranked table. Don't publish anything — this is planning only.
```

### — CONTENT & SOCIAL —

**#6 · Reel / short script from a job** — *When: you have a roof photo/video. Where: Hermes Goal Mode.*
```
Goal: Write a 30-second vertical Reel/Short script for Pineapple Roofing from this job: [describe the
job + paste photo filename]. Structure: hook (first 3 seconds), 3 quick value beats, CPPA call-to-action.
Give me on-screen captions + a spoken voiceover line for each beat. Tone: confident, local, "Roofing Made
Sweeter", The Pineapple Standard. Brand lock: no "free" (CPPA), no GAF (IKO Certified), no green,
(972) 928-0788. Save PAUSED to Outbox_Drafts/Content/.
```

**#7 · One week of social captions** — *When: filling the content calendar. Where: Hermes Goal Mode.*
```
Goal: Write 7 social captions (one per day) for Pineapple Roofing, Frisco/DFW roofing. Mix: 2 educational
(hail/roof-age tips), 2 trust (RCAT #03-0637, IKO Certified, 5-star, since 2005), 2 offer (CPPA), 1 local/community.
Each: 1 hook line + 2-3 body lines + 3 hashtags + a CPPA CTA. Brand lock: never "free", never GAF, no green,
"Roofing Made Sweeter", (972) 928-0788. Save PAUSED to Outbox_Drafts/Content/.
```

**#8 · Google review request** — *When: a happy customer just paid. Where: Hermes Goal Mode.*
```
Goal: Write 3 versions of a text/email asking a customer for a 5-star Google review — same-day, 3-day
nudge, and 7-day final. Warm, short, first-name, one clear link line [REVIEW LINK]. Mention their specific
job [JOB]. No pressure, no discounts. Brand voice "Roofing Made Sweeter". Save PAUSED to Outbox_Drafts/.
```

### — RESEARCH & KNOWLEDGE —

**#9 · Storm / competitor research brief** — *When: before a campaign or a new area. Where: Hermes Goal Mode.*
```
Goal: Research brief for Pineapple Roofing. Topic: [recent storm in ___ / top 3 competing roofers in ___].
Give me: what happened / who they are, the angle homeowners care about, 3 content ideas I can act on this
week, and any claim I should NOT make without verifying. Keep it to one page. Facts only — flag anything
unverified. This is research, do not publish.
```

**#10 · Save a good answer to my brain** — *When: an AI gave you gold. Where: Claude Code.*
```
/save
```
*(Saves the current good answer into your Second Brain vault — grounded, sourced. Set to manual so it doesn't hoard.)*

**#11 · File a document into the Second Brain** — *When: you got a PDF/doc/guide. Where: Claude Code.*
```
/wiki-ingest [paste the file path or drop it in 03_Knowledge_Mat/inbox/]
```
*(Turns the source into linked, source-cited pages. Keeps a locked original first.)*

**#12 · Ask the Second Brain** — *When: "what did we decide about ___?" Where: Claude Code.*
```
/wiki-query What do we know about [topic]? Answer only from what's in my vault, with sources.
```

### — BUILD (no coding by you) —

**#13 · Kanban card for Hy3** — *When: you want a tool/page built. Where: Hermes → Agent Kanban.*
```
Build a [thing] for Pineapple Roofing. Example: a roof-age → replacement-urgency calculator.
Inputs: roof age, material, last inspection. Output: an urgency score + a CPPA call-to-action.
Colors: navy #1A365D, gold #FBC02D, cyan #00BFFF — ZERO green. Phone (972) 928-0788. Mobile-friendly.
Deliver the code; do not deploy — I'll review it PAUSED first.
```
*(Drop this as a card; the Hy3 coder builds it. This is exactly how your roof-age calculator got built.)*

**#14 · Free coding job (no paid tokens)** — *When: any build/edit. Where: Free Claude Code or opencode.*
```
[Describe the build/edit plainly, e.g. "Make a mobile-friendly HTML quote-request form: name, phone,
address, roof issue, photo upload. Navy/gold/cyan, zero green, (972) 928-0788. Save the file, don't deploy."]
```
*(First set Model Config → `open_router/qwen/qwen3-coder:free` (or `ollama/gemma2` for unlimited local) and confirm fcc-server is running. $0.)*

### — HOUSEKEEPING —

**#15 · Brand-safety check** — *When: before staging ANY content. Where: Claude Code.*
```
Run the brand firewall check on [file/folder] and tell me every violation: "free", GAF, green,
warrior/toa/six-brothers, Tongan proverbs, wrong phone/license. Report only — don't auto-change anything.
```

**#16 · Save the session (memory)** — *When: end of every work session. Where: Claude Code.*
```
Commit and push everything to GitHub with a clear message of what we did today, so my cloud chats
have the same memory. Then give me a 3-line summary of what changed.
```

---

## 🎨 THE BRAND LOCK (baked into every prompt above — FYI, you don't type it)
- **Never:** "free" · "cheap" · GAF · green · warrior/toa/six-brothers · Tongan proverbs
- **Always:** CPPA (Complimentary Professional Photo Audit) · IKO Certified · "Roofing Made Sweeter" · The Pineapple Standard
- **Colors:** Navy `#1A365D` + Gold `#FBC02D` + Cyan `#00BFFF` — **zero green**
- **Trust:** RCAT #03-0637 · IKO Certified · 5-Star · Since 2005 · Polynesian family-owned · **(972) 928-0788**

## 🚦 OUTBOX SHIELD (never changes)
Everything an AI makes lands **PAUSED** in `01_Command_Center/Outbox_Drafts/`. **Nothing** gets published, posted, sent, or spent until **you say GO.**

<!-- M7-FIREWALL-EXEMPT: governance-reference (technical doc; "free" here = free AI models/token-saving, not marketing copy) -->
