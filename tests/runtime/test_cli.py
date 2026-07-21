import json
from pathlib import Path

from aegis_runtime.cli import EXIT_OK, main


def _make_repository(tmp_path: Path) -> Path:
    registry_dir = tmp_path / "registry" / "test"
    registry_dir.mkdir(parents=True)
    (tmp_path / "skills" / "security").mkdir(parents=True)
    (registry_dir / "test.registry.yaml").write_text(
        """
entries:
  - id: security.review-api-security
    name: Review API Security
    type: skill
    domain: security
    path: skills/security
    tags:
      - api
  - id: domain.security
    name: Security
  - id: tag.api
    name: api
    category: engineering
""".strip(),
        encoding="utf-8",
    )
    return tmp_path


def test_asset_show_command_is_reachable(tmp_path: Path, capsys) -> None:
    repo_root = _make_repository(tmp_path)

    exit_code = main(
        [
            "--repo-root",
            str(repo_root),
            "--json",
            "asset",
            "show",
            "security.review-api-security",
        ]
    )

    assert exit_code == EXIT_OK
    payload = json.loads(capsys.readouterr().out)
    assert payload["id"] == "security.review-api-security"
    assert payload["type"] == "skill"


def test_registry_catalog_commands_are_reachable(tmp_path: Path, capsys) -> None:
    repo_root = _make_repository(tmp_path)

    domains_exit_code = main(
        ["--repo-root", str(repo_root), "registry", "domains"]
    )
    domains_output = capsys.readouterr().out

    tags_exit_code = main(
        ["--repo-root", str(repo_root), "registry", "tags"]
    )
    tags_output = capsys.readouterr().out

    assert domains_exit_code == EXIT_OK
    assert "domain.security" in domains_output
    assert "Total domains: 1" in domains_output
    assert tags_exit_code == EXIT_OK
    assert "tag.api" in tags_output
    assert "Total tags: 1" in tags_output
