from pathlib import Path

from aegis_runtime.registry_loader import RegistryLoader


def test_registry_loader_normalizes_entries(tmp_path: Path) -> None:
    registry_dir = tmp_path / "registry" / "skills"
    registry_dir.mkdir(parents=True)
    (tmp_path / "skills" / "security").mkdir(parents=True)
    registry_file = registry_dir / "skills.registry.yaml"
    registry_file.write_text(
        """
version: 1
entries:
  - id: security.review-api-security
    name: Review API Security
    type: skill
    domain: security
    path: skills/security
    tags:
      - api
      - security
    related_assets:
      - engineering.api-contract-template
""".strip(),
        encoding="utf-8",
    )

    documents = RegistryLoader(tmp_path).load_all()
    assert len(documents) == 1
    assert len(documents[0].assets) == 1
    asset = documents[0].assets[0]
    assert asset.id == "security.review-api-security"
    assert asset.domain == "security"
    assert asset.tags == ["api", "security"]
    assert asset.related_assets == ["engineering.api-contract-template"]
