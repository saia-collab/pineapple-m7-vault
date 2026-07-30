# 🍍 PINEAPPLE AGENTIC OS // MEDIA NAMING JANITOR v2.0
# Prefixes unorganized assets in Room 02 with the month the asset is actually from.
#
# WHY THIS WAS REWRITTEN
#   v1.0 stamped Get-Date -- the month the script ran -- onto every file, so a
#   March clip filed in July became 2026_07_*, destroying real chronology. Its
#   only Rename-Item used -ErrorAction SilentlyContinue with logging commented
#   out, so failures were invisible: janitor_progress.log holds 3,841 entries
#   that all read "name -> name", i.e. 3,841 reported successes that renamed
#   nothing. It also had no dry run, against a 39GB library.
#
# USAGE
#   Preview (default, changes nothing):  .\review-appeal-janitor.ps1
#   Apply:                               .\review-appeal-janitor.ps1 -Apply
[CmdletBinding()]
param(
    [switch]$Apply,
    [string]$Campaign = "UNASSIGNED_CAMPAIGN"
)

$rootPath   = "C:\Pineapple Contractors M7"
$mediaVault = Join-Path $rootPath "02_Media_Vault"
$logPath    = Join-Path $rootPath "01_Command_Center\memory\janitor_progress.log"

if (-not (Test-Path $mediaVault)) {
    Write-Host "Media vault not found: $mediaVault" -ForegroundColor Red
    exit 1
}
$logDir = Split-Path $logPath
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

$mode = if ($Apply) { "APPLY" } else { "PREVIEW (no changes -- re-run with -Apply)" }
Write-Host "[*] Media Naming Janitor -- $mode" -ForegroundColor Cyan
Write-Host "    Vault: $mediaVault"

$renamed = 0; $skipped = 0; $failed = 0
$stamp   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$lines   = @()

foreach ($file in (Get-ChildItem -Path $mediaVault -File -Recurse)) {
    # Already prefixed YYYY_MM_ -- leave it alone.
    if ($file.Name -match "^\d{4}_\d{2}_") { $skipped++; continue }

    # Date the ASSET, not the run. Oldest of created/modified is the closest
    # thing to "when this was shot" that survives a copy between drives.
    $assetDate = if ($file.CreationTime -lt $file.LastWriteTime) { $file.CreationTime } else { $file.LastWriteTime }
    $newName   = "{0}_{1}_{2}" -f $assetDate.ToString("yyyy_MM"), $Campaign, $file.Name
    $target    = Join-Path $file.DirectoryName $newName

    if (Test-Path $target) {
        Write-Host "  [skip] target exists: $newName" -ForegroundColor Yellow
        $lines += "$stamp [SKIP-EXISTS] $($file.FullName) -> $newName"
        $skipped++; continue
    }

    if (-not $Apply) {
        Write-Host "  [would rename] $($file.Name)  ->  $newName"
        $renamed++; continue
    }

    try {
        Rename-Item -Path $file.FullName -NewName $newName -ErrorAction Stop
        $lines += "$stamp [RENAMED] $($file.FullName) -> $newName"
        $renamed++
    } catch {
        Write-Host "  [FAIL] $($file.Name): $($_.Exception.Message)" -ForegroundColor Red
        $lines += "$stamp [FAILED] $($file.FullName) -> $newName :: $($_.Exception.Message)"
        $failed++
    }
}

# Written once at the end -- the v1.0 comment blamed a file lock for logging
# per-iteration; batching avoids that without giving up the audit trail.
if ($lines.Count -gt 0) { Add-Content -Path $logPath -Value $lines -Encoding UTF8 }

Write-Host ""
if ($Apply) {
    Write-Host "[+] Renamed $renamed | skipped $skipped | failed $failed" -ForegroundColor Cyan
    Write-Host "    Audit trail: $logPath"
} else {
    Write-Host "[+] $renamed file(s) would be renamed, $skipped already compliant." -ForegroundColor Cyan
    Write-Host "    Nothing changed. Re-run with -Apply to commit."
}
