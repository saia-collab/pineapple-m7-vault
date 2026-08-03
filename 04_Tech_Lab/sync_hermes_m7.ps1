# ============================================================
#  Pineapple M7 — Sync Hermes (theme + profile grounding)
#  Re-deploys the M7 dashboard theme AND the M7 Playbook grounding
#  (profile SOUL files) from the VAULT masters into the Hermes install.
#
#  Run this ONCE after any `hermes update` (updates touch the vendor
#  package, not user data — but this guarantees the theme is active and
#  the grounding is current). Idempotent; safe to re-run any time.
#
#  Vault masters (single source of truth):
#    04_Tech_Lab\hermes_m7_theme.yaml         -> dashboard theme
#    04_Tech_Lab\hermes_profiles\<p>.SOUL.md  -> per-profile grounding
#    04_Tech_Lab\hermes_profiles\_base.SOUL.md-> base/default SOUL
# ============================================================
$ErrorActionPreference = "Stop"
$VAULT   = "C:\Pineapple Contractors M7\04_Tech_Lab"
$PROFSRC = "$VAULT\hermes_profiles"
$THEMESRC= "$VAULT\hermes_m7_theme.yaml"
$H       = "$env:LOCALAPPDATA\hermes"
$HERMES  = "$env:LOCALAPPDATA\hermes\hermes-agent\venv\Scripts\hermes.exe"

Write-Host "Pineapple M7 - Hermes sync" -ForegroundColor Yellow

# 1. Theme -> ~/.hermes/dashboard-themes/m7.yaml + set active
$themeDir = "$H\dashboard-themes"
if (-not (Test-Path $themeDir)) { New-Item -ItemType Directory -Path $themeDir -Force | Out-Null }
Copy-Item $THEMESRC "$themeDir\m7.yaml" -Force
Write-Host "  [OK] theme -> $themeDir\m7.yaml"
if (Test-Path $HERMES) { & $HERMES config set dashboard.theme m7 2>&1 | Out-Null; Write-Host "  [OK] dashboard.theme = m7" }

# 2. Base/default SOUL
if (Test-Path "$PROFSRC\_base.SOUL.md") { Copy-Item "$PROFSRC\_base.SOUL.md" "$H\SOUL.md" -Force; Write-Host "  [OK] base SOUL.md" }

# 3. Per-profile SOULs (only for profiles that exist)
$profiles = "main","marketing","leads","roofing","restoration","seo","content"
foreach ($p in $profiles) {
  $src = "$PROFSRC\$p.SOUL.md"
  $dstDir = "$H\profiles\$p"
  if ((Test-Path $src) -and (Test-Path $dstDir)) {
    Copy-Item $src "$dstDir\SOUL.md" -Force
    Write-Host "  [OK] profile $p SOUL.md"
  } elseif (Test-Path $src) {
    Write-Host "  [skip] profile $p not installed"
  }
}

# 4. Restart the dashboard so the theme reloads (UI already built)
if (Test-Path $HERMES) {
  & $HERMES dashboard --stop 2>&1 | Out-Null
  Start-Sleep 2
  Start-Process -FilePath $HERMES -ArgumentList "dashboard","--no-open","--port","9119","--skip-build" -WindowStyle Hidden
  Write-Host "  [OK] dashboard restarting on :9119 (theme m7)"
}

Write-Host "Sync complete. Playbook grounding: 03_Knowledge_Mat\HERMES_PLAYBOOK.md" -ForegroundColor Cyan
