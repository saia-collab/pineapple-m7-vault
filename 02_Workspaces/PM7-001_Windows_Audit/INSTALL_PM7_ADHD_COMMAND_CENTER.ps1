[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Pm7Root = "C:\Pineapple Contractors M7"
$Timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$PlaybookRoot = Join-Path $Pm7Root "01_Command_Center\Playbooks"
$MemoryRoot = Join-Path $Pm7Root "_memory"
$OutboxRoot = Join-Path $Pm7Root "01_Command_Center\Outbox_Drafts"

if (-not (Test-Path -LiteralPath $Pm7Root -PathType Container)) {
    throw "Canonical PM7 root was not found: $Pm7Root"
}

New-Item -ItemType Directory -Path $PlaybookRoot -Force | Out-Null
New-Item -ItemType Directory -Path $MemoryRoot -Force | Out-Null
New-Item -ItemType Directory -Path $OutboxRoot -Force | Out-Null

$InstallResults = @()

function Install-Pm7FileSafely {
    param(
        [Parameter(Mandatory = $true)][string]$SourceName,
        [Parameter(Mandatory = $true)][string]$DestinationPath
    )

    $SourcePath = Join-Path $PSScriptRoot $SourceName
    if (-not (Test-Path -LiteralPath $SourcePath -PathType Leaf)) {
        throw "Required package file is missing: $SourcePath"
    }

    $DestinationDirectory = Split-Path -Parent $DestinationPath
    New-Item -ItemType Directory -Path $DestinationDirectory -Force | Out-Null
    $SourceHash = (Get-FileHash -LiteralPath $SourcePath -Algorithm SHA256).Hash

    if (-not (Test-Path -LiteralPath $DestinationPath -PathType Leaf)) {
        Copy-Item -LiteralPath $SourcePath -Destination $DestinationPath
        $script:InstallResults += [pscustomobject]@{
            Source = $SourcePath
            Destination = $DestinationPath
            SHA256 = $SourceHash
            Result = "INSTALLED_NEW"
        }
        return
    }

    $DestinationHash = (Get-FileHash -LiteralPath $DestinationPath -Algorithm SHA256).Hash
    if ($SourceHash -eq $DestinationHash) {
        $script:InstallResults += [pscustomobject]@{
            Source = $SourcePath
            Destination = $DestinationPath
            SHA256 = $SourceHash
            Result = "SKIPPED_IDENTICAL"
        }
        return
    }

    $DestinationDirectory = Split-Path -Parent $DestinationPath
    $BaseName = [System.IO.Path]::GetFileNameWithoutExtension($DestinationPath)
    $Extension = [System.IO.Path]::GetExtension($DestinationPath)
    $VersionedPath = Join-Path $DestinationDirectory "$BaseName.incoming-$Timestamp$Extension"
    Copy-Item -LiteralPath $SourcePath -Destination $VersionedPath
    $script:InstallResults += [pscustomobject]@{
        Source = $SourcePath
        Destination = $VersionedPath
        SHA256 = $SourceHash
        Result = "SAVED_VERSIONED_CONFLICT_NO_OVERWRITE"
    }
}

Install-Pm7FileSafely -SourceName "PM7_ADHD_EXECUTION_COMMAND_CENTER_2026-08-15.md" -DestinationPath (Join-Path $PlaybookRoot "PM7_ADHD_EXECUTION_COMMAND_CENTER_2026-08-15.md")
Install-Pm7FileSafely -SourceName "PM7_AI_HANDOFF_AND_LEARNING_PROMPTS_2026-08-15.md" -DestinationPath (Join-Path $PlaybookRoot "PM7_AI_HANDOFF_AND_LEARNING_PROMPTS_2026-08-15.md")
Install-Pm7FileSafely -SourceName "PM7_NOTEBOOKLM_SOURCE_MANIFEST_2026-08-15.md" -DestinationPath (Join-Path $PlaybookRoot "PM7_NOTEBOOKLM_SOURCE_MANIFEST_2026-08-15.md")
Install-Pm7FileSafely -SourceName "PM7_EXECUTION_STATE_2026-08-15.json" -DestinationPath (Join-Path $MemoryRoot "PM7_EXECUTION_STATE.json")
Install-Pm7FileSafely -SourceName "PM7_AI_COACHES_CONFIG_2026-08-15.json" -DestinationPath (Join-Path $MemoryRoot "PM7_AI_COACHES_CONFIG.json")

$ReceiptPath = Join-Path $OutboxRoot "PM7_COMMAND_CENTER_INSTALL_RECEIPT_$Timestamp.md"
$Receipt = @()
$Receipt += "# PM7 ADHD Command Center Install Receipt"
$Receipt += ""
$Receipt += "- Time: $Timestamp"
$Receipt += "- Root: $Pm7Root"
$Receipt += "- Scope: new playbook/shared-memory files only"
$Receipt += "- Agent OS current changed: NO"
$Receipt += "- Apps installed/uninstalled: NO"
$Receipt += "- Files deleted: NO"
$Receipt += "- External systems changed: NO"
$Receipt += ""
$Receipt += "## Results"
$Receipt += ""
$Receipt += "| Result | Destination | SHA-256 |"
$Receipt += "|---|---|---|"
foreach ($Item in $InstallResults) {
    $Receipt += "| $($Item.Result) | ``$($Item.Destination)`` | ``$($Item.SHA256)`` |"
}
$Receipt += ""
$Receipt += "If a destination already contained different content, this installer saved the new file with an incoming timestamp and did not overwrite the existing file. An AI must reconcile that conflict before making it canonical."

$Receipt | Set-Content -LiteralPath $ReceiptPath -Encoding UTF8

Write-Host "PM7 ADHD Command Center files are prepared." -ForegroundColor Green
Write-Host "Receipt: $ReceiptPath" -ForegroundColor Cyan

