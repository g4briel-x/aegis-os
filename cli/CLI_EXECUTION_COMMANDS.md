# Execution commands

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

Planning, contracts and contexts are non-destructive. Session commands persist
state below the configured runtime workspace. Lifecycle reasons are required
for failure and cancellation transitions.
