---
title: Watched & Scrubbed — Agent OS Q&A + Claude-Obsidian 2.0 (4 videos)
type: video_notes
status: active
date: 2026-08-10
sources:
  - "Agent OS Q&A (memory / voice booking / sync) — youtu.be/hcn8Q2VPcLw"
  - "11 Claude Skills (Train-Once) — youtu.be/4guPMTnZISk  [= the train-once guide]"
  - "Claude Obsidian 2.0 — youtu.be/UZr4lLHBKyo"
  - "Claude Obsidian 2.0 (author walkthrough) — youtu.be/oN8oZkT3FZU"
captured_by: yt-dlp captions -> scrubbed to M7 branding
---

# 🎬 Agent OS Q&A + Claude-Obsidian 2.0 — what to actually do

## The through-line: ONE vault, all agents
- You don't need GBrain/Hindsight/3 memory tools. **One Obsidian vault (a folder of files) that every agent reads + writes** beats three partial ones — less token use, no confusion, no "re-explain my business." **You already run this: `03_Knowledge_Mat`.**
- Sync across machines with **one** engine (Obsidian Sync / a synced folder / Tailscale direct / MCP) — never two, or you get conflicting copies.

## claude-obsidian 2.0 — the tool I set up this session, explained
**The loop (capture → ground → connect → use):**
1. **Capture** — drop a source in `inbox/`; it keeps a locked, immutable copy first.
2. **Ground** — every claim keeps a pointer to its source; tracks strength/freshness/contradiction. **When it doesn't know, it says so** (won't invent a citation; wants 2 sources for important facts). ← this is your anti-hallucination guardrail.
3. **Connect** — linked pages, Maps of Content, and Obsidian Canvas boards, built automatically.
4. **Use** — `/wiki-query` answers *read-only* from what's in the vault.

**The one setting almost everyone skips — the MODE.** `/wiki-mode` files new notes one of four ways: default · LYT (linked) · **PARA** (Projects/Areas/Resources/Archives) · Zettelkasten. Pick one and every new note self-sorts. **Recommended for M7: PARA.** (Switching modes only affects *new* notes — it won't tear up what exists.)

**The commands (live now via `RUN_SEO_SECONDBRAIN.bat`):**
`/wiki` (init/adopt + health check) · `/wiki-ingest` (source → linked pages) · `/wiki-query <q>` (grounded answer) · `/wiki-lint` (dead links/orphans/cannibalization) · `/save` (keep one good answer — set manual so it doesn't hoard) · `/wiki-fold` (roll activity into a summary/changelog) · `/auto-research` (Karpathy bounded web search) · `/canvas` · `/defuddle` (clean a web page before ingest).

**Safety (matches your Outbox Shield):** parallel agents hand back drafts; one controller applies them in a **single recoverable transaction** with git checkpoints — if anything breaks, it rolls the vault back. Recoverable if Claude ever deletes something ("recover back"). It **never touches a code base** — only interlinks notes.
> Uses the Karpathy **HOT / INDEX / LOG** wiki model — which is exactly the pattern in your existing `CLAUDE.md` constitution.

## 📞 Voice booking = your speed-to-lead lever
A client calls/texts → the agent answers, talks, and books the slot. Two setups:
- **Simplest:** Hermes on Telegram/WhatsApp/site + **Google Workspace API** → books straight into Google Calendar. *"The phone number is the app"* — non-technical.
- **Voice:** Hermes Apollo + **11Labs** voice + **Tailscale** → answers the phone, books to the calendar (lock down what it can access).

**🍍 M7:** this is the **CPPA booking engine** — a caller books a Complimentary Professional Photo Audit without an app. Every booking still confirmed by you; nothing auto-spends.

## ✅ 3 M7 actions from these videos
1. **Set claude-obsidian to PARA mode** on `03_Knowledge_Mat` (the setting most people skip).
2. **Use `/save` + `/wiki-ingest`** to bank good agent outputs + sources into the vault (grounding = no hallucinated claims in your SOPs).
3. **Wire the voice-booking path** (Hermes + Google Workspace) as the CPPA speed-to-lead front door — PAUSED/confirmed by you.


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
