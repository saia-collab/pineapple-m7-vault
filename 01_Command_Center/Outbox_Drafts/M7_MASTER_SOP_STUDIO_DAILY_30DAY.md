---
title: M7 MASTER SOP — Local Studio Agentic OS · Daily Workflow · 30-Day Gameplan
type: master_sop
status: PAUSED — review, then move to 01_Command_Center/ when approved
for: Saia · Naa Sione · VA · Hermes (/learn this) · Claude Code
build: Agent OS 2026-08-06 (Pineapple brand paint) · Hermes v0.20.0
brand_law: CPPA (never "free") · IKO Certified (never GAF) · Full Restoration Coverage (never "$0 down") · The Pineapple Standard · RCAT #03-0637 · Navy #1A365D + Gold #FBC02D + Cyan #00BFFF · ZERO GREEN · Outbox Shield
last_updated: 2026-08-06
---

# 🍍 M7 MASTER SOP — Studio · Daily · 30-Day

> Consolidated from: MASTER_SOP_Command_Deck, HERMES_PLAYBOOK, Hormozi Playbook, Near-Me Pipeline,
> Goldie 30-Day Stack, Higgsfield Command Deck, and the Outbox_Drafts SOP library.
> **Everything lands PAUSED in `01_Command_Center/Outbox_Drafts/`. Saia is the only publisher and the only spender.**

---

## PART 1 — WHICH STUDIO TAB DOES WHAT (feature → task → exact prompt)

Open the tab, paste the prompt, fill the [BRACKETS]. Every output stays PAUSED.

### 🧠 ORCHESTRATE & BRAND (the gatekeepers)
| Tab | Use it for | Paste this |
|---|---|---|
| **Hermes → Chat** | Daily driver. Runs SOPs, drafts, files. Switch persona in the profile bar. | *"Load the `seo` profile. Read HERMES_PLAYBOOK.md. Draft [task]. Brand law + PAUSED to Outbox."* |
| **Claude** tab | Final brand/voice QC before anything is staged. | *"Brand-check this draft against CPPA/IKO/no-green/RCAT #03-0637. Flag every violation, rewrite clean."* |
| **AI Agent Mastermind** | Cross-critique a plan with several models before building. | *"Debate this campaign plan as Research/Writer/Editor/Judge until airtight. Pineapple voice."* |

### 🏗️ BUILD & CODE (pick the cheapest that fits)
| Tab | Best for | Cost |
|---|---|---|
| **Codex / GPT 5.6 Code** | Schema (JSON-LD), WordPress automation, dashboards, hardest builds | free (ChatGPT plan) |
| **opencode · jcode** | Fast free single-file tools + apps | free |
| **DeepSeek Coder · GLM 5.2 · Kimi · Qwen (Qoder)** | Cheap/fast coding second opinions | key/credits |
> Rule: free tab for drafts → Codex for the hard build → Claude/Hermes verifies brand → PAUSED.

### 📈 SEO (the revenue engine)
| Tab / sub-tab | Task | Prompt / action |
|---|---|---|
| **SEO → OpenSEO** | Pull striking-distance keywords (pos 5–20) from your GSC | needs DataForSEO key in `~/open-seo/.env` |
| **SEO → Research** | Keyword + market map for a city/service | *"SEO research for [service] in [Frisco]. Primary + supporting keywords, fan-out questions, sitemap."* |
| **SEO → Parasite** | One keyword → platform-native plays (X, Reel, Short) | pick a keyword you already rank for |
| **SEO → Generate** | Draft Pineapple-branded pages (roofing/restoration) | lands PAUSED in `Outbox_Drafts/SEO` |
| **Agent Kanban** (SEO cluster → Hermes) | Build a city×service page cluster as a board | give it a county seed; Planner→Builder→Reviewer; PAUSED |

### 🎬 CONTENT & MEDIA
| Tab | Task | Note |
|---|---|---|
| **Higgsfield** | AI images + video (ads, before/after, drone reveals) | 💳 shows credit cost, blocks until you confirm |
| **Video · OpenMontage · Video Editor · Muse Code** | 50/5/3 reels, montages, edits | Navy/Gold overlay, RCAT #03-0637 end card |
| **Thumbnails** | 6 branded thumbnail concepts | set your channel once in config |
| **Music · Game Studio · App Lab** | jingles, interactive, mini-apps | optional |

### 🔬 RESEARCH & MEMORY
| Tab | Task |
|---|---|
| **Notebook (NotebookLM)** | Ingest storm reports / policy docs / reviews → sourced briefs (needs `nlm login`) |
| **Memory (Obsidian)** | Your whole vault as searchable memory — Hermes reads it for grounding |
| **Fusion · Sakana Fugu** | Model councils for high-stakes decisions |
| **Loop** | "Loop engineering" — builder+judge until a quality gate passes |

---

## PART 2 — HERMES PROFILES: which chat runs which job
Switch in the profile bar (Hermes → Chat). Default brain = **gpt-5.6-sol via Codex** (free).

| Profile | Job | Model |
|---|---|---|
| `main` / `gpt56` | daily operator, catch-all | gpt-5.6-sol (free) |
| `seo` / `seo-lead` | SEO pages, GSC low-hanging fruit, clusters | gpt-5.6-sol (free) |
| `content` | blogs, captions, repurposing | gpt-5.6-sol (free) |
| `marketing` | campaigns, Hormozi offers | gpt-5.6-sol (free) |
| `roofing` / `restoration` | brand-safe service drafts (never cross terms) | gpt-5.6-sol (free) |
| `leads` | prospect research, outreach drafts (never sends) | gpt-5.6-sol (free) |
| `notebook-obsidian` | extract from vault + NotebookLM | gpt-5.6-sol (free) |
| `game-dev` / `blank-state` | builds, ad-hoc | gpt-5.6-sol (free) |
| `north-mini` / `omniroute` | free-model overflow | free OpenRouter |
| `glm-5-2` `kimi-k2-7` `qwen-3-7` `hy3` | premium brains | need OpenRouter credits |
> Switch brain mid-chat: `/model gpt-5.6-sol` · `/model cohere/north-mini-code:free` · (`/model anthropic/claude-sonnet-4.5` once credits added).

---

## PART 3 — HERMES GOAL MODE: daily / weekly / nightly
Paste into **Hermes → Goal Mode**. Each ends PAUSED in Outbox.

**🌅 DAILY (morning, ~15 min):**
```
Load the seo profile. Read HERMES_PLAYBOOK.md + M7_SEO_DAILY_SOP.md.
1. Pull today's top 3 striking-distance keywords (pos 5-20) for Frisco/DFW roofing.
2. Draft ONE optimized page improvement for the #1 keyword (CPPA, IKO, RCAT #03-0637, zero green, AEO first-40-words).
3. Draft 1 GBP post + 1 review-reply for any 4-5 star review.
Save all PAUSED to Outbox_Drafts/SEO. Give me a 3-bullet recap. Publish nothing.
```

**📅 WEEKLY (Monday, ~30 min):**
```
Load the marketing profile. Read M7_HORMOZI_PLAYBOOK.md + M7_INTEGRATED_CAMPAIGN.md.
1. One-page scorecard: last week's leads by source, response times, jobs closed.
2. Plan this week's 4 posts (70% value / 20% proof / 10% offer) — hooks only.
3. Pick ONE Hormozi framework to apply this week (offer, price, or content machine).
Save PAUSED to Outbox_Drafts. Nothing goes live without my GO.
```

**🌙 END-OF-NIGHT (~5 min):**
```
Load the main profile. 
1. Summarize what was drafted today and what's waiting in Outbox_Drafts for my approval.
2. List tomorrow's top 3 priorities.
3. Append the session to the Agentic OS/Memories log in my Obsidian vault.
Do not publish, send, or spend.
```

---

## PART 4 — THE DAILY WORKFLOW (who does what)
| Time | Saia / Naa Sione | Hermes / Studio | VA |
|---|---|---|---|
| AM | Approve overnight Outbox; answer hot leads <5 min | Run DAILY Goal Mode → drafts PAUSED | Lead intake sweep, review responses |
| Mid | GO/NO-GO on drafts; adjuster calls (Naa Sione) | Build approved pages/cluster (Kanban) | GBP photos, confirmations |
| PM | Review social batch (Blotato) | Higgsfield/video renders (credit-gated) | Review-request sweep, calendar prep |
| Night | Read nightly recap | Run END-OF-NIGHT Goal Mode | Speed-to-lead log |

---

## PART 5 — THE 30-DAY GAMEPLAN
**Week 1 — Foundation.** Connect NotebookLM (`nlm login`) + DataForSEO (OpenSEO). Naa Sione finalizes brand voice doc. `/learn` this SOP into Hermes. Publish 1 optimized page/day (approved).
**Week 2 — Content pipeline.** 30 keywords mapped (OpenSEO). 5 job case studies (from real jobs). Agent Kanban builds a 10-page Frisco cluster → PAUSED → approve in batches.
**Week 3 — Scale + media.** Higgsfield ad swarm (credit-gated) for top 3 offers. GBP posts 3×/week. Review velocity push. Compound the winning pages.
**Week 4 — Systematize.** VA runs the daily loop solo. Monthly content batch (30 keywords + 10 studies). Master SOP updated. Review 30-day results: leads, rankings, reviews.

> Daily reflexes that never stop: answer every lead in **5 minutes**; text every finished customer for a Google review.

---

## PART 6 — DECISIONS STILL NEEDED (blocks nothing above that's free)
- [ ] Naa Sione's brand-voice doc (unblocks confident publishing)
- [ ] HQ address: Frisco (1 Cowboys Way) vs Lewisville (4400 State Hwy 121) — NAP must match everywhere
- [ ] OpenRouter credits (only if you want Claude/GLM/Kimi quality; free models work now)
- [ ] Logins: `nlm login` (NotebookLM), DataForSEO key (OpenSEO), optional Kimi/Qwen/Grok

---

## PART 7 — ONE SYSTEM, THREE SCREENS (mobile · desktop · local computer)
The vault `C:\Pineapple Contractors M7` is the single brain. GitHub is the shared memory between machines and chats.

| Screen | What runs there | Your job |
|---|---|---|
| **🖥️ Desktop (Local Studio)** | Full Studio at :3737 — every tab, Hermes, SEO engine, media. All execution here. | Drive the build; approve the Outbox |
| **💻 Local computer (vault + scripts)** | `04_Tech_Lab/scripts/` (brand_firewall, daily sync), Hermes home, the git repo. OS/Hermes write memory to `Agentic OS/`. | Run **LAUNCH_ALL.bat** each morning |
| **📱 Mobile (phone oversight)** | `01_Command_Center/MOBILE_STATUS.md` + `.json` — phone-readable snapshot of Outbox Shield state, what's waiting for GO, telemetry. Synced to your phone via Google Drive. | Open MOBILE_STATUS in the Drive app (or ask Claude-mobile to "search Drive for MOBILE_STATUS"); GO/NO-GO from your phone |

### Auto-sync loop (hands-free)
- **`CLAUDE MOBILE/M7_DAILY_SYNC.bat`** runs: intake → brand firewall → index → telemetry → mobile snapshot → git snapshot. Outbox Shield stays on.
- **`CLAUDE MOBILE/REGISTER_MOBILE_SNAPSHOT.bat`** (double-click once) runs the snapshot every 30 min → keeps MOBILE_STATUS fresh on your phone.
- Flow: agents draft on desktop → your phone shows what needs GO → you approve → desktop executes → git pushes → every screen is current.

### The rule that ties it together
**GitHub is the shared memory.** Every session ends with `git push`. So the desktop Studio, this Claude chat, a Cowork cloud agent, and your phone all read the same vault. No screen is ever stale.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
