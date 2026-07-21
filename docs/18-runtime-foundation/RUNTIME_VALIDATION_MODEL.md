# Runtime validation model

Version: v0.7.0
Status: usable

The validator checks machine-readable repository integrity:

- YAML loading errors
- missing and duplicate asset identifiers
- declared asset paths
- related asset references
- aggregate registry loading results

```console
python -m aegis_runtime --repo-root . validate
python -m aegis_runtime --repo-root . validate --strict-related
```

Unresolved relations are warnings by default and blocking errors in strict
mode. CI and release checks use strict mode.

Exit code `0` means validation passed. Exit code `4` means at least one
blocking validation issue exists. Global `--json` returns a structured report
with counts and issue locations.
