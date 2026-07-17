<#
.SYNOPSIS
Shows Aegis OS CLI help.

.DESCRIPTION
Displays available Aegis OS CLI commands and examples.

.USAGE
.\cli\aegis.ps1 help
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS CLI" -ForegroundColor Cyan
Write-Host ""

Write-Host "Usage:" -ForegroundColor Yellow
Write-Host "  .\cli\aegis.ps1 <command> [arguments...]"
Write-Host ""

Write-Host "Core Commands:" -ForegroundColor Yellow
Write-Host "  help                          Show this help message"
Write-Host "  validate                      Run validation checks"
Write-Host "  doctor                        Run repository health checks"
Write-Host "  report                        Generate registry reports"
Write-Host ""
Write-Host "  version                       Show CLI version"
Write-Host "  info                          Show project information"
Write-Host "  status                        Show lightweight repository status"
Write-Host ""

Write-Host "Registry Commands:" -ForegroundColor Yellow
Write-Host "  registry:list                 List registry YAML files"
Write-Host "  skill:list                    List registered skills"
Write-Host "  playbook:list                 List registered playbooks"
Write-Host "  pattern:list                  List registered patterns"
Write-Host "  template:list                 List registered templates"
Write-Host "  domain:list                   List registered domains"
Write-Host "  tag:list                      List registered tags"
Write-Host "  docs:list                     List registered documentation sections"
Write-Host "  release:status                Show release status"
Write-Host ""

Write-Host "Asset Commands:" -ForegroundColor Yellow
Write-Host "  asset:find <keyword>          Search registry files by keyword"
Write-Host "  asset:show <id>               Show one asset registry block"
Write-Host "  asset:related <id>            Show related assets"
Write-Host "  asset:path <id>               Show asset repository path"
Write-Host "  asset:open <id>               Open asset path in file explorer"
Write-Host "  domain:assets <name>          List assets by domain"
Write-Host "  tag:assets <tag>              List assets by tag"
Write-Host ""

Write-Host "Config Commands:" -ForegroundColor Yellow
Write-Host "  config:show                   Show example configuration"
Write-Host "  config:path                   Show configuration file paths"
Write-Host "  config:check                  Check required configuration files"
Write-Host ""

Write-Host "Runtime Commands:" -ForegroundColor Yellow
Write-Host "  runtime:status                Show Python runtime status"
Write-Host "  runtime:validate              Validate registries with Python runtime"
Write-Host "  runtime:registry-list         List registries with Python runtime"
Write-Host "  runtime:asset-find <keyword>  Search assets with Python runtime"
Write-Host "  runtime:asset-show <id>       Show one asset with Python runtime"
Write-Host "  runtime:execution-plan <id>     Create execution plan with Python runtime"
Write-Host "  runtime:execution-dry-run <id>  Simulate execution without running actions"
Write-Host "  runtime:execution-contract <id> Build and validate execution contract"
Write-Host "  runtime:execution-context <id>  Build and inspect execution context"
Write-Host "  runtime:execution-session <id>  Build execution session and logical workspace"
Write-Host "  runtime:session-show <id>        Show a persisted execution session"
Write-Host "  runtime:execution-orchestrate <id> Orchestrate a persisted execution session"
Write-Host "  runtime:execution-lifecycle <id> <action> [reason] [actor]"
Write-Host "                         Complete, fail, or cancel a persisted session"

Write-Host "Examples:" -ForegroundColor Yellow
Write-Host "  .\cli\aegis.ps1 validate"
Write-Host "  .\cli\aegis.ps1 doctor"
Write-Host "  .\cli\aegis.ps1 registry:list"
Write-Host "  .\cli\aegis.ps1 asset:find security"
Write-Host "  .\cli\aegis.ps1 asset:show engineering.senior-developer"
Write-Host "  .\cli\aegis.ps1 asset:path business.pricing-strategy-template"
Write-Host "  .\cli\aegis.ps1 domain:assets security"
Write-Host "  .\cli\aegis.ps1 tag:assets api"
Write-Host "  .\cli\aegis.ps1 runtime:status"
Write-Host "  .\cli\aegis.ps1 runtime:registry-list"
Write-Host "  .\cli\aegis.ps1 runtime:asset-find security"
Write-Host "  .\cli\aegis.ps1 runtime:asset-show security.review-api-security"
Write-Host "  .\cli\aegis.ps1 runtime:validate"
Write-Host "  .\cli\aegis.ps1 runtime:execution-plan security.review-api-security"
Write-Host "  .\cli\aegis.ps1 runtime:execution-dry-run security.review-api-security"
Write-Host "  .\cli\aegis.ps1 runtime:execution-contract security.review-api-security"
Write-Host "  .\cli\aegis.ps1 runtime:execution-context security.review-api-security"
Write-Host "  .\cli\aegis.ps1 runtime:execution-session security.review-api-security"
Write-Host "  .\cli\aegis.ps1 runtime:session-show <session-id-or-workspace-id>"
Write-Host "  .\cli\aegis.ps1 runtime:execution-orchestrate <session-id-or-workspace-id>"
Write-Host "  .\cli\aegis.ps1 runtime:execution-lifecycle <session-id-or-workspace-id> complete"
Write-Host "  .\cli\aegis.ps1 runtime:execution-lifecycle <session-id-or-workspace-id> fail `"Validation failed.`" `"operator:name`""
Write-Host "  .\cli\aegis.ps1 runtime:execution-lifecycle <session-id-or-workspace-id> cancel `"Cancelled by operator.`""
exit 0
