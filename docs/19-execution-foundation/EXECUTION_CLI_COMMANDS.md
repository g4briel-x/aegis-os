# Execution CLI Commands

Version: v0.6.0  
Status: planning and dry-run foundation

## Role of this file

This file documents the execution-related CLI commands introduced in Aegis OS v0.6.

These commands allow Aegis OS to prepare an execution plan and simulate a safe dry-run for a registered asset.

## Python runtime commands

### execution plan

Role: create an execution plan for a registered asset.

```powershell
python -m aegis_runtime execution plan security.review-api-security
```

Expected output:

```text
Aegis OS Execution Plan
Target: security.review-api-security
Mode: plan

1. Resolve target asset
2. Load related assets
3. Validate execution readiness
4. Prepare execution report

Total steps: 4
```

### execution dry-run

Role: simulate an execution without running real actions.

```powershell
python -m aegis_runtime execution dry-run security.review-api-security
```

Expected output:

```text
Aegis OS Execution Dry Run
Status: ready
Dry-run completed. No actions were executed.
```

## PowerShell bridge commands

### runtime:execution-plan

Role: call the Python runtime execution planner from the PowerShell CLI.

```powershell
.\cli\aegis.ps1 runtime:execution-plan security.review-api-security
```

### runtime:execution-dry-run

Role: call the Python runtime dry-run engine from the PowerShell CLI.

```powershell
.\cli\aegis.ps1 runtime:execution-dry-run security.review-api-security
```

## Command behavior

The execution commands currently perform safe planning only.

They do not:

- execute real workflows;
- modify files;
- call external APIs;
- call AI providers;
- write execution history;
- perform irreversible actions.

## Recommended validation sequence

```powershell
python -m aegis_runtime execution plan security.review-api-security
python -m aegis_runtime execution dry-run security.review-api-security
.\cli\aegis.ps1 runtime:execution-plan security.review-api-security
.\cli\aegis.ps1 runtime:execution-dry-run security.review-api-security
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
```

## Exit behavior

Expected behavior:

```text
0  command succeeded
5  target asset not found
```

## Current limitation

The execution CLI is not yet a full playbook runner.

It prepares and explains execution. It does not yet execute playbooks or skills.