from pathlib import Path

from aegis_runtime.asset_resolver import AssetResolver
from aegis_runtime.models import Asset, RegistryDocument


def test_asset_resolver_filters_assets() -> None:
    document = RegistryDocument(
        path=Path("registry/test.yaml"),
        name="test",
        assets=[
            Asset(
                id="security.review-api-security",
                name="Review API Security",
                domain="security",
                type="skill",
                tags=["api", "security"],
            ),
            Asset(
                id="engineering.api-contract-template",
                name="API Contract",
                domain="engineering",
                type="template",
                tags=["api"],
            ),
        ],
    )
    resolver = AssetResolver([document])
    assert resolver.by_id("security.review-api-security") is not None
    assert len(resolver.find("contract")) == 1
    assert len(resolver.by_domain("security")) == 1
    assert len(resolver.by_tag("api")) == 2
    assert len(resolver.by_type("skill")) == 1
    assert len(resolver.by_type("template")) == 1
    assert resolver.by_type("skill")[0].id == "security.review-api-security"
