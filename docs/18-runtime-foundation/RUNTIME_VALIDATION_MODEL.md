# Runtime Validation Model

Version: v0.6.0  
Status: usable

## Role of this file

This file defines the validation model used by the Aegis OS Python runtime.

## Validation goals

The runtime validator checks whether the registry layer is structurally usable by Aegis OS.

It focuses on machine-readable correctness rather than editorial quality.

## Validated elements

The runtime validator checks:

```text
YAML parsing
Asset identifiers
Duplicate identifiers
Declared asset paths
Related asset references
Registry loading results
```

## Blocking errors

The following issues are blocking:

```text
Malformed YAML
Missing asset ID
Duplicate asset ID
Declared asset path does not exist
```

When blocking errors exist, the runtime validation fails.

## Non-blocking warnings

The following issues are warnings in v0.6:

```text
Unresolved related asset references
```

These warnings are currently non-blocking because the documentation registry references conceptual assets that are planned but not yet declared as concrete registry entries.

Examples:

```text
core.identity
core.orchestration
registry.framework
framework.skills
templates.index
```

## Validation command

PowerShell CLI:

```powershell
.\cli\aegis.ps1 runtime:validate
```

Python runtime:

```powershell
python -m aegis_runtime validate
```

## Expected v0.6 result

A successful v0.6 validation may still include warnings.

The important line is:

```text
Validation passed.
```

## Exit behavior

Expected runtime exit behavior:

```text
0  validation passed
4  validation failed because of blocking errors
```

## Current policy

In v0.6, unresolved relations remain warnings.

In v0.7 or v0.8, they may become stricter once conceptual assets are registered in dedicated core or framework registries.

## Future improvements

Planned improvements:

```text
strict relation mode
schema validation
typed registry contracts
machine-readable validation reports
runtime report export
playbook execution validation
```