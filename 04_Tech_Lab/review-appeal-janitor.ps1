# 🍍 PINEAPPLE AGENTIC OS // REVIEW APPEAL JANITOR v1.0
# Enforces strict YEAR_MONTH_CAMPAIGN_ASSET-TYPE naming conventions across Room 02

$rootPath = "C:\Pineapple Contractors M7"
$mediaVault = Join-Path $rootPath "02_Media_Vault"
$logPath = Join-Path $rootPath "01_Command_Center\memory\janitor_progress.log"

Write-Output "[*] Initializing Folder Governance Loop..."

if (-not (Test-Path $mediaVault)) {
    New-Item -ItemType Directory -Path $mediaVault -Force | Out-Null
}

# Scan for unorganized assets and tag them cleanly to avoid data entropy
$unorganizedFiles = Get-ChildItem -Path $mediaVault -File -Recurse
foreach ($file in $unorganizedFiles) {
    if ($file.Name -notmatch "^\d{4}_\d{2}_") {
        $currentDate = Get-Date -Format "yyyy_MM"
        $newName = "$currentDate___UNASSIGNED_CAMPAIGN___$($file.Name)"
        $targetPath = Join-Path $file.DirectoryName $newName
        Rename-Item -Path $file.FullName -NewName $newName -ErrorAction SilentlyContinue
        # Add-Content disabled to avoid file lock
    }
}

Write-Output "[+] Asset environment sanitized. Enforcing absolute compliance."
