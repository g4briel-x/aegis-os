from pathlib import Path

from aegis_runtime.models import Asset, RegistryDocument
from aegis_runtime.registry_loader import RegistryLoader
from aegis_runtime.validator import RegistryValidator


def test_validator_detects_duplicates_and_missing_paths(tmp_path: Path) -> None:
    document = RegistryDocument(
        path=tmp_path / "registry" / "test.yaml",
        name="test",
        assets=[
            Asset(id="asset.duplicate", path="missing/path", related_assets=["asset.future"]),
            Asset(id="asset.duplicate"),
        ],
    )
    report = RegistryValidator(tmp_path).validate([document])
    error_codes = {issue.code for issue in report.errors}
    warning_codes = {issue.code for issue in report.warnings}
    assert "duplicate_id" in error_codes
    assert "missing_path" in error_codes
    assert "unresolved_related_asset" in warning_codes
    assert not report.ok


def test_validator_accepts_existing_asset_path(tmp_path: Path) -> None:
    (tmp_path / "skills" / "example").mkdir(parents=True)
    document = RegistryDocument(
        path=tmp_path / "registry" / "test.yaml",
        name="test",
        assets=[Asset(id="skills.example", path="skills/example")],
    )
    report = RegistryValidator(tmp_path).validate([document])
    assert report.ok
    assert not report.errors


def test_strict_schema_reports_malformed_documents_and_unsafe_paths(
    tmp_path: Path,
) -> None:
    registry_path = tmp_path / "registry" / "test" / "test.registry.yaml"
    registry_path.parent.mkdir(parents=True)
    registry_path.write_text(
        """
registry:
  id: registry.test
  name: Test Registry
  schema_version: 9.9.9
entries:
  - id: Invalid Identifier
    path: ../outside
  - not-a-mapping
""".strip(),
        encoding="utf-8",
    )

    documents = RegistryLoader(tmp_path).load_all()
    report = RegistryValidator(tmp_path, strict_schema=True).validate(documents)
    error_codes = {issue.code for issue in report.errors}

    assert "unsupported_schema_version" in error_codes
    assert "invalid_registry_entry" in error_codes
    assert "invalid_asset_id" in error_codes
    assert "unsafe_path" in error_codes


def test_permissive_schema_reports_warnings_without_failing(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry" / "test" / "test.registry.yaml"
    registry_path.parent.mkdir(parents=True)
    registry_path.write_text("entries: []\n", encoding="utf-8")

    report = RegistryValidator(tmp_path).validate(RegistryLoader(tmp_path).load_all())
    assert report.ok
    assert {issue.code for issue in report.warnings} == {"missing_registry_metadata"}


def test_repository_registry_passes_strict_validation() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    documents = RegistryLoader(repo_root).load_all()
    report = RegistryValidator(
        repo_root,
        unresolved_related_as_error=True,
        strict_schema=True,
    ).validate(documents)

    issue_summary = "\n".join(
        f"{issue.code}: {issue.message} ({issue.asset_id or '-'})"
        for issue in report.issues
    )
    assert not report.issues, issue_summary
