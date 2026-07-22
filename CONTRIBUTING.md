# Contributing to Aegis OS

Use Python 3.11 or newer and work on a branch created from an up-to-date
`main`.

```console
git switch main
git pull --ff-only
git switch -c type/short-description
python -m pip install -e "./runtime[dev]"
```

Keep changes scoped, preserve registry IDs and add tests for runtime behavior.
Generated reports must be committed when their source registries change.

Before opening a pull request, run:

```console
python -m pytest tests/runtime
python -m aegis_runtime --repo-root . validate --strict-related
python -m aegis_runtime --repo-root . doctor --skip-reports
python -m aegis_runtime --repo-root . report generate all
git diff --check
git status --short
```

Pull requests should explain the intent, affected assets, validation evidence
and any compatibility impact. Never commit credentials, local configuration or
generated execution workspaces.
