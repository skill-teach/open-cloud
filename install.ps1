Write-Host "Telegram Auto-Upload Project Setup..." -ForegroundColor Cyan

# 1. Folder બનાવવું
$watchFolder = "C:\AutoUpload"

if (!(Test-Path $watchFolder)) {
    New-Item -ItemType Directory -Path $watchFolder | Out-Null
}

# 2. Python modules install કરવી
Write-Host "Python modules install થઈ રહ્યા છે..." -ForegroundColor Yellow

python -m pip install watchdog requests

# 3. Script download કરવી
Write-Host "upload_watcher.py download થઈ રહી છે..." -ForegroundColor Yellow

$scriptPath = "$watchFolder\upload_watcher.py"

$url = "https://raw.githubusercontent.com/skill-teach/open-cloud/main/upload_watcher.py"

Invoke-WebRequest -Uri $url -OutFile $scriptPath

# 4. Script run કરવી
Write-Host "Project successfully start થઈ રહ્યો છે..." -ForegroundColor Green

python $scriptPath
