# CI testing guide

`.github/workflows/aegis-ci.yml` runs the Python runtime on Linux, Windows and
macOS with Python 3.11.

The job installs `runtime[dev]`, runs pytest, exercises public CLI commands,
performs strict registry validation, runs the doctor and verifies generated
reports.

Local equivalent:

```console
python -m pip install -e "./runtime[dev]"
python -m pytest tests/runtime
python -m aegis_runtime --repo-root . validate --strict-related
python -m aegis_runtime --repo-root . doctor --skip-reports
python -m aegis_runtime --repo-root . report generate all
git diff --exit-code -- reports/registry
```
