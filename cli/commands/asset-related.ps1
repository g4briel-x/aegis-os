<#
.SYNOPSIS
Shows assets related to a given Aegis OS asset.

.DESCRIPTION
Bug fix: the original used the same regex pattern for both top-level entries
("  - id:") and related asset entries ("      - id:"), causing the state machine
to reset $insideTarget before collecting any related IDs. Fix: match top-level
entries by exact 2-space indentation and related assets by 6+ spaces.

.USAGE
.\cli\aegis.ps1 asset:related <asset-id>
#>

param([string]$Argument = "")

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:related <asset-id>" -ForegroundColor Yellow
    exit 2
}

$files = Get-ChildItem -Path "registry" -Recurse -File -Include *.yaml, *.yml
$found = $false
$related = [System.Collections.Generic.List[string]]::new()

foreach ($file in $files) {
    $lines = Get-Content $file.FullName
    $insideTarget = $false
    $insideRelated = $false

    foreach ($line in $lines) {

        # Nouvelle entrée de haut niveau — exactement 2 espaces avant "-"
        # ex: "  - id: engineering.senior-developer"
        if ($line -match "^  -\s*id:\s*(.+)\s*$") {
            $id = $Matches[1].Trim().Trim('"').Trim("'")

            # On quitte la cible si on rencontre une autre entrée principale
            if ($insideTarget -and $id -ne $Argument) {
                $insideTarget = $false
                $insideRelated = $false
            }

            if ($id -eq $Argument) {
                $found = $true
                $insideTarget = $true
                $insideRelated = $false
            }
            continue
        }

        # Entrée dans le bloc related_assets
        if ($insideTarget -and $line -match "^\s*related_assets:\s*$") {
            $insideRelated = $true
            continue
        }

        # Related asset — 6 espaces ou plus avant "-"
        # ex: "      - id: engineering.review-pull-request"
        if ($insideTarget -and $insideRelated -and $line -match "^\s{6,}-\s*id:\s*(.+)\s*$") {
            $relatedId = $Matches[1].Trim().Trim('"').Trim("'")
            if (-not [string]::IsNullOrWhiteSpace($relatedId)) {
                $related.Add($relatedId)
            }
            continue
        }

        # Fin du bloc related_assets : une clé sans "-" au niveau 4 espaces
        if ($insideRelated -and $line -match "^    [A-Za-z0-9_-]+:\s*") {
            $insideRelated = $false
        }
    }

    if ($found) { break }
}

if (-not $found) {
    Write-Host "Asset not found: $Argument" -ForegroundColor Red
    exit 1
}

Write-Host "Related assets for $Argument:" -ForegroundColor Cyan
Write-Host ""

if ($related.Count -eq 0) {
    Write-Host "No related assets found." -ForegroundColor Yellow
    exit 0
}

$related | Sort-Object -Unique | ForEach-Object { Write-Host $_ -ForegroundColor Yellow }

Write-Host ""
Write-Host "Total: $($related.Count) related asset(s)" -ForegroundColor Green
exit 0
