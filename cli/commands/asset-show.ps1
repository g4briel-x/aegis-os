
param([string]$Argument = "")

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:show <asset-id>" -ForegroundColor Yellow
    exit 1
}

$files = Get-ChildItem -Path "registry" -Recurse -File -Include *.yaml, *.yml

foreach ($file in $files) {
    $lines = Get-Content $file.FullName
    $capture = $false
    $block = [System.Collections.Generic.List[string]]::new()

    foreach ($line in $lines) {
        if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
            if ($capture) { break }

            $id = $Matches[1].Trim().Trim('"').Trim("'")

            if ($id -eq $Argument) {
                $capture = $true
                $block.Add($line)
                continue
            }
        }
        elseif ($capture) {
            $block.Add($line)
        }
    }

    if ($capture) {
        Write-Host "Asset: $Argument" -ForegroundColor Cyan
        Write-Host "Source: $(Resolve-Path $file.FullName -Relative)" -ForegroundColor Yellow
        Write-Host ""
        $block | ForEach-Object { Write-Host $_ }
        exit 0
    }
}

Write-Host "Asset not found: $Argument" -ForegroundColor Red
exit 1
