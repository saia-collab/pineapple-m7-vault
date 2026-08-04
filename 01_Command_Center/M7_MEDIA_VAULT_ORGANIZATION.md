---
type: plan
title: 39GB Media Vault — Google Drive Reorganization + OS Usage
status: active
last_updated: 2026-07-14
---

# 📦 39GB Media — Organize Once, Post Forever

Your media lives in **Google Drive** (and the `pineapple-mana-vault` GCS bucket) — not
locally (you're out of disk). So we organize IN Drive and **reference by link**, never
by re-downloading. Below is the structure + naming that makes any clip findable in
seconds and usable by the OS + Blotato.

## 🗂️ Recommended Drive folder structure
Create this once at the top of your media Drive:
```
📁 PINEAPPLE_MEDIA/
├── 📁 00_INBOX/                ← dump raw phone/drone footage here first
├── 📁 01_READY_TO_POST/        ← polished, captioned, approved clips (Blotato pulls from here)
│   ├── 📁 reels/
│   ├── 📁 photos/
│   └── 📁 before_after/
├── 📁 02_BY_SERVICE/
│   ├── 📁 roof_replacement/
│   ├── 📁 roof_repair/
│   ├── 📁 storm_hail/
│   ├── 📁 commercial/
│   └── 📁 restoration/
├── 📁 03_BY_CITY/
│   ├── 📁 frisco/  📁 lewisville/  📁 plano/  📁 mckinney/  📁 denton/
├── 📁 04_TEAM_BRAND/           ← team photos, logo, crew shots
└── 📁 99_ARCHIVE/              ← raw originals you rarely touch
```
**Rule:** raw → `00_INBOX` → edit → drop the finished version in `01_READY_TO_POST`
(and tag by service/city). You only ever post from `01_READY_TO_POST`.

## 🏷️ Naming convention (so search finds it instantly)
```
YYYY-MM-DD_city_service_type_##.ext
e.g.  2026-05-14_frisco_roof-replacement_drone_01.mp4
      2026-06-02_lewisville_storm-hail_before_03.jpg
```
Searching "frisco roof drone" in Drive now returns exactly what you want.

## 🔗 How the media connects to your OS + social
You don't move 39GB to your PC. Two ways to use it:
1. **Blotato (social posting):** point Blotato at the Drive **share link** (or the GCS
   public URL) of a clip in `01_READY_TO_POST`. It pulls and posts to IG/TikTok/FB/GBP.
2. **Website / landing pages:** host the handful of "hero" photos in your **GCS bucket**
   (`pineapple-mana-vault`) made public-read, and reference the `storage.googleapis.com`
   URL directly — zero local storage, loads fast.

## 🎬 The weekly media loop
1. New footage → `00_INBOX`.
2. Best clips → **Video Editor tab** (Tighten + captions) → download `final.mp4`.
3. Drop finished clip in `01_READY_TO_POST/reels` + copy to the right city/service folder.
4. **Hermes writes the caption** (brand voice) → Outbox → you approve.
5. **Blotato** schedules it from the Drive link.

## ⚠️ Do NOT run the Gemini PowerShell "auto-organizer"
It targets `C:\Pineapple-Mana-Global\...` — **that path doesn't exist on your machine**,
and it MOVES files (risky on 39GB). Organize in Drive's web UI instead (drag-drop into
the folders above), or ask me to script a SAFE Drive-side reorg via the Drive connector.

## 🤖 Best way to actually do the reorg
- **Fastest:** do it in Drive's web UI once (create the folders, drag your best 100–200
  clips into `01_READY_TO_POST` + city/service — you don't need to sort all 39GB, just
  the post-worthy ones).
- **Assisted:** I can use the **Google Drive connector** to list/search your media and
  build an index (a spreadsheet of clip → city → service → link) so you always know what
  you have — without moving or downloading anything. Just say go.

<!-- M7-FIREWALL-EXEMPT: plan -->
