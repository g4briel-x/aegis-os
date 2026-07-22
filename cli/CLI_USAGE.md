# CLI usage

```text
aegis [--repo-root PATH] [--json] COMMAND ...
```

Repository discovery starts at the current directory unless `--repo-root` is
provided. Global flags appear before the command.

```console
aegis --repo-root . status
aegis --repo-root . --json asset show security.review-api-security
python -m aegis_runtime --repo-root . validate --strict-related
```

Use `--help` at any level to inspect the current parser rather than relying on a
copied command list.
