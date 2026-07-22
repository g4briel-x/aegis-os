# Aegis OS Quickstart

Run every command from the repository root.

## 1. Install

```console
python -m pip install -e "./runtime[dev]"
```

## 2. Inspect the repository

```console
aegis --repo-root . info
aegis --repo-root . status
aegis --repo-root . --help
```

## 3. Search assets

```console
aegis --repo-root . asset find security
aegis --repo-root . asset show engineering.senior-developer
aegis --repo-root . asset path business.pricing-strategy-template
aegis --repo-root . asset domain security
aegis --repo-root . asset tag api
```

## 4. Run quality gates

```console
python -m pytest tests/runtime
aegis --repo-root . validate --strict-related
aegis --repo-root . doctor --skip-reports
aegis --repo-root . report generate all
git diff --exit-code -- reports/registry
```

## 5. Commit through a branch

```console
git switch -c refactor/python-only-runtime
git status --short
git add -A
git commit -m "refactor(runtime): consolidate the CLI in Python"
git push -u origin refactor/python-only-runtime
```

Open a pull request into `main` and wait for the multiplatform Python CI.
