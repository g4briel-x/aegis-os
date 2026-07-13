## FILE: `cli/CLI_CONFIG_TESTING.md`

# Aegis OS — CLI Configuration Testing

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This guide explains how to test the CLI configuration layer.

The configuration layer includes:

```text
config/aegis.config.example.yaml
config/aegis.config.local.example.yaml
cli/commands/config-path.ps1
cli/commands/config-check.ps1
cli/commands/config-show.ps1
```

---

# 2. Main Test

Run from repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-config-commands.ps1
```

---

# 3. Commands Tested

```powershell
.\cli\aegis.ps1 config:path
.\cli\aegis.ps1 config:check
.\cli\aegis.ps1 config:show
```

---

# 4. Expected Behavior

## `config:path`

Expected result:

```text
Shows expected configuration file paths.
```

## `config:check`

Expected result:

```text
Confirms required configuration example files exist.
```

## `config:show`

Expected result:

```text
Prints config/aegis.config.example.yaml.
```

---

# 5. Smoke Test Integration

The configuration command test should be included in:

```text
scripts/testing/test-cli-smoke.ps1
```

This ensures configuration commands are tested with the rest of the CLI.

---

# 6. Final Principle

> Configuration commands should be tested because future CLI behavior will depend on stable paths and defaults.
```