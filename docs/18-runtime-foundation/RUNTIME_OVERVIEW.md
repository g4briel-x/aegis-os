# Aegis OS Runtime Foundation

Version: v0.7.0
Status: usable

The Aegis OS runtime is the cross-platform Python layer responsible for
configuration discovery, registry loading, asset resolution, validation,
reporting, generation and controlled execution.

```text
Python CLI
    |
    v
Runtime services
    |
    v
Registry YAML and repository assets
```

The console launchers `aegis` and `aegis-runtime` both call
`aegis_runtime.cli:main`. `python -m aegis_runtime` is the module equivalent.
There is no secondary command bridge.

Runtime modules are separated by responsibility:

- `config.py`: repository discovery and configuration
- `registry_loader.py`: YAML loading and normalization
- `asset_resolver.py`: indexed asset queries
- `validator.py`: integrity checks
- `doctor.py`: repository health checks
- `reports.py`: deterministic Markdown reports
- `generators.py`: safe skill generation
- `execution/`: plans, contracts, contexts, sessions, lifecycle and audits

The runtime targets Python 3.11+ and uses PyYAML. Pytest is included by the
development dependency group.
