# Runtime commands

The installed CLI calls `aegis_runtime.cli:main` directly; no bridge layer is
used.

```console
aegis --repo-root . status
aegis --repo-root . registry list
aegis --repo-root . asset find security
aegis --repo-root . validate --strict-related
```

The module entrypoint is equivalent:

```console
python -m aegis_runtime --repo-root . status
```
