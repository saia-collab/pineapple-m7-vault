---
type: reference
title: M7 Google Drive → ICM Media Library plan
status: active
date: 2026-08-13
note: Target structure for the 39GB PINEAPPLE_MEDIA_HUB. I can't safely move 39GB of Drive files via tools — apply with Drive's "Suggest file moves" (Gemini) or I'll do it folder-by-folder on request.
---

# ☁️ GOOGLE DRIVE → ICM MEDIA LIBRARY

**Your Drive is already half-ICM.** `PINEAPPLE_MEDIA_HUB` has `00_INBOX / 01_READY_TO_POST / 02_BY_SERVICE / 03_BY_CITY / 04_TEAM_BRAND / 99_ARCHIVE` — that's a **Record Library** form (good). The mess is the loose month folders (`September`, `Oct`, `VIDEOS/REELS/{July 2023, 2024, 2025, Feb…}`) and a few owner-mixed folders.

## ICM role
Drive = **Layer 3 (factory / reference)** — the read-only visual inventory. Its output feeds `04_Tech_Lab` scripts (video render) and lands finished in `Outbox_Drafts`.

## Target structure (keep the numbered spine you already have)
```
PINEAPPLE_MEDIA_HUB/
├── 00_INBOX/            ← everything unsorted lands here first (incl. September, Oct, loose REELS)
├── 01_READY_TO_POST/   ← finished, on-brand, cleared to publish
├── 02_BY_SERVICE/      ← roofing / gutters / fencing / painting / storm
├── 03_BY_CITY/         ← Frisco / Plano / McKinney / Allen / Prosper …
├── 04_TEAM_BRAND/      ← team, founders, logos, brand assets
├── 05_RAW_CAPTURE/     ← unedited drone + on-site (NEW — split raw from ready)
├── 06_TESTIMONIALS/    ← client testimony videos (NEW — high-value proof)
└── 99_ARCHIVE/         ← old / superseded
```

## The one naming law (so scripts never break)
`YEAR_MONTH_CITY_SERVICE_type.ext` — e.g. `2026_05_Frisco_Roof_drone.mp4`. No spaces in machine-facing names.

## How to apply (you, not me — 39GB is too big/risky to move via my tools)
1. In Drive, open `PINEAPPLE_MEDIA_HUB` → click **"Suggest file moves"** (the Gemini button) and tell it: *"Move loose month folders (September, Oct, REELS/year folders) into 00_INBOX; testimonials into 06_TESTIMONIALS; raw drone into 05_RAW_CAPTURE. Keep 00–04 + 99."*
2. Or say the word and I'll do it **folder-by-folder** with you watching (safe, reversible), starting with the loose month folders.

## Rules
- **Read-only for non-core staff** (Viewer) so nobody moves a folder and breaks a script path.
- Testimonials + finished-roof drone = your highest-converting proof — surface them, don't bury them.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
