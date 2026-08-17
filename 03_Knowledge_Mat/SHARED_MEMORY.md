---
type: shared_agent_memory
status: active
version: "2.0"
last_compiled: 2026-08-16
classification: M7_Command_Level_1
authority: Naa Sione brand law (2026-08-14, approved by Saia). This file supersedes any older brand facts.
color_primary: "#003299"
color_secondary: "#ffdd17"
---

# 🍍 M7 SHARED MEMORY — UNIVERSAL AGENT FEED (v2, current)

> **Every agent loads this first.** It is the single current source of brand + system truth. Where any older
> vault file (navy/gold/cyan, "CPPA", "since 2005") disagrees, **THIS WINS.**
> The loop is always: **Read → Do → Stage (PAUSED in Outbox) → wait for Saia's GO.**

---

## [CURRENT] IDENTITY (verified)

- **Business:** Pineapple Roofing — residential + commercial roofing & general contracting (repairs, replacement, storm restoration).
- **Ownership:** Polynesian / minority / family-owned (NMSDC certified).
- **Founded:** **2021** (NOT 2005 — that old claim is decommissioned).
- **HQ:** 1 Cowboys Way, Suite 270W, Frisco, TX 75034 · **Secondary:** 4400 State Hwy 121 #300, Lewisville, TX 75056.
- **Phone:** (972) 928-0788 · **Email:** support@pineappleroofingllc.com
- **Live site:** pineappleroofingllc.com · **Legacy authority site:** pineapplecontractors.com
- **License:** RCAT #03-0637 · **HUB:** #1861616404400 · **Manufacturer:** IKO Certified (never GAF).
- **Operator / sole publisher:** Saia. Only Saia may activate outbound content.

---

## [CURRENT] BRAND CONSTITUTION (Naa Sione, 2026-08-14 — authoritative)

### Colors — Pineapple Blue + Pineapple Yellow ONLY
| Token | Hex | Usage |
|---|---|---|
| Pineapple Blue | `#003299` | Structure, headers, text, CTAs, the logo/pineapple crown |
| Pineapple Yellow | `#ffdd17` | Action markers, highlights, one hero accent |
| White | `#FFFFFF` | Negative space |
| **GREEN (any shade)** | **BANNED** | **Hard block — the pineapple crown is BLUE, never green** |

Retired (do NOT use): Navy `#1A365D`, Gold `#FBC02D`, Cyan `#00BFFF`.

### Language — the "free" legal rule (priority over style)
- ✅ **ALLOWED:** "free roof inspection" / "free estimate" as a CTA.
- ❌ **BANNED:** "free" anywhere it implies free roof **work/repairs**, **waived/no deductible**, or anything tied to an **insurance claim payout** (Texas Dept. of Insurance risk).
- **Field term for the offer:** "storm damage report" / "licensed inspection roof report" — **NOT "CPPA"** (that term is decommissioned).
- **Banned terms:** cheap, bargain, warrior, toa, six brothers, GAF, any waived/no-deductible language.
- **Mandatory:** "IKO Certified" (never GAF).
- **Slogan:** "Roofing Made Sweeter" + "The Pineapple Promise." **No Tongan proverbs** (decommissioned per Saia 2026-08-11).
- **Standard CTA:** *"Call (972) 928-0788 to schedule your free roof inspection/estimate today."*

### Trust signals (force on all layouts)
RCAT #03-0637 · IKO Certified · 5-Star Rated (500+ reviews) · Founded 2021 · Frisco HQ · (972) 928-0788.

### OUTBOX SHIELD (non-negotiable)
All ad/web/social/email output → `01_Command_Center/Outbox_Drafts/` in a **PAUSED** state.
**No agent may publish, post, send, index, spend, or move money.** Saia authorizes every live activation.

---

## [CURRENT] SYSTEM STATE — as of 2026-08-16

- **Local Studio build:** `2026-08-16` (installed + verified). Sidebar shows `build 2026-08-16`.
- **Services (all should be UP):** Studio `:3737` · Free Claude Code `:8082` (free coder) · Hermes `:9119` · OmniRoute `:20128` (free keyless model pool).
- **Optional / not installed:** Ollama `:11434` (needed only for GLM-5.2 :cloud — a ~600MB install; Free Claude Code + Claude cover coding without it).
- **Working models with zero extra setup:** Claude tab (Saia's subscription) · Free Claude Code (:8082) · OmniRoute (:20128) · opencode · qoder.
- **Updater:** fixed 2026-08-16 — two PowerShell stderr traps that used to roll back good builds are gone; packs now install in minutes (drop `agent-os-pack*.zip` in Downloads → double-click `M7 UPDATE (new pack).bat`).
- **Brand paint + de-Julian:** applied to the build (blue/yellow, 0 green; Julian's sites/email scrubbed to Pineapple).
- **Shared memory folder (vaultRoot):** `C:\Pineapple Contractors M7` (correct). GitHub backup: `github.com/saia-collab/pineapple-m7-vault`.

---

## [CURRENT] TOPOGRAPHY (ICM 4-Fala + memory)

```
01_Command_Center/   Decide, route, approve, record. Brand DNA, playbooks, Outbox_Drafts (the GO gate).
02_Media_Vault/      Raw media pool — drone/job photos, testimonials, reels (read filenames; syncs to Google Drive).
03_Knowledge_Mat/    SOPs, this shared memory, knowledge base, AEO city pages.
04_Tech_Lab/         Execution: scripts/, the Agent OS build (Pineapple_Agent_OS/), vendor skills.
05_Campaign_Factory/ Pipeline: Research → Copy → Creative → Deploy (all PAUSED).
_memory/             Live execution state (PM7 phase state, coach config).
```
Root `CLAUDE.md` (L0) + `CONTEXT.md` (L1 router) are current authority. Do not rearrange folders.

---

## [CURRENT] ACTIVE ENDPOINTS

| Service | Address | Purpose |
|---|---|---|
| Agent OS Studio | `http://localhost:3737` | Mission Control — all agent tabs, Memory, SEO, Pipeline |
| Free Claude Code | `http://127.0.0.1:8082` | Free coder proxy + `/admin` key panel (paste keys in a UI) |
| Hermes console | `http://127.0.0.1:9119` | Orchestration, profiles, kanban |
| OmniRoute | `http://127.0.0.1:20128` | Free keyless model pool (auto-fallback) |

---

## [CURRENT] AI FLEET

| Agent | Runtime | Role | Setup |
|---|---|---|---|
| Claude | Saia's Claude subscription | Lead writer/architect (blogs, SEO, code) | `claude login` (done) |
| Hermes | local + OpenRouter | Orchestration, content factory, kanban | up (:9119) |
| Free Claude Code | Groq / OmniRoute | Free coding, no key | up (:8082) |
| OmniRoute | keyless free pool | Free model fallback | up (:20128) |
| opencode / qoder | free / Qwen | Extra free coders | installed |
| GLM-5.2 (optional) | Ollama Cloud | Cheap web-app builds | needs Ollama install + `OLLAMA_API_KEY` |

---

## [CURRENT] SESSION RULES FOR ALL AGENTS

1. **Read this file first.** It is current; older brand files are not.
2. **Verify room:** writing to the correct 4-Fala folder?
3. **Verify brand:** blue/yellow only, zero green, "free" only for inspection/estimate, "storm damage report" not CPPA, IKO not GAF, founded 2021, no Tongan proverbs.
4. **Verify Outbox:** outbound content → PAUSED in `01_Command_Center/Outbox_Drafts/` only.
5. **Human gate:** nothing publishes/sends/spends without Saia's explicit GO.
6. **Run** `04_Tech_Lab/scripts/brand_firewall.py --check` before staging content.

<!-- M7-FIREWALL-EXEMPT: governance-reference (names banned terms as rules; contains "free" per the corrected legal rule) -->

---

## SESSION LOG (newest first)

- **2026-08-16** — Shared memory rewritten to current brand + system state. Build 2026-08-16 installed (updater's 2 stderr traps fixed); brand paint blue #003299/yellow #ffdd17 + de-Julian applied; Free Claude Code :8082 port bug fixed; brother oversight + media guide added; pushed to GitHub. Brand law = Naa Sione 2026-08-14 (blue/yellow, "free inspection" OK, storm damage report not CPPA, founded 2021).
- 2026-06-25 — (historical, superseded) initial compilation with the retired navy/gold/cyan + CPPA brand.

## AGENT LOG (historical — append-only; entries below predate the 2026-08-14 brand change and may cite retired brand)
| UTC Timestamp | Agent | Action | Note |
|---|---|---|---|
| 2026-07-06T20:58:12Z | hermes | SEO_BLOG_DRAFT_5POSTS | 5 long-form SEO posts drafted + PAUSED to Outbox_Drafts/SEO_Posts/ (historical — used the retired navy/gold/cyan + CPPA + proverb brand; re-brand before any publish). |
| 2026-06-25T18:36:55Z | hermes | SESSION_LOAD | Loaded SHARED_MEMORY.md |
| 2026-06-25T12:00:00Z | claude_code | CREATED SHARED_MEMORY.md | Initial compilation (retired brand) |
