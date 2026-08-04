# ============================================================
#  Pineapple M7 - NotebookLM Keep-Alive
#  Touches BOTH profiles (business + personal) daily so the
#  Google session cookie rotates BEFORE it expires. If a
#  profile still needs a manual reconnect, pops a Windows toast.
#  Free. No login performed here - only a lightweight check.
# ============================================================
$ErrorActionPreference = "SilentlyContinue"
$nlm = "$env:APPDATA\Python\Python314\Scripts\nlm.exe"
if (-not (Test-Path $nlm)) { $nlm = "nlm" }

$log = "C:\Pineapple Contractors M7\04_Tech_Lab\logs\notebooklm_keepalive.log"
New-Item -ItemType Directory -Path (Split-Path $log) -Force | Out-Null
$stamp = Get-Date -Format "yyyy-MM-dd HH:mm"

# Profiles to keep warm  (label => profile name)
$profiles = [ordered]@{
  "Business" = "default"
  "Personal" = "smoeprivate1@gmail.com"
}

$needsLogin = @()
foreach ($label in $profiles.Keys) {
  $p = $profiles[$label]
  # A light authenticated call rotates the cookie; --check validates without a browser.
  $out = & $nlm login --check --profile $p 2>&1 | Out-String
  if ($out -match "expired|Authentication Error|✗") {
    $needsLogin += "$label ($p)"
    Add-Content $log "$stamp  [$label/$p]  NEEDS RECONNECT"
  } else {
    # touch the session so the token refreshes/rotates
    & $nlm list notebooks --profile $p *> $null
    Add-Content $log "$stamp  [$label/$p]  OK (touched)"
  }
}

if ($needsLogin.Count -gt 0) {
  $msg = "Reconnect: " + ($needsLogin -join ", ") + ".  Run:  nlm login --profile <name>"
  try {
    Add-Type -AssemblyName System.Windows.Forms
    $n = New-Object System.Windows.Forms.NotifyIcon
    $n.Icon = [System.Drawing.SystemIcons]::Warning
    $n.Visible = $true
    $n.ShowBalloonTip(15000, "NotebookLM needs a reconnect", $msg, [System.Windows.Forms.ToolTipIcon]::Warning)
    Start-Sleep 16; $n.Dispose()
  } catch {}
}
