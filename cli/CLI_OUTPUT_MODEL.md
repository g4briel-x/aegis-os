# CLI output model

Text is the default human-readable format. The global `--json` option returns
structured output for automation.

```console
aegis --repo-root . --json status
aegis --repo-root . --json asset show engineering.senior-developer
aegis --repo-root . --json validate --strict-related
```

Global options precede the command. Errors remain on standard error and exit
codes remain stable across output formats.
