---
title: agentos.guide — 5 Latest Claude Guides, extracted & scrubbed to M7
type: knowledge_extract
status: active
date: 2026-08-10
sources: agentos.guide/{five-site-flywheel, agent-assembly-line, train-once-engine, ai-movie-machine, prime-agent}
scrub: Julian branding (aubergine/molten-gold/emerald) -> M7 Navy #1A365D + Gold #FBC02D + Cyan #00BFFF, ZERO green. "free" = organic/no-ad concept. Every output PAUSED to Outbox.
---

# 📚 5 Latest Claude Guides → M7 (extracted, scrubbed, applied)

## 1) The Five-Site Flywheel — 90-day SEO roadmap
**Method:** *One keyword in → 5 articles out → same day.* One striking-distance keyword + one real case study → 5 unique articles across 5 sites, cross-linked (~25 links/run), indexed in hours (Indexceptional).
- **Data = GSC, two signals:** **Gaps** (impressions, no page → build a page) · **Leaks** (rank but low CTR → rewrite the title).
- **13-step skill file** carries the SEO expertise; you supply only keyword + 2–3 paragraphs of real work.
- **Results claimed (16 mo):** 27.5K clicks, 1.08M impressions; one site 49 → 1,800+ clicks/week; 1,496 posts.
- **Documented failures:** guessed-email outreach (9/16 bounced → killed in 48h) · no-intent local pages (ranked, 0 clicks → removed) · 4-site cannibalization (consolidate to one owner) · cheap-model articles (didn't rank → use the strong model).

**🍍 M7 application:** You already have the inputs — **GSC connected** (striking-distance live), **real case studies** (39GB media + 430 reviews), **multiple domains** (roofingllc / contractors / restorations). Build the 13-step page skill as an M7 skill (brand-locked: CPPA, IKO, RCAT #03-0637, Navy/Gold/Cyan). Every page PAUSED to Outbox. *Note: static Eleventy/Netlify was their stack — you're on WordPress (roofingllc), so publish via wp-mcp-ultimate instead.*

## 2) The Agent Assembly Line — graph engineering
**Method:** Replace one over-loaded agent (a "loop" that suffers **context rot**) with a **team of one-job agents in parallel** (a graph). Nodes = agents, edges = handoffs. Steps with no dependency run at the same time.
- **Cost:** multi-agent ≈ 15× tokens. Fix with **prompt caching** (shared instructions → $10 run drops to ~$1) + **model-per-station** (cheap models for grunt work, best model only on the checker).
- **Limits:** ~16 parallel agents (CPU cores) in Claude Code; **pace in groups of ~6** or you trip rate limits (20-at-once → 14 fail; groups of 6 → all pass).
- **Checker rules:** (1) the builder **never** checks its own work — use a **fresh, separate** agent; (2) put your **best model** on the checker. Stack different-question checkers (correctness / simplify / verify / design).
- **10-min start:** draw the process as boxes; for each arrow ask *"does the next step need the last step's output?"* No → parallel. Hand the drawing to Claude Code.

**🍍 M7 application:** Your **Agent Kanban IS this** (dispatcher→worker→reviewer). Adopt the **checker rule** as your Outbox Shield: a separate reviewer agent brand-checks every draft (CPPA/IKO/zero-green) — never the writer. Run Kanban in waves of ~6, cheap models on grunt stations, strong model on the brand checker.

## 3) The Train-Once Engine — 11 Claude skills
**Method:** Each skill = a `.md` file (metadata · workflow · rules · edge-cases · output format · quality gates). Train once → runs forever; a **correction becomes a dated rule** appended to the file (compounds: 4 rules month 1 → 19 month 3). The 11: Voice Capture, News Radar, Winners Forge, **Keyword Scout**, **Memory Vault (read the vault FIRST)**, Ticket Dispatcher (Kanban), **SEO Miner** (GSC striking-distance pos 11–20, upgrade existing pages not new ones), Brand Designer, Video Director, **Goal Mode**, **Self-Upgrade Loop**.
- **Vault-first rule:** before any writing, read the brand/voice file + 3 past examples + the active campaign + fresh numbers — **never from memory.**
- **Evidence rule:** numbers trace to vault notes; unsourced facts ship marked `[unverified]`.

**🍍 M7 application:** This is literally your Studio's skill set. The **Memory Vault "read the vault first" + evidence rules** are your anti-hallucination guardrail — bake them into every M7 skill. **SEO Miner = upgrade existing pages, don't spawn competing ones** (avoids cannibalization). ⚠️ Their "Brand Designer" palette (aubergine/molten-gold/**emerald**) is banned here — M7 is **Navy/Gold/Cyan, zero green.**

## 4) The AI Movie Machine — Claude + Seedance 2.5
**Pipeline:** (1) **Character sheet** — 3+ reference photos + bio → Claude writes an image prompt → render (Higgsfield/GPT Image 2, neutral grey, 2K, 16:9). The exact outfit line becomes the "consistency line" reused in every scene. (2) **Scene prompts** — pitch the concept, Claude returns location/wardrobe/props/camera language, repeating the character description **word-for-word**. Avoid "8K/ultra-detailed/hyperreal." (3) **Multi-shot** — Seedance 2.5 takes one prompt with timestamped beats (0–3 wide, 3–6 close, 6–9 payoff), tag refs `@image1/@image2`.
- **Film grade:** prompt "shot on 35mm, film grain, natural skin, muted cinematic grade, shallow DoF" + an FFmpeg pass (letterbox 2.39:1, S-curve, grain). *(UGC/phone stays 9:16.)*

**🍍 M7 application:** You have **Higgsfield in the Studio + 39GB field media.** Use this for branded before/after + testimonial reels — but overlay **Navy/Gold** banners + RCAT #03-0637 end card, and keep the FFmpeg grade (it pairs with your `video-multiplier.py` 50/5/3 matrix). Everything lands PAUSED in Blotato.

## 5) Prime Agent / The Self-Upgrade Loop — /refine
**Method:** A terminal agent (Prime Intellect, MIT, Aug 2026) that keeps a **live Python session** so big files stay as *variables* (not in the token budget) — "context as a variable." **`/refine`** runs a 25-turn cycle: a separate pass reads the last 25 turns → writes small evidence-backed edits to a **JSON harness notebook** (versioned, roll-back-able) → next session loads the updated behavior. No retraining.
- ⚠️ **Cautionary tale:** in testing it saved a "cheating" shortcut as a reusable skill — *"the machinery compounds whatever works, whether or not it's what you meant."* **You stay the authority over what gets locked in.**

**🍍 M7 application:** The self-upgrade loop = the 4th part of your SEO engine (reviews its own work). Adopt the **safeguard**: every self-learned rule is **reviewed by you before it sticks** (Outbox Shield for the agent's own instructions). Context-as-variable is how to analyze your big files (the 39GB index, GSC exports) without blowing tokens.

---

## 🎯 The 3 things to actually adopt this week
1. **SEO page skill** (Five-Site + SEO Miner): striking-distance keyword + real case study → brand-locked page → PAUSED. Upgrade existing pages, don't cannibalize.
2. **The checker rule** (Assembly Line): a separate reviewer agent brand-checks every draft before Outbox; run Kanban in waves of 6.
3. **Vault-first + evidence rules** (Train-Once): every skill reads the vault + sources its numbers — no hallucinated claims.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference (extract cites banned words as rule definitions) -->
