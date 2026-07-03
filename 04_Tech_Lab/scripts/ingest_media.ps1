$Vault = "C:\Pineapple Contractors M7\02_Media_Vault"
$DroneFolder = New-Item -Path "$Vault\01_Drone_Footage_Raw" -ItemType Directory -Force -ErrorAction SilentlyContinue
$TestimonialFolder = New-Item -Path "$Vault\02_Client_Testimonials" -ItemType Directory -Force -ErrorAction SilentlyContinue
$ReelsFolder = New-Item -Path "$Vault\03_Marketing_Reels_Pool" -ItemType Directory -Force -ErrorAction SilentlyContinue

Write-Host "Creating pristine M7 media folders... Done." -ForegroundColor Green

$DropBoxLinks = @(
    @{ URL = "https://www.dropbox.com/scl/fo/xpqpbnvui63urmrsuycmt/AEifPN3TI6aIMRdu0fwfyqE?rlkey=9mii4yaas6fuglnlfh8xrya0f&e=1&st=z2vsqprw&dl=1"; Target = $DroneFolder },
    @{ URL = "https://www.dropbox.com/scl/fo/4e0rupuyl4iuebra5ttm2/AHoBUuB_xbc6JL-sZf6ffdo?rlkey=1fej67zg1a4a7fm2v9ugh26gf&e=1&st=14pz8mjz&dl=1"; Target = $TestimonialFolder },
    @{ URL = "https://www.dropbox.com/scl/fo/s8ab4ktcye0dao1asly6e/AKh-8umzCEodpkl6VLEWcWU?rlkey=9gf0k74b81rw74pkljle3v3es&st=81lrawid&dl=1"; Target = $ReelsFolder }
)

$id = 1
foreach ($DropBox in $DropBoxLinks) {
    $ZipPath = "$Vault\temp_package_$id.zip"
    Write-Host "Streaming Dropbox Package $id directly into VS Code workspace... Please wait." -ForegroundColor Cyan
    
    Invoke-WebRequest -Uri $DropBox.URL -OutFile $ZipPath -ErrorAction Stop
    
    Write-Host "Extracting assets and automatically replacing old duplicates..." -ForegroundColor Yellow
    Expand-Archive -Path $ZipPath -DestinationPath $DropBox.Target -Force
    
    Remove-Item -Path $ZipPath -Force
    $id++
}

Write-Host "AUTOMATED MEDIA INGESTION COMPLETE: All cloud assets are locked inside 02_Media_Vault!" -ForegroundColor Green
