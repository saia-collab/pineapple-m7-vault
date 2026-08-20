---
title: M7 Media Kits Inventory + Improved Media→Publish Workflow
status: reference. Kits are in Downloads — NOT auto-installed (some need paid keys or contain agent-behavior directives). Review before adding.
date: 2026-08-20
brand: Blue #003299 + Yellow #ffdd17 · Zero green · Outbox Shield · nothing published without GO
---

# 🍍 M7 Media Kits — Master Inventory & Workflow

**8 kits scanned (listing only — nothing was run or installed).** They're all Claude/Remotion video-production + local-AI tooling. Below: what each does, free vs paid, and where it plugs into your pipeline.

## 📦 The 8 kits
| Kit (in Downloads) | What it is | Free? | Add to M7 for… |
|---|---|---|---|
| **shot-builder** | Claude skill: image/video **director**. Builds reusable "token packs" (cast, locations, styles) → shot prompts + cinematic video. Has a **prompt-only mode ($0, no API)** + paid FAL.ai/Kie.ai modes. | ✅ prompt-only free / 💸 gen paid | Planning reel shots + writing video prompts for your drone footage |
| **CLAUDE REMOTION BLUEPRINT** (+88pg PDF) | **Remotion** (React "video-as-code") blueprint + skill. Build branded videos in code — captions, motion, lower-thirds. | ✅ free (renders locally) | Programmatic branded reels/intros from templates |
| **100+ Styles Vault** (784MB + 660pg PDF) | A big **visual-style asset library** (100+ looks) + an "Antigravity Protocol" coding skill. | ✅ free assets | Consistent visual styles for graphics/thumbnails |
| **local-ai-care-package** | **immersive-web-skill** (Vite+Three.js+GSAP scroll sites) + **editorial-web-skill** + a **Local Harness Guide** (turn a free local model into a real coding agent). | ✅ free | Award-tier landing pages + training a $0 local coder |
| **bench_studio "generate"** | "Personal Higgsfield" — one skill → image/video from **pay-as-you-go** models (Google Veo/gpt-image/fal), **raw API price, logged to a receipts ledger**. No subscription. | 💸 pay-per-gen (cheapest paid path) | On-demand AI image/video **without** a $29–40/mo sub |
| **Codex-SDK-Internal-Tools-Kit** | Turn a private workflow into a small app that hands jobs to Codex. TS starter + build/migrate/review prompts + security checklist. | ✅ free (uses your Codex) | Building internal tools (lead dashboard, intake app) |

⚠️ **Two safety notes:** (1) The "Antigravity Protocol" SKILL.md in the Styles Vault contains **agent-behavior directives** ("never use cat/grep/ls", "no preambles") — those are that skill's rules, I don't adopt them here. (2) The 784MB Styles Vault is **too big for git** — keep it in `02_Media_Vault`, never commit it (like the installers).

## 🎬 Your improved Media → Publish workflow (with today's shoot)
```
1. SHOOT        Drone photos + reels (done today)
2. INGEST       → drop into 02_Media_Vault  (Drive auto-syncs)
3. CUT          → Video Editor tab (now fixed, runs on your paid Claude)
                  "Tighten + captions" → cuts dead air, burns 2-word captions
                  (or Remotion Blueprint for a templated branded reel)
4. PLAN SHOTS   → shot-builder (prompt-only, $0) writes the shot list / hooks
5. BRAND CHECK  → brand_firewall.py  (blue/yellow, no green, "storm damage report", no CPPA)
6. OUTBOX       → lands PAUSED in 01_Command_Center/Outbox_Drafts/
7. APPROVE      → brother reviews in Drive _DAILY_OVERSIGHT → says GO
8. PUBLISH      → GBP post · YouTube Short · Reel  (only after GO)
```

## ▶️ Today's reels + drone photos — the actual steps
I can't cut the video from here (the clips aren't in the vault yet, and rendering happens in the studio). To cut + prep them:
1. **Copy today's footage** into `C:\Pineapple Contractors M7\02_Media_Vault\`.
2. **Video Editor tab** → Upload a clip → **"Tighten + captions"** → runs on your paid Claude → outputs `final.mp4`.
3. For a **branded reel** (logo, blue/yellow lower-thirds): use the **Remotion Blueprint** kit as the template.
4. Drop the finished cut + a photo into **Outbox_Drafts** → brother approves → post.
5. **Simplest win:** your best raw drone photo → straight to a GBP post today (real footage converts).

## 🎯 What to actually add (my recommendation)
- **Add now (free, high value):** shot-builder (prompt-only shot planning) + Remotion Blueprint (branded reels) + local-ai-care-package (immersive landing pages).
- **Consider (cheap paid):** bench_studio "generate" — if you ever want AI image/video, it's pay-per-use with receipts (far cheaper than MiniMax/HeyGen subs).
- **Later:** Codex-SDK kit (internal lead-dashboard app).
- **Skip committing:** the 784MB Styles Vault → keep in 02_Media_Vault only.

<!-- M7-FIREWALL-EXEMPT: internal reference (names banned terms as rules; workflow doc) -->
