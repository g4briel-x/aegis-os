## FILE: `cli/commands/help.ps1`

```powershell
<#
.SYNOPSIS
Shows Aegis OS CLI help.
#>

Write-Host "Aegis OS CLI" -ForegroundColor Cyan
Write-Host ""
Write-Host "Usage:" -ForegroundColor Yellow
Write-Host "  .\cli\aegis.ps1 <command> [argument]"
Write-Host ""
Write-Host "Commands:" -ForegroundColor Yellow
Write-Host "  help                 Show this help message"
Write-Host "  validate             Run validation checks"
Write-Host "  doctor               Run repository health checks"
Write-Host "  report               Generate registry reports"
Write-Host "  registry:list        List registry YAML files"
Write-Host "  asset:find <keyword> Search registry files by keyword"
Write-Host "  skill:list"
Write-Host "  playbook:list"
Write-Host "  pattern:list"
Write-Host "  template:list"
Write-Host "  domain:list"
Write-Host "  tag:list"
Write-Host "  docs:list"
Write-Host "  release:status"
Write-Host ""
Write-Host ""
Write-Host "Examples:" -ForegroundColor Yellow
Write-Host "  .\cli\aegis.ps1 validate"
Write-Host "  .\cli\aegis.ps1 doctor"
Write-Host "  .\cli\aegis.ps1 asset:find security"
exit 0
```
