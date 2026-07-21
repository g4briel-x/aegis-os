# Registry reports

Generate every committed registry report with:

```console
python -m aegis_runtime --repo-root . report generate all
```

Individual report names are shown by `report generate --help`. Generated files
are written to `reports/registry/` in deterministic order.
