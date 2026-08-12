---
type: operating_model
title: AI DOES THIS / YOU DO THIS — the delegation map
status: active
date: 2026-08-11
source: distilled from the 126-note NotebookLM extraction + M7 setup
note: The rule never changes — AI drafts & builds EVERYTHING to PAUSED. You approve + do the human-only steps.
---

# 🍍 AI DOES THIS / YOU DO THIS
**The one rule:** an AI agent can research, write, build, and organize almost everything — but it all lands **PAUSED** in `Outbox_Drafts/`. **You** are the only one who approves, publishes, spends, signs in, or talks to a customer. That's the Outbox Shield, and it's your safety net.

---

## ✅ HAND TO AI (it can execute AND finish — lands PAUSED)

| Task | Tool to use | Status |
|---|---|---|
| **SEO on-page audit** of a page | Claude Code / Hermes Goal | ✅ ready |
| **City & service pages** (Frisco, McKinney, Allen…) | Hermes Goal Mode / Kanban | ✅ ready |
| **Collin County cluster** (5 pages) | Hermes Kanban | ✅ already running |
| **LocalBusiness / FAQ JSON-LD schema** | Claude Code | ✅ ready |
| **Keyword / striking-distance scan** | SEO tab (OpenSEO) | ✅ ready |
| **GBP review replies** (ZIP-optimized) | Hermes (leads profile) | ✅ ready |
| **Reel/short scripts, weekly captions** | Hermes Muse | ✅ ready |
| **Video script + b-roll plan** | Video Director | ✅ ready |
| **Thumbnails** | Thumbnail Studio | ✅ ready |
| **Roof-age / urgency calculator, quote forms** | Hy3 / Loop / Free Claude Code | ✅ ready |
| **Competitor & storm research briefs** | Hermes Goal Mode | ✅ ready |
| **Lead scoring drafts** (1–100, CARPARK) | Hermes (leads) | ✅ ready |
| **Brand-firewall sweep** of drafts | Claude Code / brand_firewall.py | ✅ ready |
| **Ingest NotebookLM → vault** | `/notebook-ingest` | ✅ ready |
| **Organize vault, indexes, MoC** | Claude Code | ✅ ready |
| **Commit + push (shared memory)** | Claude Code | ✅ ready |
| **Draft** the CRM parser / webhook / deploy scripts | Claude Code | ⚠️ draft only — review before running |

**How you trigger these:** the copy-paste prompts are in your [Prompt Control Panel](M7_PROMPT_CONTROL_PANEL.md); which-tool-when is in your [Study Guide](M7_STUDIO_STUDY_GUIDE.md).

---

## 🙋 ONLY YOU CAN DO (human-required — by law or by design)

| Task | Why it's yours |
|---|---|
| **Say "GO" / approve a draft** | Outbox Shield — nothing ships without you |
| **Publish / deploy a page live** to WordPress | The go-live click is yours (AI stages it as a paused draft) |
| **Spend money** — ads, subscriptions, API top-ups | AI never spends. You authorize every dollar |
| **Enter credentials / API keys / passwords** | Security rule — AI never handles secrets. You paste keys yourself |
| **Sign in / OAuth / connect an account** (WordPress, xAI, OpenRouter) | Logins are yours |
| **Send a real message / call a customer** | AI drafts; you send. Speed-to-lead dial is human |
| **Change account or system settings** | Yours only |
| **Verify facts & final branding** | You confirm (esp. your brother's final branding markdown) |
| **The physical business** | Roof inspections, drone photos, the actual jobs |
| **Film YOUR founder video / record your voice** | That's you on camera (the `pineapple-founder-intro` clip) |
| **Final calls** — pricing, which leads to chase, what actually goes live | Owner decisions |

---

## 🤝 THE HANDOFF (how every task actually flows)

```
AI: research → write → build → brand-check → save PAUSED in Outbox_Drafts/
                                   │
YOU: review  →  say "GO"  ─────────┘
                                   │
YOU (or AI on your GO): publish / send / spend
```

**Your whole job in the loop = review + GO.** Everything before that, delegate. Everything that spends money, sends a message, or goes public, you gate.

---

## 🚦 A note on the "download-only" code from NotebookLM
The `.py`/`.bat` scripts (CRM parser, webhook bridge, watchers, backup) are **AI-generated drafts**. An agent can *write and stage* them — but **you (with me) review before any of them run**. Never let AI-written code auto-execute on your live site or CRM. That's the one place "AI can build it" ≠ "AI should run it unseen."

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
