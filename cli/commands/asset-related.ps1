## FILE: `cli/commands/asset-related.ps1`

```powershell
param([string]$Argument = "")

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:related <asset-id>" -ForegroundColor Yellow
    exit 1
}

$files = Get-ChildItem -Path "registry" -Recurse -File -Include *.yaml, *.yml
$found = $false
$related = @()

foreach ($file in $files) {
    $lines = Get-Content $file.FullName
    $insideTarget = $false
    $insideRelated = $false

    foreach ($line in $lines) {
        if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
            $id = $Matches[1].Trim().Trim('"').Trim("'")

            if ($insideTarget -and $id -ne $Argument) {
                $insideTarget = $false
                $insideRelated = $false
            }

            if ($id -eq $Argument) {
                $found = $true
                $insideTarget = $true
                $insideRelated = $false
                continue
            }

            if ($insideTarget -and $insideRelated) {
                $related += $id
            }
        }

        if ($insideTarget -and $line -match "^\s*related_assets:\s*$") {
            $insideRelated = $true
        }
    }
}

if (-not $found) {
    Write-Host "Asset not found: $Argument" -ForegroundColor Red
    exit 1
}

Write-Host "Related assets for $Argument" -ForegroundColor Cyan
Write-Host ""

if ($related.Count -eq 0) {
    Write-Host "No related assets found." -ForegroundColor Yellow
    exit 0
}

$related | Sort-Object -Unique | ForEach-Object { Write-Host $_ -ForegroundColor Yellow }
exit 0
```
