---
title: M7 Upgrade Cheat Sheet — 2026-08-10 (Second Brain + Video + SEO skills)
type: cheat_sheet
status: active
date: 2026-08-10
note: What was installed/scanned this session, how to use each, and how it improves the current playbook.
---

# 🍍 M7 Upgrade Cheat Sheet — 2026-08-10

## ✅ What got done today (in your order: 3 → 2 → 1 → 4)

### 3️⃣ claude-obsidian — your Second Brain engine
- **Cloned** to `04_Tech_Lab/vendor/claude-obsidian/` (15 skills: `wiki`, `wiki-ingest`, `wiki-query`, `wiki-lint`, `save`, `think`, `canvas`…).
- **Vault bound:** `CLAUDE_OBSIDIAN_VAULT` → `03_Knowledge_Mat`. Ingest folders created: `inbox/`, `raw/`, `sources/`.
- **How to use** (Claude Code, from the vault): `claude --plugin-dir "C:\Pineapple Contractors M7\04_Tech_Lab\vendor\claude-obsidian"` → then `/wiki-ingest` (turn a source into linked notes), `/wiki-query <question>` (answer from your own evidence, flags contradictions instead of hallucinating), `/wiki-lint` (fix broken links).
- **Playbook upgrade:** turns `03_Knowledge_Mat` into a *provenance-tracked* second brain — every claim cites its source, and parallel workers draft into staging while one orchestrator commits once = **your Outbox Shield, built in.**

### 2️⃣ AgriciDaniel repos — scanned, cloned, ranked for M7
| Repo | Verdict | Why it earns a place |
|---|---|---|
| **claude-seo** | ⭐ MUST | 25 SEO sub-skills + 18 agents (technical/GEO/local/schema), Google-guided action plans → your in-house SEO agency, replaces the agency audits |
| **wp-mcp-ultimate** | ⭐ HIGH | 58 WordPress abilities via MCP → Claude/Hermes publish to pineappleroofingllc.com directly. *(Installs on the WP site, not the vault.)* |
| **skill-forge** | ⭐ HIGH | The proper "create-a-skill" builder → forge custom M7 skills (e.g. a CPPA-page generator) |
| **claude-cybersecurity** | MEDIUM | Scans scripts/`.env` for leaked keys — relevant after the WP-password exposure |
- All cloned to `04_Tech_Lab/vendor/` (gitignored). **Not yet installed as active skills** — that's the next step (say the word).

### 1️⃣ Videos watched + scrubbed into the knowledge mat
- `/watch` skill is **installed + live** (yt-dlp + ffmpeg + `WATCH_VAULT_DIR` → knowledge mat). Usage: **`/watch <youtube-url> <question>`**.
- Watched + scrubbed 2 latest Julian Goldie videos → **[2026-08-10_hermes-seo-engine_and_graph-engineering.md](03_Knowledge_Mat/raw/watched/2026-08-10_hermes-seo-engine_and_graph-engineering.md)**:
  - **The 24/7 Traffic Engine** — GSC impressions-no-clicks → real-case-study content → automated editorial backlinks → self-upgrading loop. *You already own every input (GSC connected, 39GB media, 430 reviews).*
  - **Graph Engineering** — teams of one-job agents in parallel + the **checker rule** (a *fresh* agent, best model, must brand-check every draft — never the one that wrote it). *Your Agent Kanban already is this.*

### 4️⃣ UTF-8 repair — checked, clean
No mojibake in your `03_Knowledge_Mat` docs (the corrupted characters were only in the raw NotebookLM header, already dropped). Nothing to fix.

---

## 🚀 How this upgrades the playbook (the point)
1. **SEO gets an in-house engine** (claude-seo) that maps onto your *already-connected* GSC striking-distance data + real case studies — the exact 4-part loop from the video, brand-locked.
2. **Video → knowledge** is now one command (`/watch`), so every Julian Goldie update or client testimonial becomes a searchable, scrubbed note in your second brain instead of 15 minutes you have to sit through.
3. **Second brain gets provenance** (claude-obsidian) — no more hallucinated facts; every SOP claim cites a source.
4. **Multi-agent quality** — the checker rule fixes the weakest link in your Kanban: a separate reviewer agent brand-checks before the Outbox, every time.

## 👉 Not done yet (honest — pick the next one)
- **Install claude-seo + skill-forge** as active skills (they're cloned, not wired in).
- **wp-mcp-ultimate** → upload to your WordPress site (WP-side, needs your admin).
- **Fetch the 5 agentos.guide guides** you listed (five-site-flywheel, ai-movie-machine, agent-assembly-line, train-once-engine, prime-agent) → scrub → append to knowledge.
- **`/watch` more videos** from the Skool/community list.


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
