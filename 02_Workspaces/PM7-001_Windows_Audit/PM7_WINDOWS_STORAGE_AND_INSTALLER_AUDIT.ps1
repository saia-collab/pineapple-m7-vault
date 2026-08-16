[CmdletBinding()]
param(
    [switch]$ApplySafeCleanup,
    [string]$ApprovalToken = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Pm7Root = "C:\Pineapple Contractors M7"
$DownloadsRoot = "C:\Users\estim\Downloads"
$ExpectedAgentPackName = "agent-os-pack-2026-08-14.zip"
$ExpectedAgentPackHash = "F4DFCF72A71A69B37F03C8A99A3ECEE8A8A85A9EE914DE9FD6F9A7EA81CC41A5"
$Timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$OutboxRoot = Join-Path $Pm7Root "01_Command_Center\Outbox_Drafts"
$ReportRoot = Join-Path $OutboxRoot "PM7_WINDOWS_STORAGE_AUDIT_$Timestamp"

if (-not (Test-Path -LiteralPath $Pm7Root -PathType Container)) {
    throw "Canonical PM7 root was not found: $Pm7Root"
}

if (-not (Test-Path -LiteralPath $DownloadsRoot -PathType Container)) {
    throw "Expected Downloads folder was not found: $DownloadsRoot"
}

New-Item -ItemType Directory -Path $ReportRoot -Force | Out-Null

function ConvertTo-FriendlySize {
    param([long]$Bytes)
    if ($Bytes -ge 1TB) { return ("{0:N2} TB" -f ($Bytes / 1TB)) }
    if ($Bytes -ge 1GB) { return ("{0:N2} GB" -f ($Bytes / 1GB)) }
    if ($Bytes -ge 1MB) { return ("{0:N2} MB" -f ($Bytes / 1MB)) }
    if ($Bytes -ge 1KB) { return ("{0:N2} KB" -f ($Bytes / 1KB)) }
    return "$Bytes bytes"
}

function Get-FolderSizeFact {
    param([Parameter(Mandatory = $true)][string]$Path)

    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        return [pscustomobject]@{
            Path = $Path
            Exists = $false
            Bytes = 0
            FriendlySize = "MISSING"
            FileCount = 0
            Error = ""
        }
    }

    try {
        # Stream file facts through Measure-Object so a large PM7 folder does not
        # have to be loaded into RAM as one giant array.
        $Measurement = Get-ChildItem -LiteralPath $Path -File -Recurse -Force -ErrorAction SilentlyContinue |
            Measure-Object -Property Length -Sum
        $TotalBytes = if ($null -eq $Measurement.Sum) { 0L } else { [long]$Measurement.Sum }
        return [pscustomobject]@{
            Path = $Path
            Exists = $true
            Bytes = $TotalBytes
            FriendlySize = ConvertTo-FriendlySize $TotalBytes
            FileCount = [long]$Measurement.Count
            Error = ""
        }
    }
    catch {
        return [pscustomobject]@{
            Path = $Path
            Exists = $true
            Bytes = 0
            FriendlySize = "ERROR"
            FileCount = 0
            Error = $_.Exception.Message
        }
    }
}

function Get-FileEvidence {
    param(
        [Parameter(Mandatory = $true)][System.IO.FileInfo]$File,
        [Parameter(Mandatory = $true)][string]$Category
    )

    $Hash = (Get-FileHash -LiteralPath $File.FullName -Algorithm SHA256).Hash.ToUpperInvariant()
    $Signature = Get-AuthenticodeSignature -LiteralPath $File.FullName
    $Signer = if ($null -ne $Signature.SignerCertificate) { $Signature.SignerCertificate.Subject } else { "" }
    $OpenAiSigned = ($Signature.Status -eq "Valid" -and $Signer -match "OpenAI")
    $KnownAgentPack = ($File.Name -ieq $ExpectedAgentPackName -and $Hash -eq $ExpectedAgentPackHash)

    return [pscustomobject]@{
        Category = $Category
        Name = $File.Name
        FullName = $File.FullName
        Bytes = [long]$File.Length
        FriendlySize = ConvertTo-FriendlySize $File.Length
        LastWriteTime = $File.LastWriteTime
        SHA256 = $Hash
        SignatureStatus = [string]$Signature.Status
        SignerSubject = $Signer
        OpenAISigned = $OpenAiSigned
        MatchesAuditedAugust14Pack = $KnownAgentPack
    }
}

function Send-FileToRecycleBin {
    param([Parameter(Mandatory = $true)][string]$Path)

    $ResolvedDownloads = (Resolve-Path -LiteralPath $DownloadsRoot).Path.TrimEnd('\')
    $ResolvedFile = (Resolve-Path -LiteralPath $Path).Path
    if (-not $ResolvedFile.StartsWith($ResolvedDownloads + "\", [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Cleanup refused because the file is outside Downloads: $ResolvedFile"
    }

    Add-Type -AssemblyName Microsoft.VisualBasic
    [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile(
        $ResolvedFile,
        [Microsoft.VisualBasic.FileIO.UIOption]::OnlyErrorDialogs,
        [Microsoft.VisualBasic.FileIO.RecycleOption]::SendToRecycleBin
    )
}

$ComputerSystem = Get-CimInstance Win32_ComputerSystem
$OperatingSystem = Get-CimInstance Win32_OperatingSystem
$LogicalDisk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$TotalDiskBytes = [long]$LogicalDisk.Size
$FreeDiskBytes = [long]$LogicalDisk.FreeSpace
$FreeDiskPercent = if ($TotalDiskBytes -gt 0) { [math]::Round(($FreeDiskBytes / $TotalDiskBytes) * 100, 2) } else { 0 }
$StorageState = if ($FreeDiskPercent -lt 10) { "CRITICAL_LOW_SPACE" } elseif ($FreeDiskPercent -lt 20) { "LOW_SPACE" } else { "OK" }

$InstallerFiles = @(Get-ChildItem -LiteralPath $DownloadsRoot -File -ErrorAction SilentlyContinue | Where-Object {
    $_.Name -match '^(ChatGPT|Codex) Installer(?: \(\d+\))?\.exe$'
})

$AgentPackFiles = @(Get-ChildItem -LiteralPath $DownloadsRoot -File -ErrorAction SilentlyContinue | Where-Object {
    $_.Name -match '^agent-os-pack-\d{4}-\d{2}-\d{2}(?: \(\d+\))?\.zip$'
})

$InstallerEvidence = @($InstallerFiles | ForEach-Object { Get-FileEvidence -File $_ -Category "OpenAI installer candidate" })
$AgentPackEvidence = @($AgentPackFiles | ForEach-Object { Get-FileEvidence -File $_ -Category "Agent OS pack" })
$AllCandidateEvidence = @($InstallerEvidence + $AgentPackEvidence)

$DuplicateGroups = @($AllCandidateEvidence | Group-Object SHA256 | Where-Object { $_.Count -gt 1 })
$DuplicateRows = @()
foreach ($Group in $DuplicateGroups) {
    $Ordered = @($Group.Group | Sort-Object LastWriteTime -Descending)
    $KeepPath = $Ordered[0].FullName
    foreach ($Item in $Ordered) {
        $DuplicateRows += [pscustomobject]@{
            SHA256 = $Group.Name
            Count = $Group.Count
            Name = $Item.Name
            FullName = $Item.FullName
            Decision = if ($Item.FullName -eq $KeepPath) { "KEEP_NEWEST_COPY" } else { "SAFE_DUPLICATE_CANDIDATE" }
        }
    }
}

$RegistryPaths = @(
    "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*"
)

$InstalledDesktopApps = @(
    Get-ItemProperty $RegistryPaths -ErrorAction SilentlyContinue |
        Where-Object { $_.PSObject.Properties['DisplayName'] -and $_.DisplayName -match "ChatGPT|Codex|OpenAI|Ollama|Docker" } |
        Select-Object DisplayName, DisplayVersion, Publisher, InstallLocation, UninstallString
)

$InstalledAppx = @(
    Get-AppxPackage -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match "ChatGPT|Codex|OpenAI" -or $_.PackageFullName -match "ChatGPT|Codex|OpenAI" } |
        Select-Object Name, Version, Publisher, InstallLocation, PackageFullName
)

$CandidateFolders = @(
    $DownloadsRoot,
    $Pm7Root,
    (Join-Path $Pm7Root "04_Tech_Lab\Pineapple_Agent_OS"),
    (Join-Path $Pm7Root "Agentic OS"),
    (Join-Path $Pm7Root "Launcher_Archive"),
    (Join-Path $Pm7Root "legacy_backup"),
    (Join-Path $env:USERPROFILE ".ollama\models"),
    (Join-Path $env:LOCALAPPDATA "Docker"),
    (Join-Path $env:LOCALAPPDATA "hermes"),
    (Join-Path $env:USERPROFILE ".codex"),
    $env:TEMP
)

$FolderSizes = @()
foreach ($Folder in $CandidateFolders) {
    Write-Host "Measuring: $Folder"
    $FolderSizes += Get-FolderSizeFact -Path $Folder
}

$TopProcesses = @(Get-Process -ErrorAction SilentlyContinue |
    Sort-Object WorkingSet64 -Descending |
    Select-Object -First 30 Name, Id, CPU,
        @{Name = "WorkingSetMB"; Expression = { [math]::Round($_.WorkingSet64 / 1MB, 1) } },
        @{Name = "PrivateMemoryMB"; Expression = { [math]::Round($_.PrivateMemorySize64 / 1MB, 1) } })

$CleanupResults = @()
if ($ApplySafeCleanup) {
    if ($ApprovalToken -cne "PM7_SAFE_DUPLICATE_CLEANUP") {
        throw "Cleanup refused. ApprovalToken must exactly equal PM7_SAFE_DUPLICATE_CLEANUP."
    }

    foreach ($Row in @($DuplicateRows | Where-Object { $_.Decision -eq "SAFE_DUPLICATE_CANDIDATE" })) {
        try {
            Send-FileToRecycleBin -Path $Row.FullName
            $CleanupResults += [pscustomobject]@{
                Path = $Row.FullName
                Result = "SENT_TO_RECYCLE_BIN"
                SHA256 = $Row.SHA256
            }
        }
        catch {
            $CleanupResults += [pscustomobject]@{
                Path = $Row.FullName
                Result = "FAILED: $($_.Exception.Message)"
                SHA256 = $Row.SHA256
            }
        }
    }
}

$InstallerEvidence | Export-Csv -LiteralPath (Join-Path $ReportRoot "01_INSTALLER_EVIDENCE.csv") -NoTypeInformation -Encoding UTF8
$AgentPackEvidence | Export-Csv -LiteralPath (Join-Path $ReportRoot "02_AGENT_OS_PACK_EVIDENCE.csv") -NoTypeInformation -Encoding UTF8
$DuplicateRows | Export-Csv -LiteralPath (Join-Path $ReportRoot "03_EXACT_DUPLICATE_GROUPS.csv") -NoTypeInformation -Encoding UTF8
$InstalledDesktopApps | Export-Csv -LiteralPath (Join-Path $ReportRoot "04_INSTALLED_DESKTOP_APPS.csv") -NoTypeInformation -Encoding UTF8
$InstalledAppx | Export-Csv -LiteralPath (Join-Path $ReportRoot "05_INSTALLED_APPX_PACKAGES.csv") -NoTypeInformation -Encoding UTF8
$FolderSizes | Sort-Object Bytes -Descending | Export-Csv -LiteralPath (Join-Path $ReportRoot "06_FOLDER_SIZES.csv") -NoTypeInformation -Encoding UTF8
$TopProcesses | Export-Csv -LiteralPath (Join-Path $ReportRoot "07_TOP_MEMORY_PROCESSES.csv") -NoTypeInformation -Encoding UTF8
$CleanupResults | Export-Csv -LiteralPath (Join-Path $ReportRoot "08_CLEANUP_RESULTS.csv") -NoTypeInformation -Encoding UTF8

$Summary = @()
$Summary += "# PM7 Windows Storage and Installer Audit"
$Summary += ""
$Summary += "- Run: $Timestamp"
$Summary += "- Computer: $($env:COMPUTERNAME)"
$Summary += "- Windows: $($OperatingSystem.Caption) $($OperatingSystem.Version)"
$Summary += "- Processor/system: $($ComputerSystem.Model)"
$Summary += "- Installed RAM: $(ConvertTo-FriendlySize ([long]$ComputerSystem.TotalPhysicalMemory))"
$Summary += "- C: capacity: $(ConvertTo-FriendlySize $TotalDiskBytes)"
$Summary += "- C: free: $(ConvertTo-FriendlySize $FreeDiskBytes) ($FreeDiskPercent%)"
$Summary += "- Storage status: **$StorageState**"
$Summary += "- Mode: $(if ($ApplySafeCleanup) { 'SAFE CLEANUP' } else { 'READ-ONLY AUDIT' })"
$Summary += ""
$Summary += "## Key counts"
$Summary += ""
$Summary += "- OpenAI installer candidates in Downloads: $($InstallerEvidence.Count)"
$Summary += "- Agent OS ZIPs in Downloads: $($AgentPackEvidence.Count)"
$Summary += "- Exact SHA-256 duplicate groups: $($DuplicateGroups.Count)"
$Summary += "- Installed desktop app records found: $($InstalledDesktopApps.Count)"
$Summary += "- Installed AppX package records found: $($InstalledAppx.Count)"
$Summary += "- August 14 audited Agent OS pack hash match: $(@($AgentPackEvidence | Where-Object MatchesAuditedAugust14Pack).Count)"
$Summary += "- Files sent to Recycle Bin: $(@($CleanupResults | Where-Object Result -eq 'SENT_TO_RECYCLE_BIN').Count)"
$Summary += ""
$Summary += "## Automatic decision boundary"
$Summary += ""
$Summary += "This audit never uninstalls applications, stops services, edits PM7, changes launchers, deletes Agent OS versions, or removes files with different hashes. Cleanup mode can send only exact SHA-256 duplicate installer/ZIP copies from Downloads to the Windows Recycle Bin."
$Summary += ""
$Summary += "Review the CSV files in this receipt folder before approving any installed-app uninstall, old Agent OS version retirement, Ollama-model removal, Docker cleanup, or PM7 folder migration."

$SummaryPath = Join-Path $ReportRoot "00_READ_ME_FIRST.md"
$Summary | Set-Content -LiteralPath $SummaryPath -Encoding UTF8

$JsonReceipt = [pscustomobject]@{
    run = $Timestamp
    mode = if ($ApplySafeCleanup) { "safe_cleanup" } else { "read_only_audit" }
    pm7_root = $Pm7Root
    report_root = $ReportRoot
    system = [pscustomobject]@{
        computer = $env:COMPUTERNAME
        windows = "$($OperatingSystem.Caption) $($OperatingSystem.Version)"
        total_ram_bytes = [long]$ComputerSystem.TotalPhysicalMemory
        disk_total_bytes = $TotalDiskBytes
        disk_free_bytes = $FreeDiskBytes
        disk_free_percent = $FreeDiskPercent
        storage_state = $StorageState
    }
    installer_evidence = $InstallerEvidence
    agent_pack_evidence = $AgentPackEvidence
    duplicate_groups = $DuplicateRows
    installed_desktop_apps = $InstalledDesktopApps
    installed_appx = $InstalledAppx
    folder_sizes = $FolderSizes
    top_processes = $TopProcesses
    cleanup_results = $CleanupResults
}

$JsonReceipt | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $ReportRoot "PM7_WINDOWS_STORAGE_AUDIT.json") -Encoding UTF8

Write-Host ""
Write-Host "PM7 audit complete." -ForegroundColor Green
Write-Host "Report: $SummaryPath" -ForegroundColor Cyan
Start-Process explorer.exe $ReportRoot
