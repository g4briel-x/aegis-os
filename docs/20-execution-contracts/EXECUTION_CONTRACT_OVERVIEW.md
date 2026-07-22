# Execution Contract Overview

Version: v0.6.0  
Status: contract foundation  
Branch: develop/v0.6-runtime

## Role of this file

This file documents the execution contract foundation introduced in Aegis OS v0.6.

Execution contracts define the boundaries, inputs, outputs, safety requirements and dependencies of playbooks and skills before any real execution is allowed.

## Purpose

An execution contract provides a machine-readable agreement between an Aegis asset and the runtime.

It answers the following questions:

```text
What asset is being prepared for execution?
Is the asset a playbook or a skill?
Which execution modes are allowed?
Which inputs are required?
Which outputs may be produced?
Which related assets are required?
Which actions are forbidden?
What safety level applies?
```

## Runtime implementation

The execution contract foundation is implemented in:

```text
runtime/src/aegis_runtime/execution/contracts.py
runtime/src/aegis_runtime/execution/contract_builder.py
runtime/src/aegis_runtime/execution/contract_validator.py
```

## Contract types

Current contract types:

```text
playbook
skill
```

### Playbook contract

A playbook contract describes the requirements and restrictions of a multi-step operational workflow.

### Skill contract

A skill contract describes the requirements and restrictions of a reusable capability.

## Contract structure

An execution contract contains:

```text
asset_id
contract_type
safety_level
description
allowed_modes
inputs
outputs
required_assets
forbidden_actions
metadata
```

## Generated contracts

The `ExecutionContractBuilder` generates conservative contracts from registered Aegis assets.

Generated contracts currently:

- allow `plan` and `dry-run`;
- use the `safe-dry-run` safety level;
- declare the target asset as an input;
- declare execution plans and dry-run reports as outputs;
- include related assets as required assets;
- forbid file deletion, file modification, external calls and shell execution.

## Contract validation

The `ExecutionContractValidator` checks:

```text
asset identifier presence
supported contract type
safety level
allowed execution modes
dry-run availability
forbidden action declarations
```

## CLI commands

Runtime command:

```console
python -m aegis_runtime --repo-root . execution contract security.review-api-security
```

## Expected result

```text
Aegis OS Execution Contract
Asset: security.review-api-security
Type: skill
Safety: safe-dry-run
Validation: passed
Errors: 0
```

The exact contract type depends on the registered asset type.

## Current limitation

Execution contracts do not yet authorize real actions.

They currently support planning, validation and dry-run preparation only.

## Next evolution

Future contract capabilities may include:

```text
approval requirements
policy bindings
tool permissions
provider permissions
resource limits
execution timeout
rollback requirements
artifact contracts
audit requirements
```
