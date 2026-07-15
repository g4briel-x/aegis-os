"""Registry validation services."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from pathlib import Path

from .models import RegistryDocument, ValidationReport


class RegistryValidator:
    """Validates normalized Aegis registry documents."""

    def __init__(
        self,
        repo_root: str | Path,
        *,
        unresolved_related_as_error: bool = False,
    ) -> None:
        self.repo_root = Path(repo_root).resolve()
        self.unresolved_related_as_error = unresolved_related_as_error

    def validate(self, documents: Iterable[RegistryDocument]) -> ValidationReport:
        document_list = list(documents)
        assets = [asset for document in document_list for asset in document.assets]
        report = ValidationReport(
            registry_count=len(document_list),
            asset_count=len(assets),
        )

        for document in document_list:
            for error in document.errors:
                report.add("error", "yaml_error", error, source_file=document.path)

        for asset in assets:
            if not asset.id:
                report.add(
                    "error",
                    "missing_id",
                    "Registry entry has no identifier.",
                    source_file=asset.source_file,
                )

        counts = Counter(asset.id for asset in assets if asset.id)
        for asset_id, count in sorted(counts.items()):
            if count > 1:
                report.add(
                    "error",
                    "duplicate_id",
                    f"Identifier is declared {count} times.",
                    asset_id=asset_id,
                )

        declared_ids = {asset.id for asset in assets if asset.id}
        for asset in assets:
            if asset.path:
                resolved_path = self._resolve_asset_path(asset.path)
                if not resolved_path.exists():
                    report.add(
                        "error",
                        "missing_path",
                        f"Declared path does not exist: {asset.path}",
                        source_file=asset.source_file,
                        asset_id=asset.id or None,
                    )

            for related_id in asset.related_assets:
                if related_id in declared_ids:
                    continue
                severity = "error" if self.unresolved_related_as_error else "warning"
                report.add(
                    severity,
                    "unresolved_related_asset",
                    f"Related asset is not registered: {related_id}",
                    source_file=asset.source_file,
                    asset_id=asset.id or None,
                )

        return report

    def _resolve_asset_path(self, declared_path: str) -> Path:
        path = Path(declared_path)
        return path if path.is_absolute() else self.repo_root / path
