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


def test_validator_flags_missing_id() -> None:
    document = RegistryDocument(
        path=Path("registry/test.yaml"),
        name="test",
        assets=[Asset(id="", name="No id here")],
    )
    report = RegistryValidator(Path(".")).validate([document])
    assert not report.ok
    assert {issue.code for issue in report.errors} == {"missing_id"}
    # An asset with no id must not also be counted as a duplicate.
    assert "duplicate_id" not in {issue.code for issue in report.issues}


def test_validator_strict_related_promotes_warning_to_error() -> None:
    document = RegistryDocument(
        path=Path("registry/test.yaml"),
        name="test",
        assets=[Asset(id="asset.one", related_assets=["asset.missing"])],
    )

    lenient_report = RegistryValidator(
        Path("."), unresolved_related_as_error=False
    ).validate([document])
    assert lenient_report.ok
    assert {issue.code for issue in lenient_report.warnings} == {
        "unresolved_related_asset"
    }

    strict_report = RegistryValidator(
        Path("."), unresolved_related_as_error=True
    ).validate([document])
    assert not strict_report.ok
    assert {issue.code for issue in strict_report.errors} == {
        "unresolved_related_asset"
    }


def test_validator_records_yaml_errors_from_documents() -> None:
    document = RegistryDocument(
        path=Path("registry/broken.yaml"),
        name="broken",
        errors=["while parsing a block mapping"],
    )
    report = RegistryValidator(Path(".")).validate([document])
    assert not report.ok
    assert [issue.code for issue in report.errors] == ["yaml_error"]
    assert report.registry_count == 1
    assert report.asset_count == 0


def test_validator_accepts_absolute_asset_path_inside_repo_root(
    tmp_path: Path,
) -> None:
    absolute_target = (
        tmp_path
        / "skills"
        / "example"
    )
    absolute_target.mkdir(
        parents=True
    )

    document = RegistryDocument(
        path=(
            tmp_path
            / "registry"
            / "test.yaml"
        ),
        name="test",
        assets=[
            Asset(
                id="skills.example",
                path=str(
                    absolute_target
                ),
            )
        ],
    )

    report = RegistryValidator(
        tmp_path
    ).validate(
        [document]
    )

    assert report.ok
    assert not report.errors


def test_validator_rejects_absolute_asset_path_outside_repo_root(
    tmp_path: Path,
) -> None:
    repo_root = tmp_path / "repository"
    repo_root.mkdir()

    outside_target = (
        tmp_path
        / "outside"
        / "skills"
        / "example"
    )
    outside_target.mkdir(
        parents=True
    )

    document = RegistryDocument(
        path=(
            repo_root
            / "registry"
            / "test.yaml"
        ),
        name="test",
        assets=[
            Asset(
                id="skills.example",
                path=str(
                    outside_target
                ),
            )
        ],
    )

    report = RegistryValidator(
        repo_root
    ).validate(
        [document]
    )

    assert not report.ok
    assert {
        issue.code
        for issue in report.errors
    } == {
        "unsafe_path"
    }


def test_validator_aggregates_counts_across_documents() -> None:
    first = RegistryDocument(
        path=Path("registry/a.yaml"),
        name="a",
        assets=[Asset(id="a.one")],
    )
    second = RegistryDocument(
        path=Path("registry/b.yaml"),
        name="b",
        assets=[Asset(id="b.one"), Asset(id="b.two")],
    )
    report = RegistryValidator(Path(".")).validate([first, second])
    assert report.registry_count == 2
    assert report.asset_count == 3
    assert report.ok


def test_validation_report_to_dict_shape() -> None:
    document = RegistryDocument(
        path=Path("registry/test.yaml"),
        name="test",
        assets=[Asset(id="asset.duplicate"), Asset(id="asset.duplicate")],
    )
    report = RegistryValidator(Path(".")).validate([document])
    payload = report.to_dict()

    assert payload["ok"] is False
    assert payload["registry_count"] == 1
    assert payload["asset_count"] == 2
    assert payload["error_count"] == 1
    assert payload["warning_count"] == 0
    assert payload["issues"][0]["code"] == "duplicate_id"
