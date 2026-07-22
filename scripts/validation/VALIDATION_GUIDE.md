# Registry validation guide

The Python validator checks YAML loading, required metadata, duplicate IDs,
declared paths and related asset references.

```console
python -m aegis_runtime --repo-root . validate
```

For release and CI gates, unresolved related assets are errors:

```console
python -m aegis_runtime --repo-root . validate --strict-related
```

JSON output is available through the global option:

```console
python -m aegis_runtime --repo-root . --json validate --strict-related
```

Exit code `0` means validation passed; exit code `4` means validation issues
prevent acceptance.
