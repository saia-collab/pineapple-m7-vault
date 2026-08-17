# Outbox brand scrub — brings drafted content to Naa Sione law (2026-08-14).
# Mechanical find/replace on .md/.html in Outbox_Drafts. Skips files marked M7-FIREWALL-EXEMPT
# (governance docs that intentionally name banned terms). Filenames are NOT changed (avoids breaking links).
# Uses an ordered array of [from,to] pairs (case-sensitive .Replace; hashtable keys would collide on case).
param([string]$Root = "C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts", [switch]$IgnoreExempt)

$pairs = @(
  ,@('Complimentary Professional Photo Audit (CPPA)','free roof inspection')
  ,@('Complimentary Professional Photo Audit','free roof inspection')
  ,@('Book Your CPPA','Book Your Free Roof Inspection')
  ,@('Claim Your CPPA','Book Your Free Roof Inspection')
  ,@('Your CPPA','Your Free Roof Inspection')
  ,@('the CPPA','the free roof inspection')
  ,@('CPPA','free roof inspection')
  ,@('cppa','free roof inspection')
  ,@('Cppa','Free roof inspection')
  ,@('#1A365D','#003299')
  ,@('#1a365d','#003299')
  ,@('#FBC02D','#ffdd17')
  ,@('#fbc02d','#ffdd17')
  ,@('#00BFFF','#003299')
  ,@('#00bfff','#003299')
  ,@('Royal Navy','Pineapple Blue')
  ,@('Pineapple Gold','Pineapple Yellow')
  ,@('in DFW since 2005','in DFW since 2021')
  ,@('family-owned since 2005','family-owned since 2021')
  ,@('since 2005','since 2021')
  ,@('Since 2005','Since 2021')
  ,@('SINCE 2005','SINCE 2021')
  ,@('founded in 2005','founded in 2021')
  ,@('Founded in 2005','Founded in 2021')
  ,@('established in 2005','established in 2021')
  ,@('founded 2005','founded 2021')
  ,@('Founded 2005','Founded 2021')
  ,@('GAF Certified','IKO Certified')
  ,@('GAF-Certified','IKO Certified')
  ,@('$0 Out of Pocket','Full Restoration Coverage')
  ,@('$0 out of pocket','full restoration coverage')
  ,@('$0 Down','Full Restoration Coverage')
  ,@('$0 down','full restoration coverage')
  ,@('waived deductible','the full scope the carrier pays for')
)

$changed = 0; $scanned = 0; $skipped = 0
Get-ChildItem $Root -Recurse -Include *.md,*.html,*.css -File | ForEach-Object {
  $scanned++
  $t = [System.IO.File]::ReadAllText($_.FullName)
  if (-not $IgnoreExempt -and ($t -match 'M7-FIREWALL-EXEMPT')) { $skipped++; return }
  $orig = $t
  foreach ($p in $pairs) { $t = $t.Replace($p[0], $p[1]) }
  if ($t -ne $orig) { [System.IO.File]::WriteAllText($_.FullName, $t); $changed++; Write-Host ("  scrubbed: " + $_.Name) }
}
Write-Host ""
Write-Host ("SCRUB DONE - scanned " + $scanned + ", changed " + $changed + ", skipped(exempt) " + $skipped) -ForegroundColor Yellow
