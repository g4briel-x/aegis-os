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
        normalized = query.strip().lower()
        if not normalized:
            return []
        return sorted(
            (asset for asset in self.assets if normalized in asset.searchable_text()),
            key=lambda asset: asset.id,
        )

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
