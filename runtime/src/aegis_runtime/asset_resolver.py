"""Asset lookup and filtering services."""

from __future__ import annotations

from collections.abc import Iterable

from .models import Asset, RegistryDocument


class AssetResolver:
    """Provides indexed access to normalized registry assets."""

    def __init__(self, documents: Iterable[RegistryDocument]) -> None:
        self.documents = list(documents)
        self.assets = [asset for document in self.documents for asset in document.assets]
        self._by_id: dict[str, Asset] = {}
        for asset in self.assets:
            if asset.id and asset.id not in self._by_id:
                self._by_id[asset.id] = asset

    def by_id(self, asset_id: str) -> Asset | None:
        return self._by_id.get(asset_id)

    def require(self, asset_id: str) -> Asset:
        asset = self.by_id(asset_id)
        if asset is None:
            raise KeyError(f"Asset not found: {asset_id}")
        return asset

    def find(self, query: str) -> list[Asset]:
        return self.search(query=query)

    def search(
        self,
        *,
        query: str = "",
        domain: str | None = None,
        type_name: str | None = None,
        tags: Iterable[str] = (),
        limit: int | None = None,
    ) -> list[Asset]:
        """Search assets with optional exact domain, type and tag filters."""

        normalized_query = query.strip().lower()
        normalized_domain = domain.strip().lower() if domain else ""
        normalized_type = type_name.strip().lower() if type_name else ""
        normalized_tags = {tag.strip().lower() for tag in tags if tag.strip()}

        matches = (
            asset
            for asset in self.assets
            if (not normalized_query or normalized_query in asset.searchable_text())
            and (not normalized_domain or asset.domain.lower() == normalized_domain)
            and (not normalized_type or asset.type.lower() == normalized_type)
            and (
                not normalized_tags
                or normalized_tags.issubset({tag.lower() for tag in asset.tags})
            )
        )
        results = sorted(matches, key=lambda asset: asset.id)
        return results[:limit] if limit is not None else results

    def by_domain(self, domain: str) -> list[Asset]:
        normalized = domain.strip().lower()
        return sorted(
            (asset for asset in self.assets if asset.domain.lower() == normalized),
            key=lambda asset: asset.id,
        )

    def by_type(self, type_name: str) -> list[Asset]:
        normalized = type_name.strip().lower()
        return sorted(
            (asset for asset in self.assets if asset.type.lower() == normalized),
            key=lambda asset: asset.id,
        )

    def by_tag(self, tag: str) -> list[Asset]:
        normalized = tag.strip().lower()
        return sorted(
            (
                asset
                for asset in self.assets
                if normalized in {item.lower() for item in asset.tags}
            ),
            key=lambda asset: asset.id,
        )

    def related(self, asset_id: str) -> list[Asset]:
        asset = self.require(asset_id)
        return [
            related
            for related_id in asset.related_assets
            if (related := self.by_id(related_id)) is not None
        ]
