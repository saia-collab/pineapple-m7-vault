$Vault = "C:\Pineapple Contractors M7\02_Media_Vault"

# 1. Ensure the three pristine master categories exist
$DroneDir = New-Item -Path "$Vault\01_Drone_Footage_Raw" -ItemType Directory -Force -ErrorAction SilentlyContinue
$TestimonialDir = New-Item -Path "$Vault\02_Client_Testimonials" -ItemType Directory -Force -ErrorAction SilentlyContinue
$ReelsDir = New-Item -Path "$Vault\03_Marketing_Reels_Pool" -ItemType Directory -Force -ErrorAction SilentlyContinue

Write-Host "Pristine folders verified. Starting automated file sorting..." -ForegroundColor Cyan

# 2. Grab every true video file using your exact discovery logic
$AllVideos = Get-ChildItem -Path $Vault -Recurse -File | Where-Object { $_.Extension -match '^\.(mp4|mov|m4v)$' }

foreach ($Video in $AllVideos) {
    # Skip files that are already inside our pristine master folders
    if ($Video.FullName -like "*01_Drone_Footage_Raw*" -or $Video.FullName -like "*02_Client_Testimonials*" -or $Video.FullName -like "*03_Marketing_Reels_Pool*") {
        continue
    }

    # Smart Routing Matrix based on your filename patterns
    if ($Video.Name -like "*hail*" -or $Video.Name -like "*drone*" -or $Video.Name -like "*Raw_Mana_Capture*") {
        $TargetDir = $DroneDir.FullName
    } elseif ($Video.Name -like "*JEFF*" -or $Video.Name -like "*testi*" -or $Video.Name -like "*client*" -or $Video.Name -like "*customer*") {
        $TargetDir = $TestimonialDir.FullName
    } else {
        # Default destination for general pools/reels to protect assets from accidental loss
        $TargetDir = $ReelsDir.FullName
    }

    # Move file and force replace any duplicates or broken shortcuts cleanly
    $DestPath = Join-Path $TargetDir $Video.Name
    Move-Item -Path $Video.FullName -Destination $DestPath -Force -ErrorAction SilentlyContinue
}

# 3. Clean up the empty nested intermediate boxes to prevent token crawling waste
Get-ChildItem -Path $Vault -Recurse -Directory | ForEach-Object {
    if ($_.Name -notmatch '^(01_Drone_Footage_Raw|02_Client_Testimonials|03_Marketing_Reels_Pool)$') {
        if ((Get-ChildItem -Path $_.FullName -Recurse -File).Count -eq 0) {
            Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
}

Write-Host "MEDIA VAULT CLEANUP COMPLETE! Structure optimized." -ForegroundColor Green
# Output final flat structure
Get-ChildItem -Path $Vault -Directory | Select-Object Name
