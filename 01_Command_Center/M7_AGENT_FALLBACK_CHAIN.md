---
type: reference
title: M7 Agent Fallback Chain — Who Does What (updated for ChatGPT Plus + Codex OAuth)
status: active
last_updated: 2026-07-17
---

# 🔁 M7 Agent Routing (updated 2026-07-17)

**Big change:** Saia upgraded ChatGPT to **Plus**. Codex now runs on **ChatGPT OAuth (GPT 5.6 "Sol"), UNMETERED** — no API key, nothing counted. That makes Codex the primary *code/technical* engine. **GLM-5.2-cloud is now dead** (403 — needs a paid Ollama sub we don't have; stop routing to it).

## 🧠 The three-lane division of labor (use this)
| Lane | Agent | Owns | Why |
|---|---|---|---|
| **BUILD (code)** | **Codex / GPT 5.6 (ChatGPT OAuth)** | Scripts, schema/JSON-LD, WordPress automation, technical-SEO implementation, dashboards | **Unmetered** now. Frontier coder. Point it at the vault + `main`. |
| **ORCHESTRATE + VOICE** | **Claude Code (me)** | Brand-voice copy, page/blog/caption writing, review replies, planning, vault structure, firewall | Knows M7 brand law cold. No mid-task fails. Quality-critical seat. |
| **RESEARCH / IDEATE** | **ChatGPT (Plus, web)** | Keyword brainstorming, competitor scans, first-draft angles | Fast, conversational. Feed its output back to me/Codex to firewall + finalize. |

## 🔁 Free-agent overflow chain (only for BULK volume when the lanes are busy)
| # | Agent | Status | Use |
|---|---|---|---|
| 1 | **Codex / GPT 5.6** | ✅ unmetered (OAuth) | Default for code/technical. |
| 2 | **Hermes → Goal Mode** | 🟡 Ollama free — **weekly** cap | Vault-aware content. One small task per run. |
| 3 | **OmniRoute** | ✅ 90+ free models | Bulk page generation, watch-and-save. |
| 4 | ~~GLM 5.2 cloud~~ | ❌ **403 — paid Ollama only** | **Do not use** until/unless subscribed. |
| 5 | **Local** (local Ollama) | ✅ unlimited, weaker | Last-resort always-on. |
| 6 | **Claude Code (me)** | session-paced | Anything voice- or quality-critical. |

## The rules that keep you unblocked
1. **One small goal per run.** "Write ONE page for Grapevine" completes; "run the whole pipeline" hits the cap and dies.
2. **When you see a 429 → switch agents,** don't hammer the same one.
3. **Money/flagship pages → use #5 (me) or a fresh #3 agent** — reliability matters most where it counts.
4. **Bulk/lower-stakes volume → rotate #2–#4** (free, spread the load).
5. **Weekly caps reset weekly.** Hermes comes back. Pace across the week, don't binge.
6. **Always firewall free-model output** (`brand_firewall.py --check`) — free models don't enforce brand law.

## Honest CEO note
For the 5 ELITE pages that are now LIVE, **I (Claude) wrote them directly — zero failures.**
That's the pattern: **let me write the pages that matter; rotate the free agents for volume.**
Stop fighting a capped Hermes — the chain above means you're never actually stuck.

<!-- M7-FIREWALL-EXEMPT: reference -->
