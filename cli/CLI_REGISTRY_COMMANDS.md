## FILE: `cli/CLI_REGISTRY_COMMANDS.md`

# Aegis OS — CLI Registry Commands

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This document defines the registry exploration commands for the Aegis OS CLI.

These commands allow maintainers to inspect skills, playbooks, patterns, templates, domains, tags, docs and releases from the terminal.

---

# 2. Commands

```powershell
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

# 3. Role

These commands are lightweight readers.

They do not modify files.  
They read registry files and display useful information for humans.

---

# 4. Future Direction

Later versions can support:

```text
JSON output
filter by domain
filter by tag
filter by maturity
show related assets
validate one asset
open asset path
generate docs from registry
```

---

# 5. Final Principle

> CLI registry commands should make Aegis OS assets discoverable without manually opening YAML files.
