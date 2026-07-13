## FILE: `cli/CLI_ASSET_COMMANDS.md`

# Aegis OS — CLI Asset Commands

Version: 0.1.0  
Status: Draft

## Purpose

These CLI commands inspect Aegis OS assets from registry metadata.

They allow maintainers to search, inspect, locate and open assets without manually browsing registry YAML files.

## Commands

```powershell
.\cli\aegis.ps1 asset:show engineering.senior-developer
.\cli\aegis.ps1 asset:related security.security-review-template
.\cli\aegis.ps1 asset:path business.pricing-strategy-template
.\cli\aegis.ps1 asset:open design.ux-flow-template
.\cli\aegis.ps1 domain:assets security
.\cli\aegis.ps1 tag:assets api
```

## Final Principle

> Asset commands turn registries into practical repository navigation.
