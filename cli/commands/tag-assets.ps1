## FILE: `cli/commands/tag-assets.ps1`

```powershell
param([string]$Argument = "")

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 tag:assets <tag>" -ForegroundColor Yellow
    exit 1
}

$files = Get-ChildItem -Path "registry" -Recurse -File -Include *.yaml, *.yml
$matches = @()

foreach ($file in $files) {
    $lines = Get-Content $file.FullName
    $currentId = ""
    $entryLines = @()

    foreach ($line in $lines) {
        if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
            if (-not [string]::IsNullOrWhiteSpace($currentId)) {
                if ($entryLines -match "^\s*-\s*$Argument\s*$|^\s*-\s*tag\.$Argument\s*$") {
                    $matches += $currentId
                }
            }

            $currentId = $Matches[1].Trim().Trim('"').Trim("'")
            $entryLines = @($line)
        }
        else {
            $entryLines += $line
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($currentId)) {
        if ($entryLines -match "^\s*-\s*$Argument\s*$|^\s*-\s*tag\.$Argument\s*$") {
            $matches += $currentId
        }
    }
}

Write-Host "Assets with tag '$Argument':" -ForegroundColor Cyan
Write-Host ""

if ($matches.Count -eq 0) {
    Write-Host "No assets found." -ForegroundColor Yellow
    exit 0
}

$matches | Sort-Object -Unique | ForEach-Object { Write-Host $_ -ForegroundColor Yellow }
exit 0