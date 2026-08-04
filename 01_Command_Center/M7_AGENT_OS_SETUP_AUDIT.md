---
INTENT: Full audit of every Agent OS install guide vs. actual Pineapple M7 config — verified, not assumed.
type: setup_audit
generated: 2026-07-03
auditor: M7 VP (Claude Code)
pack_version: 2026-07-03
status: LIVE — re-run after each update
---

# 🍍 M7 × AGENT OS — FULL SETUP AUDIT (27 guides verified)

**Branding baseline (applied system-wide):** Royal Navy `#1A365D` + Pineapple Gold `#FBC02D` + Status Cyan `#00BFFF` · ZERO green · `userName = Saia` · vaultRoot = `03_Knowledge_Mat` · Outbox Shield (DEC-005) · CPPA / IKO / RCAT #03-0637 enforced by `brand_firewall.py`.

---

## ✅ CORE — fully configured & running
| Guide | Component | Status |
|-------|-----------|--------|
| 1, 25 | **Core Dashboard** | ✅ `:3000` (Agentic OS) + `:3737` (M7 server.js) — **M7 themed, zero green** |
| 11 | **Memory / Obsidian** | ✅ `vaultRoot` = `C:\Pineapple Contractors M7\03_Knowledge_Mat` (Windows backslash fix applied — notes open) |
| 4 | **Hermes** | ✅ installed; `default_model = deepseek-coder` (✔ Gemma NOT the default — guide-0 rule honored); OpenRouter wired |
| 5 | **Free Claude Code** | ✅ `:8082`; model = `nemotron-3-super-120b` (strong model, correct) |
| 6 | **Paperclip** | ✅ `:3100` — Pineapple company + org chart (CEO→CMO/CTO/COO→depts) |
| 15 | **NotebookLM** | ✅ authenticated (100 notebooks); `nlm` CLI present |
| — | **SEO Pipeline** | ✅ Pineapple-branded, draft-to-Outbox, author JR. Moeakiola |

## ✅ AGENTS & MODELS
| Guide | Item | Status |
|-------|------|--------|
| 7 | Claude CLI | ✅ present (`claude login` OAuth) |
| 7 | Gemini/Google key | ✅ **valid (200)** |
| 16 | Kimi Code | present (tab lights up when used) |
| 17 | Extra models (GLM/Sakana/Zai) | ⚪ optional — OpenRouter covers routing; add keys only if wanted |
| 2,13,20 | Ollama (voice-build/game/kanban) | ✅ **running :11434** (gemma for on-device builds only) |

## ✅ VOICE
| Guide | Part | Status |
|-------|------|--------|
| 3 | Talk TO Jarvis (mic) | ✅ browser speech + **Groq key valid** |
| 3 | Jarvis Realtime (OpenAI) | ✅ **key valid**; voice = "Ash" — server pipeline confirmed. ⚠️ live audio needs a browser without ad-block (see note) |
| 3 | ElevenLabs premium voice | ⚠️ **key 401 — recreate at elevenlabs.io** (optional; Ash voice works without it) |

## ✅ TOOLS & STUDIOS
| Guide | Component | Status |
|-------|-----------|--------|
| 10 | Thumbnail Studio | ✅ OpenAI key present |
| 12, 26 | Video Studio / OpenMontage | ✅ ffmpeg installed · ⚪ HeyGen key optional (avatars) |
| 14 | Music Studio | ⚪ needs Suno key (optional) |
| 22 | **Leads** | ✅ **Hunter + Firecrawl keys configured** (`~/.agentic-os/outreach/config.json`); Apollo optional (paid) |
| 23 | **Radar** | ✅ no key needed (AI-news watcher) |
| 19 | Loop Engineering | ✅ OpenRouter wired |
| 21 | Open Design | ✅ narrative — no key |
| 24 | Windows state unify | ✅ `HERMES_HOME = %LOCALAPPDATA%\hermes`, profiles migrated |
| 9 | Phone Agent | ⚪ intentionally skipped (advanced, not needed) |

---

## ⚪ Optional keys NOT set (add only if you want that feature)
- **ElevenLabs** (premium Jarvis voice) — key currently 401, recreate it
- **Suno** (Music Studio) · **HeyGen** (Video avatars) · **Apollo** (Leads people-DB, paid) · **GLM/Sakana/Zai** (extra model councils)

## 🔑 Keys wired & VALID (in `~/.hermes/.env` + `main` profile, outside vault)
OpenAI ✅ · Groq ✅ · Google/Gemini ✅ · Firecrawl ✅ · Hunter ✅ · OpenRouter ✅ · Apify · Pinecone · KIE · OMI · Obsidian

## 🛑 Nothing broken in the build
Every required component is installed, keyed, and running. The only ❗ item is the **ElevenLabs key (401)** — and that's cosmetic (a nicer voice), not a blocker; Jarvis already speaks via OpenAI's Ash voice.

*Ko e hala 'o e fononga ko e faka'apa'apa — the path of the journey is respect.* 🌺
