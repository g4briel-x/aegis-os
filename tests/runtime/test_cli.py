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
    summary: Practical security review guidance.
    tags:
      - api
  - id: domain.security
    name: Security
  - id: tag.api
    name: api
    category: engineering
  - id: docs.runtime-overview
    name: Runtime overview
    type: doc
    path: docs/runtime.md
  - id: release.0.7.0
    name: Python-only runtime
    version: 0.7.0
    status: active
    maturity: usable
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


def test_asset_search_combines_query_and_catalog_filters(tmp_path: Path, capsys) -> None:
    repo_root = _make_repository(tmp_path)

    exit_code = main(
        [
            "--repo-root",
            str(repo_root),
            "--json",
            "asset",
            "search",
            "guidance",
            "--domain",
            "security",
            "--type",
            "skill",
            "--tag",
            "api",
            "--limit",
            "1",
        ]
    )

    assert exit_code == EXIT_OK
    payload = json.loads(capsys.readouterr().out)
    assert [asset["id"] for asset in payload] == ["security.review-api-security"]


def test_python_only_project_commands_are_reachable(tmp_path: Path, capsys) -> None:
    repo_root = _make_repository(tmp_path)

    info_exit_code = main(["--repo-root", str(repo_root), "info"])
    info_output = capsys.readouterr().out
    docs_exit_code = main(["--repo-root", str(repo_root), "docs", "list"])
    docs_output = capsys.readouterr().out
    release_exit_code = main(
        ["--repo-root", str(repo_root), "release", "status"]
    )
    release_output = capsys.readouterr().out

    assert info_exit_code == EXIT_OK
    assert "Runtime: Python" in info_output
    assert "Entrypoints: aegis, aegis-runtime, python -m aegis_runtime" in info_output
    assert docs_exit_code == EXIT_OK
    assert "docs.runtime-overview" in docs_output
    assert "Total assets: 1" in docs_output
    assert release_exit_code == EXIT_OK
    assert "release.0.7.0" in release_output
    assert "status=active" in release_output
    assert "Total releases: 1" in release_output


def test_generate_skill_command_is_reachable(tmp_path: Path, capsys) -> None:
    repo_root = _make_repository(tmp_path)
    definition = repo_root / "generators" / "test-engineer.yaml"
    definition.parent.mkdir(parents=True)
    definition.write_text(
        """
name: Test Engineer
category: Engineering
path: engineering/test-engineer
role: Senior Test Engineer
mission: Make behavior verifiable.
responsibilities: Test design and automation.
expertise: Python and quality engineering.
""".strip(),
        encoding="utf-8",
    )

    exit_code = main(
        [
            "--repo-root",
            str(repo_root),
            "generate",
            "skill",
            "generators/test-engineer.yaml",
        ]
    )

    output = capsys.readouterr().out
    assert exit_code == EXIT_OK
    assert "Generated skill: Test Engineer" in output
    assert (repo_root / "skills" / "engineering" / "test-engineer" / "SKILL.md").is_file()
