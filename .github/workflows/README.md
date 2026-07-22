# Aegis OS — GitHub Workflows

Version: 0.7.0
Status: Active

The repository uses one Python-only workflow:

```text
.github/workflows/aegis-ci.yml
```

It runs on pushes and pull requests to `main`, and can also be started
manually. The job executes on Linux, Windows and macOS with Python 3.11.

The workflow installs `runtime[dev]`, runs all runtime tests, exercises the
public CLI, performs strict registry validation, runs repository health checks,
regenerates reports and verifies that committed reports are current.

> Validation should run before broken metadata reaches the main branch.
