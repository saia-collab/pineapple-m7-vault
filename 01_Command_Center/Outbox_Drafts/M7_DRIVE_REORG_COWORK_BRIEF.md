---
type: cowork_brief
title: Google Drive Media Reorg — Cowork Project Brief
status: PAUSED — hand to Claude Cowork with Drive + Dropbox connectors. Needs Saia GO.
last_updated: 2026-07-20
---

# 🗂️ COWORK BRIEF — Reorganize the Pineapple Media Drive

## Goal
Consolidate all Pineapple media (photos + video, ~39GB across Google Drive + your brother's Dropbox) into ONE clean, findable structure so any post is a 30-second grab. **Move only — never delete. Report duplicates.**

## The target structure (already exists in My Drive → PINEAPPLE_MEDIA_HUB)
```
PINEAPPLE_MEDIA_HUB/
├── 00_INBOX/            ← unsorted drops land here first
├── 01_RAW_DOWNLOADS/    ← unedited from the field
├── 01_READY_TO_POST/    ← trimmed clips + edited photos, post-ready
├── 02_BY_SERVICE/       ← roofing / storm / commercial / restoration
├── 03_BY_CITY/          ← Frisco / Lewisville / Plano / McKinney / Allen…
├── 04_TEAM_BRAND/       ← crew, family, culture, recruitment
├── 04_FINAL_FOR_BLATATO/← Blotato-ready, captioned
└── 99_ARCHIVE/          ← old / superseded
```

## What Cowork should do
1. **Connect** the user's Google Drive + this Dropbox folder (Saia provides the link).
2. **Scan** every media file across all source locations (Drive "Mana Folders" shared drive, loose files, Dropbox).
3. **Classify each file** by looking at filename + folder context:
   - unedited field capture → `01_RAW_DOWNLOADS`
   - trimmed/edited, post-ready → `01_READY_TO_POST`
   - before/after or service-specific → `02_BY_SERVICE`
   - a specific city job → `03_BY_CITY/<city>`
   - crew/family/festival (e.g. "Poly fest") → `04_TEAM_BRAND`
   - captioned/Blotato-ready → `04_FINAL_FOR_BLATATO`
4. **Move** (not copy, not delete) each file into the matching folder.
5. **Report:** a summary of what moved where, a list of duplicates found (don't delete — flag for Saia), and anything ambiguous it left in `00_INBOX`.

## Hard rules
- **MOVE only. Never delete anything.** Duplicates → flag, don't remove.
- Don't rename originals unless Saia approves a naming convention.
- Leave anything ambiguous in `00_INBOX` for a human to sort.
- Don't touch non-media files (docs, SOPs) — media only.
- Report at the end; don't publish or post anything.

## Why this first (VP note)
This is the **safest, highest-relief** Cowork job — it needs the Drive/Dropbox connectors (Cowork's strength), carries no SEO risk, and once done, every future reel/post is a 30-second grab from `01_READY_TO_POST`. Run this before the domain consolidation.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: cowork-brief -->
