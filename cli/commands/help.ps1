<#
.SYNOPSIS
Shows Aegis OS CLI help.
#>

Write-Host "Aegis OS CLI" -ForegroundColor Cyan
Write-Host ""
Write-Host "Usage:" -ForegroundColor Yellow
Write-Host "  .\cli\aegis.ps1 <command> [argument]"
Write-Host ""

Write-Host "Core Commands:" -ForegroundColor Yellow
Write-Host "  help                       Show this help message"
Write-Host "  validate                   Run validation checks"
Write-Host "  doctor                     Run repository health checks"
Write-Host "  report                     Generate registry reports"
Write-Host ""

Write-Host "  version                    Show CLI version"
Write-Host "  info                       Show project information"
Write-Host "  status                     Show lightweight repository status"
Write-Host ""

Write-Host "Registry Commands:" -ForegroundColor Yellow
Write-Host "  registry:list              List registry YAML files"
Write-Host "  skill:list                 List registered skills"
Write-Host "  playbook:list              List registered playbooks"
Write-Host "  pattern:list               List registered patterns"
Write-Host "  template:list              List registered templates"
Write-Host "  domain:list                List registered domains"
Write-Host "  tag:list                   List registered tags"
Write-Host "  docs:list                  List registered documentation sections"
Write-Host "  release:status             Show release status"
Write-Host ""

Write-Host "Asset Commands:" -ForegroundColor Yellow
Write-Host "  asset:find <keyword>       Search registry files by keyword"
Write-Host "  asset:show <id>            Show one asset registry block"
Write-Host "  asset:related <id>         Show related assets"
Write-Host "  asset:path <id>            Show asset repository path"
Write-Host "  asset:open <id>            Open asset path in file explorer"
Write-Host "  domain:assets <name>       List assets by domain"
Write-Host "  tag:assets <tag>           List assets by tag"
Write-Host ""

# Fix: section Config ajoutée avec titre et alignement correct (manquait dans l'original)
Write-Host "Config Commands:" -ForegroundColor Yellow
Write-Host "  config:show                Show example configuration"
Write-Host "  config:path                Show configuration file paths"
Write-Host "  config:check               Check required configuration files"
Write-Host ""

Write-Host "Examples:" -ForegroundColor Yellow
Write-Host "  .\cli\aegis.ps1 validate"
Write-Host "  .\cli\aegis.ps1 doctor"
Write-Host "  .\cli\aegis.ps1 registry:list"
Write-Host "  .\cli\aegis.ps1 asset:find security"
Write-Host "  .\cli\aegis.ps1 asset:show engineering.senior-developer"
Write-Host "  .\cli\aegis.ps1 asset:path business.pricing-strategy-template"
Write-Host "  .\cli\aegis.ps1 domain:assets security"
Write-Host "  .\cli\aegis.ps1 tag:assets api"
Write-Host ""

exit 0
