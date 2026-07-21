# Execution Contract Validation Model

Version: v0.6.0  
Status: validation foundation  
Branch: develop/v0.6-runtime

## Role of this file

This file documents how Aegis OS validates execution contracts before planning or future execution.

The validation model ensures that every contract declares a valid asset, supported modes and explicit safety boundaries.

## Runtime implementation

The contract validator is implemented in:

```text
runtime/src/aegis_runtime/execution/contract_validator.py
```

It validates objects defined in:

```text
runtime/src/aegis_runtime/execution/contracts.py
```

## Validation goals

Contract validation must answer these questions:

```text
Is the target asset identified?
Is the contract type supported?
Is the contract blocked?
Are all execution modes supported?
Is dry-run explicitly available?
Are forbidden actions declared?
Are forbidden action names recognized?
```

## Validation result

Validation returns a `ContractValidationResult`.

The result contains:

```text
contract
issues
errors
warnings
ok
```

The `ok` property is true only when no blocking errors are present.

## Blocking errors

### missing_asset_id

Condition:

```text
The execution contract does not declare a usable asset ID.
```

Result:

```text
Validation failed.
```

### invalid_contract_type

Condition:

```text
The contract type is not playbook or skill.
```

Result:

```text
Validation failed.
```

### blocked_contract

Condition:

```text
The contract safety level is blocked.
```

Result:

```text
Validation failed.
```

### invalid_execution_mode

Condition:

```text
The contract declares an unsupported execution mode.
```

Currently supported modes:

```text
plan
dry-run
```

Result:

```text
Validation failed.
```

## Non-blocking warnings

### dry_run_not_declared

Condition:

```text
The allowed execution modes do not contain dry-run.
```

This warning does not currently block validation.

### no_forbidden_actions

Condition:

```text
The contract does not explicitly declare forbidden actions.
```

A contract without explicit restrictions may be incomplete, even when no immediate error is present.

### unknown_forbidden_action

Condition:

```text
The contract declares a forbidden action that is not part of the known action catalog.
```

This warning helps detect spelling errors or unsupported action names.

## Known forbidden actions

The current action catalog includes:

```text
delete_file
delete_directory
write_file
modify_file
send_email
call_external_api
execute_shell_command
run_untrusted_code
```

## Generated contract behavior

Contracts produced by `ExecutionContractBuilder` should normally validate successfully because they declare:

```text
a valid asset ID
a playbook or skill type
safe-dry-run safety
plan and dry-run modes
explicit forbidden actions
```

Expected result:

```text
Validation: passed
Errors: 0
Warnings: 0
```

## CLI validation

Runtime command:

```console
python -m aegis_runtime --repo-root . execution contract security.review-api-security
```

## Unit tests

The validation model is tested in:

```text
tests/runtime/test_execution_contracts.py
```

The tests cover:

```text
skill contract generation
playbook contract generation
valid generated contracts
blocked contracts
missing dry-run declarations
missing forbidden action declarations
```

## Exit behavior

Expected runtime behavior:

```text
0  contract validation passed
4  contract validation failed
5  target asset was not found
```

## Future validation rules

Future versions may validate:

```text
required input values
output schemas
approval requirements
policy bindings
tool permissions
provider permissions
resource limits
execution timeouts
rollback requirements
artifact declarations
```

## Final principle

> A contract must be structurally valid and explicitly safe before Aegis OS can consider executing it.
