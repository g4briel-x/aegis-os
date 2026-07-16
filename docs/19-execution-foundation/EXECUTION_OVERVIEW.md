# Aegis OS Execution Foundation

Version: v0.6.0  
Status: planning and dry-run foundation  
Branch: develop/v0.6-runtime

## Role of this file

This file documents the execution foundation introduced in Aegis OS v0.6.

It explains what the execution layer does, what it does not yet do, and how it fits into the Python runtime.

## Purpose

The execution foundation is the first step toward making Aegis OS capable of preparing controlled execution flows for registered assets.

In v0.6, the execution layer can create an execution plan and simulate a dry-run.

It does not yet execute real actions.

## Current execution architecture

```text
PowerShell CLI
      |
      v
Python Runtime
      |
      v
Execution Planner
      |
      v
Execution Plan
      |
      v
Dry-Run Report
```

## Current capabilities

The execution foundation can:

- resolve a target asset by ID;
- create a structured execution plan;
- prepare ordered execution steps;
- include target metadata in the plan;
- simulate execution with a dry-run;
- return a report without running real actions.

## Current commands

Direct Python commands:

```powershell
python -m aegis_runtime execution plan security.review-api-security
python -m aegis_runtime execution dry-run security.review-api-security
```

PowerShell bridge commands:

```powershell
.\cli\aegis.ps1 runtime:execution-plan security.review-api-security
.\cli\aegis.ps1 runtime:execution-dry-run security.review-api-security
```

## Execution plan model

A plan contains:

```text
target asset ID
execution mode
ordered steps
target metadata
step metadata
```

Current step sequence:

```text
1. Resolve target asset
2. Load related assets
3. Validate execution readiness
4. Prepare execution report
```

## Dry-run model

A dry-run creates the same execution plan but does not run real actions.

Expected dry-run message:

```text
Dry-run completed. No actions were executed.
The target asset is ready for planned execution.
```

## Current limitation

The v0.6 execution foundation is not yet a full execution engine.

It does not yet:

- execute playbook instructions;
- run skill logic;
- modify files;
- call AI providers;
- call external tools;
- persist execution history;
- generate full run artifacts.

## Safety principle

The first execution layer is intentionally conservative.

Aegis OS must be able to explain what it intends to do before it performs actions.

Planning and dry-run come before real execution.

## Next step

The next stage is to add:

```text
playbook execution contracts
skill execution contracts
execution reports
execution history
safe action runners
policy checks
```