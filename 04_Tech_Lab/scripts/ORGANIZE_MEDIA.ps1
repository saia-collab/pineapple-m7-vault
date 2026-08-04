# ============================================================
#  ORGANIZE_MEDIA.ps1 — Pineapple Standard media organizer
#  Creates the clean folder structure + renames/moves your reels.
#  MOVE-ONLY. Nothing is deleted. Safe to re-run.
#  Naming: YYYY-MM-DD_City_AssetType_Descriptor_vN.ext
# ============================================================
$root = "C:\Pineapple Contractors M7\02_Media_Vault"
$src  = Join-Path $root "03_Marketing_Reels_Pool"

Write-Host ""
Write-Host "  Pineapple Standard — organizing media..." -ForegroundColor Yellow
Write-Host ""

# 1) Clean folder structure (no Blotato)
$folders = @(
  "01_RAW_INTAKE",
  "02_READY_TO_POST",
  "03_BY_CITY",
  "03_BY_CITY\Irving",
  "04_BEFORE_AFTER\Roofing",
  "04_BEFORE_AFTER\Restoration",
  "04_BEFORE_AFTER\Construction",
  "05_TEAM_BRAND"
)
foreach ($f in $folders) { New-Item -ItemType Directory -Force -Path (Join-Path $root $f) | Out-Null }
Write-Host "  Folder structure ready." -ForegroundColor Cyan

# 2) Rename + move the 6 reels (edit dates/cities later if you want)
$map = @(
  @{ from = "2432 W 6th St, Irving, TX 75060, USA.mp4"; to = "03_BY_CITY\Irving\2026-06-15_Irving_Reel_2432W6thSt_v1.mp4" }
  @{ from = "4605 Birkshire Ln.mp4";                    to = "03_BY_CITY\2026-06-18_DFW_Reel_4605BirkshireLn_v1.mp4" }
  @{ from = "5104 Mohawk Dr ].mp4";                     to = "03_BY_CITY\2026-06-18_DFW_Reel_5104MohawkDr_v1.mp4" }
  @{ from = "Poly fest 2026.mp4";                       to = "05_TEAM_BRAND\2026-06-15_Culture_Reel_PolyFest2026_v1.mp4" }
  @{ from = "property managers.MP4";                    to = "02_READY_TO_POST\2026-06-15_DFW_Reel_PropertyManagers_v1.mp4" }
  @{ from = "why pineapple roofing.MP4";                to = "02_READY_TO_POST\2026-06-15_DFW_Reel_WhyPineappleRoofing_v1.mp4" }
)
foreach ($m in $map) {
  $s = Join-Path $src  $m.from
  $d = Join-Path $root $m.to
  if (Test-Path -LiteralPath $s) {
    Move-Item -LiteralPath $s -Destination $d -Force
    Write-Host ("  moved -> " + $m.to) -ForegroundColor Yellow
  } else {
    Write-Host ("  skip (not found): " + $m.from) -ForegroundColor DarkGray
  }
}

Write-Host ""
Write-Host "  Done. READY-TO-POST first: 'WhyPineappleRoofing' + 'PropertyManagers'." -ForegroundColor Cyan
Write-Host "  Ko e hala 'o e fononga ko e faka'apa'apa." -ForegroundColor Cyan
