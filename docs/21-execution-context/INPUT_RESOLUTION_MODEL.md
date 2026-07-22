# Execution Input Resolution Model

Version: v0.6.0  
Status: input resolution foundation  
Branch: develop/v0.6-runtime

## Role of this file

This file documents the Aegis OS execution input resolution model.

Input resolution converts runtime parameters and contract declarations into structured values that can be attached to an execution context.

## Runtime implementation

The input resolution model is implemented in:

```text
runtime/src/aegis_runtime/execution/input_resolver.py
```

The resolved input model is declared in:

```text
runtime/src/aegis_runtime/execution/context.py
```

Contract input declarations are defined in:

```text
runtime/src/aegis_runtime/execution/contracts.py
```

## Main components

### ExecutionInputResolver

`ExecutionInputResolver` resolves runtime parameters against the inputs declared by an execution contract.

Primary method:

```python
resolve(
    contract: ExecutionContract,
    parameters: dict[str, Any] | None = None,
) -> InputResolutionResult
```

### ResolvedExecutionInput

A resolved input contains:

```text
name
value
source
required
```

### InputResolutionResult

The resolution result contains:

```text
resolved_inputs
issues
errors
warnings
ok
values
```

The `ok` property is true when no blocking error is present.

The `values` property returns resolved inputs as a name-to-value mapping.

## Resolution priority

For every input declared by the execution contract, the resolver applies this priority:

```text
1. Explicit runtime parameter
2. Runtime-generated target asset identifier
3. Contract default value
4. Optional empty value
5. Missing required input error
```

## Parameter source

When a value is explicitly supplied through runtime parameters, the resolved source is:

```text
parameter
```

Example:

```console
python -m aegis_runtime --repo-root . execution context <asset-id> --input scope=public-api
```

Result:

```text
name: scope
value: public-api
source: parameter
```

## Runtime source

The runtime automatically resolves the special input:

```text
target_asset_id
```

Its value is taken from:

```text
contract.asset_id
```

Resolved source:

```text
runtime
```

## Contract default source

When an input is not explicitly supplied but declares a non-null default value, the resolver uses that value.

Resolved source:

```text
contract-default
```

Example contract input:

```python
ExecutionInput(
    name="report_format",
    required=False,
    default="markdown",
)
```

Resolved value:

```text
report_format: markdown
source: contract-default
```

## Optional input source

When an input:

```text
is not supplied
has no default
is not required
```

the resolver creates a resolved input with:

```text
value: null
source: optional
required: false
```

## Missing required input

When a required input:

```text
is not supplied
has no runtime-generated value
has no contract default
```

the resolver produces a blocking error.

Error code:

```text
missing_required_input
```

Example message:

```text
Required input 'scope' was not provided.
```

The missing input is not added to the resolved value mapping.

## Unknown parameters

A runtime parameter is considered unknown when its name is not declared in the execution contract.

Warning code:

```text
unknown_input_parameter
```

Example message:

```text
Parameter 'unexpected' is not declared by the execution contract.
```

Unknown parameters:

```text
remain visible in the original parameters mapping
are not added to resolved_inputs
do not currently block context construction
```

## Duplicate CLI parameters

The runtime CLI rejects duplicate input names before the resolver is called.

Example:

```console
python -m aegis_runtime --repo-root . execution context <asset-id> --input scope=public-api --input scope=internal-api
```

Expected result:

```text
Input error: Execution input 'scope' was provided more than once.
```

## Invalid CLI input syntax

Each CLI input must follow:

```text
NAME=VALUE
```

Invalid example:

```console
--input scope
```

Expected result:

```text
Input error: Invalid execution input 'scope'. Expected NAME=VALUE.
```

An empty input name is also rejected.

Invalid example:

```console
--input =value
```

## Resolution result example

```text
Resolved inputs:
- target_asset_id=security.review-api-security
  source: runtime
  required: true

- scope=public-api
  source: parameter
  required: true

- report_format=markdown
  source: contract-default
  required: false
```

## Serialization

Input resolution results support dictionary serialization:

```python
result.to_dict()
```

Serialized structure:

```text
ok
resolved_inputs
issues
```

Each issue contains:

```text
severity
code
message
input_name
```

## Automated tests

The input resolution model is tested in:

```text
tests/runtime/test_execution_context.py
```

Validated scenarios include:

```text
runtime-generated target asset input
explicit parameter resolution
contract default resolution
missing required input rejection
unknown parameter warning
result serialization
```

## Current limitations

The v0.6 resolver does not yet provide:

```text
type conversion
schema validation
enum validation
range validation
secret resolution
file input validation
nested input structures
environment variable resolution
interactive input collection
```

All CLI values are currently received as strings.

## Future evolution

Future versions may support:

```text
typed inputs
JSON values
boolean and numeric conversion
input schemas
secret references
environment references
validation constraints
parameter aliases
sensitive-value masking
input provenance
```

## Final principle

> Every required contract input must be resolved explicitly, safely and predictably before execution can proceed.
