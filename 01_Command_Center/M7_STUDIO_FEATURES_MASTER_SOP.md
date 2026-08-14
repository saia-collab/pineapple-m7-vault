---
type: studio_features_master_sop
title: M7 STUDIO FEATURES MASTER SOP — EVERY AI feature, what it does, pro/con, old vs new
audience: non-technical co-owner (brother)
date: 2026-08-14
companion_to: M7_MASTER_HANDOFF_FOR_BROTHER.md
scope: All 28 studio tabs + all 28 Hermes profiles — nothing left out.
one_rule: Every output lands PAUSED in the Outbox. Nothing goes live without a brother's GO.
---

# 🍍 STUDIO FEATURES MASTER SOP — THE COMPLETE LIST
**Every single AI feature on our Local Studio — what it's for, what you get, the pro, the con, and the old way vs the new way.** Nothing summarized away. Look at any tab and know exactly why it exists.

**📄 About the shareable link (Artifact):** this document also opens as a private **web page** (an "Artifact") that works on any phone or computer — no app, no login — so anyone can read it. It's the viewable copy of this vault file; update the file and the link updates.

**🖥️ Desktop or phone?** The **Studio below runs only on the Mac desktop** — that's where the coaches build. Your **phone is for reading this + approving plays**, not running the studio.

## 🏈 The one idea first
The Studio (`localhost:3737` on the Mac) is our **coaching facility.** Four kinds of staff:
1. **Coder agents** = **position coaches** (different brains for a task).
2. **Hermes** = the **front office** — one cockpit that swaps in a **roster of 28 personas** (Muse, Roofing, SEO, Leads…).
3. **Creative studio** = the **media department**.
4. **Coordinators** = they break a big goal into small assignments.

**Golden rule:** they all **draft; you approve.** Everything lands paused in the Outbox.

---

## PART 1 — THE CODER AGENTS (11 tabs — the position coaches)
| # | Agent tab | Use it for | Output goal | ✅ Pro | ⚠️ Con |
|---|---|---|---|---|---|
| 1 | **Claude** ⭐ | Anything a customer reads; building pages/files; brand-locked work | Brand-perfect page/post saved to vault | Best quality, obeys brand law, auto-saves | Uses our paid Claude plan |
| 2 | **OpenClaw** | An open-source Claude-style agent for self-driving tasks | A task run start-to-finish | Free/open, autonomous | Give it clear guardrails |
| 3 | **Hermes** | The front office — pick a persona (see Part 2) | Whatever that persona does | 28 specialists in one place, mostly free | Quality = the model you pick |
| 4 | **Antigravity** | Big multi-step builds by a **team** of agents | A whole task built by a squad | Powerful (Gemini), plans + splits work | Newer; a little setup |
| 5 | **Codex** | Heavy code + technical builds | Working code | Strong engineer (GPT-5.6) | Rate-capped; needs ChatGPT login |
| 6 | **Kimi Code** | Cheap long coding + drafting | Bulk code/text | Strong + cheap | Not brand-aware |
| 7 | **GLM 5.2** | Cheap heavy lifting, coding | Bulk output on a budget | Strong + free/cheap | Better at code than customer words |
| 8 | **Prime Agent** | A lead/premium orchestrator agent | Larger tasks coordinated | Handles bigger jobs | Keep it scoped |
| 9 | **Grok Build** | Anything needing **live/real-time** info (trends, X) | Current, of-the-moment takes | Sees today's signals | Needs X Premium; less brand-disciplined |
| 10 | **Free Claude Code** | Quick drafts that don't need to be perfect | A fast rough draft | **Free** (cloud), works when Mac is full | Smaller brain — not final customer copy |
| 11 | **Free AI Coder** | A second free coding option | A free code/text draft | No cost | Lighter than the paid coders |

**Pick rule:** customer-facing/brand → **Claude.** Free + quick → **Free Claude Code.** Live trends → **Grok.** Big team build → **Antigravity.** Unsure → **Claude.**

---

## PART 2 — HERMES FRONT OFFICE (all 28 profiles)
Hermes is **one cockpit** where a **"profile"** = a saved combo of *(a job personality + a model + skills)*. Two kinds: **job personas** (hire by the task) and **engine-runners** (just = which brain). Most run on free/cheap engines; all save to the vault.

### A) Job personas — hire these by the task
| Profile | Use it for | Output goal | ✅ Pro | ⚠️ Con |
|---|---|---|---|---|
| **main** | The default M7 Hermes for general work | On-brand general answer | Knows our whole context | Jack-of-all-trades |
| **muse** 🎨 | Content ideas — "10 angles for hail season" | A list of on-brand ideas | Endless ideas, brand-tuned | Ideas, not finished pieces |
| **roofing** | Roofing questions + roof-page copy | Roofing draft in our voice | Knows our roofing offer | Roofing only |
| **restoration** | Water/fire/mold restoration side | Restoration draft | Keeps that brand separate | Restoration only |
| **seo** | SEO briefs, keyword work | An SEO draft/brief | Ranking-focused | Needs GO to publish |
| **seo-lead** | Leads an SEO project across steps | A coordinated SEO push | Runs a whole SEO play | Bigger scope |
| **leads** | Lead intake + follow-up messages | A follow-up ready to send | Speed-to-lead | Paused until you send |
| **content** | Social + content copy | Ready-to-schedule content | On-brand, fast | Paused in Outbox |
| **marketing** | Campaign copy + angles | Campaign assets | Marketing-minded | Paused in Outbox |
| **jarvis** 🎙️ | Voice — hands-free talk | Spoken answers, logged | Great while driving | Voice quality varies |
| **julian** 🔐 | Holds credentials/keys safely | Secure key vault | Secrets out of chats | Don't expose it |
| **notebook-obsidian** | Pulls research notebooks into the vault | Synced research | Keeps film library current | Background job |
| **openmontage** | Video/montage assembly | A montage draft | Turns film into content | Rendering takes time |
| **game-dev** | Interactive/experiment builds | A prototype | Creative R&D | Not core business |
| **blank-state** | A clean Hermes with base M7 context | A fresh start | No leftover context | You supply the task |

### B) Engine-runners — same Hermes, different brain (pick for a specific model)
| Profile | Which brain | Best when |
|---|---|---|
| **gpt56** | OpenAI GPT-5.6 | Top reasoning (login/limits apply) |
| **grok-build** | xAI Grok | Live/real-time signals |
| **glm-5-2** | Zhipu GLM 5.2 | Cheap strong coding |
| **kimi-k2-7** | Moonshot Kimi K2 | Long context, cheap |
| **qwen-3-7** | Alibaba Qwen 3 | Free multilingual/coding |
| **hermes-cloud** | Nous Hermes (cloud) | Reliable free default |
| **local** | A model on the Mac | Offline (needs disk/RAM) |
| **ollama-glm-512** | Local Ollama GLM | Fully offline GLM |
| **omniroute** | OmniRoute free pool | Free, but flaky |
| **north-mini** | A small fast model | Quick cheap answers |
| **fusion** | A blended/general setup | All-purpose |
| **hy3** | An alternate engine | Backup option |
| **sakana-fugu** | Experimental (Sakana) | R&D only |

**Hermes overall:** ✅ one place, 28-deep bench, mostly free, auto-saves. ⚠️ free brains are weaker than **Claude** for final customer copy — draft in Hermes, brand-lock the final in Claude.

> **"Oracle" & "Apollo"** aren't set up yet. Want a dedicated **Oracle** (deep research/analysis) and **Apollo** (creative/campaign)? Say so — I'll build them like Muse: a named specialist with its own brief.

---

## PART 3 — THE MEDIA DEPARTMENT (9 tabs)
| Feature | Use it for | Output goal | ✅ Pro | ⚠️ Con |
|---|---|---|---|---|
| **Open Design** | Landing pages, graphics, dashboards, decks | A designed page/graphic | Designs locally, drives your agents | Must be **Started** + pointed at a cloud model |
| **Video** | Turn job footage into video | A video clip | Uses our 39 GB of film | Rendering needs disk + time |
| **OpenMontage** | Auto-assemble montages/reels | A montage/reel | Fast from raw clips | Needs source footage |
| **Video Editor** | Trim/polish a clip by hand | A finished cut | Fine control | More hands-on |
| **Music** | Background tracks for videos | A music bed | Royalty-free, fast | Supporting role |
| **Game Studio** | Build little interactive games/tools | A playable prototype | Creative experiments | Not core business |
| **App Lab** | Prototype small apps/tools | A working mini-app | Turn ideas into tools | R&D |
| **Thumbnails** | Eye-catching post/video covers | A thumbnail | Boosts clicks | Cosmetic |
| **Notebook** (NotebookLM) | Study our 100 research notebooks; audio overviews | Research + summaries | Learns from Goldie/Hormozi/our playbooks | Research, not publishing |

---

## PART 4 — THE COORDINATORS (7 tabs)
| Feature | Use it for | Output goal | ✅ Pro | ⚠️ Con |
|---|---|---|---|---|
| **Mission Control** | See the whole studio at a glance | System status | One dashboard | View-only |
| **Pipeline** ("Inbox → Shipped") | Idea → agents plan → you approve once → built | A finished, filed deliverable | One human checkpoint, agents do the rest | Approve the plan first |
| **Kanban** | A task board you drive | Cards moving to Done | Simple + visual | You steer it |
| **Agent Kanban** | Drop a goal → agents plan/build/review live | A board built by agents | Hands-off building | Offline planner needs a local model (disk) — use cloud |
| **AI Agent Mastermind** | Many agents brainstorm one problem | A plan + assignments | Lots of brains at once | Keep it scoped |
| **Paperclip** | Assistant that files/organizes work | Sorted, filed output | Tidies the workspace | Helper role |
| **Memory** | What the agents remember about us | Our saved context | Nothing forgotten | — |

**Plus: SEO Content Pipeline** (inside Hermes) — the assembly line: **one keyword → 5 SEO articles → deploy.** ✅ bulk SEO fast. ⚠️ still paused for your GO.

---

## PART 5 — ⏮️ OLD WAY vs ⏭️ NEW WAY (the whole point)
| The task | 🐌 Old way | 🚀 New way (Studio) |
|---|---|---|
| **A city/SEO page** | Agency, weeks, $, off-brand | **Claude tab**, ~15 min, brand-locked, paused |
| **5 SEO articles** | Weeks of writing | **SEO Content Pipeline**, one keyword → 5 drafts |
| **Post a finished job** | Forget, or caption days later | **`/gbp-post`**, ~2 min |
| **Reply to a review** | Slow or ignored | **`/review-response`**, seconds |
| **A landing page** | Scorpion — green, "$99", "FREE", weeks | **Open Design + our Kit**, minutes, brand-perfect |
| **A job-site reel** | Editor, days, $ | **OpenMontage** from our film, same day |
| **Content ideas** | Blank page | **Hermes Muse**, 10 angles instantly |
| **Research a competitor** | Hours of googling | **Notebook / Claude**, minutes |
| **A whole campaign** | Brief the agency, wait | **Antigravity / Pipeline** builds it, you approve |
| **Remember decisions** | Lost in texts + chats | **Vault + GitHub**, permanent, on your phone |
| **Cost + control** | Pay outsiders, hope it's on-brand | Mostly free/cheap, minutes, **you approve every piece** |

---

## PART 6 — "WHICH ONE DO I OPEN?" (cheat sheet)
- Customer will read it / must be on-brand → **Claude tab**
- Free + fast draft → **Free Claude Code**
- 5 SEO articles from a keyword → **SEO Content Pipeline**
- Content ideas → **Hermes → Muse**
- A designed landing page → **Open Design** (or paste our Kit into Antigravity / Google AI Studio)
- A video from job footage → **OpenMontage / Video**
- Research a topic → **Notebook**
- Break a big goal into steps → **Pipeline** or **Agent Kanban**
- Live trends / X → **Grok Build**
- A specific engine (GPT/Grok/GLM/Kimi/Qwen) → **Hermes → that engine-runner profile**

---

## THE ONE RULE
Every feature above is an **assistant coach.** They draft, design, research, and plan at incredible speed — but **a play only runs when you or Saia signal GO.** Everything lands **paused in the Outbox** first. That's what keeps us fast *and* safe. 🍍

<!-- M7-FIREWALL-EXEMPT: features SOP — governance doc; quotes banned terms ("free"/"$99") to contrast old vs new -->
