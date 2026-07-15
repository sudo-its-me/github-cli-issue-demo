from bulk_issue_importer.models.config import Config

config = Config(
    repository="owner/repo",
    csv_file="data/tasks.csv",
    dry_run=False,
    skip_duplicates=True,
    project_name="Demo"
)

print(config)