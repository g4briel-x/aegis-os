# Execution CLI commands

Version: v0.7.0
Status: usable

```console
aegis --repo-root . execution plan <asset-id>
aegis --repo-root . execution dry-run <asset-id>
aegis --repo-root . execution contract <asset-id>
aegis --repo-root . execution context <asset-id> --input name=value
aegis --repo-root . execution session <asset-id>
aegis --repo-root . execution session-show <workspace-or-session-id>
aegis --repo-root . execution orchestrate <workspace-or-session-id>
aegis --repo-root . execution audit-history <workspace-or-session-id>
aegis --repo-root . execution audit-verify <workspace-or-session-id>
aegis --repo-root . execution lifecycle <workspace-or-session-id> <action>
```

Use global `--json` for automation. Asset lookup failures return exit code `5`;
contract, input or lifecycle validation failures return exit code `4`.

Recommended smoke check:

```console
python -m aegis_runtime --repo-root . execution plan security.review-api-security
python -m aegis_runtime --repo-root . execution dry-run security.review-api-security
python -m pytest tests/runtime
```
