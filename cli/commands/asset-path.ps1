
param([string]$Argument = "")

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:path <asset-id>" -ForegroundColor Yellow
    exit 1
}

$files = Get-ChildItem -Path "registry" -Recurse -File -Include *.yaml, *.yml

foreach ($file in $files) {
    $lines = Get-Content $file.FullName
    $insideTarget = $false

    foreach ($line in $lines) {
        if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
            $id = $Matches[1].Trim().Trim('"').Trim("'")
            $insideTarget = ($id -eq $Argument)
            continue
        }

        if ($insideTarget -and $line -match "^\s*path:\s*(.+)\s*$") {
            Write-Host $Matches[1].Trim().Trim('"').Trim("'") -ForegroundColor Cyan
            exit 0
        }
    }
}

Write-Host "Path not found for asset: $Argument" -ForegroundColor Red
exit 1
