from __future__ import annotations

import json

from .models import ValidationResult


def validation_markdown(result: ValidationResult) -> str:
    lines = [
        "# Validation Report",
        "",
        f"- Skills checked: {result.skills_checked}",
        f"- Errors: {len(result.errors)}",
        f"- Warnings: {len(result.warnings)}",
        f"- Status: {'PASS' if result.is_valid else 'FAIL'}",
        "",
    ]
    if result.issues:
        lines.extend(
            [
                "## Issues",
                "",
                "| Severity | Code | Path | Message |",
                "|---|---|---|---|",
            ]
        )
        for issue in result.issues:
            message = issue.message.replace("|", "\\|")
            lines.append(
                f"| {issue.severity} | `{issue.code}` | `{issue.path}` | {message} |"
            )
    else:
        lines.append("No issues found.")
    return "\n".join(lines) + "\n"


def validation_json(result: ValidationResult) -> str:
    payload = {
        "skills_checked": result.skills_checked,
        "errors": len(result.errors),
        "warnings": len(result.warnings),
        "status": "pass" if result.is_valid else "fail",
        "issues": [issue.__dict__ for issue in result.issues],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
