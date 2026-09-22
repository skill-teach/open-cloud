Write-Host "⚙️ ટેલિગ્રામ ઓટો-અપલોડ પ્રોજેક્ટ સેટઅપ..." -ForegroundColor Cyan

# ૧. ફોલ્ડર બનાવવું
$watchFolder = "C:\AutoUpload"
if (!(Test-Path $watchFolder)) {
    New-Item -ItemType Directory -Path $watchFolder | Out-Null
}

# ૨. ડિપેન્ડન્સી ઇન્સ્ટોલ કરવી
Write-Host "📦 પાયથોન મોડ્યુલ્સ ઇન્સ્ટોલ થઈ રહ્યા છે..." -ForegroundColor Yellow
pip install watchdog requests --quiet

# ૩. સ્ક્રિપ્ટ ડાઉનલોડ કરવી (લિંક હવે પૂરી અને સાચી છે)
$scriptPath = "$watchFolder\upload_watcher.py"
$url = "https://githubusercontent.com"
Invoke-WebRequest -Uri $url -OutFile $scriptPath

Write-Host "🚀 પ્રોજેક્ટ સક્સેસફુલી રન થઈ રહ્યો છે..." -ForegroundColor Green
python $scriptPath
