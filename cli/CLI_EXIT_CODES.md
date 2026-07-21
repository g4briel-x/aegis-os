# CLI exit codes

| Code | Meaning |
| ---: | --- |
| `0` | Success |
| `2` | Invalid command usage |
| `3` | Repository, configuration or I/O error |
| `4` | Validation, generation safety or execution contract failure |
| `5` | Asset, path, session or workspace not found |

Commands write normal results to standard output and actionable errors to
standard error. JSON mode preserves the same exit-code contract.
