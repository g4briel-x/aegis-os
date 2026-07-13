## FILE: `cli/commands/domain-assets.ps1`

```powershell
param([string]$Argument = "")

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 domain:assets <domain>" -ForegroundColor Yellow
    exit 1
}

$files = Get-ChildItem -Path "registry" -Recurse -File -Include *.yaml, *.yml
$matches = @()

foreach ($file in $files) {
    $lines = Get-Content $file.FullName
    $currentId = ""
    $currentDomain = ""

    foreach ($line in $lines) {
        if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
            if ($currentDomain -eq $Argument -and -not [string]::IsNullOrWhiteSpace($currentId)) {
                $matches += $currentId
            }

            $currentId = $Matches[1].Trim().Trim('"').Trim("'")
            $currentDomain = ""
        }
        elseif ($line -match "^\s*domain:\s*(.+)\s*$") {
            $currentDomain = $Matches[1].Trim().Trim('"').Trim("'")
        }
    }

    if ($currentDomain -eq $Argument -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $matches += $currentId
    }
}

Write-Host "Assets in domain '$Argument':" -ForegroundColor Cyan
Write-Host ""

if ($matches.Count -eq 0) {
    Write-Host "No assets found." -ForegroundColor Yellow
    exit 0
}

$matches | Sort-Object -Unique | ForEach-Object { Write-Host $_ -ForegroundColor Yellow }
exit 0
```