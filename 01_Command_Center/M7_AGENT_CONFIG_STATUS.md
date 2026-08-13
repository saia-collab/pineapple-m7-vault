---
INTENT: Live agent configuration status — what's wired, what's broken, how to fix each.
type: config_status
generated: 2026-06-30
architect: M7 VP Marketing (Claude Code)
status: LIVE — update after each session
---

# M7 AGENT CONFIGURATION STATUS — 2026-06-30

---

## CLAUDE (Claude Code) — ✅ FULLY OPERATIONAL
- **Model:** claude-sonnet-4-6
- **Vault:** `C:\Pineapple Contractors M7` (working directory)
- **SOPs loaded on boot:** `CLAUDE.md` → `M7_MASTER_SOP.md` + `SHARED_MEMORY.md`
- **Launch:** `LAUNCH_CLAUDE_CODE.bat`
- **Fix needed:** None

---

## HERMES — ⚠ PARTIAL (3 items)

### ✅ Working
- CLI: `hermes v0.17.0` at `C:\Users\estim\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe`
- Profiles available: `main`, `roofing`, `marketing`, `content`, `julian`
- OpenRouter key: authenticated in credential pool
- Model: `minimax-m3:cloud` via `ollama-launch`

### ⚠ Fix 1 — Realtime Voice Tab (OPENAI_API_KEY)
**Error:** "OpenAI key not found — set OPENAI_API_KEY"
**Root cause:** Hermes Realtime uses OpenAI's WebSocket Realtime API (`wss://api.openai.com/v1/realtime`). OpenRouter does NOT support this endpoint.
**Current state:** `~/.hermes/.env` now has `OPENAI_API_KEY` + `OPENAI_BASE_URL` pointing to OpenRouter (fixes some OpenAI-compatible endpoints, NOT realtime voice).
**Permanent fix:** Purchase an OpenAI API key at platform.openai.com → add `OPENAI_API_KEY=sk-...` to `~/.hermes/.env`
**Workaround:** Use **Hermes-Jarvis** tab (Talk) → this uses Groq Whisper which is already funded.

### ⚠ Fix 2 — MiniMax Studio OAuth
**Error:** "MiniMax isn't connected. Run hermes auth add minimax-oauth"
**Status:** OAuth initiated via terminal — browser should have opened. If browser didn't open automatically:
1. Open a terminal
2. Run: `hermes auth add minimax-oauth`
3. Sign in with your MiniMax account
4. Refresh Hermes → Studio tab → switch from MiniMax to **Grok** (already available, no OAuth needed)

### ⚠ Fix 3 — SOUL.md SOP Wiring (FIXED THIS SESSION)
**Status:** ✅ DONE — all 3 Hermes profiles now reference M7 vault paths:
- `~/.hermes/profiles/roofing/SOUL.md` → M7_MASTER_SOP + M7_LEAD_ENGINE
- `~/.hermes/profiles/marketing/SOUL.md` → already correct
- `~/.hermes/profiles/content/SOUL.md` → M7_CONTENT_FACTORY + M7_CAMPAIGN

### How to use Hermes profiles
```bash
hermes chat --profile roofing    # leads, CRM, CPPA booking
hermes chat --profile marketing  # social posts, ad copy
hermes chat --profile content    # 1→6 video repurposing
hermes chat --profile julian     # general research
```

---

## PAPERCLIP — ✅ LIVE at :3100 | COMPANY BUILT
- **URL:** http://127.0.0.1:3100
- **Company:** Pineapple Contractors M7 (ID: f20dadda-9d7d-4c92-985d-372245ccd32c)
- **Agents:** M7 CEO → (CMO, CTO, COO) → (Marketing Agent, SEO Strategist, Lead Engine, Ops Agent)
- **Projects:** Marketing & Content | Lead Engine | Tech Build | Brand & Compliance
- **Kanban:** PIN-1 through PIN-9 issues created
- **Adapter:** hermes_local + openrouter configured on all agents
- **⚠ Hermes binary path:** Must be set via Paperclip UI → Agents → each agent → Adapter → verify `hermes` is in PATH or enter full path: `C:\Users\estim\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe`
- **Agent OS iframe:** Fixed to company UUID (page.tsx updated 2026-06-30)

---

## NOTEBOOKLM — ⚠ PARTIAL (2 accounts, 1 needs reauth)

### ✅ Business Account
- **Email:** saia@pineappleroofingllc.com
- **Status:** Active — 100 notebooks, `Tatafu Veehala: Core Influence & Roofing` active
- **Profile:** `default` (active)

### ⚠ Personal Account  
- **Email:** smoeprivate1@gmail.com
- **Status:** Profile exists, credentials INVALID (expired)
- **Fix:** Run `nlm login --profile smoeprivate1@gmail.com --clear` in terminal → browser opens → sign in with personal Google account
- **After fix:** Switch between accounts with `nlm login switch default` (business) or `nlm login switch smoeprivate1@gmail.com` (personal)

### ⚠ MCP Timeout Error (-32001)
**Error:** "McpError: MCP error -32001: Request timed out"
**Fix:** Restart the NotebookLM MCP server in Claude settings, or run `nlm doctor` to diagnose

---

## OPENCLAW — ❌ OFFLINE
- **Status:** Not running
- **Fix:** Launch from 04_Tech_Lab/scripts/ or from the Agentic OS dashboard

---

## FREE CLAUDE (fcc-server) — ✅ LIVE at :8082
- **Status:** Running on port 8082
- **Config:** `C:\Users\estim\.fcc\.env`
- **⚠ ACTION REQUIRED:** Rotate OpenRouter API key at openrouter.ai/keys (visible in screenshot)

---

## AGENTIC OS DASHBOARD — ✅ LIVE at :3000
- **URL:** http://127.0.0.1:3000
- **All agent cards:** now wired to correct status (Claude Online, Hermes Online, OpenClaw Offline, Paperclip Live)

---

## PENDING — NEXT SESSION PRIORITIES

| #   | Item                                  | Command / Action                                                                         | Time   |
| --- | ------------------------------------- | ---------------------------------------------------------------------------------------- | ------ |
| 1   | OpenAI key for Hermes Realtime voice  | Add real OpenAI key to `~/.hermes/.env`                                                  | 5 min  |
| 2   | MiniMax OAuth in Hermes               | `hermes auth add minimax-oauth` in terminal                                              | 2 min  |
| 3   | NotebookLM personal reauth            | `nlm login --profile smoeprivate1@gmail.com --clear`                                     | 3 min  |
| 4   | ~~Paperclip company setup~~ ✅ DONE   | Company + org chart + Kanban built 2026-06-30                                            | —      |
| 5   | ant CLI — Windows install             | Download from platform.claude.com or `npm install -g @anthropic-ai/claude-code-agent`   | 10 min |
| 6   | Hermes binary path in Paperclip UI   | Agents → each agent → Adapter → set path to `C:\...\hermes.exe`                         | 5 min  |
| 7   | OpenSEO Docker start                  | `cd ~/open-seo && docker compose up -d`                                                  | 5 min  |
| 8   | Rotate OpenRouter API key             | openrouter.ai/keys → revoke old, update `~/.fcc/.env`                                   | 5 min  |
| 9   | Week 1 content REDO                   | Redo without Airtable. Run brand_firewall.py → save to Outbox_Drafts PAUSED             | 30 min |
| 10  | Hermes Mixture-of-Agents test         | `hermes chat --profile marketing` → `/mixture`                                           | 15 min |

---


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
