from dataclasses import dataclass


@dataclass(slots=True)
class Config:
    """
    Represents the application's configuration.

    Attributes:
        repository: GitHub repository in the format 'owner/repository'.
        csv_file: Path to the CSV file containing issues.
        dry_run: If True, no changes will be made to GitHub.
        skip_duplicates: Skip creating issues that already exist.
        project_name: GitHub Project name to add created issues to.
    """

    repository: str
    csv_file: str
    dry_run: bool
    skip_duplicates: bool
    project_name: str