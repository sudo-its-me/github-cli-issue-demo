from dataclasses import dataclass


@dataclass(slots=True)
class Config:
    repository: str
    csv_file: str
    dry_run: bool
    skip_duplicates: bool
    project_name: str