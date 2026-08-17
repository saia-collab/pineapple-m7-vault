[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$M7Root = "C:\Pineapple Contractors M7"
$TechRoot = Join-Path $M7Root "04_Tech_Lab"
$AppRoot = Join-Path $TechRoot "Pineapple_Agent_OS"
$Current = Join-Path $AppRoot "current"
$Safety = Join-Path $AppRoot "pineapple-safety"
$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$Work = Join-Path $AppRoot "update-staging-$Stamp"
$Extracted = Join-Path $Work "extracted"
$Candidate = Join-Path $Work "candidate"
$Backup = Join-Path (Join-Path $TechRoot "_agentos_backups") "safe-update-$Stamp"
$Marker = Join-Path $AppRoot "last-update-zip.txt"
$StartScript = Join-Path $AppRoot "START-PINEAPPLE-AGENT-OS.ps1"
$HermesHome = Join-Path $env:LOCALAPPDATA "hermes"

function Stage([string]$Text) { Write-Host "`n==> $Text" -ForegroundColor Cyan }
function Copy-Tree([string]$From, [string]$To, [string[]]$Extra = @()) {
  New-Item -ItemType Directory -Force -Path $To | Out-Null
  & robocopy $From $To /E /R:1 /W:1 /NFL /NDL /NJH /NJS /NP @Extra | Out-Null
  if ($LASTEXITCODE -ge 8) { throw "Windows could not safely copy $From" }
}
# Resilient single-file copy: create the destination folder if the new pack changed
# its layout (e.g. dropped config/), and skip quietly if the safety source is absent.
function Copy-Safe([string]$From, [string]$To) {
  if (-not (Test-Path $From)) { Write-Host "  (skip, no source: $From)" -ForegroundColor DarkGray; return }
  New-Item -ItemType Directory -Force -Path (Split-Path $To -Parent) | Out-Null
  Copy-Item $From $To -Force
}
function Stop-Port([int]$Port) {
  $ids = (Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction SilentlyContinue).OwningProcess | Select-Object -Unique
  foreach ($id in $ids) { if ($id) { Stop-Process -Id $id -Force -ErrorAction SilentlyContinue } }
}
function Stop-Studio {
  # Stop Studio (3737) + Hermes (9119) + omniroute (20128) before a swap.
  # omniroute's CWD sat inside current\, locking the folder — that made a prior swap fail with
  # "the file is being used by another process". Kill it by port AND by name (its cmd/node wrapper
  # can outlive the port and keep the handle), then wait for Windows to release file handles.
  Stop-Port 3737; Stop-Port 9119; Stop-Port 20128
  Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -like '*omniroute*' } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
  Start-Sleep -Seconds 3
}
function Move-Retry([string]$From, [string]$To, [int]$Tries = 6) {
  # Windows can hold a lock for a second or two after a process dies — retry instead of aborting the whole update.
  for ($i = 1; $i -le $Tries; $i++) {
    try { Move-Item $From $To -ErrorAction Stop; return }
    catch { if ($i -eq $Tries) { throw }; Start-Sleep -Seconds 2 }
  }
}
function Remove-Quiet([string]$Path) {
  if ($Path -and (Test-Path $Path)) { Remove-Item $Path -Recurse -Force -ErrorAction SilentlyContinue }
}
function Find-Hermes {
  $found = Get-Command hermes.exe -ErrorAction SilentlyContinue
  if ($found) { return $found.Source }
  $known = Join-Path $env:LOCALAPPDATA "hermes\hermes-agent\venv\Scripts\hermes.exe"
  if (Test-Path $known) { return $known }
  return $null
}

$previous = $null
$swapped = $false
try {
  if (-not (Test-Path $Current)) { throw "Run the one-click installer first." }
  New-Item -ItemType Directory -Force -Path $Work, $Extracted, $Backup | Out-Null
  $downloads = Join-Path $env:USERPROFILE "Downloads"
  $zip = Get-ChildItem -Path $downloads -Filter "agent-os-pack*.zip" -File -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if (-not $zip) { throw "No new agent-os-pack ZIP was found in Downloads. Put the new ZIP there, then double-click this updater again." }
  $fingerprint = "$($zip.FullName)|$($zip.Length)|$($zip.LastWriteTimeUtc.Ticks)"
  if ((Test-Path $Marker) -and ((Get-Content $Marker -Raw).Trim() -eq $fingerprint)) {
    Write-Host "That ZIP is already installed. Nothing was changed." -ForegroundColor Yellow
    & $StartScript
    exit $LASTEXITCODE
  }

  Stage "Opening the newest update in a safe staging area"
  Expand-Archive -LiteralPath $zip.FullName -DestinationPath $Extracted -Force
  $package = Get-ChildItem $Extracted -Recurse -Filter package.json -File |
    Where-Object { Test-Path (Join-Path $_.Directory.FullName "src") } | Select-Object -First 1
  if (-not $package) { throw "The ZIP does not contain a valid Agent OS source folder." }
  $source = $package.Directory.FullName
  $seoView = Join-Path $source "src\components\SEOView.tsx"
  if (-not (Test-Path $seoView)) { throw "The update is missing the SEO workspace." }
  $seoText = Get-Content $seoView -Raw
  if ($seoText -notmatch 'parasite' -or $seoText -notmatch 'openseo') {
    throw "This ZIP is older than your repaired SEO build, so it was rejected instead of downgrading you."
  }

  Stage "Reapplying Pineapple safety rules without restoring old SEO screens"
  Copy-Tree $source $Candidate @('/XD','node_modules','.next')
  Copy-Safe (Join-Path $Safety "seo\generate-route.ts") (Join-Path $Candidate "src\app\api\seo\generate\route.ts")
  Copy-Safe (Join-Path $Safety "seo\deploy-route.ts") (Join-Path $Candidate "src\app\api\seo\deploy\route.ts")
  Copy-Safe (Join-Path $Safety "seo\seoPipeline.ts") (Join-Path $Candidate "src\lib\seoPipeline.ts")
  Copy-Safe (Join-Path $Safety "seo\pineapple-seo-skill.md") (Join-Path $Candidate "config\pineapple-seo-skill.md")

  Stage "Repainting the UI to Pineapple brand law (Blue #003299 / Yellow #ffdd17, zero green, de-Julian)"
  $brandPaint = Join-Path $TechRoot "scripts\pineapple_os_brandpaint.ps1"
  if (Test-Path $brandPaint) {
    & powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File $brandPaint -SrcRoot (Join-Path $Candidate "src")
  }

  Stage "Testing the update before touching the working Local Studio"
  $npm = Get-Command npm.cmd -ErrorAction SilentlyContinue
  if (-not $npm) { throw "Node.js/npm is missing." }
  Push-Location $Candidate
  try {
    # npm + next print progress AND warnings to stderr. The updater runs under
    # $ErrorActionPreference='Stop', which makes PowerShell turn the FIRST stderr line into a
    # fatal NativeCommandError — that rolled back a perfectly good build (exit 0) the moment Next
    # printed "Turbopack build encountered 1 warnings". Drop to 'Continue' around the native
    # tools so stderr warnings are non-fatal, and judge pass/fail ONLY by the real exit code.
    $eap = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
      & $npm.Source ci --no-audit --no-fund
      $ciCode = $LASTEXITCODE
      $env:PORT = "3737"
      & $npm.Source run build
      $buildCode = $LASTEXITCODE
    } finally { $ErrorActionPreference = $eap }
    if ($ciCode -ne 0) { throw "The new ZIP could not install its dependencies." }
    if ($buildCode -ne 0) { throw "The new ZIP failed its build test; your working version was left alone." }
  } finally { Pop-Location }

  Stage "Backing up and switching to the tested update"
  Copy-Item (Join-Path $env:USERPROFILE ".agentic-os\config.json") $Backup -Force -ErrorAction SilentlyContinue
  Stop-Studio
  Set-Location $AppRoot   # never hold candidate/current as CWD during the swap (Windows dir lock)
  $previous = Join-Path $AppRoot "previous-$Stamp"
  Move-Retry $Current $previous       # retry so a lingering file lock doesn't abort the whole update
  Move-Retry $Candidate $Current
  $swapped = $true

  Stage "Updating Hermes and restoring the Pineapple SEO skill"
  $env:HERMES_HOME = $HermesHome
  $hermes = Find-Hermes
  if ($hermes) {
    # `hermes update` (uv/pip) prints "Using Python … environment at: venv" to stderr, which under
    # $ErrorActionPreference='Stop' PowerShell treats as fatal — needlessly rolling back an app that
    # already built + swapped fine. Updating Hermes is optional to the app working, so make it
    # non-fatal: don't let its stderr abort the whole update.
    $eapH = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    try { & $hermes update --backup --yes } catch { Write-Host "  (Hermes self-update skipped: $($_.Exception.Message))" -ForegroundColor DarkGray }
    $ErrorActionPreference = $eapH
    $skillSource = Join-Path $Safety "pineapple-seo-operator"
    if (Test-Path $skillSource) {
      Copy-Tree $skillSource (Join-Path $HermesHome "skills\pineapple-seo-operator")
      Get-ChildItem (Join-Path $HermesHome "profiles") -Directory -ErrorAction SilentlyContinue | ForEach-Object {
        Copy-Tree $skillSource (Join-Path $_.FullName "skills\pineapple-seo-operator")
      }
    }
  }

  Stage "Starting the updated Local Studio"
  & $StartScript -NoPause
  if ($LASTEXITCODE -ne 0) { throw "The update built but did not start." }
  Set-Content -Path $Marker -Value $fingerprint -Encoding UTF8
  Remove-Quiet $Work   # delete this run's staging folder so updates never pile up duplicates
  # keep only the 2 most recent previous-*/failed-* rollback copies; prune the rest
  Get-ChildItem $AppRoot -Directory | Where-Object { $_.Name -match '^previous-|^failed-' } |
    Sort-Object LastWriteTime -Descending | Select-Object -Skip 2 | ForEach-Object { Remove-Quiet $_.FullName }
  Write-Host "UPDATE COMPLETE. Your old working version is still backed up at $previous" -ForegroundColor Yellow
  exit 0
} catch {
  Write-Host "`nSAFE STOP: $($_.Exception.Message)" -ForegroundColor Red
  if ($swapped -and $previous -and (Test-Path $previous)) {
    Write-Host "Restoring the previous working version automatically..." -ForegroundColor Yellow
    Stop-Port 3737
    $failed = Join-Path $AppRoot "failed-$Stamp"
    if (Test-Path $Current) { Move-Item $Current $failed }
    Move-Item $previous $Current
    & $StartScript -NoPause
  }
  Remove-Quiet $Work   # clean up this failed run's staging folder so it doesn't pile up as a duplicate
  Write-Host "Your last working Local Studio remains available." -ForegroundColor Yellow
  exit 1
}
