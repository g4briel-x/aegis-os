
## FILE: `scripts/testing/README.md`

# Aegis OS — Testing Scripts

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains test scripts for Aegis OS automation and CLI behavior.

The first test layer focuses on CLI smoke tests.

Smoke tests verify that the CLI entrypoint exists, command scripts exist and basic commands execute without immediate failure.

---

# 2. Main Command

Run from repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
```

---

# 3. What Is Tested

```text
CLI entrypoint exists
CLI command files exist
core commands execute
registry commands execute
asset inspection commands execute against known asset ids
```

---

# 4. Final Principle

> Smoke tests should quickly detect broken command wiring before deeper validation begins.