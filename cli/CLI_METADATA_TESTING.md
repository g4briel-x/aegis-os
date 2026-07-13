## FILE: `cli/CLI_METADATA_TESTING.md`

# Aegis OS — CLI Metadata Testing

Version: 0.1.0  
Status: Draft  
Domain: CLI  
Category: Testing

---

# 1. Purpose

This guide explains how to test the Aegis OS CLI metadata commands.

The metadata command layer includes:

```text
version
info
status
```

These commands provide identity, version and lightweight repository status information.

---

# 2. Main Test

Run from repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-metadata-commands.ps1
```

---

# 3. Commands Tested

```powershell
.\cli\aegis.ps1 version
.\cli\aegis.ps1 info
.\cli\aegis.ps1 status
```

---

# 4. Expected Behavior

## `version`

Expected result:

```text
Displays the current Aegis OS CLI version.
```

---

## `info`

Expected result:

```text
Displays project identity, important folders and core entrypoints.
```

---

## `status`

Expected result:

```text
Runs a lightweight repository status check and reports missing files if any.
```

---

# 5. Smoke Test Integration

This test should be included in:

```text
scripts/testing/test-cli-smoke.ps1
```

Expected list:

```powershell
$tests = @(
    "test-cli-files.ps1",
    "test-cli-core-commands.ps1",
    "test-cli-registry-commands.ps1",
    "test-cli-asset-commands.ps1",
    "test-cli-config-commands.ps1",
    "test-cli-metadata-commands.ps1"
)
```

---

# 6. CI Integration

No workflow file change is required if GitHub Actions already runs:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
```

Once the smoke test includes `test-cli-metadata-commands.ps1`, CI will automatically test metadata commands.

---

# 7. Final Principle

> Metadata commands should be tested because users depend on them to understand the local repository state.
```