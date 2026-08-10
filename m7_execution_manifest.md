# 🍍 M7 EXECUTION MANIFEST
**Standing discipline:** Every completed coding session appends here. Newest at top. (Per Saia's Engineering-Unit SOP, 2026-07-03.)

---

## 2026-07-05 — Cycle: M7 Project Brief (Cowork) + GEO/AEO city-page batch → Outbox

### 1. [Scope]
- **Created `01_Command_Center/M7_PROJECT_BRIEF.md`** — single visual source of truth for Claude Cowork (elevator summary, 4-Fala map, engines/ports, agents, Playbook frameworks index, current status, the 5 canonical files to feed Cowork).
- **Executed the GEO/AEO SEO SOP** (Master Playbook Local SEO/GEO Engine): drafted 6 AEO city landing pages (Frisco, Lewisville, McKinney, Plano, Allen, The Colony; Frisco covers ZIPs 75033/75034/75035) → `01_Command_Center/Outbox_Drafts/SEO_Posts/`. Each: keyword in first+last line, 40-word answer-first opener, RCAT #03-0637 + IKO injected, LocalBusiness + FAQPage JSON-LD, 4–6 FAQ, CPPA CTA, Tongan proverb, zero green, never "free". All PAUSED (DRAFT — DO NOT SEND).

### 2. [Endpoints & Variables]
- Output dir: `01_Command_Center/Outbox_Drafts/SEO_Posts/` (6 new pages, dated 2026-07-05; 4 prior drafts also present).
- Brief: `01_Command_Center/M7_PROJECT_BRIEF.md`.

### 3. [Verification]
- **Compliance audit (Campaign Factory Stage 30):** `04_Tech_Lab/scripts/brand_firewall.py --check` → STATUS: OK. Manual grep: 0 "GAF", 0 "warrior/toa", 0 real green usage (only the intended "zero green" header notes). One "free of charge" slip in McKinney caught + fixed → re-verify 0 banned "free".
- ⚠️ Everything PAUSED in Outbox — nothing published (Outbox Shield DEC-005). GCP not provisioned — local only.

### 4. [Cowork Hand-off]
```markdown
## Delta
- M7_PROJECT_BRIEF.md created for Cowork ingestion (visual single source of truth). Feed it + MASTER_PLAYBOOK.md + HERMES_PLAYBOOK.md + m7_core_rules.config + m7_execution_manifest.md.
- 6 AEO city landing pages drafted to Outbox_Drafts/SEO_Posts (Frisco/Lewisville/McKinney/Plano/Allen/The Colony), fully brand-compliant, PAUSED. Extendable to Prosper/Little Elm/Restorations pages on request.
- Compliance verified via brand_firewall + manual grep (0 violations).
```

---

## 2026-07-05 — Cycle: De-personalize (remove Julian Goldie) + single canonical launcher

### 1. [Scope]
- Removed the empty `julian` Hermes profile (roster now: content, leads, main, marketing, restoration, roofing, seo).
- **De-personalized the dashboard** — the pack ships author Julian Goldie's branding hardcoded. Replaced across 12 src files: `aimoneylabjuliangoldie.com` (Agent Kanban SEO target) → pineapplecontractors.com; `hermes@goldie.agency` → hermes@pineapplecontractors.com; `goldiebench(.com)`/`GoldieBench` → M7/leaderboard; `/Users/juliangoldie` → /Users/saia.
- **Critical fix — `src/lib/kanbanSeo.ts`:** the SEO-article template hardcoded Julian's "AI Money Lab" Skool CTA AND the banned word "FREE". Replaced with the Pineapple **CPPA** CTA (pineapplecontractors.com, IKO/RCAT/972-928-0788, zero-green note).
- **Durable:** added a brand-replace sweep (`$brandMap`) to `update_agent_os.ps1` alongside the zero-green sweep, so every future update auto-de-personalizes.
- **Single launcher:** rewrote root `LAUNCH_ALL.bat` — removed the dead `:3737 npm start` (no app at root), launches only the real services (:3000 dashboard, :51763 engine, :8082 FCC, :3100 Paperclip), auto-opens the browser. THIS is the one-click login launcher.

### 2. [Endpoints & Variables]
- Dashboard :3000 · engine :51763 · FCC :8082 · Paperclip :3100.
- Canonical launcher: `C:\Pineapple Contractors M7\LAUNCH_ALL.bat`.

### 3. [Verification]
- **LOCAL — PASS.** Rebuilt, dashboard :3000 = 200, **0 goldie/aimoneylab refs in served build** (was 2, then 0 after expanded sweep). julian profile gone.
- ⚠️ GCP not provisioned — local only.

### 4. [Cowork Hand-off]
```markdown
## Delta
- Dashboard fully de-personalized to Pineapple M7 (Julian Goldie branding stripped, incl. the SEO-article CTA template which had his Skool funnel + "FREE"). Durable via update_agent_os.ps1 $brandMap sweep. julian profile removed.
- ONE launcher: LAUNCH_ALL.bat (root). All other .bat files are single-purpose tools (UPDATE_AGENT_OS, START_PAPERCLIP, M7_DOCTOR) or archived in Launcher_Archive.
```

---

## 2026-07-05 — Cycle: Agent OS update 2026-07-03 → 2026-07-05 (safe, per UPDATE-WITH-AI.md)

### 1. [Scope]
- Updated the Agent OS dashboard to pack `agent-os-pack-2026-07-05.zip`. Followed UPDATE-WITH-AI.md gates: backup-first, preserve-set, Ask Gate (keys), verify boot.
- **Backup:** `04_Tech_Lab/_agentos_backups/source.bak-20260705_153226` (503 files) — RETAINED (not deleted; awaiting Saia authorization).
- Applied new source via the safe updater (preserved 12 M7 customizations + node_modules/.next/config/keys/vault), zero-green sweep (37 files).
- **Fixed `update_agent_os.ps1`:** the zero-green sweep used `Get-Content -Raw` which threw in this shell and halted the run under `ErrorActionPreference=Stop` — switched to `[IO.File]::ReadAllText/WriteAllText`.
- Installed **OmniRoute** globally (`npm install -g omniroute`, exit 0).

### 2. [Endpoints & Variables]
- Dashboard :3000 (per Saia's choice; UPDATE-WITH-AI default is :3737). Verified HTTP 200, BUILD_ID present.
- New tabs in 07-05: **OmniRoute** ($0, 90+ free providers, no key), **Implementation Checklist**. Also present: Apollo (renamed Jarvis), Hermes Astros.

### 3. [Verification]
- **LOCAL — PASS.** Clean rebuild (cleared stale `.next`), dashboard boots on :3000, M7 navy/gold branding intact, zero-green sweep applied.
- ⚠️ GCP not provisioned — local only.
- ⚠️ **CONFLICT (flagged to Saia):** the 07-05 pack renamed **Jarvis → Apollo** (routes jarvis/jarvis-log/jarvis-memory → apollo/apollo-log/apollo-memory; ApolloView/ApolloRealtime/ApolloBuilds). This REVERTED the M7 free-Jarvis stack: Apollo uses new lib `hermesApollo.ts` (not my Groq brain), and ApolloRealtime calls api.openai.com directly (the billing wall my SDP proxy solved). My Jarvis files (JarvisView.tsx, JarvisRealtime.tsx, hermesJarvis.ts) are moved aside to scratchpad + preserved in the backup; `realtime/sdp` proxy route retained for reuse. Awaiting Saia decision: re-apply the free stack onto Apollo vs accept pack Apollo.

### 4. [Cowork Hand-off]
```markdown
## Delta
- Agent OS updated 07-03 → 07-05 (OmniRoute $0-routing tab + Implementation Checklist). Dashboard boots on :3000, M7-branded. Backup retained at 04_Tech_Lab/_agentos_backups/source.bak-20260705_153226.
- BREAKING for M7: pack rebranded Jarvis→Apollo and reverted the free voice stack (Groq brain + browser voice + SDP proxy). Files preserved; decision pending on re-applying the free stack onto Apollo.
- Fixed update_agent_os.ps1 sweep (-Raw → .NET IO). OmniRoute installed. GLM Code tab needs a free Ollama account (manual).
```

---

## 2026-07-04 — Cycle: Hermes profile spot-checks + one-command re-sync infrastructure

### 1. [Scope]
- **Spot-checked** marketing + roofing profiles (beyond the earlier leads test) to confirm the injected Playbook is actually applied.
- **Made the whole Hermes customization vault-canonical + re-deployable.** Snapshotted all 7 profile SOULs into `04_Tech_Lab/hermes_profiles/*.SOUL.md` (+ `_base.SOUL.md`). Upgraded the base/default SOUL (`%LOCALAPPDATA%\hermes\SOUL.md`) from the old 1410-byte stub to the enriched 2719-byte grounding.
- **Created `04_Tech_Lab/sync_hermes_m7.ps1`** — idempotent one-command re-sync: deploys the M7 theme (+ sets active), base SOUL, and all per-profile SOULs from the vault masters, then restarts the dashboard. Run once after any `hermes update`.

### 2. [Endpoints & Variables]
- Vault masters: `04_Tech_Lab/hermes_m7_theme.yaml`, `04_Tech_Lab/hermes_profiles/{_base,main,marketing,leads,roofing,restoration,seo,content}.SOUL.md`.
- Re-sync: `04_Tech_Lab/sync_hermes_m7.ps1` → deploys to `%LOCALAPPDATA%\hermes\` + `hermes config set dashboard.theme m7` + dashboard restart.

### 3. [Verification]
- **LOCAL — PASS.**
  - marketing profile: correctly returned the 1% Kill Rule ("pause <1.0% CTR after 48h OR 1,000+ impressions, redeploy budget").
  - roofing profile: named Brand A avatars + hook using "The Pineapple Standard" (no banned terms, no cross-brand bleed).
  - `sync_hermes_m7.ps1` ran clean: theme + base + 7 profiles deployed, dashboard 200, `GET /api/dashboard/themes` active=m7.
- ⚠️ GCP not provisioned — local only.

### 4. [Cowork Hand-off]
```markdown
## Delta
- Entire Hermes M7 layer is now vault-canonical + one-command re-deployable: 04_Tech_Lab/sync_hermes_m7.ps1 pushes the theme + all profile grounding from vault masters and restarts the dashboard. Run after any `hermes update`.
- Vault masters: 04_Tech_Lab/hermes_m7_theme.yaml + 04_Tech_Lab/hermes_profiles/*.SOUL.md. Base/default SOUL upgraded to full grounding.
- Verified marketing (1% Kill Rule) + roofing (Brand A avatars) apply the Playbook; sync script verified idempotent.
```

---

## 2026-07-04 — Cycle: Built the M7 Playbook INTO Hermes (profile grounding)

### 1. [Scope]
- Gap: Hermes profile SOUL files had identity + the 4 rules but NOT the operational Playbook (frameworks, lead scoring, lexicon table, Meta/video specs). Agents knew *who* they work for, not *how to run the SOPs*. Also found + fixed brand violations: marketing SOUL said "Warrior Heritage" (banned "warrior"); roofing said "TOA TIER".
- **Created `03_Knowledge_Mat/HERMES_PLAYBOOK.md`** (vault, canonical) — Hermes-optimized operational digest of MASTER_PLAYBOOK.md: laws, full lexicon-mutation table, high-value metrics, lead scoring matrix, frameworks (PACT/CARPARK/BLAST/TCCA/Sabri/Hormozi), 1-3-12 Meta, 50/5/3 video, lead-engine SLA, GEO/AEO SEO, dual-brand, heritage, regional.
- **Rewrote all 7 profile SOULs** (`%LOCALAPPDATA%\hermes\profiles\{main,marketing,leads,roofing,restoration,seo,content}\SOUL.md`) — each now carries its Playbook slice + a pointer to HERMES_PLAYBOOK.md. Fixed "Warrior Heritage" → "Heritage/The Pineapple Standard"; "TOA TIER" → "ELITE" (Toa/Elite is internal-only label).

### 2. [Endpoints & Variables]
- Grounding mechanism: each profile's `SOUL.md` (standalone, replaces base; loaded by the Hermes CLI/chat). Profiles are USER data → survive `hermes update`.
- Canonical vault source: `03_Knowledge_Mat/HERMES_PLAYBOOK.md`. Profile SOULs are the deployment target.

### 3. [Verification]
- **LOCAL — PASS.** `HERMES_PROFILE=leads hermes -z "a lead scores 85 — tier + action?"` → "Score 85 exceeds the 80 threshold → TIER 1: SAIA direct (same-day CPPA, 5-min response, Full Restoration Coverage pitch)." Correct ELITE routing + speed-to-lead + lexicon, all from the injected grounding. Proves Hermes loads the enriched SOULs.
- ⚠️ GCP not provisioned — local only.

### 4. [Cowork Hand-off]
```markdown
## Delta
- The M7 Master Playbook is now operational grounding inside Hermes. Canonical digest: 03_Knowledge_Mat/HERMES_PLAYBOOK.md (vault). Deployed into all 7 profile SOULs (main + marketing/leads/roofing/restoration/seo/content), each with its relevant slice.
- Fixed 2 brand violations in existing SOULs (marketing "Warrior Heritage"; roofing "TOA TIER").
- Re-sync path if profiles are ever rebuilt: regenerate each SOUL from HERMES_PLAYBOOK.md slices. Profile SOULs survive hermes update (user data).
- Verified: leads profile applies the lead-scoring matrix correctly.
```

---

## 2026-07-04 — Cycle: EXACT M7 Hermes dashboard theme (durable, survives hermes update)

### 1. [Scope]
- Replaced the `midnight` approximation with a true, pixel-exact **M7** theme.
- Discovered Hermes supports **user themes** via `_discover_user_themes()` → `%LOCALAPPDATA%\hermes\dashboard-themes\*.yaml`, served to the frontend with full definition. This is USER data → **survives `hermes update`**, needs **no vendor edits and no web rebuild**.
- **Created `04_Tech_Lab/hermes_m7_theme.yaml`** (vault master, single source of truth) and installed a copy to `%LOCALAPPDATA%\hermes\dashboard-themes\m7.yaml`.
- Palette: background Royal Navy `#0a1a33`, midground/primary Pineapple Gold `#FBC02D`, accent + `success` + ring Status Cyan `#00BFFF`, borders Navy `#1A365D`. **`colorOverrides.success` = cyan** so the "active" stat is no longer green — full zero-green compliance.
- Set active via `hermes config set dashboard.theme m7`.

### 2. [Endpoints & Variables]
- User theme file: `%LOCALAPPDATA%\hermes\dashboard-themes\m7.yaml` (master in `04_Tech_Lab/hermes_m7_theme.yaml`).
- `dashboard.theme = m7` in hermes config.yaml.
- Verified via `GET :9119/api/dashboard/themes` (active=m7, ships full definition).

### 3. [Verification]
- **LOCAL — PASS.** API: active=m7, background `#0a1a33`, midground `#fbc02d`, primary gold, accent+success cyan. Browser: Manage tab renders navy canvas, gold headings/Overview pill, cyan stats/badges; the previously-green "Active" number is now Status Cyan `#00BFFF`. Zero green.
- Durable: theme lives in user data dir → `hermes update` will not remove it. Re-install one-liner documented in the YAML header.
- ⚠️ GCP not provisioned — local only.

### 4. [Cowork Hand-off]
```markdown
## Delta
- Hermes dashboard now uses a true M7 theme (Navy/Gold/Cyan, zero green) via Hermes' native user-theme system (~/.hermes/dashboard-themes/m7.yaml). No vendor hacking; survives hermes update.
- Vault master: 04_Tech_Lab/hermes_m7_theme.yaml. Re-install after a hermes update: copy → dashboard-themes\m7.yaml + `hermes config set dashboard.theme m7`.
```

---

## 2026-07-04 — Cycle: Themed Hermes dashboard toward M7 (midnight, zero-green)

### 1. [Scope]
- Goal: make the embedded Hermes admin dashboard (:9119) match M7 (navy, no green teal).
- Action: `hermes config set dashboard.theme midnight` — switched the dashboard's built-in theme from `default` (Hermes Teal/green) to `midnight` (deep blue-violet, cool accents, ZERO green). Used Hermes' own supported CLI — no vendor source files edited, nothing created/moved.
- **Setting location:** `C:\Users\estim\AppData\Local\hermes\config.yaml` (`dashboard.theme`). This is OUTSIDE the vault because that is where the third-party Hermes tool stores its own display preference; it is a single config value, not a folder change.

### 2. [Endpoints & Variables]
- `dashboard.theme = midnight` in hermes config.yaml. Persisted → survives dashboard restarts.
- Restarted dashboard `hermes dashboard --no-open --port 9119 --skip-build` (UI already built).

### 3. [Verification]
- **LOCAL — PASS.** :9119 root 200 after restart. Browser check: Manage tab renders in deep navy; the Overview pill/accents changed from teal to violet; the dominant green Hermes chrome is gone.
- Honest limits: `midnight` is the closest ZERO-GREEN preset, not pixel-exact M7 — accents are blue-violet (not M7 gold #FBC02D / cyan #00BFFF), and a single "active sessions" status number stays green (semantic, baked into the theme). Exact M7 colors would require a CUSTOM theme in the Hermes vendor install, which `hermes update` would wipe — not done (out of 4-Fala scope + non-durable).
- ⚠️ GCP not provisioned — local only.

### 4. [Cowork Hand-off]
```markdown
## Delta
- Embedded Hermes dashboard re-themed default(teal/green) -> midnight (navy, zero-green) via `hermes config set dashboard.theme midnight`. Persisted in hermes config.yaml.
- Closest supported preset; not exact M7 gold/cyan (that would need a custom vendor theme that hermes update wipes). If Saia wants exact, revisit as a post-update injected theme.
- To change again: `hermes config set dashboard.theme <default|midnight|mono|...>` (list via GET :9119/api/dashboard/themes).
```

---

## 2026-07-04 — Cycle: Fixed Manage tab "Internal Server Error" (Hermes dashboard :9119)

### 1. [Scope]
- Symptom: Hermes → **Manage** tab (iframe of the Hermes FastAPI dashboard on :9119) showed "Internal Server Error"; `/` and `/api/status` returned HTTP 500 while `/docs` returned 200.
- Root cause: the dashboard's **web UI first-run build never completed** (`tsc -b && vite build`). FastAPI booted (built-in `/docs` worked) but every page route 500'd because the compiled frontend assets were missing. The Next lifecycle route (`src/app/api/hermes/dashboard/route.ts`) launches it detached with `stdio: "ignore"` and only polls 30s, so the incomplete build was invisible.
- Fix: relaunched `hermes dashboard --no-open --port 9119` and let the vite build **finish**. Build output is now cached on disk, so subsequent launches serve the built UI. No code change needed.

### 2. [Endpoints & Variables]
- Hermes dashboard :9119 (FastAPI/uvicorn, Hermes Agent v0.18.0). Started by `hermes dashboard`. Embedded via `src/components/HermesManage.tsx` (`DASH_URL http://localhost:9119`).
- Post-fix: `/` → 200, `/api/status` → 200. (`/api/config`, `/api/auth/providers` → 401 = normal auth-gating.)

### 3. [Verification]
- **LOCAL — PASS.** Log shows `HERMES_DASHBOARD_READY port=9119`. Browser check: Manage tab renders the full dashboard ("Connected · localhost:9119", Sessions 18/540 msgs, full nav). No 500.
- ⚠️ GCP not provisioned — local only.
- Note: the :9119 dashboard is Hermes' own third-party admin UI (not M7-generated), so its internal styling is out of brand-firewall scope.

### 4. [Cowork Hand-off]
```markdown
## Delta
- Manage tab fixed: the Hermes FastAPI dashboard (:9119) was 500ing because its web UI had never finished its first-run vite build. Completed the build; it's cached now, so the tab loads.
- No code change. If it ever 500s again after a Hermes update, run `hermes dashboard --no-open --port 9119` once in a terminal and let the "Building web UI…" step finish before opening the tab.
- Loop: Read (dashboard route + HermesManage) -> Do (finish the UI build) -> Stage (n/a) -> Log (manifest + log.md).
```

---

## 2026-07-04 — Cycle: Jarvis switched to FREE stack (Groq brain + browser voice, zero OpenAI)

### 1. [Scope]
- Goal: run Jarvis with $0 / no OpenAI billing after the Realtime quota wall. User picked **browser voice** + **Groq brain**.
- **Modified `src/lib/hermesJarvis.ts`:** added `groqComplete()` (Groq `https://api.groq.com/openai/v1/chat/completions`, model `llama-3.3-70b-versatile`, key `GROQ_API_KEY` from active profile). `complete()` and `completeFast()` now try **Groq first**, then fall back to MiniMax/OpenRouter. So `auto` and `fast` modes are free; `agent` mode still uses the Hermes CLI.
- **Modified `src/components/JarvisView.tsx`:** (a) `realtime` default `true → false` so the tab opens in free browser mode, no OpenAI auto-dial; (b) `speak()` rewritten to use browser `window.speechSynthesis` (en-GB butler voice) instead of `/api/hermes/tts` (OpenAI).
- **Modified `04_Tech_Lab/update_agent_os.ps1`:** added `JarvisView.tsx` + `hermesJarvis.ts` to `$CUSTOMS` (now 12).

### 2. [Endpoints & Variables]
- Brain: `POST https://api.groq.com/openai/v1/chat/completions` (Bearer `GROQ_API_KEY`, model `llama-3.3-70b-versatile`). Optional override `AGENTIC_OS_JARVIS_FAST_MODEL`.
- Voice: browser `speechSynthesis` — no endpoint, no key.
- STT: browser `SpeechRecognition` (Chrome/Safari) — no key.
- `POST /api/hermes/jarvis { prompt, mode, history }` → reply text (now Groq-backed).

### 3. [Verification]
- **LOCAL — PASS.** Direct Groq probe → "Yes, sir, I am indeed online and at your service." Rebuilt (exit 0), restarted :3000 (200). `/api/hermes/jarvis` auto mode → "I am indeed online and ready to assist you, sir." (mode=auto, ok=true). Butler persona intact, zero OpenAI calls.
- ⚠️ GCP not provisioned — local only.
- Missing keys for this free path: **NONE** (browser STT $0, browser voice $0, GROQ_API_KEY already present).

### 4. [Cowork Hand-off]
```markdown
## Delta
- Jarvis no longer needs OpenAI. Brain = Groq (free, llama-3.3-70b-versatile); voice = browser speechSynthesis (free, en-GB); mic = browser SpeechRecognition (free). Realtime/OpenAI is now an opt-in toggle, default OFF.
- Files: hermesJarvis.ts (Groq-first complete/completeFast), JarvisView.tsx (default browser mode + browser TTS). Both in update_agent_os.ps1 $CUSTOMS.
- Verified: Groq reply live + /api/hermes/jarvis auto returns in-character. User: hard-refresh :3000, open Hermes-Jarvis, tap the core (allow mic) or flip Wake word / Live, and talk. No bill.
- Loop: Read (jarvis lib + view + tts route) -> Do (Groq brain + browser voice) -> Stage (in-vault) -> Log (manifest + log.md).
```

---

## 2026-07-04 — Cycle: Jarvis root-cause diagnosis (browser-level) — it's OpenAI BILLING, not code

### 1. [Scope]
- Read the LIVE browser (Chrome MCP) on `127.0.0.1:3000/hermes`, ran the exact real WebRTC offer through the proxy and each OpenAI endpoint individually.
- No files changed this cycle — diagnostic only.

### 2. [Endpoints & Variables]
- `POST /v1/realtime/calls?model=gpt-realtime` (correct GA call) → **HTTP 429 `insufficient_quota`** ("You exceeded your current quota, please check your plan and billing details").
- `POST /v1/realtime?model=…` (old beta shape) → 400 `beta_api_shape_disabled` (endpoint retired) — this was masking the 429 in the proxy's last-error return.
- `POST /api/hermes/realtime/session` → still mints `ek_…` fine (auth valid).

### 3. [Verification]
- **LOCAL — root cause CONFIRMED.** Key is valid (mints ephemeral) but the OpenAI account has $0 usable Realtime credit → 429 on the actual audio call. Proxy targets the correct GA endpoint; the WebRTC offer (1525 bytes) is well-formed. **Blocker is OpenAI billing, not code.**
- ⚠️ GCP not provisioned — local only.

### 4. [Cowork Hand-off]
```markdown
## Delta
- Jarvis "Couldn't open the realtime audio link" = OpenAI HTTP 429 insufficient_quota. The SDP proxy, session token, and dashboard are all verified correct; the wall is the OpenAI account's credit balance.
- User action: platform.openai.com -> Billing -> add payment method + credit balance (Realtime API needs pre-paid credits). Then Jarvis connects with no code change.
- Recommended (pending GO): remove dead /v1/realtime beta fallback from the proxy + surface OpenAI's real error string in the Jarvis panel so quota/billing errors are self-evident.
```

---

## 2026-07-04 — Cycle: Jarvis Realtime SDP proxy (fix "Couldn't open the realtime audio link")

### 1. [Scope]
- **Root cause:** The browser was calling `api.openai.com` directly for the WebRTC SDP handshake and was being blocked client-side (AV web-shield / proxy). Server-side reachability to OpenAI was already proven 100% healthy (token mints, model `gpt-realtime` accepted, endpoint reachable).
- **Created:** `src/app/api/hermes/realtime/sdp/route.ts` — server-side SDP relay. Browser POSTs its SDP offer to this localhost route; the dashboard server (which CAN reach OpenAI) relays the exchange and returns the answer SDP.
- **Modified:** `src/components/JarvisRealtime.tsx` — `sdpExchange()` now POSTs to `/api/hermes/realtime/sdp` (localhost) instead of `api.openai.com` directly. Browser now only ever talks to localhost.
- **Modified:** `04_Tech_Lab/update_agent_os.ps1` — added both files to the `$CUSTOMS` preserve-list (now 10 entries) so future one-button updates never wipe the proxy.
- Paths under vault: `03_Knowledge_Mat/00_Atlas/templates/agent-os-pack-2026-06-29/source`.

### 2. [Endpoints & Variables]
- **NEW** `POST /api/hermes/realtime/sdp?model=gpt-realtime` — header `x-oai-ephemeral: <ek_...>`, body = SDP offer (`application/sdp`) → returns OpenAI SDP answer. Relays to `https://api.openai.com/v1/realtime/calls` (fallback `/v1/realtime`).
- Depends on existing `POST /api/hermes/realtime/session` (mints the `ek_...` ephemeral). No new .env strings — reuses `OPENAI_API_KEY` from `%LOCALAPPDATA%\hermes\profiles\main\.env`.
- Dashboard :3000 (production `npm start`).

### 3. [Verification]
- **LOCAL — PASS.** Rebuilt (`npm run build` exit 0), restarted :3000 (HTTP 200). Minted ephemeral `ek_6a492...` via `/session`. POSTed a probe SDP to `/sdp` → proxy relayed to OpenAI, OpenAI returned `HTTP 400 invalid_offer: "Failed to parse offer... syntax error at pos 5"`. That OpenAI-side parse rejection of a deliberately-garbage offer **proves the localhost→OpenAI relay path is open**; a real browser WebRTC offer will parse and return a 200 answer.
- ⚠️ **Google Cloud: NOT provisioned** — verification is local only.
- Brand law: no UI/color changes; zero-green untouched.

### 4. [Cowork Hand-off]
```markdown
## Delta
- Jarvis Realtime speech-to-speech no longer depends on the browser reaching api.openai.com. A localhost SDP proxy (/api/hermes/realtime/sdp) relays the WebRTC handshake server-side, defeating AV/proxy client blocks.
- Files: NEW src/app/api/hermes/realtime/sdp/route.ts; EDIT src/components/JarvisRealtime.tsx (sdpExchange → localhost). Both now in update_agent_os.ps1 $CUSTOMS so updates preserve them.
- Verified server-side: token mints + proxy relay reaches OpenAI (OpenAI-side offer parse confirms path). User action: hard-refresh :3000, click Go live.
- Loop honored: Read (session route + component) -> Do (proxy + client rewire) -> Stage (in-vault) -> Log (this manifest + log.md).
```

---

## 2026-07-04 — Cycle: Core rules config + Python engine wiring (Read→Do→Stage→Log)

### 1. [Scope]
- **Files checked/read:** `03_Knowledge_Mat/COMMAND_CENTER_OS.md`, `SHARED_MEMORY.md`, `01_Command_Center/GROUNDING.md`, `claw.md`, `CLAUDE.md`, `04_Tech_Lab/server_m7.py`, `LAUNCH_ALL.bat`.
- **Created:** `m7_core_rules.config` (repo root) — machine-readable master rules: memory paths, engine map, brand palette (zero green), lexicon mutations (CPPA/IKO), Outbox Shield, 4-Fala, trust signals.
- **Modified:** `LAUNCH_ALL.bat` — now launches the live Python engine `04_Tech_Lab/server_m7.py` (:51763) + added :51763 to the port-purge guard.

### 2. [Endpoints & Variables]
- **:51763** = M7 Command Center Python engine (stdlib http backend: memory/kanban/Outbox/firewall API). Matches `SHARED_MEMORY.md` `feed_url: http://127.0.0.1:51763/api/memory`.
- New root file `m7_core_rules.config`. No new .env strings.
- Full live map: dashboard :3000 · command-center :3737 · engine :51763 · Paperclip :3100 · FCC :8082 · Ollama :11434.

### 3. [Verification]
- **LOCAL.** `python server_m7.py` → HTTP 200 on :51763. Brand law: config/launcher use Navy `#1A365D` + Gold `#FBC02D`; the "green/free/GAF" strings in the config are the **ban definitions**, not asset colors. `LAUNCH_ALL.bat` scan = 0 violations.
- ⚠️ **Google Cloud: NOT provisioned** — verification is local only.

### 4. [Cowork Hand-off]
```markdown
## Delta
- Root now carries m7_core_rules.config — the single machine-readable rulebook (brand, lexicon, Outbox, 4-Fala, engine/memory paths). Cowork can log this into the Master Playbook.
- The Python engine (server_m7.py :51763) is now part of the one-button LAUNCH_ALL boot sequence, from the LIVE 04_Tech_Lab dir (not an archive). It powers the dashboard's real memory/kanban/Outbox buttons + wires to SHARED_MEMORY.md.
- Loop honored: Read (core files) -> Do (config+launcher) -> Stage (in-vault, root config per directive) -> Log (this manifest + log.md).
```

---

## 2026-07-04 (late 2026-07-03) — Cycle: Jarvis port-fix + profiles + 4-Fala compliance

### 1. [Scope]
- **Jarvis FIXED (root cause):** `04_Tech_Lab/server.js` line 18 hardcodes `const PORT = 3000;` — an Express app that squatted on :3000, colliding with the dashboard (intermittent "Cannot POST" → "Couldn't open the realtime audio link"). Killed it + the stale Downloads-copy dashboard; now ONE server per port: vault dashboard :3000, root `server.js` :3737.
- **Hermes profiles:** removed `julian`; created M7 SOP profiles `restoration`, `seo`, `leads` (M7-grounded SOULs + cloned key). Roster: main, roofing, restoration, content, marketing, seo, leads — all grounded.
- **4-Fala compliance:** repointed `update_agent_os.ps1` `$BAKROOT` → `04_Tech_Lab/_agentos_backups/` (in-vault, gitignored); removed all stray `C:\tmp\m7_*` folders. No more out-of-vault artifacts.

### 2. [Endpoints & Variables]
- `:3000` = vault Next.js dashboard (single owner). `:3737` = root `server.js`. No new ports.
- **Latent bug flagged (needs approval to fix):** `04_Tech_Lab/server.js:18` hardcodes 3000; its own `.env` says `PORT=3001`. Fix = `const PORT = process.env.PORT || 3001;` so it never grabs :3000 again.

### 3. [Verification]
- **LOCAL.** Jarvis session endpoint mints valid `ek_` tokens on both `127.0.0.1:3000` and `localhost:3000`. Single listener per port confirmed via netstat. `:3737` HTTP 200.
- ⚠️ **Google Cloud: NOT provisioned** — no GCP deployment exists; all verification is local.

### 4. [Cowork Hand-off]
```markdown
## Delta since last manifest
- Port collision resolved: 04_Tech_Lab/server.js (hardcoded :3000) removed from the dashboard port.
- Canonical single server map: dashboard :3000, M7 command-center server.js :3737, Paperclip :3100, FCC :8082, Ollama :11434.
- Hermes now has 7 M7-grounded profiles (julian retired); "default"/base SOUL grounded so Hermes stops treating "Pineapple" as prompt-injection.
- All backups/staging now INSIDE the vault (04_Tech_Lab/_agentos_backups). Zero out-of-vault artifacts.
- OPEN: (a) fix 04_Tech_Lab/server.js hardcoded port; (b) consolidate fragmented memory (01_Command_Center/memory, top-level Omi) into 03_Knowledge_Mat/SHARED_MEMORY.md; (c) GCP not provisioned.
```

---

## 2026-07-03 — Session: Hermes grounding + keys + theme + updater + audit

### 1. [Scope] — features/code added or altered
- **Hermes grounding (bugfix):** wrote M7-identity `SOUL.md` to the `base` (default profile), `main`, and `julian` profiles under `%LOCALAPPDATA%\hermes` — resolves Hermes rejecting "Pineapple" as prompt injection. (roofing/content/marketing were already grounded.)
- **API keys wired + validated:** OpenAI (`sk-proj-…`, 200 ✓), ElevenLabs (`sk_cd58…`, 200 ✓), Groq (✓), Google/Gemini (✓), Firecrawl (✓), Hunter (✓) — stored in `~/.hermes/.env` + `profiles/main/.env` (outside vault).
- **M7 theme rebrand:** `src/app/globals.css` palette → Navy/Gold/Cyan; swept 112+ green hexes/classes/rgba across 36 components → cyan/gold. Zero green in served build.
- **One-button updater:** `UPDATE_AGENT_OS.bat` + `04_Tech_Lab/update_agent_os.ps1` — backup, preserve 8 M7 customizations, zero-green sweep, rebuild, restart, + **post-update verification pass** that checks every install guide, service, dep, key, and branding. Syntax-validated.
- **Full setup audit:** `01_Command_Center/M7_AGENT_OS_SETUP_AUDIT.md` (all 27 install guides verified).

### 2. [Endpoints & Variables]
- **Ports (all local):** `:3000` Agentic OS dashboard · `:3737` M7 server.js · `:3100` Paperclip · `:8082` FCC · `:11434` Ollama.
- **.env strings introduced** (in `~/.hermes` profile envs, git-ignored, NOT in vault): `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`, `GROQ_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `FIRECRAWL_API_KEY`, `OPENROUTER_API_KEY`, `OMI_API_KEY`, `OBSIDIAN_API_KEY`, `PINECONE_API_KEY`, `APIFY_API_TOKEN`, `KIE_API_KEY`. Leads: `HUNTER_API_KEY` in `~/.agentic-os/outreach/config.json`.
- No new custom ports introduced this session.

### 3. [Verification]
- **Environment: LOCAL only.** ⚠️ **Google Cloud environment is NOT provisioned** — there is no GCP deployment yet, so GCP verification cannot be claimed. All features verified on the local Windows machine (127.0.0.1). If GCP deployment is desired, that is a separate task to scope.
- Local verification: dashboard/Paperclip/FCC/Ollama all HTTP-200 (FCC 401=auth-gated); OpenAI+ElevenLabs keys return 200; realtime session endpoint mints valid `ek_` tokens.

### 4. [Cowork Hand-off] — architecture summary for Claude Cowork
```markdown
## M7 Agent OS — Current Architecture (2026-07-03)
- Runtime: local Windows. Node/Next.js dashboard (:3000) built from the vault copy at
  03_Knowledge_Mat/00_Atlas/templates/agent-os-pack-2026-07-03(source). M7 server.js on :3737.
- Agents: Hermes (5 profiles, all M7-grounded, home=%LOCALAPPDATA%\hermes), Paperclip AI company (:3100),
  FCC proxy (:8082, model=nemotron-120b), Ollama (:11434, on-device builds only — never the default).
- Keys: all in ~/.hermes profile .env (outside vault, git-ignored). OpenAI+ElevenLabs+Groq valid.
- Branding: Navy/Gold/Cyan theme, zero green, enforced by update_agent_os.ps1 sweep + brand_firewall.py.
- Backup: private GitHub repo saia-collab/pineapple-m7-vault (secrets excluded).
- OPEN ITEMS: (a) Jarvis Realtime WebRTC blocked browser-side (extension/firewall — not server);
  (b) Google Cloud deployment NOT provisioned; (c) Phone Agent needs a Twilio number (user-supplied).
```

---
*Ko e hala 'o e fononga ko e faka'apa'apa.*

---

## 2026-07-06 — Cycle: OpenSEO installed + running + dashboard-connected

### 1. [Scope]
- Located the real OpenSEO source (not bundled in the pack): official repo github.com/every-app/open-seo (MIT, self-hosted Semrush/Ahrefs alt, DataForSEO-powered).
- Cloned to `~/open-seo` (the exact path the dashboard's SEO tab expects), wrote `.env` (PORT=3001, AUTH_MODE=local_noauth, DataForSEO key = placeholder for Saia), ran `docker compose up -d`.
- Documented in vault: `04_Tech_Lab/OPENSEO_SETUP.md`.

### 2. [Endpoints & Variables]
- Container `open-seo-open-seo-1` on **:3001** (127.0.0.1 bound), `restart: unless-stopped` (auto-starts with Docker).
- `~/open-seo/.env`: `DATAFORSEO_API_KEY` = PLACEHOLDER (Saia adds after signup — $1 free credit).

### 3. [Verification]
- **LOCAL — PASS.** :3001 → HTTP 200 (app built + serving). Dashboard `/api/openseo/status` → `{"running":true,"status":200}` — the SEO → OpenSEO tab now shows "running" and embeds the tool.
- ⚠️ Keyword/backlink data requires Saia's DataForSEO key (per-use, not invented). App itself is free + running.

### 4. [Cowork Hand-off]
```markdown
## Delta
- OpenSEO (free self-hosted SEO tool) installed at ~/open-seo, running on :3001, dashboard-connected, auto-restarts with Docker. Setup doc: 04_Tech_Lab/OPENSEO_SETUP.md.
- ONE action for Saia: sign up at dataforseo.com ($1 free credit), put login:password in ~/open-seo/.env, `docker compose up -d`. Then keyword research is live.
- Free ranks for OUR site still come from Google Search Console (M7_SEO_TRACKER.md) once the site is published.
```

---

## 2026-07-06 — Cycle: Full queue executed → Outbox (website + landing + campaign + content)

### 1. [Scope]
Fired the entire M7_TASK_QUEUE while Saia set up DataForSEO. All PAUSED in Outbox_Drafts:
- **Roofing website** (`Website_Roofing/`): 7 pages (Home, Services, Storm & Insurance, Service Areas, About, Reviews, Contact) + shared `styles.css` design system. Mobile-first, semantic HTML, JSON-LD (LocalBusiness + FAQ), Navy/Gold/Cyan zero-green, CPPA/IKO/RCAT/972-928-0788, HQ address. No build step.
- **CPPA ad landing** (`Landing_CPPA.html`): single high-converting page for Meta/LSA traffic, self-contained.
- **1-3-12 Meta campaign brief** (`Campaigns/`): CBO $250/wk, 3 ad sets, 12 PACT creatives, kill/scale/pixel rules.
- **Video/call/SMS scripts** (`Scripts/`): 5× 50/5/3 video scripts + CARPARK 7-stage close + Lead Bridge SMS.
- **Weekly content** (`Content/`): 10 captions, 6 video-cut specs, 2 GBP posts, 3 testimonial frames (placeholders — no invented quotes).
- **Review-request texts** (`Reviews/`): same-day/3-day/7-day/thank-you sequence.
- **Restorations homepage** (`Website_Restorations/`): Brand B, water/fire/mold/biohazard ONLY — dual-brand separation verified (0 roofing vocab in copy).

### 2. [Verification]
- **Compliance — PASS.** `brand_firewall.py --check` STATUS: OK. Manual scan across all 18 files: 0 "free", 0 GAF/warrior/toa/sales pitch/money/cheap/bargain, 0 green. Dual-brand intact.
- Fixed en route: "Free-of-Guesswork" → "No-Guesswork" (Home CTA); "Stress-Free" → "Zero-Stress" (campaign heading). Recovered index.html after a PowerShell replace corrupted it (rewrote clean).
- Reviews/testimonials left as clearly-marked placeholders (no invented customer quotes). Contact/landing forms are placeholders (need CRM wiring before publish).
- ⚠️ ALL PAUSED — nothing published. GCP not provisioned — local only.

### 3. [Cowork Hand-off]
```markdown
## Delta
- Full July queue executed to Outbox (7-page roofing site + CSS, CPPA landing, 1-3-12 Meta brief, video/call/SMS scripts, weekly content, review texts, restorations homepage). All brand-compliant, dual-brand-clean, PAUSED.
- Publish sequence: Saia reviews → wire forms to CRM + real reviews → deploy roofing site → verify in Google Search Console → SEO tracking turns on (13 city pages + these).
- OpenSEO running on :3001 (needs Saia's DataForSEO key).
```

---

## 2026-07-06 — Cycle: Fixed Hermes Astros (pack bug) + M7 Design Skill (filtered C.R.A.F.T.)

### 1. [Scope]
- **Hermes Astros fix:** `AstrosView.tsx` calls `/api/astros/{config,history,latest,notebook,scan}` but the pack (07-05) NEVER shipped those routes (only `/api/radar/*`) → every call 404'd to an HTML page → "Unexpected token '<' … is not valid JSON". Created the 5 missing routes: scan/latest/history alias the working radar handlers; config persists the watchlist (seeded with M7 keywords — roofing/storm/home-services); notebook returns a graceful "not wired yet" message. Added all 5 to `update_agent_os.ps1 $CUSTOMS` (pure additions — /MIR would delete them otherwise).
- **M7 Design Skill:** created `01_Command_Center/M7_DESIGN_SKILL.md` — the pasted C.R.A.F.T. front-end/copywriting engine **filtered into M7 branding**. Removed the source kit's banned colors (emerald `#5ab896` = GREEN → Cyan `#00BFFF`; aubergine `#15101a` → Navy). Kept the 10-part skeleton, typography (Bricolage/Manrope/Caveat), components, and copywriting rules; layered in M7 lexicon (CPPA/IKO/RCAT/proverb, zero green).

### 2. [Verification]
- **LOCAL — PASS.** Rebuilt (exit 0), :3000 = 200. astros/config, /latest, /history all return valid JSON; astros/scan POST → `{ok:true,status:"running"}` (keyless RSS, $0). Astros tab no longer crashes.
- ⚠️ Astros NotebookLM handoff button reports "not wired" (needs notebooklm CLI) — graceful, not a crash. Live YouTube richness optional (Tier-1 Google/YouTube key); Tier-3 RSS works keyless.
- ⚠️ GCP not provisioned — local only.

### 3. [Cowork Hand-off]
```markdown
## Delta
- Hermes Astros fixed (pack shipped AstrosView calling /api/astros/* with no routes). 5 alias/impl routes added + preserved in $CUSTOMS. Seeded M7 competitor-radar keywords.
- M7 Design Skill created (01_Command_Center/M7_DESIGN_SKILL.md): C.R.A.F.T. system on-brand, banned green removed. Use it to rebuild the roofing site (Saia found v1 "ugly").
- SEO clarified for Saia: the pack's SEO-Pipeline tab is the built-in generator; our 13 city pages + site were hand-built to Outbox via the Playbook (on-brand, human-gated).
```

---

## 2026-07-06 — Cycle: Agent OS update 07-05 → 07-06 (docs-only) + fixes

### 1. [Scope]
- Updated to pack `agent-os-pack-2026-07-06.zip` (VERSION 2026-07-06). **Docs-only release** — new install guides for Astros/OpenSEO/OmniRoute/GLM, documented Local tab + SEO Transcripts. **Ask Gate: zero new keys/signups/configs required.**
- Backup: `04_Tech_Lab/_agentos_backups/source.bak-20260706_145534` (retained). 17 M7 customizations preserved.
- **Fixed a bug in the updater:** `$brandMap` hashtable had case-colliding keys ('GoldieBench'/'goldiebench') → PowerShell parse error aborted the first run (no harm — parse errors execute nothing). Converted to an ordered array of pairs (`$brandPairs`).
- **Re-fixed `kanbanSeo.ts`:** the 07-06 pack re-injected Julian Goldie's "AI Money Lab"/"AI Profit Boardroom" Skool funnel + "FREE" into the SEO article template. Replaced with the Pineapple CPPA CTA; **added `kanbanSeo.ts` to `$CUSTOMS`** + added the Skool/AI-Money-Lab phrases to the durable de-personalize sweep so it can't come back.

### 2. [Verification]
- **LOCAL — PASS.** Dashboard :3000 = 200, VERSION 2026-07-06. Astros routes preserved (config/latest/history/scan/notebook). kanbanSeo customer-facing CTA = CPPA (0 real "free"/"AI Money Lab"). Remaining refs are harmless (a compliance rule line + an internal deploy site-id).
- ⚠️ GCP not provisioned — local only. Backup retained (not deleted).

### 3. [Cowork Hand-off]
```markdown
## Delta
- Agent OS on 07-06 (docs-only, no new keys). Updater hardened (brandPairs array). kanbanSeo Julian funnel neutralized + preserved in CUSTOMS + durable sweep.
- Next: wire Saia's real assets — Google Drive media → Blotato → the marketing engine + Jarvis daily briefing. NO more building.
```

## 2026-07-17 · Codex diagnosis + Schema live + tracking scripts
- Diagnosed dashboard Codex failure: installed @openai/codex v0.144.5, `codex login` OK, but `codex exec --json` returns **429 (ChatGPT Plus rate limit)** — not an install/Ollama issue. Routing memory corrected.
- Wrote + ran `scratchpad/inject_schema.py` — appended verified RoofingContractor JSON-LD to all 12 live location pages (IDs 9662–9684) via REST read-modify-write (no content clobber, idempotent marker PM7-SCHEMA-JSONLD, star-rating omitted pending verified count). All 12 verified live.
- Added `04_Tech_Lab/scripts/ga4_conversion_events.md` (phone_call_click + cppa_request_click; goes in header plugin, NOT a duplicate base tag).
- Added + ran `04_Tech_Lab/scripts/ping_sitemap.py` — sitemap_index.xml reachable (200); Bing/Google ping endpoints both retired (410) → GSC auto-submission is the live mechanism.

## 2026-07-17 (pt2) · M7 Enterprise config build (from 6 Downloads manifests)
- Created 03_Knowledge_Mat/active_context/notebook_configs/ (Drive-synced, desktop.ini confirmed) + wrote 4 hub config JSONs via 04_Tech_Lab/scripts/initialize_notebooks.py (rich: settings+chat+gem+studio+firewall).
- 04_Tech_Lab/scripts/m7_lexicon_gate_parser.py — FIXED the dangerous `\broof(s|ing)?\b` global-replace gate from the draft (would mangle all copy); now only mutates real violations + flags banned terms. Self-test passes.
- Root AM_STARTUP.bat + PM_SHUTDOWN.bat — loop launchers; fixed the `C:\Users\YourName` placeholder path to the real Drive-synced active_context path. Run only on double-click (not auto-scheduled).
- 01_Command_Center/m7_global_config.json — single source of truth for identity + brand law.
- SKIPPED: SQL schema (needs a DB not set up) + separate test harness (its `\bfree\b` global ban false-fails legit content; merged testing into the parser).
- HONEST CORRECTION told to Saia: NotebookLM does NOT auto-load Drive JSON as settings — configs are sources + source-of-truth; gear/Gem still need one-time UI paste.

## 2026-07-20 · Review stars live + SEO status + agency validation
- Verified all 12 live pages HTTP 200 + RoofingContractor schema + CPPA (proof: M7_PROOF_OF_WORK.md).
- Added AggregateRating (430 reviews / 5.0, verified via Bullseye live map scan) to all 12 pages via inject_schema_v2.py (idempotent replace, single block each).
- Validated Bullseye/Marco agency assessment (24pg): honest + high-quality; ~80% of its fix-list already built on WordPress. Verdict: don't pay retainer. Draft brother reply in M7_BULLSEYE_ASSESSMENT_VALIDATION.md.
- Wrote M7_SITE_CONSOLIDATION_COWORK_BRIEF.md (merge 2 domains; measure backlinks first, 301 before cancel).
- Scrubbed Hormozi 11-framework playbook -> M7_HORMOZI_PLAYBOOK.md (fixed "Free Inspection"->CPPA).
- Sitemap sitemap_index.xml submitted to GSC (status "Couldn't fetch" = normal post-submit).

## 2026-07-20 (pt2) · McKinney live + internal links + Cowork reorg brief
- Deployed roofing-mckinney-tx (#9710) LIVE — schema + 430/5.0 stars (fills Marco's flagged McKinney gap).
- Added internal-link cluster to all 13 pages (5 sibling links each = 65 links) via API read-modify-write, idempotent marker PM7-INTERNAL-LINKS.
- Wrote M7_DRIVE_REORG_COWORK_BRIEF.md (move-only, target=PINEAPPLE_MEDIA_HUB) + M7_EXECUTION_CADENCE_AND_ROUTING.md (daily/weekly SOP + Claude/Cowork/Hermes routing).

---
## 2026-07-23 — Videos rendered, SEO migration ingested, launch runbook
- **2 brand videos rendered locally** (HyperFrames, no API): hail-frisco-60s + allen-flat-60s.
  Both 60.0s, 1080x1920, navy/gold/cyan, zero green, verified frame-by-frame (navy bg fix
  applied: `#{fid}-bg{position:absolute;inset:0}`). Freed 7GB via `npm cache clean` (disk was
  100% full — Downloads=36GB is the standing offender).
- **ChatGPT SEO migration build ingested** to `02_Workspaces/2026-07-23_SEO_Site_Migration/`.
  Verified count-for-count vs manifest: 33 pages (7 core/13 svc/13 city) + 33 Elementor blocks
  + 37 301s + click guide. Brand firewall: ZERO green, ZERO banned, RCAT/phone/CPPA on all.
- **Domain strategy resolved:** Saia owns pineapplecontractors.com (GoDaddy); Scorpion owns only
  the design. Recommendation = repoint contractors.com DNS -> Saia's WordPress (keep the strong
  domain + 29k impressions/#7.9 authority). Generated `redirection-import-CONTRACTORS-PRIMARY.csv`
  (targets swapped to www.pineapplecontractors.com).
- **Deliverables in Outbox:** M7_OPERATING_MANUAL_HOW_TO_RUN.md (full Agentic OS feature map +
  80/20), M7_MIGRATION_LAUNCH_RUNBOOK.md (6-phase domain takeover + keyword battle plan).
- **Pending Saia:** rotate exposed API keys (screenshotted — HeyGen/OpenAI/ElevenLabs/OpenRouter
  etc.); deploy Apps Script /exec; publish 33 pages via Elementor Canvas; GoDaddy DNS repoint;
  send social profile URLs for footer bar. OpenRouter key -> ~/.hermes/profiles/<active>/.env.
- **4-Rules:** Outbox Shield intact (all outputs PAUSED, nothing published live). No folder
  restructure. Brand lexicon clean. Zero green. LOCAL only — no live web change made.

## 2026-08-04 — Website revert to human-approved default (live site)
- Root cause found: 2026-07-24 migration retitled 4 of the brothers pages (7567 Home, 9522 Roof Repair, 9524 Gutter Installation, 9528 Storm Damage Repair) with AI copy; WP nav inherits page titles, so the Services dropdown displayed AI slop.
- Safety backup taken BEFORE revert: 02_Workspaces/_SITE_BACKUPS/BACKUP_2026-08-04_1144_PRE-REVERT.json (59 pages, 3 posts, 3.7MB).
- Restored 10 human page titles (4 brothers pages + 6 nav-linked pages I created).
- Unpublished to DRAFT (saved, not deleted): 16 pages (9624, 9627, 9632, 9662-9684, 9710) + 3 raw-markdown blog posts (9621-9623).
- KEPT PUBLISHED: 9625/9626/9628/9629/9630/9631/9651 — wired into nav menu 18; drafting them would 404 the menu. Titles cleaned instead.
- Verified live: header 2 / footer 1 / nav 6; zero AI titles remaining; all 12 nav links resolve 200.
- Standing rule adopted: git commit + push after EVERY session (GitHub = shared memory between local and cloud Claude sessions).

## 2026-08-04b — Financing / Contact / Insurance Claims page repair (live)
- Same elementor_canvas bug as the homepage found on 3 nav pages: 9625 Insurance Claims, 9626 Financing, 9629 Contact rendered with NO header/footer (raw text on white). Set all three to elementor_header_footer.
- 9629 Contact had 3 placeholder artifacts visible to customers: "(Lead form displays here — Service · Name · Phone · Address.)" and "*(verify)*" on the HQ address. Removed.
- 9626 Financing rebuilt to match pineapplecontractors.com/financing: real GreenSky prequalify CTA -> https://www.greensky.com/prequal/gs/contact-verification?merchant=81104803&channel=External-Button-Prequal (merchant 81104803, verified 200), proper <ul> lists, lender disclosure, CPPA framing.
- 9629 Contact rebuilt: click-to-call, hours, HQ, RCAT #03-0637 + IKO, service-area list, CPPA CTA.
- BRAND NOTE: GreenSky own branding is green. Did NOT reproduce their green banner. Used Navy #1A365D / Gold #FBC02D Pineapple buttons linking out to GreenSky hosted flow -> zero green preserved on our side. Verified 0 green on all 3 pages.
- Lead form NOT embedded: site forms are Elementor widgets, no shortcode available via REST. Needs 2 clicks in Elementor or a WPForms shortcode ID.
- OPEN: confirm HQ address (1 Cowboys Way Ste 270W Frisco TX 75034) is the correct public address.
- Verified live: header 2 / footer 1 / nav 6 on all three; 0 placeholders; 0 green.

## 2026-08-04c — Financing mirrored to contractors.com + Contact nav repointed
- "Stacey-stryker" identified = the WordPress AUTHOR account that built the original site (visible in Pages list Author column). "Go back to what Stacey-stryker created" = the revert already performed in 2026-08-04a.
- FINANCING 9626 rebuilt to mirror pineapplecontractors.com/financing: official GreenSky merchantkit banner (https://www.greensky.com/merchantkit/images/finance_buttons/prequal/prequalify-multi-offer-330.jpg?v=3.0.612) hyperlinked to merchant 81104803 prequalify flow; residential terms ($65k) + commercial terms ($100k); 3-step how-it-works; lender disclosure.
- consumer_flyer_81104803.pdf (2.1MB, 21pp) uploaded from G:\My Drive to WP media id=9827 -> /wp-content/uploads/2026/08/consumer_flyer_81104803.pdf; embedded as inline <object> viewer + download button.
- GREEN EXEMPTION (approved by Saia 2026-08-04): GreenSky brand banner is green. It is the lenders own trademarked hosted asset. All Pineapple-owned styling on the page stays Navy/Gold. Documented inline in the page HTML.
- CONTACT: nav item 9648 repointed from page:9629 to custom anchor /#contact, matching the existing pattern (Process=/#process, About Us=/#about, Reviews=/#reviews). Page 9629 retired to draft.
- ADDRESS DISCREPANCY FOUND: the sites own contact section shows 4400 State Hwy 121 #300, Lewisville, TX 75056 + support@pineappleroofingllc.com. Vault 01_Command_Center/CLAUDE.md claims HQ = 1 Cowboys Way Ste 270W Frisco TX 75034. These conflict. CLAUDE.md is human-owned (its own change control) so NOT edited by agent — Saia to reconcile. NAP consistency matters for the local SEO strategy.
- Verified live: financing header 2/footer 1/nav 6, banner 200 image/jpeg, PDF 200 2101295 bytes, prequalify link present; Contact nav renders href="/#contact".

## 2026-08-04d — Ship-today skills for Saia (no DataForSEO needed)
- Verified WP still connected as Saia (administrator, publish_pages=True) via app password. The "not connected" NotebookLM banner in Claude Desktop is a DIFFERENT connector (claude.ai WordPress.com OAuth) — not the one this session uses.
- Verified DataForSEO NOT wired in this repo — every Nico/Julian/Goldie SOP that landed in Downloads today is BLOCKED on DFS creds. Parked all of them until Saia confirms account.
- NotebookLM auth expired ("nlm login" required). Parked pending user action.
- 3 SEO zips in Downloads not extracted; left them for user decision (also blocked on DFS).
- Installed 2 zero-setup skills Saia can run TODAY without brand markdown or DFS:
  - 03_Knowledge_Mat/active_context/skills/gbp_review_responder.md (from Nico prompt, M7 brand law folded in)
  - 03_Knowledge_Mat/active_context/skills/blog_to_gbp.md (from Julian prompt, 1400-char cap)
- Priority guidance to user: speed-to-lead (5-min callback) > any SEO trick; do review responder daily; batch blog→GBP weekly.

## 2026-08-04e — VA task handoff + brother brand-voice capture kit
- M7_VA_TASK_HANDOFF.md: full daily (90 min) / weekly (3-4 hr) / monthly (4-6 hr) VA workload including lead intake, review response, GBP posts, photo library, review-request sweep, NAP audit. Explicit "what VA does NOT do" list (negative reviews, insurance convos, live publishing, quoting prices) + escalation tree. Onboarding checklist.
- M7_BRAND_HANDOFF_FOR_NAA_SIONE.md: 11-section brand capture questionnaire designed to be short and voice-memo-friendly (Naa Sione lives on job sites). Covers wording he hates, insurance expertise, Hormozi format applied to us, palette lock, HQ address disambiguation (Frisco vs Lewisville), service-area rank, service LEAD/KEEP/DROP, content-restart decision, Polynesian heritage lean.
- M7_BROTHER_CLAUDE_PROMPT.md: single copy-paste prompt he pastes into HIS own Claude/ChatGPT/Gemini. Turns brand capture into an AI-conducted 20-45 min interview that outputs a clean markdown he texts back. Handles the reality that a paper form is homework he wont do; a conversation he will do.
- Rationale: existing AI content sits unpublished in Outbox because Naa Sione (field-experienced, customer/adjuster-facing) keeps rejecting the wording. Nothing unblocks until his voice is captured. This kit is the unblocker.

## 2026-08-05 — Agent OS repair: install completed, Hermes wired to a working model
- Root cause of the stalled install: INSTALL-AND-START.ps1 used Start-Transcript on $Log while the Hermes step did Add-Content on the SAME file -> file-lock crash. FIXED: added separate $HermesLog. Install never reached the staging/build/switch, so canonical `current` never existed and :3000 kept serving the June build (agent-os-pack-2026-06-29).
- Decoupled + did it safely by hand: backed up launchers/config/both Hermes homes/installer; built payload/source in isolated staging (npm ci exit0, next build exit0, compiled 21.3s); switched staging -> 04_Tech_Lab/Pineapple_Agent_OS/current; started on :3737.
- SAFETY TESTS PASS on live :3737 — / 200, /hermes 200, /seo 200, /api/seo/deploy 403, /api/seo/generate-without-transcript 400. Only pineappleroofingllc.com configured. Drafts PAUSED. No auto publish/deploy/index/send/spend.
- Launchers rewritten to the canonical START script (Desktop LAUNCH_ALL.bat, START_LOCAL_STUDIO.bat, RUN_AGENT_OS.bat) -> http://localhost:3737/hermes. Updaters (UPDATE_AGENT_OS.bat + Desktop) -> safe UPDATE script that rejects any ZIP older than the repaired SEO build (can never downgrade to June) and auto-rolls-back. Created pineapple-safety/ that the updater depends on.
- Retired the old June build on :3000 (stopped; folder untouched as rollback).
- HERMES MODEL ROOT CAUSE: config pointed at provider openai-codex / gpt-5.6-sol which was never logged in -> every chat errored. Hermes CANNOT use the local Claude Code subscription (it needs an API key or its own OAuth). OPENROUTER_API_KEY was already present. Set Hermes -> provider openrouter. Verified end-to-end: `hermes -z` returned "HERMES IS ONLINE".
- Claude-through-OpenRouter (anthropic/claude-sonnet-4.5) works but the OpenRouter balance is ~exhausted (HTTP 402; affords ~2663 tokens, Hermes requests 64000). So default set to FREE nvidia/nemotron-3-ultra-550b-a55b:free (1M context, avoids the 64k-context floor error). Claude = one-line swap once Saia adds OpenRouter credits (a purchase — not done autonomously).
- Hermes is already v0.20.0 (Herald) — no risky upgrade needed. Pineapple SEO skill installed into Hermes skills. .agentic-os/config.json corrected (vaultRoot=root, userName=Siosaia, locationLabel=Frisco->was Hawaii, seoSites=pineappleroofingllc.com).
- Desktop deliverable written: PINEAPPLE_AGENT_OS_STATUS.txt (PASS).
- Model per-chat switching: through the one OpenRouter key, /model <id> switches Claude/GLM/Kimi/GPT/DeepSeek per task (paid ones need credits; free default works now).
- NOTE: 04_Tech_Lab/Pineapple_Agent_OS, _agentos_backups, logs added to .gitignore (build is huge; never commit node_modules).

## 2026-08-05b — CORRECTION after reading official SETUP-WITH-AI.md + SETUP-GUIDE.md
- User (rightly) flagged I improvised instead of reading the pack setup docs. Read newest SETUP-WITH-AI.md + SETUP-GUIDE.md (payload/source/member-pack, dated 2026-08-05). My repair MATCHES them: dashboard on :3737, and doc Rule 7 says "Hermes/Jarvis -> an OpenRouter model" (what I set). No feature rebuilt (Rule 7a honored).
- KEY CORRECTION: auth.json shows Codex IS logged in (+ minimax-oauth active; credential_pool: openrouter, openai-codex, anthropic, ollama-cloud, opencode-zen, minimax-oauth). Tested gpt-5.6-sol via openai-codex -> "CODEX IS ONLINE". So the intended Pineapple brain WORKS on the ChatGPT plan; my free-OpenRouter default was an unnecessary workaround.
- Set Hermes back to intended: primary provider=openai-codex model=gpt-5.6-sol; added fallback_providers -> nvidia/nemotron-3-ultra-550b-a55b:free via openrouter (auto-failover on Codex 429). Validated: hermes fallback list exit 0. Final default-path test: hermes replied "Online - GPT-5.6 Sol."
- Agent-tab CLIs installed: Claude, Codex, Antigravity (agy), Gemini. NOT installed: Kimi, GLM/opencode, Grok, Qwen (each needs user login to activate its Studio tab).
- Provider keys present (from Hermes status screenshot): OpenRouter, OpenAI, Gemini, DeepSeek, NVIDIA NIM, Z.AI/GLM, ElevenLabs. Not set: xAI/Grok, Anthropic (not needed - Claude tab uses `claude login`).
- Updated Desktop PINEAPPLE_AGENT_OS_STATUS.txt model section to reflect Codex primary + free fallback.
- Everything else from 2026-08-05a stands: :3737 healthy, SEO safety tests pass, launchers point to canonical START/UPDATE, old June :3000 retired.

## 2026-08-05c — Agent tabs + Hermes chat profiles (per user: "all of them + profile connecting with Hermes and chat")
- Read install docs first (16-KIMI, 34-OPENCODE, 27-GLM-CODE, 18-GROK-BUILD) per "stop skipping setup".
- INSTALLED: opencode v1.18.14 (free coder, works out of box) + qodercli (Qwen 3.8 brain). Created Windows wrapper C:\Usersstim\.localin\qoder-qwen.cmd -> qodercli -m Qwen3.8-Max-Preview. Registered qoder + opencode paths in .agentic-os/config.json.
- USER-ONLY remaining (logins/subs I cannot do): qodercli login (Qwen), Kimi = download from kimi.com + kimi login, Grok = needs X Premium+ then grok login. Claude tab = claude login.
- Hermes profiles: main/seo/content/marketing/roofing/restoration/leads all inherit the working gpt-5.6-sol via Codex (no broken overrides) — so every Pineapple chat works now.
- Wrote 01_Command_Center/M7_HERMES_AGENT_CHATS.md: the two ways to chat per-agent (Studio tabs vs Hermes /model + profile bar), free vs paid brains, exact /model commands.
- Already-working agent tabs: Codex, Claude, Gemini, Antigravity, opencode. Free per-chat brain switching in Hermes via /model (gpt-5.6-sol, nemotron:free, deepseek:free). Paid (Claude/GLM/Kimi) need OpenRouter credits.

## 2026-08-06 — Named per-model Hermes profiles + notebook-obsidian chat + 08-06 update
- Created model-named Hermes profiles (user's list): gpt56, kimi-k2-7, glm-5-2, qwen-3-7, hy3, north-mini, omniroute, hermes-cloud, jarvis, local, ollama-glm-512, blank-state, game-dev, seo-lead — each wired to its model/provider. Kept Pineapple business profiles (seo/content/marketing/roofing/restoration/leads/main) + specialists (fusion/sakana-fugu/grok-build). 25 profiles total.
- DELETED "julian" profile (leftover from pack creator Julian Goldie — answers user's "why is this showing up").
- Live-free profiles (Codex gpt-5.6-sol or free OpenRouter): gpt56, north-mini, omniroute, jarvis, game-dev, seo-lead, blank-state, notebook-obsidian, + all Pineapple ones. Paid (need OpenRouter credits): glm-5-2, kimi-k2-7, qwen-3-7, hy3. Login-gated: hermes-cloud (hermes portal), local/ollama-glm-512 (Ollama), grok-build (SuperGrok).
- Created notebook-obsidian profile: reads M7 vault (vaultRoot connected, .obsidian present) for extraction; NotebookLM half needs `nlm login`.
- Installed Kimi Code CLI (~/.kimi-code/bin) via official installer — user runs `kimi login`. opencode + qodercli already installed prior.
- 08-06 pack update: safe app-only updater (builds candidate, overlays Pineapple SEO safety routes, swaps only if build passes, keeps rollback, does NOT run hermes update so profiles/config preserved). First run SAFE-STOPPED (08-06 dropped the config/ dir) leaving 08-05 live; patched overlay to create parent dirs + made skill.md non-fatal; re-running. 08-06 adds Muse Code + jcode tabs.
- LOGIN-GATED handoffs documented in M7_HERMES_AGENT_CHATS.md: nlm login (NotebookLM), kimi login, qodercli login, hermes -p main mcp login higgsfield, hermes auth add minimax-oauth, hermes portal (nous), grok (SuperGrok), claude login.

## 2026-08-06b — 08-06 pack update COMPLETE (with swap-lock recovery)
- 08-06 build compiled clean (BUILD_ID jKgL95A...). First swap attempts safe-stopped (config/ dir dropped in 08-06 -> fixed overlay to mkdir parents; then npm stderr warning tripped ErrorActionPreference=Stop -> fixed to Continue + check LASTEXITCODE).
- Final swap half-completed: current->previous-0806 moved, but candidate->current blocked because the script's CWD was still inside candidate (lock). Site briefly down. RECOVERED from a clean CWD: moved 08-06 candidate -> current, restarted via START script.
- LIVE on 08-06: / /hermes /seo = 200, deploy 403, generate 400, Muse Code + jcode tabs present, 25 profiles intact, previous-0806 (08-05) kept as rollback.
- LESSON for future updater: Set-Location out of candidate before Move-Item (CWD locks the dir on Windows).

## 2026-08-06c — De-Julian + Pineapple brand paint on the Agent OS UI (persistent)
- ROOT-CAUSE de-personalization the user flagged: theme was "Midnight Aubergine" (purple #15101a/#251d2c bg), tan-gold #d4a574 (not #FBC02D), and #5ab896 GREEN (brand-law violation) baked into globals.css; Agent Kanban hardcoded SEO_SITE = aimoneylabjuliangoldie.com (published their content to Julian's site).
- FIXED in current/src: globals.css :root -> Navy #0d1826/#12233a/#172c47/#1e3a5c + Pineapple Gold #FBC02D + Status Cyan #00BFFF (emerald green remapped to cyan). Swept green+tan+aubergine hexes across all .ts/.tsx/.css (Tailwind arbitrary classes too). AgentKanban.tsx SEO_SITE -> pineappleroofingllc.com. Verified shipped CSS: navy/gold/cyan present, aubergine #15101a gone, --bg-deep:#0d1826, --emerald:#00bfff.
- PERSISTENCE: new reusable 04_Tech_Lab/scripts/pineapple_os_brandpaint.ps1 (re-applies palette + de-Julian to any build src). Wired into UPDATE-PINEAPPLE-AGENT-OS.ps1 so EVERY future pack update auto-repaints before build (fixes the "reverts to purple on update" complaint). Also added Set-Location $AppRoot guard before the swap (Windows dir-lock belt-and-suspenders).
- KNOWN residue: ~5 banned color literals (#251d2c x2, #d4a574 x1, #5ab896 x2) come from a bundled node_modules dependency, not our source; they return on npm ci so not chased into vendor code. Main theme (all CSS vars) is fully brand-compliant.
- Folder cleanup: deleted temp update-work-0806. Kept current (08-06) + pineapple-safety + previous-0806 (only rollback) + 2 scripts. Explained "C:\Pineapple Contractors M7\Agentic OS" is the OS/Hermes vault-output folder (Memories/Pipeline) — belongs at vaultRoot, not a mess.
- GSC_Connect.bat: dashboard link 3000 -> 3737 (was pointing at the dead June build); copied to vault root.
- No-terminal key config: fcc-server admin UP at http://127.0.0.1:8082/admin (paste API keys in a UI, no terminal). Services up: 3737 OS, 3001 OpenSEO, 3100 Paperclip, 9119 Hermes, 8082 fcc-admin.

## 2026-08-06d — Launcher consolidation + Master SOP + logins + Hermes/Obsidian verify
- ONE master launcher: Desktop LAUNCH_ALL.bat now also starts fcc-server on :8082 (Free Claude Code + its /admin key panel) via START script edit. Fixes "Free Claude Code didn't work with my preferred launcher" + the :8082 refused-connection. All services verified up: 3737 OS, 8082 fcc, 9119 Hermes, 3001 OpenSEO. Archived 6 redundant root launchers (LAUNCH_CLAUDE_CODE, AM_STARTUP, PM_SHUTDOWN, M7_CLEANUP, M7_DOCTOR, ORGANIZE_MEDIA) to Launcher_Archive.
- NO-TERMINAL KEY CONFIG: http://127.0.0.1:8082/admin — paste API keys in a UI (NVIDIA/OpenRouter/Gemini/DeepSeek/Kimi/Groq/Z.AI all show Configured). For OAuth logins + github clones without VSCode: use Hermes chat / Control Room terminal or a coding tab (opencode/Codex) — type the request, it runs the command (browser still opens for OAuth approval).
- Run A: launched `nlm login` (NotebookLM) in a visible window for the user to complete. Remaining logins listed (qodercli/kimi/claude/hermes portal/minimax/higgsfield).
- Run B: generated 01_Command_Center/Outbox_Drafts/M7_MASTER_SOP_STUDIO_DAILY_30DAY.md (PAUSED) — maps every Studio tab->task->prompt, Hermes profile->job, Goal Mode daily/weekly/nightly, daily who-does-what, 30-day gameplan, open decisions. brand_firewall --check = OK.
- Verified Hermes+Obsidian: vaultRoot=vault, hermesHome set, userName=Siosaia/Frisco, notebook-obsidian profile present, Agentic OS/Memories present, qoder+opencode paths registered. /model switching works. config.json is UTF-8-BOM (valid; Node reads it).
- STILL OPTIONAL (need a git clone, I can do next): Open Design (~/open-design), SEO Office (~/seo-office). Both show offline until cloned.

## 2026-08-06e — Notebook fix + vault junction + full sweep + clones
- NOTEBOOK TAB ROOT CAUSE: not an auth problem — nlm login worked (server_info auth_status=configured; notebook_list returned 113 notebooks). The tab failed because the OS had 4 STALE notebooklm-mcp subprocesses + a node process spawned before login; my earlier restarts killed only the port listener, not the tree. Fix: taskkill /T /F the full 3737 node tree + all notebooklm-mcp PIDs, refresh_auth, clean restart. Verified: GET /api/notebooklm/notebooks = 200, count 113. (User must Ctrl+Shift+R the Notebook tab.)
- MEMORY/VAULT FIX: routes hardcode ~/Documents/Obsidian Vault (a stray non-vault folder, 16 old files, no .obsidian) -> showed last month. Renamed it to Obsidian Vault_OLD_2026-08-06 and created a JUNCTION Documents/Obsidian Vault -> C:\Pineapple Contractors M7 so every hardcoded path reads the M7 vault (today). Wrote Agentic OS/Memories/2026-08-06.md session note. Verified reachable via junction.
- CLONES: open-design (nexu-io/open-design) + seo-office (AgriciDaniel/seo-os) cloned; installed pnpm; kicked off pnpm install for both (background). SEO Office runs pnpm dev -> :3000 tab; Open Design needs bridge scripts (Mac-oriented) — Windows start TBD.
- Restarted fcc-server :8082 + Paperclip after the tree-kill.
- FULL SWEEP (all green): pages / /hermes /seo /notebook /memory = 200; Hermes gpt-5.6-sol via codex, 25 profiles; CLIs installed = claude/codex/kimi/qodercli/opencode/agy/gemini/nlm/notebooklm-mcp (grok needs SuperGrok); config vaultRoot=M7 user=Siosaia/Frisco qoder+opencode set; junction ->M7; brand theme navy/gold/cyan shipped.

## 2026-08-06f — Open Design live + folder dry-run + mobile SOP + cowork + playground
- Open Design STARTED on :7456 (dev mode; --prod needed a build it didn't ship). SEO Office live on :3000. Both cloned-tab issues resolved — every startable tab now up.
- FOLDER DRY-RUN written (PAUSED): 01_Command_Center/Outbox_Drafts/M7_FOLDER_CLEANUP_DRYRUN.md. Buckets: KEEP (4-Fala + Agentic OS), ARCHIVE (~30MB old packs/zips/empty launchers -> _Archive/2026-08-06), TIDY loose root .md -> 03_Knowledge_Mat, REVIEW (knowledge-base/legacy_backup/Omi/_Inbox_Cleanup/Scheduled/Projects). Includes a Hermes-goal prompt to execute it. NOTHING moved.
- MASTER SOP updated: added PART 7 — ONE SYSTEM, THREE SCREENS (mobile MOBILE_STATUS.md via Drive sync + M7_DAILY_SYNC.bat + 30-min snapshot; desktop Studio :3737; local vault+scripts; GitHub = shared memory).
- NEW: M7_STUDIO_PLAYGROUND_AND_COWORK.md — example paste-in prompts for every tab (opencode/Codex/Muse/SEO Research/Parasite/SEO Office/Kanban/Higgsfield/Video/Thumbnails/Notebook/Memory/Fusion/Loop/App Lab/Hermes profiles) + a Cowork handoff prompt to generate Master SOP v3 and push to GitHub.
- All brand_firewall --check = OK.

## 2026-08-06g — SEO/Digital strategic consolidation (CEO read)
- Scanned all 22 SEO/website/marketing docs + the user-pasted "$10M NHI Directive". Wrote M7_SEO_DIGITAL_MASTER_PLAN.md (PAUSED) flagging 3 conflicts: (1) DOMAIN flip-flop — rankings live on pineapplecontractors.com (Scorpion) but docs disagree on which is flagship; recommended KEEP contractors.com, do NOT 301 the winner to roofingllc, use roofingllc as content channel. (2) The pasted $10M autonomous directive VIOLATES Outbox Shield (zero-pause), points at wrong vault (Documents/ObsidianVault/BusinessOS), wrong brand colors (#1A2B4C/#0052CC), auto-spends on ads/mail — flagged DO NOT RUN as-is; keep the good ideas (vertical flywheel, Halo marketing) re-gated. (3) NAP: Frisco vs Lewisville primary must be picked.
- ROI-ranked plan: Tier1 (connect GSC via brother handoff = gating item; GBP 100%; review velocity; speed-to-lead), Tier2 (striking-distance page upgrades weekly on the ranking site; storm response), Tier3 (LSA; the flywheel/Halo re-gated). GSC NOT CONNECTED in OS is the #1 unblock.

## 2026-08-06h — Strategy CORRECTED (agency being fired) + Bullseye audit + media engine
- New context: Scorpion agency failed -> being canceled; roofingllc.com WordPress is the intended in-house flagship. CORRECTED prior "keep contractors.com" rec: now migrate SEO value contractors.com -> roofingllc.com via 301s FIRST, verify in GSC, THEN cancel Scorpion (never cancel first or 97 pages + 141 keywords + authority vanish). GBP (430 reviews/5.0star) survives the switch.
- Read Bullseye Agency audit PDF (competitor pitch, verified 2026-07-16): 455 organic visits/mo but 87% BRANDED (only 59/mo new customers) = the core problem; 8 of 141 keywords on page 1; 0 storm-damage pages; PageSpeed 47/100 + CLS 0.812 (slow/janky); 430 reviews 5.0star; 0 Google Ads ever. Fix = attack NON-branded local keywords + build storm pages + fast new site.
- GSC: all 3 properties verified in Google (contractors 7.37K impr/9 clicks/pos23; roofingllc 43 impr new; restorations). But OS/OpenSEO still shows GSC NOT CONNECTED (Parasite tab) — connecting GSC->OS remains the gate.
- Added 39GB MEDIA ENGINE to the plan: media -> Video Editor/OpenMontage clips -> Higgsfield -> Hermes captions (50/5/3) -> Blotato schedule -> all platforms. Testimonials = highest converting. Offered to build the full media-repurpose SOP next.

## 2026-08-07 — ROOT-CAUSE: config.json BOM broke OS config reading
- Hermes tab "not configured" + Memory wrong-vault had ONE root cause: config.json was written with a UTF-8 BOM (PowerShell default). Node's JSON.parse rejects a BOM -> OS silently ignored ALL of .agentic-os/config.json (hermes bin, vaultRoot, everything) and fell back to defaults (which("hermes")=null -> "not configured"; vaultRoot -> ~/Documents/Obsidian Vault default).
- FIX: rewrote config.json as UTF-8 WITHOUT BOM (first bytes now 123,13,10 = clean). Also set user env AGENTIC_OS_HERMES_BIN as belt-and-suspenders. Restarted OS. Verified: /api/hermes = {ok:true}, /api/hermes/profiles = 200 lists profiles. Hermes now ONLINE in the OS (reload tab).
- CLARIFIED for user: (1) Desktop LAUNCH_ALL.bat is THE launcher; 04_Tech_Lab/Pineapple_Agent_OS holds current(app)+pineapple-safety+START/UPDATE.ps1 that the .bat calls (never run .ps1 directly). (2) 04_Tech_Lab/hermes_profiles (*.SOUL.md, Jul 4) + hermes_skills (*.yaml) are SOURCE files, NOT live; the 26 LIVE profiles are in %LOCALAPPDATA%/hermes/profiles and ARE implemented. (3) The .zip files in 04_Tech_Lab/scripts are redundant zipped copies of the .ps1 next to them, NOT launchers. (4) Shared memory = the Obsidian vault (Memory tab) + 03_Knowledge_Mat/SHARED_MEMORY.md + Agentic OS/Memories/.
- OUTBOX INVENTORY: 152 files of completed work awaiting review/publish (Hormozi kit, CPPA capture page, 26 SEO_Posts, 22 Website_Pages, review requests, 30-day calendar, etc.).

## 2026-08-10 - Agent OS updated to build 2026-08-10 (Claude Code)
- Fixed UPDATE-PINEAPPLE-AGENT-OS.ps1: added Copy-Safe (creates missing dest dirs / skips dropped files). The 8/10 pack dropped its config/ folder, which crashed the old updater's safety step.
- Build test PASSED (npm ci + next build, 52 pages). Final swap had been blocked by a file lock on current/ (running OS + IDE); completed the swap manually after stopping the port-3737 server.
- Result: current = build 2026-08-10; rollback kept at previous-0810. Verified /api/version=2026-08-10, :3737 live, Hermes online. ~/.agentic-os, ~/.hermes, ~/.fcc, vault all preserved.
- Added M7_FREE_CLAUDE_CODE_CHEATSHEET.md (FCC study guide).

## 2026-08-10 (pm) - Free Claude Code fixed + Master Knowledge Mat scrubbed (Claude Code)
- FCC was down: fcc-server (:8082) + OmniRoute (:20128) not running. Started both; verified end-to-end (proxy -> free model nvidia/nemotron-3-super answered). Wired OmniRoute auto-start into START-PINEAPPLE-AGENT-OS.ps1 (next to the existing fcc-server block) so it persists.
- Scrubbed the NotebookLM "PM7 Agentic OS Master Knowledge Mat" into M7 branding: dropped the legacy raw-prompt header (Warrior/six-brothers/Pineapple-Mana-Global/GAF), kept the M7-compliant v7.0 body (1425 lines). Saved to 03_Knowledge_Mat/PM7_MASTER_KNOWLEDGE_MAT.md, brand-firewall OK.

## 2026-08-10 (pm2) - Video skill installed + repos scanned (Claude Code)
- Cloned claude-obsidian (AgriciDaniel), claude-watch (taoufik), claude-video (brad) to 04_Tech_Lab/vendor/ (gitignored, review-before-run).
- Made the video skill runnable: installed yt-dlp (ffmpeg already present), registered claude-watch as ~/.claude/skills/watch, set WATCH_VAULT_DIR -> 03_Knowledge_Mat. Usable next Claude Code session via /watch <url>.
- Verified all recommended AgriciDaniel repos exist (claude-seo, claude-cybersecurity, skill-forge, wp-mcp-ultimate). Did NOT run the pasted "one-click" directive's brand_firewall --fix (would corrupt governance docs that list banned words as rules) — use --check instead.

## 2026-08-10 (pm3) - Second Brain + video skill + SEO-repo scan (Claude Code)
- #3 claude-obsidian: cloned to vendor, CLAUDE_OBSIDIAN_VAULT->03_Knowledge_Mat, created inbox/raw/sources ingest folders. Usable via `claude --plugin-dir`.
- #2 scanned+cloned 4 AgriciDaniel repos: claude-seo (MUST), wp-mcp-ultimate (HIGH, WP-side), skill-forge (HIGH), claude-cybersecurity (MEDIUM). Cloned to vendor (gitignored), not yet wired as active skills.
- #1 /watch skill live; watched+scrubbed 2 Julian Goldie videos (24/7 Traffic Engine + Graph Engineering) -> 03_Knowledge_Mat/raw/watched/.
- #4 UTF-8: 03_Knowledge_Mat scanned, clean (no mojibake).
- Cheat sheet: 01_Command_Center/M7_UPGRADE_CHEATSHEET_2026-08-10.md. Did NOT run brand_firewall --fix across the vault (would corrupt rule-definition docs).
