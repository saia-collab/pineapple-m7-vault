---
type: execution_priority
status: active
last_updated: 2026-08-02
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🍍 BACK FROM VACATION — DO THIS, NOT MORE SETUP

**Pineapple Contractors** · RCAT #03-0637 · IKO Certified · Since 2005 · 972-928-0788

> You have been **configuring**, not **executing**. Everything you need is already
> installed. This file tells you what to *do* — in order, by day — to get leads.
> **Do not download, unzip, or install one more thing until you have run §1 for a week.**

---

## FIRST: the 3 "Claudes" — stop mixing them up

This is why you keep getting stuck. There are **three different Claudes** and each
does a different job. They are not the same window.

| # | Which Claude | Where it lives | What it does | You use it for |
|---|--------------|----------------|--------------|----------------|
| 1 | **Claude Desktop app** | The purple app on your taskbar | Chat + **Skills** + Connectors (DataForSEO) | **The 6 SEO skills.** This is where they go. |
| 2 | **Claude Code** | Inside the vault / terminal | Edits files, fixes launchers, git | Fixing the OS, building docs (what I am) |
| 3 | **"Claude" tab in Agentic OS** | localhost:3737 studio, left sidebar | A view *of* Claude inside the dashboard | Just a window — ignore for now |

**The SEO skills from the video go into #1 — the Claude Desktop app. Nowhere else.**
Not the Agentic OS. Not here. The Desktop app.

---

## 1. THE MONEY LAYER — leads THIS WEEK (do this first, every day)

SEO is real, but it is a **6–12 week** payoff. If you need leads *this week*, leads
come from these four, in this order. This is your daily money loop.

### ☀️ EVERY MORNING (15 min) — Speed-to-Lead
1. Open your phone + LSA notifications. Any lead from overnight?
2. **Text back within 5 minutes** using the pinned template in `M7_LEAD_ENGINE.md`.
   → A 5-minute reply can *double* your booking rate. This is the single biggest win.
3. Every lead older than 5 min while you were away — text them the follow-up template anyway.

### 🌆 EVERY EVENING (10 min) — Reviews
1. Any job finished today? Send the same-day review text (`M7_LEAD_ENGINE.md`).
2. Any review from the last 3 days you haven't replied to? Reply to it.
   → More 5-star reviews = higher LSA rank = **cheaper** leads next week.

### 📅 TWICE A WEEK (20 min) — Google Business Profile
1. Post one photo + caption to GBP (a recent job, a crew shot, a storm callout).
2. Drafts go to `Outbox_Drafts/` first. You review, then you post. Never auto-post.

### 💰 WHEN READY — Meta / LSA spend
- Only after the above is a habit. Ads amplify a working loop; they don't replace it.
- Budget + kill rules live in `M7_INTEGRATED_CAMPAIGN.md`. **You** click launch. Agents never spend.

> **If you do only ONE thing this week: reply to every lead in 5 minutes and ask
> every finished job for a review.** That alone moves revenue. Everything below is
> to make *next month* cheaper — not this week.

---

## 2. THE SEO LAYER — the 5-skill loop (set up once, run weekly)

This is the "One Keyword Empire" system from the video. It is a **compounding**
play: set it up now, run it weekly, and in 6–12 weeks it lowers your cost per lead
because you rank and get cited instead of paying per click.

### One-time setup (in the Claude DESKTOP app — 15 min)
1. **DataForSEO account:** sign up (free $1 credit — a full 5-skill run costs cents).
2. In Claude Desktop: **Customize → Connectors → Add custom connector**
   - Name: `DataForSEO`  ·  URL: `https://mcp.dataforseo.com/mcp`
   - Connect → approve OAuth → choose **allow all** so it stops interrupting.
3. **Settings → Capabilities →** turn ON code execution + file creation.
4. Create a Claude **Project** named `Pineapple Roofing` (one website = one Project).
   That Project is where the site's memory (`site-brief.md`) lives.
5. **Customize → Skills → upload skill**, one at a time — all 6 zips.
   Your backup copies are in `04_Tech_Lab/claude_seo_skills/`.

### The weekly run order (always this order — each skill feeds the next)
| Order | Skill | Command | Output |
|-------|-------|---------|--------|
| **0 — once** | Site Brief Builder | `Use site-brief-builder on https://pineappleroofingllc.com/` | `site-brief.md` → upload into Project knowledge |
| **1** | Keyword & Fan-Out Map | `Run keyword-fanout-map with the seed keyword "roof replacement frisco tx"` | HTML dashboard + CSV of clusters |
| **2** | SEO Content Writer | `Run seo-content-writer` | A page draft — **answer its experience questions honestly** |
| **3** | On-Page Optimizer | `Run onpage-optimizer on [URL]` | Priority fix list |
| **4** | Internal Link Architect | `Run internal-link-architect on [URL]` | Where to link + anchor text |
| **5** | AI Visibility Checker | `Run ai-visibility-checker on pineappleroofingllc.com` | Citation baseline + gap list |

> **Skill 3 is the weekly traffic mover.** In Google Search Console → Pages →
> **"Crawled, currently not indexed"** — pick 1–2 pages/week, run On-Page Optimizer,
> do exactly what it says, resubmit. That is `GSC_Connect.bat`'s whole purpose:
> get you to that Search Console screen fast.

The loop closes: Skill 5's gap list becomes Skill 1's next seed keyword. That's why
it's a loop, not a one-time task.

---

## 3. THE LAUNCHER — one button, already fixed

- **`LAUNCH_ALL.bat`** (on your Desktop + vault root) — starts the whole local OS.
  Now points to the correct **2026-07-31** pack. Just double-click it.
- **`GSC_Connect.bat`** — shortcut to your Google Search Console (for Skill 3 weekly).
- Ports: Command Center **3939**, Agentic OS **3737**. Never change these — see `PORT_MAP.md`.

Do **not** run `UPDATE_AGENT_OS.bat` again unless a genuinely newer pack than
2026-07-31 exists. You are current.

---

## 4. THE ONE RULE THAT KEEPS YOU UNSTUCK

> **Execute for a full week before adding anything new.**
> Not a new pack. Not a new Hermes version. Not a new skill. Not a new tab.
> If it isn't in §1 (leads this week) or §2 (SEO weekly), it waits.
> Red badges on tabs you don't use are **not problems.** Ignore them.

You have more working than you think. Go reply to a lead.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
