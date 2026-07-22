# Repository doctor

Health checks are part of the Python runtime:

```console
python -m aegis_runtime --repo-root . doctor
```

Use `--skip-validate` or `--skip-reports` for focused diagnostics. The command
returns exit code `0` when structure checks and enabled validation pass.
