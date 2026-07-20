from pathlib import Path

from aegis_runtime.asset_resolver import AssetResolver
from aegis_runtime.models import Asset, RegistryDocument
from aegis_runtime.reports import (
    generate_all_reports,
    generate_asset_map,
    generate_domain_report,
    generate_registry_summary,
    generate_release_report,
    generate_report,
)


def _sample_resolver(repo_root: Path) -> tuple[AssetResolver, list[Path]]:
    registry_file = repo_root / "registry" / "skills" / "skills.registry.yaml"
    registry_file.parent.mkdir(parents=True, exist_ok=True)
    registry_file.write_text("entries: []\n", encoding="utf-8")

    document = RegistryDocument(
        path=registry_file,
        name="skills",
        assets=[
            Asset(
                id="security.review-api-security",
                name="Review API Security",
                type="skill",
                domain="security",
                path="skills/security/review-api-security",
                source_file=registry_file,
            ),
            Asset(
                id="release.0.6.0",
                name="Aegis OS v0.6.0",
                domain="",
                source_file=registry_file,
                metadata={
                    "version": "0.6.0",
                    "status": "draft",
                    "maturity": "usable",
                    "summary": "Adds the Python execution runtime.",
                },
            ),
        ],
    )
    resolver = AssetResolver([document])
    return resolver, [registry_file]


def test_generate_registry_summary_counts_entries_per_file(tmp_path: Path) -> None:
    resolver, registry_files = _sample_resolver(tmp_path)
    content = generate_registry_summary(resolver, tmp_path, registry_files)
    assert "Registry files: 1" in content
    assert "Total entries: 2" in content
    assert "skills.registry.yaml" in content


def test_generate_asset_map_lists_assets(tmp_path: Path) -> None:
    resolver, _ = _sample_resolver(tmp_path)
    content = generate_asset_map(resolver, tmp_path)
    assert "security.review-api-security" in content
    assert "Total assets: 2" in content


def test_generate_domain_report_groups_by_domain(tmp_path: Path) -> None:
    resolver, _ = _sample_resolver(tmp_path)
    content = generate_domain_report(resolver, tmp_path)
    assert "### security" in content
    assert "Domains: 1" in content
    # release.0.6.0 has no domain and must not create an empty ### section
    assert "###  " not in content


def test_generate_release_report_reads_metadata_not_type(tmp_path: Path) -> None:
    resolver, _ = _sample_resolver(tmp_path)
    content = generate_release_report(resolver)
    assert "release.0.6.0" in content
    assert "0.6.0" in content
    assert "Adds the Python execution runtime." in content
    # the skill asset must not be picked up as a release
    assert "security.review-api-security" not in content


def test_generate_report_writes_file(tmp_path: Path) -> None:
    resolver, registry_files = _sample_resolver(tmp_path)
    result = generate_report("asset-map", resolver, tmp_path, registry_files)
    assert result.path.exists()
    assert result.path.name == "ASSET_MAP.md"
    assert "security.review-api-security" in result.path.read_text(encoding="utf-8")


def test_generate_all_reports_writes_four_files(tmp_path: Path) -> None:
    resolver, registry_files = _sample_resolver(tmp_path)
    results = generate_all_reports(resolver, tmp_path, registry_files)
    assert len(results) == 4
    for result in results:
        assert result.path.exists()
    names = {result.path.name for result in results}
    assert names == {
        "REGISTRY_SUMMARY.md",
        "ASSET_MAP.md",
        "DOMAIN_REPORT.md",
        "RELEASE_REPORT.md",
    }
