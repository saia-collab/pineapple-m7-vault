---
type: hermes_profile_guide
title: M7 HERMES PROFILE GUIDE — which employee, when, on which feature
status: active
date: 2026-08-12
source: distilled from 17 Hermes video transcripts + 15 markdown SOPs + your live 27 profiles
pairs_with: M7_HERMES_MASTER_CHEATSHEET.md · M7_HERMES_101_WALKTHROUGH.md · M7_STUDIO_STUDY_GUIDE.md
brand_lock: CPPA not "free" · IKO Certified not GAF · Navy/Gold/Cyan, zero green · Roofing Made Sweeter · no proverbs · (972) 928-0788 · RCAT #03-0637
note: Everything lands PAUSED in Outbox_Drafts. Saia is sole publisher.
---

# 🛰️ M7 HERMES PROFILE GUIDE
**A profile = one isolated employee: its own model + SOUL.md (brand rules) + tools + memory.** Switch with the pill bar in Hermes → Chat, or `hermes -p <name>`. You have **27**. Use the right one for the job so a roofing employee never writes restoration copy.

---

## 👥 YOUR PROFILES — which one, when, what model

### 🍍 Roofing-work profiles (customer-facing — full brand law)
| Profile | Use it for | Model | Best studio feature |
|---|---|---|---|
| **main** / **default** | general roofing questions, daily driver | gpt-5.6-sol | Chat, Goal Mode |
| **roofing** | speed-to-lead, CPPA booking, lead scoring, CARPARK close | gpt-5.6-sol | Chat, Kanban |
| **seo** | city/service pages, on-page, schema | gpt-5.6-sol | Goal Mode, SEO tab |
| **seo-lead** | the SEO orchestrator (runs the Kanban SEO cluster) | gpt-5.6-sol | Kanban |
| **leads** | GBP review replies, follow-ups, lead routing | gpt-5.6-sol | Outreach (PAUSED) |
| **marketing** | campaigns, offers, social captions | gpt-5.6-sol | Goal Mode, Muse |
| **content** | blog/reels drafts, repurposing | gpt-5.6-sol | Muse, Studio |
| **restoration** | **Brand B only** (fire/water/mold) — never roofing vocab | gpt-5.6-sol | Chat |

### 🎙️ Content + voice
| Profile | Use it for | Notes |
|---|---|---|
| **muse** | the 24/7 content furnace — daily ranked video ideas | reads your channel; forges ideas |
| **jarvis** | hands-free voice ("hey Hermes"), daily briefing | voice persona; needs mic |

### 🧠 Model-runner profiles (pick the brain for the job)
| Profile | Model | When |
|---|---|---|
| **gpt56** | GPT-5.6 Sol (Codex, free) | strong default, BUILD/code lane |
| **local** / **ollama-glm-512** | Ollama local | $0 bulk drafts/cleanup |
| **qwen-3-7** | Qwen 3.7 Max (1M ctx) | long autonomous runs (hours) |
| **kimi-k2-7** | Kimi K2.7 | heavy coding builds |
| **grok-build** | Grok/xAI | real-time X + image/video (needs SuperGrok login) |
| **glm-5-2** | GLM 5.2 (z.ai) | needs credits |
| **hy3** | Tencent Hy3 | needs credits |
| **omniroute** | free-model gateway (:20128) | big free pool (paste key in auth.json) |
| **hermes-cloud** | Nous Portal | run in the cloud |
| **game-dev** | gpt-5.6-sol | build tools/games/quizzes (App Lab) |
| **north-mini / fusion / sakana-fugu / blank-state** | assorted / template | experimental — skip until needed |

### 🔒 Special
- **julian** = your credential vault (Hy3/Higgsfield/xAI). **Leave it alone.**
- **notebook-obsidian** = the vault/memory + MCP profile (now has Jupyter + Unreal + **Obsidian** bridge).

---

## 🎛️ THE STUDIO FEATURES — when to reach for each
| Feature (Hermes tab) | What it's for | Which profile |
|---|---|---|
| **Chat** | ask one thing, quick | any (pick by topic) |
| **Goal Mode** | give a goal, it runs all steps to done | seo / marketing / roofing |
| **Kanban** | drop a big job → agents build in parallel | seo-lead (orchestrator) |
| **Mixture (MoA)** `/moa` | council of models → 1 best answer | any hard decision |
| **Sub-agents** | `delegate_task background=true` — spawn workers, keep working | any big multi-part job |
| **Muse** | daily content ideas from your channel | muse |
| **Oracle** | grounded Q&A from your vault | notebook-obsidian |
| **Astros** | YouTube trend ideas (keyless works) | any |
| **Apollo** | voice conversation | jarvis |
| **Studio** | generate image/video/voice | content |
| **Outreach** | draft messages (PAUSED) | leads |
| **MCPs** | connect tools (GitHub, Obsidian, WordPress) | notebook-obsidian |
| **Control Room / Manage** | health, skills, profiles | any |

**Non-Hermes studio tabs:** Free Claude Code / opencode = $0 coding · SEO = keyword engine · Video/OpenMontage = video · Open Design = pages/decks · Thumbnails · Loop = build-until-it-passes · Prime Agent = autonomous Python.

---

## 🔄 THE ONE PATTERN (every guide says the same thing)
**Brain (model) → Agent (Hermes profile) → Memory (Obsidian vault) → Loop.** The profile picks the brain; the vault gives it your context; every run makes it smarter. Route cheap jobs to free models, save premium for hard work.

## 📅 DAILY FLOW
1. **Morning:** `main` or `roofing` → Chat → "top 3 roofing tasks today + which tab for each."
2. **Build:** `seo` → Goal Mode (a city page) OR `seo-lead` → Kanban (the 5-page cluster, parallel).
3. **Content:** `muse` → 10 ranked ideas.
4. **Decide:** `/moa` for a big call.
5. **Evening:** review Outbox → say GO → "commit and push."

## 🆕 v0.20 features to lean on
Wake word ("hey Hermes") · grounded citations (research) · async sub-agents (parallel) · mid-turn correction (steer without restart) · smart approvals (asks before publish/send/spend).

## 🔒 STANDING RULES
Brand: CPPA · IKO Certified · Full Restoration Coverage · The Pineapple Standard · zero green · no Tongan proverbs · (972) 928-0788 · RCAT #03-0637. **Outbox Shield:** all output PAUSED; Saia publishes.

> Study deeper: **NotebookLM notebook "PM7 Hermes Study + Daily Updates"** now holds all 17 videos + the cheat sheet — ask it *"explain profiles / MoA / sub-agents with the exact commands."*

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
