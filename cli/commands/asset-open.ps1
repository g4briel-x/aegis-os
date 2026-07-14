
param([string]$Argument = "")

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:open <asset-id>" -ForegroundColor Yellow
    exit 1
}

$pathOutput = & powershell -ExecutionPolicy Bypass -File "cli\commands\asset-path.ps1" -Argument $Argument

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

$assetPath = $pathOutput | Select-Object -First 1

if (-not (Test-Path $assetPath)) {
    Write-Host "Asset path not found in repository: $assetPath" -ForegroundColor Red
    exit 1
}

Invoke-Item $assetPath
exit 0
