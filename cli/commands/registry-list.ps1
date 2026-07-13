## FILE: `cli/commands/registry-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS registry YAML files.
#>

$ErrorActionPreference = "Stop"

$registryRoot = "registry"

if (-not (Test-Path $registryRoot)) {
    Write-Host "Registry folder not found." -ForegroundColor Red
    exit 1
}

$files = Get-ChildItem -Path $registryRoot -Recurse -File -Include *.yaml, *.yml

if ($files.Count -eq 0) {
    Write-Host "No registry YAML files found." -ForegroundColor Yellow
    exit 0
}

Write-Host "Aegis OS Registries" -ForegroundColor Cyan
Write-Host ""

foreach ($file in $files | Sort-Object FullName) {
    Write-Host (Resolve-Path $file.FullName -Relative)
}

exit 0
```