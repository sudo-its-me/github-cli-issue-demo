from dataclasses import dataclass


@dataclass(slots=True)
class ImportResult:
    """
    Represents the result of an import operation.
    """

    total: int = 0
    created: int = 0
    skipped: int = 0
    failed: int = 0
    dry_run: bool = False
    would_create: int = 0