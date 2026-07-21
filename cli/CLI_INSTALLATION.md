# CLI installation

Python 3.11 or newer is required.

```console
python -m pip install -e "./runtime[dev]"
aegis version
```

This editable install creates the `aegis` and `aegis-runtime` launchers. No
shell-specific alias or profile edit is needed. Use
`python -m pip uninstall aegis-runtime` to remove the package.
