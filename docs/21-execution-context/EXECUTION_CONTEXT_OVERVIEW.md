# Execution Context Overview

Version: v0.6.0  
Status: context foundation  
Branch: develop/v0.6-runtime

## Role of this file

This file documents the Aegis OS execution context foundation.

An execution context represents the resolved runtime state associated with one playbook or skill before any real action is permitted.

## Purpose

The execution context connects:

```text
registered asset
execution contract
execution mode
runtime parameters
resolved inputs
environment metadata
declared artifacts
```

It provides a structured and serializable representation of everything required to prepare an execution.

## Runtime implementation

The execution context foundation is implemented in:

```text
runtime/src/aegis_runtime/execution/context.py
runtime/src/aegis_runtime/execution/input_resolver.py
runtime/src/aegis_runtime/execution/context_builder.py
```

Public exports are declared in:

```text
runtime/src/aegis_runtime/execution/__init__.py
```

## Main components

### ExecutionContext

`ExecutionContext` represents the complete resolved state of an execution.

It contains:

```text
target_asset_id
mode
parameters
resolved_inputs
environment
artifacts
metadata
```

### ResolvedExecutionInput

A resolved input contains:

```text
name
value
source
required
```

Supported input sources currently include:

```text
parameter
runtime
contract-default
optional
```

### ExecutionEnvironment

The environment model records safe local metadata:

```text
environment name
working directory
Python version
platform
environment variables
```

Environment variables are currently not collected automatically.

### ExecutionArtifact

An execution artifact represents an output declared by the execution contract.

Current artifact fields:

```text
name
artifact_type
location
metadata
```

Generated artifacts currently use:

```text
artifact_type: declared-output
status: declared
```

They are declarations only and do not represent files written to disk.

## Context construction flow

The current context construction process is:

```text
1. Resolve the registered asset.
2. Build its execution contract.
3. Validate the execution contract.
4. Parse runtime parameters.
5. Resolve contract inputs.
6. Validate the requested execution mode.
7. Collect local environment metadata.
8. Declare expected output artifacts.
9. Return the execution context build result.
```

## Input resolution

The `ExecutionInputResolver` applies the following priority:

```text
explicit runtime parameter
runtime-generated value
contract default
optional empty value
missing required input error
```

The `target_asset_id` input may be supplied automatically by the runtime.

## Input resolution errors

The current resolver reports an error when:

```text
a required input has no value
```

Error code:

```text
missing_required_input
```

## Input resolution warnings

The resolver reports a warning when a supplied parameter is not declared by the contract.

Warning code:

```text
unknown_input_parameter
```

Unknown parameters remain visible in the original `parameters` mapping but are not added to `resolved_inputs`.

## Context build validation

The context builder checks that the requested mode is included in the execution contract.

Supported modes:

```text
plan
dry-run
```

When the selected mode is not permitted, the builder reports:

```text
execution_mode_not_allowed
```

## CLI commands

Runtime command:

```console
python -m aegis_runtime --repo-root . execution context security.review-api-security
```

Explicit plan mode:

```console
python -m aegis_runtime --repo-root . execution context security.review-api-security --mode plan
```

Runtime parameters:

```console
python -m aegis_runtime --repo-root . execution context <asset-id> --input scope=public-api
```

## Expected output

```text
Aegis OS Execution Context
Target: security.review-api-security
Mode: dry-run
Build: passed

Resolved inputs:
- target_asset_id=security.review-api-security

Environment:
- name: local
- working directory: repository path
- Python: current Python version
- platform: current operating system

Declared artifacts:
- execution_plan
- dry_run_report

Input resolution: passed
Errors: 0
Warnings: 0
```

## Serialization

Execution context objects support dictionary serialization through:

```python
context.to_dict()
result.to_dict()
```

JSON output may be requested with the global runtime option:

```console
python -m aegis_runtime --repo-root . --json execution context security.review-api-security
```

## Current safety boundary

The execution context does not authorize real execution.

Aegis OS v0.6 currently limits context behavior to:

```text
parameter parsing
input resolution
environment inspection
artifact declaration
plan preparation
dry-run preparation
```

No files are created, modified or deleted by the context builder.

No external API or shell action is executed.

## Future evolution

Future versions may add:

```text
typed input schemas
secret references
validated environment profiles
execution identifiers
session identifiers
workspace isolation
artifact persistence
resource limits
approval metadata
policy bindings
audit metadata
```

## Final principle

> An execution context must be complete, validated and safe before any executable action can be considered.
