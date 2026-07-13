## FILE: `cli/CLI_CONFIG.md`

# Aegis OS — CLI Configuration Guide

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This guide explains how configuration works for the Aegis OS CLI.

The configuration layer defines expected folders, registry files, validation entrypoints and report outputs.

---

# 2. Main Configuration File

```text
config/aegis.config.example.yaml
```

Role:

```text
Provides the default configuration model for Aegis OS tooling.
```

---

# 3. Local Configuration File

Optional local override:

```text
config/aegis.config.local.yaml
```

Create it from:

```powershell
Copy-Item config\aegis.config.local.example.yaml config\aegis.config.local.yaml
```

---

# 4. CLI Commands

```powershell
.\cli\aegis.ps1 config:path
.\cli\aegis.ps1 config:show
.\cli\aegis.ps1 config:check
```

---

# 5. Command Roles

## `config:path`

```text
Displays expected configuration file paths.
```

## `config:show`

```text
Displays the main example configuration.
```

## `config:check`

```text
Checks whether expected configuration files exist.
```

---

# 6. Final Principle

> CLI configuration should be explicit before automation starts depending on paths and defaults.
