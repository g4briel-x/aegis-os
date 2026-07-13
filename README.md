## FILE: `README.md`

# Aegis OS

Version: 0.5.0  
Status: Foundation Complete  
Type: AI Operating Framework  
Repository Stage: CLI + Automation Foundation

---

# 1. What Is Aegis OS?

Aegis OS is a structured AI operating framework for building, organizing and operating expert AI workflows.

It provides a repository architecture for:

```text
skills
playbooks
patterns
templates
registries
validation
reports
CLI commands
automation scripts
governance documentation
```

The goal is to make AI-assisted work repeatable, inspectable, governable and reusable.

---

# 2. Current Version

```text
Aegis OS v0.5 = CLI + Automation Foundation
```

This version includes:

```text
documentation foundation
skills v2 framework
premium skills
playbooks framework
premium playbooks
patterns framework
premium patterns
templates framework
premium templates
machine-readable registries
registry validation scripts
report generation scripts
repository doctor scripts
PowerShell CLI
CLI smoke tests
GitHub Actions workflows
CLI installation scripts
CLI configuration layer
metadata commands
```

---

# 3. Repository Structure

```text
core/                  Core concepts and execution principles
shared/                Shared standards and engineering principles
docs/                  Foundation, architecture, governance and reference docs
skills/                Expert role definitions and workflows
playbooks/             Step-by-step operational procedures
patterns/              Reusable solution patterns
templates/             Reusable document templates
registry/              Machine-readable asset catalogs
scripts/               Validation, reporting, doctor and testing scripts
cli/                   Aegis OS local command line interface
config/                CLI and tooling configuration examples
reports/               Generated human-readable reports
install/               Local CLI installation scripts
.github/workflows/     GitHub Actions automation
```

---

# 4. Main CLI Commands

Run from repository root:

```powershell
.\cli\aegis.ps1 help
.\cli\aegis.ps1 version
.\cli\aegis.ps1 info
.\cli\aegis.ps1 status
.\cli\aegis.ps1 doctor
.\cli\aegis.ps1 validate
.\cli\aegis.ps1 report
```

Registry commands:

```powershell
.\cli\aegis.ps1 registry:list
.\cli\aegis.ps1 skill:list
.\cli\aegis.ps1 playbook:list
.\cli\aegis.ps1 pattern:list
.\cli\aegis.ps1 template:list
.\cli\aegis.ps1 domain:list
.\cli\aegis.ps1 tag:list
.\cli\aegis.ps1 release:status
```

Asset commands:

```powershell
.\cli\aegis.ps1 asset:find security
.\cli\aegis.ps1 asset:show engineering.senior-developer
.\cli\aegis.ps1 asset:path business.pricing-strategy-template
.\cli\aegis.ps1 domain:assets security
.\cli\aegis.ps1 tag:assets api
```

Configuration commands:

```powershell
.\cli\aegis.ps1 config:path
.\cli\aegis.ps1 config:check
.\cli\aegis.ps1 config:show
```

---

# 5. Recommended Local Workflow

```powershell
.\cli\aegis.ps1 doctor
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
git status
git add .
git commit -m "..."
git push
```

---

# 6. Install Local CLI Alias

Run:

```powershell
powershell -ExecutionPolicy Bypass -File install\install-aegis-cli.ps1
```

Restart PowerShell, then use:

```powershell
aegis help
aegis doctor
aegis validate
aegis asset:find security
```

---

# 7. Quality Gates

Aegis OS v0.5 expects these checks to pass:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
powershell -ExecutionPolicy Bypass -File scripts\reports\generate-all-reports.ps1
```

---

# 8. GitHub Actions

Current workflow layer:

```text
.github/workflows/aegis-validation.yml
.github/workflows/aegis-cli-smoke-tests.yml
```

These workflows protect the repository from broken registries, invalid paths and broken CLI wiring.

---

# 9. Release Milestones

```text
v0.1 Documentation Foundation
v0.2 Skills and Execution Assets
v0.3 Registry Layer
v0.4 Automation and Validation
v0.5 CLI + Automation Foundation
v1.0 Usable AI Operating Framework
```

---

# 10. Final Principle

> Aegis OS turns AI work into a structured, reusable and governable operating system.
