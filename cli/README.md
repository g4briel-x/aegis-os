# Aegis OS CLI

The CLI is implemented entirely by the Python package in `runtime/`. Install it
with `python -m pip install -e "./runtime[dev]"`, then run `aegis` from any
operating system.

```console
aegis --repo-root . --help
aegis --repo-root . info
aegis --repo-root . status
aegis --repo-root . validate --strict-related
```

`aegis-runtime` and `python -m aegis_runtime` expose the same command tree.
Global options such as `--repo-root` and `--json` must appear before the command.

See [`COMMANDS.md`](COMMANDS.md) for the command index.
