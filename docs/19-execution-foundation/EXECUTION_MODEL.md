# Execution Model

Version: v0.6.0  
Status: planning and dry-run foundation

## Role of this file

This file documents the internal execution models introduced in the Aegis OS Python runtime.

The execution model defines how Aegis OS represents planned execution before any real action is performed.

## Runtime location

The execution model is implemented in:

```text
runtime/src/aegis_runtime/execution/models.py
```

## ExecutionMode

Role: define the supported execution modes.

Current modes:

```text
plan
dry-run
```

### plan

The `plan` mode creates a structured execution plan for an asset.

It does not execute actions.

### dry-run

The `dry-run` mode simulates execution readiness.

It creates a report showing what would happen, without modifying files or calling external systems.

## ExecutionStatus

Role: define execution state values.

Current statuses:

```text
planned
ready
skipped
failed
```

### planned

The step or plan has been created but not yet evaluated for readiness.

### ready

The step or plan is ready for safe execution or simulation.

### skipped

The step was intentionally skipped.

### failed

The step or plan failed.

## ExecutionStep

Role: represent one ordered step in an execution plan.

A step contains:

```text
index
title
action
asset_id
asset_type
status
metadata
```

Current default execution steps:

```text
1. Resolve target asset
2. Load related assets
3. Validate execution readiness
4. Prepare execution report
```

## ExecutionPlan

Role: represent the full planned execution for one target asset.

A plan contains:

```text
target_asset_id
mode
steps
metadata
```

The plan is designed to be serializable as JSON through the runtime CLI.

## ExecutionReport

Role: represent the result of planning or dry-running an execution.

A report contains:

```text
status
message
plan
```

In v0.6, the dry-run report confirms that no real actions were executed.

## Safety model

The execution model is intentionally conservative.

Aegis OS must first produce an explainable execution plan before it can perform real operations.

This keeps the runtime auditable and safe.

## Future extensions

Future versions may extend the model with:

```text
execution context
input parameters
outputs
artifacts
logs
policy checks
approval requirements
rollback instructions
execution history
```