---
type: ops_sop
title: M7 — Media Hub Consolidation (Drive + Dropbox → PINEAPPLE_MEDIA_HUB, move-only)
status: active
last_updated: 2026-07-05
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 📦 M7 — CONSOLIDATE ALL MEDIA → PINEAPPLE_MEDIA_HUB (move-only, dedupe report)

**Why rclone (not a chat agent):** rclone is free, connects Google Drive + Dropbox natively, does
**server-side moves** (fast, no re-download), **moves without deleting**, and has a real **dedupe report**.
A chat agent crawling tens of GB file-by-file is the wrong tool. Run this once and it's done.

> Safety: every command below is **move-only** (`rclone move`, never `delete`) and we **run `--dry-run`
> first** to preview. The dedupe step only **reports** duplicates — it never auto-deletes.

---

## STEP 0 — Connect (one-time)
- **Dropbox:** click the **Connect Dropbox** button (or claude.ai → Settings → Connectors) to authorize it.
- **Install rclone** (free): download from rclone.org, or on the GCP VM: `curl https://rclone.org/install.sh | sudo bash`.
- **Configure the two remotes:** run `rclone config` → add:
  - `gdrive` (type = Google Drive, your business account)
  - `dropbox` (type = Dropbox)
  - `hub` = the remote that holds **PINEAPPLE_MEDIA_HUB** (whichever cloud it lives on).

---

## STEP 1 — Map the moves (your existing hub structure)
| Source (Drive/Dropbox) | → Hub folder |
|------------------------|--------------|
| raw / unedited footage | `PINEAPPLE_MEDIA_HUB/01_RAW_DOWNLOADS` |
| edited / post-ready | `PINEAPPLE_MEDIA_HUB/01_READY_TO_POST` |
| before/afters | `PINEAPPLE_MEDIA_HUB/02_BEFORE_AFTER/<service>` (Roofing / Restoration / Construction) |
| city jobs | `PINEAPPLE_MEDIA_HUB/03_BY_CITY/<city>` |
| crew / family | `PINEAPPLE_MEDIA_HUB/04_TEAM_BRAND` |
| Blotato-ready | `PINEAPPLE_MEDIA_HUB/04_FINAL_FOR_BLATATO` |

---

## STEP 2 — DRY RUN first (preview, moves nothing)
```bash
rclone move gdrive:"path/to/raw"        hub:"PINEAPPLE_MEDIA_HUB/01_RAW_DOWNLOADS"     --dry-run -P
rclone move dropbox:"path/to/edited"    hub:"PINEAPPLE_MEDIA_HUB/01_READY_TO_POST"     --dry-run -P
rclone move gdrive:"path/to/beforeafter" hub:"PINEAPPLE_MEDIA_HUB/02_BEFORE_AFTER"     --dry-run -P
rclone move gdrive:"path/to/cityjobs"   hub:"PINEAPPLE_MEDIA_HUB/03_BY_CITY"           --dry-run -P
rclone move dropbox:"path/to/crew"      hub:"PINEAPPLE_MEDIA_HUB/04_TEAM_BRAND"         --dry-run -P
rclone move gdrive:"path/to/blotato"    hub:"PINEAPPLE_MEDIA_HUB/04_FINAL_FOR_BLATATO"  --dry-run -P
```
Read the output. When it looks right, **remove `--dry-run`** and re-run to actually move (move-only, source
is emptied but nothing is deleted — files land in the hub).

---

## STEP 3 — DUPLICATE REPORT (report only, no deletion)
```bash
# Report duplicate files inside the hub (by content hash), write to a file:
rclone dedupe --by-hash --dedupe-mode list hub:"PINEAPPLE_MEDIA_HUB" > 03_Knowledge_Mat/00_Atlas/media_duplicates_report.txt

# Cross-cloud: confirm nothing was lost after the move (source vs hub):
rclone check gdrive:"path/to/raw" hub:"PINEAPPLE_MEDIA_HUB/01_RAW_DOWNLOADS" --one-way
```
Review `media_duplicates_report.txt`. **Do not auto-delete** — decide which duplicates to remove manually,
or run `rclone dedupe --by-hash --dedupe-mode newest` later only after you've reviewed.

---

## STEP 4 — Verify + log
- Confirm counts: `rclone size hub:"PINEAPPLE_MEDIA_HUB"` and per-folder `rclone size hub:"…/01_RAW_DOWNLOADS"`.
- Append one line to `03_Knowledge_Mat/log.md`: what moved, from where, total GB, duplicate count.

---

## ⚠️ WHAT I NEED FROM YOU TO FINALIZE THE COMMANDS
Tell me (or fill into the template): (1) which cloud holds **PINEAPPLE_MEDIA_HUB**, (2) the exact **source
folder paths** in Drive and in the Dropbox folder, (3) whether the files are already sorted (raw vs edited vs
before/after) or a pile that needs an AI classification pass first. With those, I'll write your exact commands.

> If a pile is un-sorted, an agent (Hermes/Claude Code with Drive access) can classify by filename/date first
> — but the actual bytes move via rclone, not the chat agent.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
