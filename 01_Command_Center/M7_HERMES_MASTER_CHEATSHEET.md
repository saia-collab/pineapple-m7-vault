---
type: hermes_cheatsheet
title: M7 HERMES MASTER CHEAT SHEET — commands, profiles, features, brand-locked prompts
status: active
date: 2026-08-12
source: distilled from 15 Hermes guides (v0.15 Velocity → v0.20 Herald, MoA, MCP, Grok/Qwen/Kimi/MiniMax, Obsidian, Muse, Paperclip, browser agents)
brand_lock: CPPA not "free" · IKO Certified not GAF · Navy #1A365D + Gold #FBC02D + Cyan #00BFFF · ZERO green · "Roofing Made Sweeter" / "The Pineapple Standard" · no Tongan proverbs · (972) 928-0788 · RCAT #03-0637
note: Everything lands PAUSED in Outbox_Drafts. Nothing publishes/sends/spends without Saia GO.
---

# 🛰️ M7 HERMES MASTER CHEAT SHEET

## ⌨️ CORE COMMANDS (terminal or Studio → Hermes)
| Command | Does |
|---|---|
| `hermes` | start chatting (active profile) |
| `hermes model` | pick the LLM (OpenRouter / Grok OAuth / Kimi / MiniMax / omniroute) |
| `hermes tools` | toggle tools (web, X search, file ops) |
| `hermes gateway` | connect Telegram/Discord/WhatsApp/Signal |
| `hermes update` | latest version |
| `hermes doctor` | diagnose + fix |
| `hermes -p <profile>` | run a specific profile |
| `hermes profile create <name>` | new isolated agent (`--clone` copies current setup) |
| `hermes profile list` / `use <name>` | list / set sticky default |
| `hermes mcp serve` | run Hermes as an MCP server (for Codex/Claude) |
| `hermes import-agent` | migrate a Claude Code / Codex setup into Hermes |
| `/new · /model · /compress · /skills · !cmd` | in-chat: fresh chat · swap model · shrink context · skills · run shell |

## 👥 PROFILES = your M7 staff (isolated, no cross-contamination)
Each lives at `%LOCALAPPDATA%\hermes\profiles\<name>\` with **`config.yaml`** (model/tools) + **`SOUL.md`** (brand persona) + **`.env`** (keys). You already have 27, all brand-scrubbed. Roofing-core: `roofing · seo · seo-lead · leads · marketing · content · muse · main`. Keep **Restoration** separate (Brand B — fire/water/mold, never roofing vocab).
- Create a new one: `hermes profile create <name> --clone` → then it inherits your working model/keys.
- Its rules live in `SOUL.md`; master template = `01_Command_Center/Brand_DNA/M7_HERMES_SOUL.md`.

## 🚀 v0.20 "HERALD" — the 5 upgrades that matter
1. **Real-time voice + wake word** — say *"hey Hermes"*, interrupt mid-sentence, on-device detection (no audio leaves PC).
2. **Grounded citations** — every claim gets a checkable source; built-in fact-check pass. *Use for all research.*
3. **Async sub-agents** — `delegate_task background=true`: spawn workers, keep chatting, results fly back as they finish.
4. **Mid-turn correction** — type a correction while it works; it redirects without restarting.
5. **Smarter approvals** — auto-does safe/reversible/internal; **stops and asks** before publish/send/spend/delete.

## 🧠 MIXTURE OF AGENTS (MoA) — `/moa` (council + chair)
Two reference models write private opinions; one chair synthesizes. Edit profile `config.yaml`:
```yaml
moa:
  presets:
    default:
      reference_models:
        - { provider: openai-codex, model: gpt-5.6-sol }
        - { provider: openrouter, model: deepseek/deepseek-v4-pro }
      aggregator: { provider: openrouter, model: anthropic/claude-opus-4.8 }
      reference_temperature: 0.6
      aggregator_temperature: 0.4
      enabled: true
```
Use `/moa` for hard calls (best marketing move, code review, offer design).

## 🔌 MCP (give Hermes hands) — GitHub / filesystem / WordPress
Add to profile `config.yaml` under `mcp_servers:` (or `mcp_config.json`), then `/reload-mcp`:
```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env: { GITHUB_PERSONAL_ACCESS_TOKEN: "PASTE_TOKEN" }
```
- **Hermes ⇄ Codex/Claude:** `hermes mcp serve`, add the `hermes` block to the client's mcpServers, restart.
- **Obsidian memory bridge:** calclavia mcp-obsidian → agent reads the vault.

## 🔀 MODEL ROUTING (cheapest that does the job)
| Job | Model |
|---|---|
| Bulk/drafts, $0 | **Ollama local** (qwen2.5-coder) |
| Long autonomous builds (35h) | **Qwen 3.7 Max** (1M ctx, OpenRouter) |
| Heavy coding | **Kimi K2.7** (coding plan) / **MiniMax M3** |
| Real-time X + image/video/TTS | **Grok** (xAI OAuth — needs SuperGrok login) |
| Hard synthesis | **MoA** (council → Opus 4.8 chair) |
| Free bigger pool | **omniroute** profile (paste key in its `auth.json`) |

## 🔥 HERMES MUSE — 24/7 content furnace
Reads your channel, ranks by heat, forges ideas nightly. Set channel in `~/.agentic-os/config.json`: `"youtubeChannel": "https://youtube.com/@YourHandle"`.

---

## 📋 M7 COPY-PASTE PROMPTS (brand-locked — paste as-is)

**Morning triage (Chat / Kanban):**
```
Act as Lead Ops Manager for Pineapple Roofing. Read M7_PROMPT_CONTROL_PANEL.md + the Kanban. Give me today's 3 highest-value roofing tasks (storm/hail/replacement first), each with the tab + prompt to use. Confirm Outbox Shield ON. One screen. Brand: CPPA not free, IKO not GAF, no green, Roofing Made Sweeter.
```

**Goal Mode — city page:**
```
/goal "Lead SEO Copywriter for Pineapple Roofing. Build a location page for 'hail damage roof repair [CITY] TX'. 1,000+ words, direct-answer hook in first 40 words, RCAT #03-0637, IKO Certified, since 2005, (972) 928-0788, CPPA CTA, FAQ, LocalBusiness JSON-LD for ZIPs 75033/75034/75035. One sentence per line. No free/GAF/green/proverbs. Run brand_firewall.py. Save PAUSED to Outbox_Drafts/SEO/."
```

**Async sub-agents — 5 city pages at once:**
```
Delegate in background (delegate_task background=true): write 5 roofing city pages — McKinney, Allen, Plano, Frisco, Prosper — each 900 words, CPPA CTA, LocalBusiness schema, our credentials. Navy/gold/cyan, zero green. Each returns PAUSED to Outbox_Drafts/SEO/. Report as each finishes.
```

**MoA — best marketing move:**
```
/moa Frisco/DFW roofing, $500/mo budget. Best 90-day move: neighborhood storm-check events, Meta funnel, or LSA+reviews? Council argues each; chair picks ONE with first 3 steps. The Pineapple Standard.
```

**Grounded research (with citations):**
```
Research [recent DFW hail storm / competitor]. Every claim gets a checkable source; separate fact from inference; flag unverified. Then fact-check yourself. This is research — do not publish.
```

**GBP review replies (leads profile):**
```
Lead Customer Relations for Pineapple Roofing. Replies to these reviews [PASTE]: 40–80 words, humble, weave ZIPs 75033/75034/75035 + neighborhood + service. No "free" (CPPA), include (972) 928-0788 + HQ 1 Cowboys Way Ste 270W Frisco TX 75034. Save PAUSED to Outbox_Drafts/.
```

**Muse — weekly content:**
```
Content muse for Pineapple Roofing. 10 saveable short-video ideas this week (hail signs, roof-age tips, insurance myths, drone reveals). Each: 3-sec hook + CPPA CTA. No free/proverbs, Roofing Made Sweeter.
```

**Cron (plain English):**
```
Every morning 7am, check DFW roofing/storm news + my top 3 priorities, send me a summary. Every Friday 4pm, weekly lead + pipeline summary. Nothing publishes.
```

**Daily brief with memory:**
```
Read my Obsidian vault (03_Knowledge_Mat). Based on my goals + what I worked on, give 3 priorities today + which Studio tab for each. Roofing context only.
```

## 🔒 STANDING RULES
- Brand: CPPA · IKO Certified · Full Restoration Coverage · The Pineapple Standard · Navy/Gold/Cyan, **zero green** · **no Tongan proverbs** · (972) 928-0788 · RCAT #03-0637.
- **Outbox Shield:** every output PAUSED in `Outbox_Drafts/`. Saia is sole publisher.
- Approvals: auto safe/reversible; ask before publish/send/spend/delete.

<!-- M7-FIREWALL-EXEMPT: governance-reference (cheat sheet; "free" named only as the banned term → CPPA) -->
