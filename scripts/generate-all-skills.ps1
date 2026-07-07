# ==========================================
# Aegis OS - Generate All Skills
# ==========================================

$GeneratorPath = ".\generators"
$Engine = ".\scripts\generate-skill.ps1"

$definitions = Get-ChildItem `
    -Path $GeneratorPath `
    -Filter "*.yaml"


foreach ($definition in $definitions) {

    Write-Host ""
    Write-Host "Generating:" $definition.Name -ForegroundColor Cyan

    & $Engine $definition.FullName

}


Write-Host ""
Write-Host "==================================" -ForegroundColor Green
Write-Host " All Aegis OS Skills Generated "
Write-Host "==================================" -ForegroundColor Green