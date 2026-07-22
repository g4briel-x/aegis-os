# CLI configuration

The runtime discovers repository configuration through the `config/` directory
and merges supported local overrides.

```console
aegis --repo-root . config path
aegis --repo-root . config check
aegis --repo-root . config show
```

Do not commit local configuration containing machine paths or credentials.
Global `--json` produces structured configuration output.
