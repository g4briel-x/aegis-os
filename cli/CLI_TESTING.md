# CLI testing

CLI behavior is tested through the public `main()` entrypoint and repository
regression tests.

```console
python -m pytest tests/runtime
python -m aegis_runtime --repo-root . validate --strict-related
python -m aegis_runtime --repo-root . doctor --skip-reports
```

The CI repeats the suite on Linux, Windows and macOS.
