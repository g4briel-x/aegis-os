# Aegis OS CLI Execution Commands

Version: v0.6.0  
Status: planning and dry-run foundation

## Role of this file

This file is the official CLI reference for execution-related commands exposed through the PowerShell CLI.

## Command list

```text
runtime:execution-plan
runtime:execution-dry-run
```

## runtime:execution-plan

Role: create an execution plan for a registered Aegis asset.

```powershell
.\cli\aegis.ps1 runtime:execution-plan security.review-api-security
```

This command delegates to the Python runtime:

```powershell
python -m aegis_runtime execution plan security.review-api-security
```

Expected behavior:

```text
Aegis OS Execution Plan
Target: security.review-api-security
Mode: plan
Total steps: 4
```

## runtime:execution-dry-run

Role: simulate an execution plan without running real actions.

```powershell
.\cli\aegis.ps1 runtime:execution-dry-run security.review-api-security
```

This command delegates to the Python runtime:

```powershell
python -m aegis_runtime execution dry-run security.review-api-security
```

Expected behavior:

```text
Aegis OS Execution Dry Run
Status: ready
Dry-run completed. No actions were executed.
```

## Safety behavior

The execution commands introduced in v0.6 are safe by design.

They do not:

- modify files;
- call external APIs;
- execute playbooks;
- run skills;
- call AI providers;
- perform irreversible operations.

## Validation

Recommended validation sequence:

```powershell
.\cli\aegis.ps1 runtime:execution-plan security.review-api-security
.\cli\aegis.ps1 runtime:execution-dry-run security.review-api-security
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-runtime-commands.ps1
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
```

## Future scope

Future versions may add:

```text
runtime:playbook-run
runtime:skill-run
runtime:execution-report
runtime:execution-history
runtime:execution-approve
runtime:execution-rollback
```