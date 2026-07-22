# Repository automation

Repository automation is implemented by the `aegis_runtime` Python package and
its pytest suite. This directory retains focused operating guides; executable
logic lives under `runtime/src/aegis_runtime`.

```console
python -m pytest tests/runtime
python -m aegis_runtime --repo-root . validate --strict-related
python -m aegis_runtime --repo-root . doctor --skip-reports
python -m aegis_runtime --repo-root . report generate all
```
