---
type: sop_update
title: M7 SOP Update — Agent OS 2026-07-13 (new tabs, key-protection, build version)
status: paused
date: 2026-07-13
author: JR. Moeakiola
supersedes: nothing — additive patch on top of M7_MASTER_SOP.md v1.0 (2026-06-27)
applies_to: Pineapple Contractors M7 Agent OS (agent-os-pack 2026-07-13)
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🍍 M7 SOP UPDATE — 2026-07-13

> **⏸ PAUSED — INTERNAL DOCUMENT, NOT FOR PUBLISH.**
> This is a vault SOP / agent operating patch. It does not get posted, sent,
> scheduled, or spent. Saia approves any future roll-in into
> `01_Command_Center/M7_MASTER_SOP.md`. Until then, treat this file as the
> source of truth for the 07-06 → 07-13 changes.
>
> Author byline: **JR. Moeakiola** · RCAT License #03-0637 · IKO Certified · 5-Star · Since 2005 · 972-928-0788

## 0. WHY THIS FILE EXISTS

The third-party **Agent OS** pack (lives in our vault at
`03_Knowledge_Mat/00_Atlas/templates/agent-os-pack-2026-06-29/` and the
newer `source/member-pack/` build at 2026-07-13) shipped seven things
between 2026-07-06 and 2026-07-13 that change how we run the Pineapple
marketing engine. This SOP folds them into the M7 workflow **without**
breaking brand law or the Outbox Shield.

| # | Change (date) | Why it matters to M7 |
|---|---|---|
| 1 | **Hy3 Coder** tab (2026-07-07) | Cheap, fast one-shot build (Tencent Hy3 via OpenRouter). A few cents a build. |
| 2 | **Video Editor** tab (2026-07-08) | Chat-edit a clip → `final.mp4`. Replaces most of what we hand-FFmpeg'd. |
| 3 | **SEO Office** guide (2026-07-08) | Local SEO agency OS as a sub-tab in SEO; clone + `pnpm dev`. |
| 4 | **"Connect Everything" SETUP-GUIDE** (2026-07-08) | One-sentence AI wiring for every key. |
| 5 | **Build version** shown under the logo (2026-07-08) | At-a-glance check we're on the latest pack. |
| 6 | **Grok Build on grok-4.5** (2026-07-09) | Stronger builds, same X Premium+ login. |
| 7 | **Updates now protect keys/config** (2026-07-09) | `.env`, `.env.local`, `agentic-os.config.json` no longer wiped on update. |
| 8 | **Build Guide tab REMOVED** (2026-07-09) | Sidebar cleanup. |
| 9 | **Thumbnail Studio auto-researches + designs 6 thumbnails** (2026-07-13) | Set `"youtubeChannel"` in `~/.agentic-os/config.json` for channel-tuned research. |

Lexicon discipline still applies to **every customer-facing surface** the
new tools can produce (thumbnails, video captions, on-screen text, SEO
copy, blog posts): **CPPA** not "free", **IKO Certified (RCAT #03-0637)**
not "GAF", **The Pineapple Standard** not "warrior/Toa", **$0 → Full
Restoration Coverage**, **green is banned**.

## 1. THE FIVE RULES THAT STILL NEVER CHANGE

Reaffirmed from `M7_MASTER_SOP.md` §0 — every change below is filtered
through them:

1. **Outbox Shield (DEC-005):** thumbnails, video files, captions,
   blog posts, ad creatives — anything that could reach a customer —
   lands **PAUSED** in `01_Command_Center/Outbox_Drafts/`. Never publish,
   post, send, schedule, or spend (ad budget, paid-API credits) without
   Saia's explicit GO. Agents never call publish/send/post APIs directly.
2. **Never restructure folders** or delete files unless Saia says so.
   Move/clean only via the launchers.
3. **Brand lexicon** (regex gate before any file is written). Banned in
   customer-facing copy: `free`/`free inspection`/`free quote`,
   `$0 down`/`$0 out of pocket`, `cheap`/`bargain`/`discount`,
   `save money`, `GAF`/`GAF Certified`, `warrior`/`toa`/`six brothers`,
   `repair patch`, `shingle repair cost`, `DIY`, `discount code`,
   `job openings`, `salary`. Required mutations live in
   `04_Tech_Lab/scripts/brand_firewall.py`.
4. **No green** anywhere. Palette: Royal Navy `#1A365D`, Pineapple Gold
   `#FBC02D`, Status Cyan `#00BFFF`.
5. **Verify, don't hallucinate.** Run `brand_firewall.py --check` before
   staging. If a fact isn't sourced, flag it. Identity: Polynesian-owned,
   RCAT #03-0637, IKO Certified, since 2005, 972-928-0788.

## 2. THE TOOL MAP (M7, post-2026-07-13)

| Tool / Tab | What it does | Pineapple fit (M7 brand A vs B) | Spend | Status |
|---|---|---|---|---|
| **Hy3 Coder** *(new 07-07)* | One-shot single-file build (Tencent Hy3 via OpenRouter). Streams a small page/app in 60–180s. | Brand A & B landing-page micro-iterations (CPPA variants, ZIP micro-pages). **Outbox → Saia GO → publish.** | A few cents / build (OpenRouter pay-as-you-go) | Optional. `install/31-HY3-CODER.md` |
| **Video Editor** *(new 07-08)* | Upload clip → describe edit in chat → `final.mp4` out. Powered by `video-use` skill + ffmpeg. | Brand A **reels / shorts** (50/5/3 Lego cut-downs, hail-claim walkthroughs); Brand B **emergency-mitigation** before/after. Drafts → `01_Command_Center/Outbox_Drafts/Scripts/`. | Free (local ffmpeg) | Optional. `install/33-VIDEO-EDITOR.md`. Needs `video-use` skill + `brew install ffmpeg` (Mac) / `winget install ffmpeg` (Windows). |
| **SEO Office** *(guide 07-08)* | 3D-office "SEO agency in a box" with claude-seo specialist agents. Sub-tab in **SEO**. | AEO/GEO engine for ZIP 75033/75034/75035/75067/75068 city pages. | Free (local) | Optional, advanced. `install/32-SEO-OFFICE.md` — `git clone https://github.com/AgriciDaniel/seo-os ~/seo-office && pnpm install && pnpm dev`. |
| **SETUP-GUIDE** ("Connect Everything") *(new 07-08)* | One-sentence AI wiring for every model/tool/API. | Onboarding new agents to the M7 vault. | Free | Recommended. Paste: *"Read SETUP-GUIDE and set up my whole Agent OS. Go tab by tab…"* |
| **Build version (under logo)** *(new 07-08)* | Shows `build <date>` so we can tell at a glance if we're current. | Operationally, confirms we're on `2026-07-13` (or newer). | Free | Read-only. |
| **Grok Build on grok-4.5** *(upgrade 07-09)* | xAI's `grok-build` CLI coding agent — same tab, stronger model. | Build internal tools (lead-scoring dashboard, brand_firewall wrappers). | Requires **X Premium+ (SuperGrok)**. No per-message cost. | Optional. `install/18-GROK-BUILD.md`. |
| **Key/config protection on update** *(fix 07-09)* | All four update paths now explicitly protect `.env`, `.env.local`, `agentic-os.config.json`. | **Stops us losing** `OPENAI_API_KEY` (Thumbnail Studio) and the `youtubeChannel` setting on update. | Free | Already on. Keep settings in `~/.agentic-os/config.json` (lives outside the app folder, never touched). |
| **Build Guide tab** *(REMOVED 07-09)* | Was an in-app how-to guide. | None — clean uninstall. | — | Removed. Use `install/0-HOW-IT-ALL-WORKS.md` instead. |
| **Thumbnail Studio auto-research + 6 designs** *(new 07-13)* | Give it a topic → live-searches what's winning on YouTube → designs 6 thumbnail concepts. Set `"youtubeChannel"` in `~/.agentic-os/config.json` for channel-tuned research. | **YouTube content for Brand A** (hail/wind/insurance walkthroughs) and **Brand B** (fire/water/mold emergency explainers). Generate → Outbox → Saia picks the best → upload. | ~$0.04 / image (OpenAI gpt-image-2). 6 designs ≈ $0.24 / round. | Recommended. `install/10-THUMBNAIL-STUDIO.md`. Set `"youtubeChannel"` in `~/.agentic-os/config.json` once (e.g. `@pineapplecontractors` — confirm actual handle before writing the key). |

## 3. WHAT EACH NEW TOOL DOES (the long answer)

### 3.1 Hy3 Coder (new tab, 2026-07-07)

Source: `03_Knowledge_Mat/00_Atlas/templates/agent-os-pack-2026-06-29/source/member-pack/install/31-HY3-CODER.md`.

- **Model:** Tencent **Hy3** (Hunyuan 3, Apache-2.0) via **OpenRouter**.
- **What it does:** describe what you want in plain English; it streams a
  full **single-file** build on the right pane. You copy or download.
- **Best for:** one-shot small pages and snippets. For long multi-step
  work use Claude / Free Claude Code; for $0 builds use **OmniRoute**
  or the local model.
- **Pineapple use:** rapid-fire CPPA landing variants (e.g.
  "Frisco hail CPPA v3, Navy hero, gold CTA, one file"). Output file →
  Outbox_Drafts → run `brand_firewall.py --check` → Saia reviews → Saia
  publishes. **Never** push directly to
  pineapplecontractors.com / pineapplerestorations.com.
- **Cost guardrail:** a few cents per build via OpenRouter. Set a
  per-session cap in `OPENROUTER_*` config; agents do not auto-charge.
  If we exceed **$5/week** on Hy3 alone, pause and re-evaluate.

### 3.2 Video Editor (new tab, 2026-07-08)

Source: `…/install/33-VIDEO-EDITOR.md`.

- **What it does:** upload a video → chat *"cut the dead air, add
  subtitles, punch up colour, end on the CPPA CTA"* → download
  `final.mp4`.
- **Powered by:** the `video-use` skill running through your coding
  agent (Claude Code, or GLM Code runner) + **ffmpeg** on your box.
- **Pineapple use (Brand A — Pineapple Roofing):** repurpose the long
  hail/insurance walkthrough into 50/5/3 Lego cuts (50s total, 5s hook,
  3s end card — Navy + Gold + **972-928-0788**).
- **Pineapple use (Brand B — Pineapple Restorations):** emergency
  rapid-response before/after, water-damage mitigation reel. Brand B
  copy only — never cross-contaminate with roofing claims.
- **Required install (one-time):**
  - `brew install ffmpeg` (Mac) or `winget install ffmpeg` (Windows).
  - `video-use` skill for the coding agent you drive.
- **Output:** `final.mp4` lands in your Workspace → **move** to
  `01_Command_Center/Outbox_Drafts/Scripts/YYYY-MM-DD_Video_*.mp4` →
  Saia uploads + posts. **Agents never upload to YouTube/Instagram/TikTok.**

### 3.3 SEO Office (new guide, 2026-07-08)

Source: `…/install/32-SEO-OFFICE.md`.

- **What it is:** a 3D-office "SEO agency in a box" UI with
  claude-seo specialist agents. Sits as a sub-tab inside the **SEO**
  section. Separate open-source project, AGPL-3.0; **not bundled**.
- **Install (one-time):**
  ```bash
  git clone https://github.com/AgriciDaniel/seo-os ~/seo-office
  cd ~/seo-office && pnpm install
  cd ~/seo-office && pnpm dev     # serves on http://localhost:3000
  ```
  Then Agent OS → **SEO → SEO Office** embeds it when the badge shows
  *running*.
- **Pineapple use:** the **AEO/GEO engine** already called for in
  `HERMES_PLAYBOOK.md` §"LOCAL SEO / GEO ENGINE" — answer the query in
  the first 40 words, inject "RCAT Licensed #03-0637" + "IKO Certified",
  tag ZIPs 75033/75034/75035 in schema arrays. SEO Office is where we
  draft the city/cluster pages, FAQ schema, and citation-bait assets.
- **Coexistence:** sits alongside **OpenSEO** (DataForSEO-backed
  keyword/rank tool) and **SEO → Transcripts** (paste a YouTube
  transcript → SEO article). All three are optional; pick whichever
  is wired.

### 3.4 "Connect Everything" SETUP-GUIDE (new 2026-07-08)

Source: `…/source/member-pack/SETUP-GUIDE.md`.

- **What it is:** the canonical how-do-I-wire-everything doc. Leads
  with the easy path (paste one sentence to Claude/Hermes), then a
  reference table of which key unlocks which tab + where to get it.
- **M7 application:** when onboarding a new box or a new agent, paste:
  > *"Read SETUP-GUIDE and set up my whole Agent OS. Go tab by tab.
  > For each model, tool and API, tell me what it does and whether I
  > need a paid key — and if I do, give me the exact link to get it,
  > wait for me to paste it, then wire it into the right place and
  > confirm it works. Never enter my card or do a login for me."*
- **Key table (filtered to M7-relevant tabs):**

  | Tab | Key it needs | M7 use |
  |---|---|---|
  | **Hermes / Fusion / OmniRoute / Hy3 Coder** | `OPENROUTER_API_KEY` (many `:free` models) | Hermes orchestration + Hy3 cheap builds |
  | **Jarvis voice / TTS** | `ELEVENLABS_API_KEY` (free tier) | Optional — on-hold messaging, video VO |
  | **Thumbnail Studio** | `OPENAI_API_KEY` (paid, cheap; separate from ChatGPT Plus) | YouTube thumbnails — set in `~/.claude/skills/youtube-thumbnails/.env` |
  | **Video Studio (avatars)** | `HEYGEN_API_KEY` (paid) | AI talking-heads — only if we adopt avatars |
  | **Grok Build** | none (X Premium+ / SuperGrok login) | Internal tool builds |
  | **Free Claude Code / OmniRoute / Local** | none | $0 builds |
  | **SEO → OpenSEO** | `DataForSEO` key in `~/open-seo/.env` (paid, cheap) | Rank tracking + keyword research |

  > 💡 All Hermes-routed keys live in `~/.hermes/.env`; a few tools
  > have their own place. **Let the AI put them there** — that's the
  > whole reason the easy path exists.

### 3.5 Build version under the logo (new 2026-07-08)

- **What it shows:** `build <date>` under the "Agentic OS" logo.
- **M7 use:** glance at the dashboard top-left; if it's older than the
  newest pack on the Boardroom, run `Update Agent OS.command`. Today
  the target is **2026-07-13**.
- **On Windows (our box):** the `.command` double-click updater is
  Mac-only. Use `UPDATE-WITH-AI.md` (cross-platform, any agent) or the
  PowerShell path in `UPDATE.md`.

### 3.6 Grok Build on grok-4.5 (upgrade 2026-07-09)

Source: `…/install/18-GROK-BUILD.md`.

- **What changed:** the `grok-build` tab now runs on **grok-4.5**
  (was older Grok). Same X Premium+ (SuperGrok) login, same tab,
  stronger code outputs.
- **M7 use:** build internal tools (lead-scoring widget, brand-firewall
  wrappers, Kanban card generators). Outputs land in the **Workspace**
  tab; we review then move useful ones into the vault. **Never** expose
  Grok-built tools to customers without a Saia pass.
- **Sign-in (one-time):** `grok login --device-auth`. Lives inside the
  `grok` CLI — no key gets pasted into any config file.

### 3.7 Key / config protection on update (fix 2026-07-09)

- **What it means:** `.env`, `.env.local`, and `agentic-os.config.json`
  are no longer deleted by the updater across **all four** update paths
  (Mac `.command`, Windows PowerShell, the AI updater, manual rsync).
- **M7 use:** this is the fix that keeps our `OPENAI_API_KEY` (Thumbnail
  Studio) and any future `youtubeChannel` setting from disappearing on
  every update.
- **Discipline (re-stated):** keep settings in
  `~/.agentic-os/config.json` (lives **outside** the app folder, never
  touched). If a fix lives in source code, hand it upstream so it
  ships for everyone and survives updates.

### 3.8 Build Guide tab REMOVED (2026-07-09)

- **What it means:** the in-app "Build Guide" tab is gone from the
  sidebar. No action — read `install/0-HOW-IT-ALL-WORKS.md` instead.

### 3.9 Thumbnail Studio auto-research + 6 designs (new 2026-07-13)

Source: `…/install/10-THUMBNAIL-STUDIO.md` + CHANGELOG 2026-07-13.

- **What's new:** the Thumbnails tab now **live-searches** what's
  winning on YouTube right now for your topic, then designs **6
  distinct thumbnail concepts** (faceless, or with your own photo).
- **Required setup (one-time):** set `"youtubeChannel"` in
  `~/.agentic-os/config.json` for channel-tuned research. Example:
  ```json
  {
    "youtubeChannel": "@pineapplecontractors",
    "userName": "JR. Moeakiola"
  }
  ```
  > ⚠ **Verify the actual channel handle** before writing the key.
  > If we have not published to YouTube yet, set the field once we
  > do. If multiple brands, we may run two configs (Brand A
  > roofing, Brand B restorations) — confirm with Saia first.
- **Pineapple use (M7 content engine):**
  - **Brand A — Pineapple Roofing** thumbnails for: "Hail damage in
    Frisco — what to do in 7 days", "IKO Certified vs uncertified
    roofers", "Insurance claim denied? Full Restoration Coverage",
    "Thermal-shock warning signs", "CPPA walkthrough".
  - **Brand B — Pineapple Restorations** thumbnails for: "Water
    damage first 24 hours", "Mold remediation Frisco", "Fire &
    smoke documentation", "Biohazard cleanup".
  - All thumbnails must use the **Navy `#1A365D` + Gold `#FBC02D`
    + Cyan `#00BFFF`** palette. **No green.** Verify with
    `brand_firewall.py --check` before staging.
- **Output → Outbox:** every generation is logged to the Obsidian
  vault under `Thumbnails/`. Move the chosen PNG into
  `01_Command_Center/Outbox_Drafts/Content/YYYY-MM-DD_Thumbnail_*.png`
  and stage PAUSED. Saia picks the best, writes the final title
  overlay (legible, Navy or Cyan text, **972-928-0788** on every
  end card for paid Brand-A assets), and uploads to YouTube.

## 4. UPDATE THE TOOL MAP (delta on top of `M7_MASTER_SOP.md` §2)

> Apply this table **on top of** the existing `M7_MASTER_SOP.md` §2
> FILE MAP — do not delete rows. Reordering is fine; deleting is not.

| File / Tab | What it is | Change |
|---|---|---|
| `source/src/app/hy3-coder/page.tsx` + `components/Hy3CoderView.tsx` | Hy3 Coder tab UI | **NEW** (07-07). Cheap one-shot build via OpenRouter. |
| `source/src/lib/videouse.ts` + `components/VideoUseView.tsx` + `install/33-VIDEO-EDITOR.md` | Video Editor tab | **NEW** (07-08). Chat-edit video → `final.mp4`. |
| `source/src/components/SEOView.tsx` + `install/32-SEO-OFFICE.md` | SEO → SEO Office sub-tab | **NEW** sub-tab + guide (07-08). Local 3D SEO agency; clone + `pnpm dev`. |
| `source/member-pack/SETUP-GUIDE.md` | "Connect Everything" doc | **NEW** (07-08). One-sentence AI wiring + key table. |
| `source/src/app/api/grok/chat/route.ts` + `install/18-GROK-BUILD.md` | Grok Build tab | **UPGRADED** (07-09). Now on `grok-4.5`. |
| Update pipeline (`.command`, `UPDATE-WITH-AI.md`, PowerShell path, manual rsync) | All four update paths | **FIXED** (07-09). Protect `.env`, `.env.local`, `agentic-os.config.json`. |
| `install/10-THUMBNAIL-STUDIO.md` + `source/src/lib/thumbnailPrompt.ts` + `source/src/lib/thumbnailLog.ts` | Thumbnail Studio | **UPGRADED** (07-13). Auto-research + 6 designs; honours `"youtubeChannel"`. |
| `config.example.json` | `~/.agentic-os/config.json` template | **NEW key**: `"youtubeChannel"` (string, channel handle or URL). Survives updates because it lives outside the app. |
| Sidebar — **Build Guide** entry | In-app how-to tab | **REMOVED** (07-09). Use `install/0-HOW-IT-ALL-WORKS.md`. |
| Top-bar build version (under "Agentic OS" logo) | `build <date>` chip | **NEW** (07-08). Glance-check. |
| `~/.agentic-os/config.json` (user-side) | Settings | **Action:** add `"youtubeChannel"` once the YouTube handle is confirmed. |

## 5. NEW SOPs THIS UPDATE ADDS

> These slot into `M7_MASTER_SOP.md` §4 alphabetically when Saia
> rolls this patch in. They are PAUSED until then.

### SOP-V · Pineapple Reel (50/5/3 Lego cut) via Video Editor

```
Read 01_Command_Center/M7_SOP_UPDATE_2026-07-13.md §3.2.
Take [source long-form video]. Use the Video Editor tab.
Cut to 50s total at 30fps. First 5s = hook (Navy background, Gold
text, the question). Middle 42s = body (CPPA + IKO Certified + RCAT
#03-0637). Last 3s = end card (Navy, Gold CTA, 972-928-0788).
Subtitles on. Export final.mp4. Stage PAUSED to
01_Command_Center/Outbox_Drafts/Scripts/YYYY-MM-DD_Video_*.mp4.
Run brand_firewall.py --check on any on-screen text. Never upload.
```

### SOP-T · Thumbnail Studio batch (YouTube, 6 designs)

```
Read 01_Command_M7_SOP_UPDATE_2026-07-13.md §3.9.
Open the Thumbnails tab. Topic: [e.g. "Hail damage Frisco 7-day
checklist"]. Reference images: [logo + current thumbnail].
Hit generate. Take all 6 PNGs. Move the strongest into
01_Command_Craft/Outbox_Drafts/Content/YYYY-MM-DD_Thumbnail_*.png.
Stage PAUSED. Saia picks + uploads. Verify youtubeChannel is set
in ~/.agentic-os/config.json first.
```

### SOP-H · Hy3 micro-build (one-shot landing variant)

```
Read 01_Command_Center/M7_SOP_UPDATE_2026-07-13.md §3.1.
Open the Hy3 Coder tab. Prompt: [one-line brief — e.g. "CPPA
landing for Frisco 75034, Navy + Gold, one file, no JS"].
Wait for the stream. Copy the file into
01_Command_Craft/Outbox_Drafts/Website_Roofing/experiments/
YYYY-MM-DD_Hy3_*.html. Run brand_firewall.py --check. Stage PAUSED.
Never push to pineapplecontractors.com directly.
```

### SOP-S · SEO Office setup (one-time, then embed)

```
Read 01_Command_Center/M7_SOP_UPDATE_2026-07-13.md §3.3.
Run, in this order, on Saia's GO:
  git clone https://github.com/AgriciDaniel/seo-os ~/seo-office
  cd ~/seo-office && pnpm install
  cd ~/seo-office && pnpm dev        # leave running on :3000
Then in Agent OS: SEO → SEO Office → confirm "running" badge.
Draft AEO city pages (ZIP 75033/75034/75035) PAUSED into
01_Command_Center/Outbox_Drafts/SEO_Posts/. First 40 words answer
the query; inject "RCAT Licensed #03-0637" + "IKO Certified"; tag
the ZIPs in schema arrays.
```

### SOP-CG · "Connect Everything" — key wiring (one-time per box)

```
Read 01_Command_Center/M7_SOP_UPDATE_2026-07-13.md §3.4.
Open any coding agent (Hermes, Claude Code, Codex) in the agent-os
folder. Paste:
  "Read SETUP-GUIDE and set up my whole Agent OS. Go tab by tab.
   For each model, tool and API, tell me what it does and whether
   I need a paid key — and if I do, give me the exact link to get
   it, wait for me to paste it, then wire it into the right place
   and confirm it works. Never enter my card or do a login for me."
Agent walks every tab, asks for each key, wires it, confirms.
Brand Firewall check after wiring.
```

## 6. BRAND FIREWALL — SELF-CHECK (run before this file ships)

Run mentally against the **lexicon table** in
`HERMES_PLAYBOOK.md` §LEXICON and `M7_MASTER_SOP.md` §0.3:

- [x] No `free`, `free inspection`, `free quote`, `complimentary consultation`
  in customer-facing copy this update introduces. The Thumbnail Studio
  generator prompt is internal, not customer-facing.
- [x] No `$0 down`, `$0 out of pocket`. The `Full Restoration Coverage`
  phrase is reserved for Brand-B copy.
- [x] No `GAF` / `GAF Certified` anywhere — all references are
  `IKO Certified (RCAT #03-0637)`.
- [x] No `warrior` / `toa` / `six brothers` — all use
  `The Pineapple Standard`.
- [x] No `repair patch`, `shingle repair cost`, `DIY`, `discount code`,
  `job openings`, `salary`.
- [x] **No green** referenced as a brand color anywhere in this file
  (only as a *prohibition*: "no green", "green is banned").
- [x] Trust signals present: RCAT #03-0637, IKO Certified, 5-Star,
  Since 2005, 972-928-0788, JR. Moeakiola byline.
- [x] PAUSED banner at top + Outbox Shield reaffirmed.
- [x] Two-brand separation preserved: Brand A (Pineapple Roofing) and
  Brand B (Pineapple Restorations) are called out separately for
  Video Editor and Thumbnail Studio use.

## 7. ROLL-IN CHECKLIST (when Saia approves the merge into MASTER_SOP)

When Saia says "GO," the roll-in to `M7_MASTER_SOP.md` is:

1. Bump MASTER_SOP version: `1.0 — 2026-06-27` → `1.1 — 2026-07-13`.
2. In §2 FILE MAP, append the new rows from §4 above (do not delete
   or reorder existing rows).
3. In §4 SOPs, add SOP-V, SOP-T, SOP-H, SOP-S, SOP-CG alphabetically
   after SOP-J.
4. In §5 Weekly Operating Rhythm, add **Thu-2 (new):** generate next
   week's Thumbnail Studio batch + Hy3 micro-builds PAUSED, so the
   Mon planning brief has assets to schedule.
5. In §6 Troubleshooting, add a row: *"`youtubeChannel` not honoured
   on Thumbnail Studio research"* → check `~/.agentic-os/config.json`
   is outside the app folder (survives updates) and that
   `build 2026-07-13` or newer is shown under the logo.
6. `git add . && git commit -m "SOP update 2026-07-13 (Agent OS 2026-07-13 patch)" && git push` per SOP-F.
7. Append a one-liner to `03_Knowledge_Mat/SHARED_MEMORY.md`:
   *"2026-07-13: Agent OS patch rolled into MASTER_SOP v1.1 — Hy3,
   Video Editor, SEO Office, SETUP-GUIDE, build version, Grok-4.5,
   key-protection, Thumbnail Studio auto-research (youtubeChannel
   key)."*

Until Saia says GO, **this file is the source of truth** for the
07-06 → 07-13 changes. No agent edits the Master SOP on its own.

## 8. CLOSE

> *""* — the path of the
> journey is respect. We adopt new tools on our terms, at our pace,
> with the brand law and the Outbox Shield unbroken.

— JR. Moeakiola · RCAT #03-0637 · IKO Certified · 5-Star · Since 2005 · 972-928-0788

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
