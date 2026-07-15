from pathlib import Path

from aegis_runtime.models import Asset, RegistryDocument
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
