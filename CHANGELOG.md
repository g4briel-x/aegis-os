## FILE: `CHANGELOG.md`

# Changelog

All notable changes to Aegis OS are documented in this file.

Format inspired by Keep a Changelog.  
Versioning follows semantic milestone releases.

---

## [0.7.0] — Python Runtime Consolidation — 2026-07-21

### Added

- installable `aegis` command alongside `aegis-runtime`;
- `info`, `docs list`, `release status`, `generate skill` and `generate skills`;
- guarded, deterministic YAML-to-skill generation;
- one Python CI workflow for Linux, Windows and macOS;
- release `0.7.0` metadata and regenerated registry reports;
- six runtime regression tests, bringing the suite to 105 tests.

### Changed

- made Python 3.11+ the single CLI and automation implementation;
- updated configuration, current documentation and command references;
- consolidated validation, doctor and report generation behind the runtime;
- enabled strict related-asset validation in CI.

### Removed

- 71 legacy `.ps1` command, installer, validation, report and test files;
- three superseded shell-specific GitHub workflows;
- unsafe shared-content generation that overwrote tracked documentation.

---

## [0.5.0] — CLI + Automation Foundation

Status: Foundation Complete  
Release Type: Foundation Release  
Scope: CLI, automation, validation, registry, testing, documentation

---

### Added

#### Root Documentation

Added root-level documentation files:

```text
README.md
QUICKSTART.md
PROJECT_STATUS.md
```

These files define the public entrypoint, quickstart workflow and current state of the repository.

---

#### CLI Foundation

Added the first local Aegis OS CLI layer:

```text
cli/aegis.ps1
cli/COMMANDS.md
cli/CLI_USAGE.md
cli/commands/
```

The CLI supports:

```text
help
version
info
status
validate
doctor
report
registry:list
asset:find
asset:show
asset:related
asset:path
asset:open
skill:list
playbook:list
pattern:list
template:list
domain:list
domain:assets
tag:list
tag:assets
docs:list
release:status
config:path
config:check
config:show
```

---

#### CLI Installation

Added local installation scripts:

```text
install/install-aegis-cli.ps1
install/uninstall-aegis-cli.ps1
install/check-aegis-cli.ps1
cli/CLI_INSTALLATION.md
```

These scripts allow the local command:

```powershell
aegis help
```

instead of:

```powershell
.\cli\aegis.ps1 help
```

---

#### CLI Configuration

Added configuration layer:

```text
config/README.md
config/aegis.config.example.yaml
config/aegis.config.local.example.yaml
cli/CLI_CONFIG.md
cli/commands/config-show.ps1
cli/commands/config-path.ps1
cli/commands/config-check.ps1
```

---

#### CLI Metadata and Output Standards

Added metadata commands and CLI standards:

```text
cli/CLI_OUTPUT_MODEL.md
cli/CLI_EXIT_CODES.md
cli/CLI_METADATA_COMMANDS.md
cli/commands/version.ps1
cli/commands/info.ps1
cli/commands/status.ps1
```

---

#### CLI Smoke Tests

Added CLI smoke testing layer:

```text
scripts/testing/README.md
scripts/testing/test-cli-files.ps1
scripts/testing/test-cli-core-commands.ps1
scripts/testing/test-cli-registry-commands.ps1
scripts/testing/test-cli-asset-commands.ps1
scripts/testing/test-cli-config-commands.ps1
scripts/testing/test-cli-metadata-commands.ps1
scripts/testing/test-cli-smoke.ps1
cli/CLI_TESTING.md
cli/CLI_CONFIG_TESTING.md
cli/CLI_METADATA_TESTING.md
```

---

#### GitHub Actions

Added CI workflows:

```text
.github/workflows/aegis-validation.yml
.github/workflows/aegis-cli-smoke-tests.yml
.github/workflows/CLI_SMOKE_TEST_WORKFLOW.md
```

---

#### Repository Doctor

Added repository health checks:

```text
scripts/doctor/README.md
scripts/doctor/check-repository-structure.ps1
scripts/doctor/check-required-indexes.ps1
scripts/doctor/check-git-status.ps1
scripts/doctor/aegis-doctor.ps1
```

---

#### Registry Validation

Added registry validation scripts:

```text
scripts/validation/validate-yaml.ps1
scripts/validation/validate-paths.ps1
scripts/validation/validate-ids.ps1
scripts/validation/validate-related-assets.ps1
scripts/validation/validate-registry.ps1
scripts/validation/validate-all.ps1
scripts/validation/VALIDATION_GUIDE.md
```

---

#### Registry Reports

Added report generation scripts:

```text
reports/README.md
scripts/reports/README.md
scripts/reports/generate-registry-summary.ps1
scripts/reports/generate-asset-map.ps1
scripts/reports/generate-domain-report.ps1
scripts/reports/generate-release-report.ps1
scripts/reports/generate-all-reports.ps1
```

---

#### Registries

Added machine-readable registries:

```text
registry/skills/skills.registry.yaml
registry/playbooks/playbooks.registry.yaml
registry/patterns/patterns.registry.yaml
registry/templates/templates.registry.yaml
registry/docs/docs.registry.yaml
registry/domains/domains.registry.yaml
registry/tags/tags.registry.yaml
registry/releases/releases.registry.yaml
registry/INDEX.md
```

---

#### Asset Libraries

Completed foundation libraries for:

```text
skills
playbooks
patterns
templates
docs
```

---

### Changed

Improved the repository from a documentation-heavy knowledge base into an operable local framework with:

```text
CLI access
validation
testing
reports
configuration
installation
CI workflows
machine-readable registries
```

---

### Fixed

Improved reliability by adding:

```text
duplicate id detection
missing path detection
related asset validation
CLI file existence checks
CLI command smoke tests
repository structure checks
required index checks
```

---

### Known Limitations

Aegis OS v0.5 does not yet include:

```text
real runtime execution engine
agent execution implementation
package manager behavior
marketplace publishing implementation
SDK implementation
JSON output mode
full cross-platform installer
deep unit test framework
```

---

## [0.4.0] — Automation and Validation

Status: Complete  
Scope: validation scripts, report scripts, doctor scripts, GitHub validation workflow

---

## [0.3.0] — Registry Layer

Status: Complete  
Scope: machine-readable registry files for assets, domains, tags and releases

---

## [0.2.0] — Skills and Execution Assets

Status: Complete  
Scope: skills, playbooks, patterns and templates

---

## [0.1.0] — Documentation Foundation

Status: Complete  
Scope: core documentation, architecture, governance, specifications and references

---

## Final Principle

> Aegis OS v0.5 establishes the repository as locally operable, testable and ready for v1.0 implementation work.
