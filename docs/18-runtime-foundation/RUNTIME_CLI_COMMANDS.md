# Runtime CLI commands

Version: v0.7.0
Status: usable

Install the editable package from the repository root:

```console
python -m pip install -e "./runtime[dev]"
```

Core runtime operations:

```console
aegis version
aegis --repo-root . info
aegis --repo-root . status
aegis --repo-root . registry list
aegis --repo-root . asset find security
aegis --repo-root . asset show security.review-api-security
aegis --repo-root . validate --strict-related
```

The module form is equivalent:

```console
python -m aegis_runtime --repo-root . status
```

Recommended verification:

```console
python -m pytest tests/runtime
python -m aegis_runtime --repo-root . validate --strict-related
python -m aegis_runtime --repo-root . doctor --skip-reports
python -m aegis_runtime --repo-root . report generate all
```
