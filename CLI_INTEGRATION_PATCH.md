# CLI integration patch

## Role

This patch connects the existing PowerShell entrypoint to the new Python
runtime commands.

Open `cli/aegis.ps1` and add these command routes to the existing dispatch
block, using the same structure as the other commands:

```powershell
'runtime:status' {
    & "$PSScriptRoot\commands\runtime-status.ps1"
    exit $LASTEXITCODE
}

'runtime:validate' {
    & "$PSScriptRoot\commands\runtime-validate.ps1"
    exit $LASTEXITCODE
}
```

Also add these lines to the help output:

```text
runtime:status     Show Python runtime status
runtime:validate   Validate registries with the Python runtime
```

Do not replace the whole `cli/aegis.ps1` file unless its current dispatch
structure has been reviewed first.
