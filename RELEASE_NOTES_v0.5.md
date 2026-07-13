## FILE: `RELEASE_NOTES_v0.5.md`

# Aegis OS v0.5 Release Notes

Release: v0.5.0  
Name: CLI + Automation Foundation  
Status: Foundation Complete  
Release Type: Foundation Release

---

# 1. Summary

Aegis OS v0.5 completes the first usable foundation of the project.

This release transforms Aegis OS from a structured repository of documentation and assets into an operable local framework with:

```text
CLI commands
validation scripts
report generation
repository doctor
configuration files
installation scripts
smoke tests
GitHub Actions workflows
machine-readable registries
root documentation
```

---

# 2. What This Release Enables

A local maintainer can now:

```text
inspect the repository
list registered assets
search assets
show asset metadata
check repository status
validate registries
generate reports
run smoke tests
install a local CLI alias
run CI checks in GitHub Actions
```

---

# 3. Main CLI Commands

```powershell
.\cli\aegis.ps1 help
.\cli\aegis.ps1 version
.\cli\aegis.ps1 info
.\cli\aegis.ps1 status
.\cli\aegis.ps1 doctor
.\cli\aegis.ps1 validate
.\cli\aegis.ps1 report
```

---

# 4. Registry Exploration

```powershell
.\cli\aegis.ps1 registry:list
.\cli\aegis.ps1 skill:list
.\cli\aegis.ps1 playbook:list
.\cli\aegis.ps1 pattern:list
.\cli\aegis.ps1 template:list
.\cli\aegis.ps1 domain:list
.\cli\aegis.ps1 tag:list
.\cli\aegis.ps1 docs:list
.\cli\aegis.ps1 release:status
```

---

# 5. Asset Inspection

```powershell
.\cli\aegis.ps1 asset:find security
.\cli\aegis.ps1 asset:show engineering.senior-developer
.\cli\aegis.ps1 asset:related security.security-review-template
.\cli\aegis.ps1 asset:path business.pricing-strategy-template
.\cli\aegis.ps1 asset:open design.ux-flow-template
.\cli\aegis.ps1 domain:assets security
.\cli\aegis.ps1 tag:assets api
```

---

# 6. Configuration Commands

```powershell
.\cli\aegis.ps1 config:path
.\cli\aegis.ps1 config:check
.\cli\aegis.ps1 config:show
```

---

# 7. Local Installation

The CLI can be installed as a local PowerShell function:

```powershell
powershell -ExecutionPolicy Bypass -File install\install-aegis-cli.ps1
```

After restarting PowerShell:

```powershell
aegis help
aegis doctor
aegis status
```

---

# 8. Validation

Run:

```powershell
.\cli\aegis.ps1 validate
```

or:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
```

Validation checks:

```text
YAML files
asset paths
duplicate ids
related asset references
registry structure
```

---

# 9. Testing

Run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
```

Smoke tests check:

```text
CLI files
core commands
registry commands
asset commands
configuration commands
metadata commands
```

---

# 10. Reports

Run:

```powershell
.\cli\aegis.ps1 report
```

Expected output folder:

```text
reports/registry/
```

Reports include:

```text
REGISTRY_SUMMARY.md
ASSET_MAP.md
DOMAIN_REPORT.md
RELEASE_REPORT.md
```

---

# 11. GitHub Actions

This release includes CI workflows:

```text
.github/workflows/aegis-validation.yml
.github/workflows/aegis-cli-smoke-tests.yml
```

They protect the repository against:

```text
invalid registries
missing paths
broken CLI command wiring
failed smoke tests
failed report generation
```

---

# 12. Completed Foundation Areas

Aegis OS v0.5 includes completed foundation layers for:

```text
documentation
skills
playbooks
patterns
templates
registries
automation
validation
reports
CLI
testing
CI
configuration
installation
```

---

# 13. Not Included Yet

Aegis OS v0.5 does not yet include:

```text
runtime implementation
agent execution runtime
marketplace publishing workflow
package manager
SDK package
JSON CLI output
production installer
plugin system implementation
```

These belong to v1.0 and later milestones.

---

# 14. Recommended Post-Release Direction

After v0.5 closure, the next recommended milestone is:

```text
Aegis OS v1.0 — Usable AI Operating Framework
```

Main v1.0 workstreams:

```text
runtime execution engine
SDK implementation
CLI JSON mode
asset installation workflow
package manager behavior
agent orchestration implementation
marketplace publishing model
stronger automated tests
```

---

# 15. Release Decision

Aegis OS v0.5 can be considered complete when:

```text
README.md exists
QUICKSTART.md exists
PROJECT_STATUS.md exists
CHANGELOG.md exists
RELEASE_NOTES_v0.5.md exists
V0_5_CLOSURE_REPORT.md exists
CLI smoke tests pass
registry validation passes
report generation works
GitHub Actions are present
```

---

# 16. Final Statement

```text
Aegis OS v0.5 establishes a complete CLI and automation foundation.
The project is ready to close the foundation phase and prepare v1.0 implementation.
```

---

# Final Principle

> v0.5 is the point where Aegis OS becomes locally operable, testable and maintainable.