# Configuration command testing

Configuration discovery is covered by `tests/runtime/test_config.py` and CLI
regression tests.

```console
python -m pytest tests/runtime/test_config.py tests/runtime/test_cli.py
aegis --repo-root . config check
```
