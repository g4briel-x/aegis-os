## FILE: `cli/CLI_TESTING.md`

# Aegis OS — CLI Testing Guide

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This guide explains how to test the Aegis OS CLI locally.

The CLI should be tested whenever command routing, command scripts or registry files change.

---

# 2. Main Smoke Test

Run from repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
```

---

# 3. Individual Tests

## File Test

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-files.ps1
```

Role:

```text
Checks that the expected CLI files exist.
```

---

## Core Command Test

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-core-commands.ps1
```

Role:

```text
Checks that basic commands like help and registry:list work.
```

---

## Registry Command Test

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-registry-commands.ps1
```

Role:

```text
Checks that registry list commands execute.
```

---

## Asset Command Test

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-asset-commands.ps1
```

Role:

```text
Checks that asset search, show, related, path, domain and tag commands execute.
```

---

# 4. Recommended Workflow

Before pushing CLI changes:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
git status
git add .
git commit -m "..."
git push
```

---

# 5. Final Principle

> CLI smoke tests confirm that the command layer is usable before future runtime features depend on it.