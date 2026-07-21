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


def test_repository_registry_passes_strict_validation() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    documents = RegistryLoader(repo_root).load_all()
    report = RegistryValidator(
        repo_root,
        unresolved_related_as_error=True,
    ).validate(documents)

    issue_summary = "\n".join(
        f"{issue.code}: {issue.message} ({issue.asset_id or '-'})"
        for issue in report.issues
    )
    assert not report.issues, issue_summary
