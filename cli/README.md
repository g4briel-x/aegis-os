## FILE: `cli/README.md`

# Aegis OS — CLI Foundation

Version: 0.1.0  
Status: Draft  
Domain: CLI  
Category: Developer Tooling

---

# 1. Purpose

The Aegis OS CLI Foundation provides the first local command interface for interacting with the repository.

The CLI is a PowerShell-based entrypoint that wraps validation, doctor, report and registry inspection scripts.

---

# 2. Why CLI Exists

Before Aegis OS becomes a runtime system or marketplace, it needs a local command layer.

The CLI allows maintainers to run commands such as:

```powershell
.\cli\aegis.ps1 help
.\cli\aegis.ps1 validate
.\cli\aegis.ps1 doctor
.\cli\aegis.ps1 report
.\cli\aegis.ps1 registry:list
.\cli\aegis.ps1 asset:find security
```

---

# 3. CLI Responsibilities

The CLI should:

```text
provide one entrypoint for common commands
wrap validation scripts
wrap doctor scripts
wrap report scripts
read registry files
find assets by keyword
prepare future automation
```

---

# 4. CLI Non-Goals

The first CLI does not:

```text
execute AI agents
install marketplace packages
modify registry files automatically
generate production code
replace Git
replace GitHub Actions
```

---

# 5. Final Principle

> The CLI turns repository operations into repeatable commands.
