---
type: shared_agent_memory
status: active
version: "1.0"
last_compiled: 2026-06-25
classification: M7_Command_Level_1
feed_url: http://127.0.0.1:51763/api/memory
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# M7 SHARED MEMORY — UNIVERSAL AGENT FEED

> 🍍 **FRONT DOOR:** New here or lost? Open **[COMMAND_CENTER_OS.md](COMMAND_CENTER_OS.md)** — the one router with every tab/agent workflow + copy-paste prompts. Daily ritual: **[DAILY_LOOP.md](DAILY_LOOP.md)**. Laws: **[AGENT_READ_ME_FIRST.md](AGENT_READ_ME_FIRST.md)**.
> The loop is always: **Read → Do → Stage (PAUSED) → Log.**

<!-- AUTO-COMPILED by memory_sync.py — DO NOT HAND-EDIT the sections marked [SYNC]. Edit source files instead. -->
<!-- Agents: load this file at session start. POST to /api/memory/log to record actions. -->

---

## [SYNC] IDENTITY

- **Operator:** Saia (sole publisher — only human who may activate outbound content)
- **Company:** Pineapple Contractors M7 — Polynesian-owned, family-operated roofing/restoration, North Texas since 2005
- **HQ:** 1 Cowboys Way, Suite 270W, Frisco, TX 75034
- **Brands:** Pineapple Roofing (`pineapplecontractors.com`) · Pineapple Restorations (`pineapplerestorations.com`)
- **License:** RCAT #03-0637 · HUB #1861616404400

---

## [SYNC] BRAND CONSTITUTION (abridged from GROUNDING.md)

### Colors
| Token | Hex | Usage |
|---|---|---|
| Royal Navy | `#1A365D` | Structure, text, nav, footers |
| Pineapple Gold | `#FBC02D` | CTAs, banners, highlights |
| Process Cyan | `#00BFFF` | Status indicators only |
| White | `#FFFFFF` | Negative space |
| **GREEN (any)** | **BANNED** | **Hard block — exit 1** |

### Mandatory Lexicon Mutations
| BANNED | REQUIRED SUBSTITUTE |
|---|---|
| Free / Free Inspection | Complimentary Professional Photo Audit (CPPA) |
| $0 Down / $0 Out of Pocket | Full Restoration Coverage |
| Save Money | Protecting your family's investment |
| GAF Certified | IKO Certified (RCAT License #03-0637) |
| Warrior / Toa / Six Brothers / Consultation | The Pineapple Standard |

### Revenue Gate
- Minimum baseline: **$18,000+** — auto-reject below
- Speed-to-lead: **5 minutes** (older = dead)
- Lead score ≥80 → dispatch to Saia

### OUTBOX SHIELD (non-negotiable)
All ad/web/social output → `01_Command_Center/Outbox_Drafts/` in PAUSED state.
**No agent may publish, post, send, or move money.** Saia authorizes all live activations.

---

## [SYNC] TOPOGRAPHY (4-Fala Rooms)

```
01_Command_Center/   Strategic brain, brand DNA, governance, Kanban
02_Media_Vault/      Raw media pool (read filenames only — no byte processing)
03_Knowledge_Mat/    SOPs, knowledge base, Obsidian vault, AEO pages
04_Tech_Lab/         Execution engine (server_m7.py), scripts/, agent runtime
05_Campaign_Factory/ Stage pipeline: Research → Copy → Creative → Deploy
```

No loose files in root. No directory drift. All `.py` utilities → `04_Tech_Lab/scripts/`.

---

## [SYNC] ACTIVE ENDPOINTS

| Service | Address | Purpose |
|---|---|---|
| M7 Command Server | `http://127.0.0.1:51763` | Kanban, outbox, research, memory API |
| Obsidian REST API | `http://127.0.0.1:27123` | Vault read/write via MCP |
| Ollama | `http://127.0.0.1:11434` | Local model inference |

**Memory API:**
- `GET  /api/memory`        → Full SHARED_MEMORY.md as JSON + raw markdown
- `POST /api/memory/log`    → Append agent action to rolling log (`{"agent":"…","action":"…","note":"…"}`)

---

## [SYNC] AI FLEET ROSTER

| Agent | Runtime | Role | Memory Access |
|---|---|---|---|
| Claude Code | Anthropic API | Lead architect, code, research | Obsidian MCP + `/api/memory` |
| Hermes | Gemini / local | Kanban dispatch, content factory | `/api/memory` GET |
| NotebookLM | Google | Research synthesis, podcast | Vault file as source |
| OpenClaw / Antigravity | Custom | Creative generation | `/api/memory` GET |

**Cross-agent envelope:** see `01_Command_Center/CROSS_AGENT_PROTOCOL.md` for the universal JSON contract.

---

## [SYNC] SESSION RULES FOR ALL AGENTS

1. **Read this file first** before any generation, mutation, or publish action.
2. **Verify room:** "Am I writing to the correct 4-Fala folder?"
3. **Verify compliance:** "Does this violate the brand constitution above?"
4. **Verify outbox:** "Is this outbound content? If yes — PAUSED state only."
5. **Log action:** POST to `/api/memory/log` after any significant file write or stage transition.
6. **Cultural anchor:** Include `Ko e hala 'o e fononga ko e faka'apa'apa` on significant consumer-facing outputs.

---

## [SYNC] LIVE METRICS (from GROUNDING.md)

- Minimum project baseline: $18,000+ (auto-reject below).
- Speed-to-lead: 5 minutes (older = dead).
- Lead matrix: +25 Frisco ZIP, +30 Property Manager, +20 $700K+ estate, +20 storm mention; ≥80 → dispatch to Saia.
- Estimate validity: 7–14 days.

## [SYNC] EXECUTION GUARDRAILS (from GROUNDING.md)

- 1-3-12 Meta Offensive: 1 CBO ($250/wk), 3 avatars, 12 creatives. 1% Kill / 1.5% Scale. CPL target $50, max $250.
- 50/5/3 video engine: 50s total, hook frames 0–15, end card frames 1411–1500.
- Advantage+ creative enhancements hardcoded OFF.
- OUTBOX SHIELD: all ad/web/social output written to `01_Command_Center/Outbox_Drafts/` in a PAUSED state. Live activation requires explicit human authorization. No agent may publish live or move money.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->

## [SYNC] VAULT SESSION LOG

- 2026-06-17 — Consolidated playbooks, built firewall/scoring/factory/intake, wired AI fleet + Hermes dispatch, merged Master Execution Spec, added hermes_skills + daemon + compose.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->

---

## AGENT LOG
<!-- APPEND-ONLY — memory_sync.py prepends new entries. Do not reorder or delete. -->

| UTC Timestamp | Agent | Action | Note |
|---|---|---|---|
| 2026-06-25T18:36:55Z | hermes | SESSION_LOAD | Loaded SHARED_MEMORY.md via GET /api/memory |
| 2026-06-25T18:36:54Z | claude_code | MEMORY_SYSTEM_ONLINE | Shared memory feed + API endpoints deployed |
| 2026-06-25T12:00:00Z | claude_code | CREATED SHARED_MEMORY.md | Initial compilation from GROUNDING + MEMORY + CLAUDE.md |
