# Aegis OS

Version: 0.6.0
Status: Runtime Foundation
Type: AI Operating Framework
Repository Stage: Cross-platform Runtime + Controlled Execution

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
Aegis OS v0.6 = Python Runtime + Controlled Execution
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
cross-platform Python CLI
execution planning and contracts
persistent execution sessions
audit history and integrity verification
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
runtime/               Cross-platform Python runtime and CLI
tests/runtime/         Python runtime regression tests
config/                CLI and tooling configuration examples
reports/               Generated human-readable reports
install/               Local CLI installation scripts
.github/workflows/     GitHub Actions automation
```

---

# 4. Python Runtime CLI

Install the runtime from the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".\runtime[dev]"
```

Run the main commands:

```powershell
aegis-runtime version
aegis-runtime --repo-root . status
aegis-runtime --repo-root . registry list
aegis-runtime --repo-root . registry domains
aegis-runtime --repo-root . registry tags
aegis-runtime --repo-root . asset show security.review-api-security
aegis-runtime --repo-root . asset find security
aegis-runtime --repo-root . asset type skill
aegis-runtime --repo-root . validate
aegis-runtime --repo-root . doctor
aegis-runtime --repo-root . report generate all
```

See [`runtime/README.md`](runtime/README.md) for repository discovery,
validation policy, and additional commands.

---

# 5. PowerShell CLI

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

# 6. Recommended Local Workflow

```powershell
aegis-runtime --repo-root . validate
python -m pytest tests/runtime
.\cli\aegis.ps1 doctor
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
git status
git add .
git commit -m "..."
git push
```

---

# 7. Install PowerShell CLI Alias

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

# 8. Quality Gates

Aegis OS v0.6 expects these checks to pass:

```powershell
python -m pytest tests/runtime
aegis-runtime --repo-root . validate
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
powershell -ExecutionPolicy Bypass -File scripts\reports\generate-all-reports.ps1
```

---

# 9. GitHub Actions

Current workflow layer:

```text
.github/workflows/aegis-validation.yml
.github/workflows/aegis-cli-smoke-tests.yml
.github/workflows/aegis-runtime-tests.yml
```

These workflows protect the repository from broken registries, invalid paths and broken CLI wiring.

---

# 10. Release Milestones

```text
v0.1 Documentation Foundation
v0.2 Skills and Execution Assets
v0.3 Registry Layer
v0.4 Automation and Validation
v0.5 CLI + Automation Foundation
v0.6 Python Runtime + Controlled Execution
v1.0 Usable AI Operating Framework
```

---

# 11. Final Principle

> Aegis OS turns AI work into a structured, reusable and governable operating system.
