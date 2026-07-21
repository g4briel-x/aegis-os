# CLI command index

| Area | Commands |
| --- | --- |
| Project | `version`, `info`, `status`, `doctor` |
| Registry | `registry list`, `registry domains`, `registry tags`, `docs list`, `release status` |
| Assets | `asset show`, `asset find`, `asset domain`, `asset tag`, `asset type`, `asset related`, `asset path`, `asset open` |
| Configuration | `config show`, `config path`, `config check` |
| Quality | `validate`, `report generate` |
| Generation | `generate skill`, `generate skills` |
| Execution | `execution plan`, `dry-run`, `contract`, `context`, `session`, `session-show`, `orchestrate`, `audit-history`, `audit-verify`, `lifecycle` |

Use `aegis <command> --help` or `aegis <command> <subcommand> --help` for
arguments and choices.

```console
aegis --repo-root . registry list
aegis --repo-root . asset find security
aegis --repo-root . report generate all
aegis --repo-root . execution plan security.review-api-security
```
