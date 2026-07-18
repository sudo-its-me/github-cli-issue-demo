from bulk_issue_importer.managers.issue_manager import IssueManager
from bulk_issue_importer.models.config import Config
from bulk_issue_importer.models.issue import Issue


class FakeReader:
    def read(self):
        return [
            Issue("Issue 1", "Body 1"),
            Issue("Issue 2", "Body 2"),
            Issue("Issue 3", "Body 3"),
        ]

class FakeProjectManager:
    pass  

class FakeGitHubClient:
    def __init__(self):
        self.created = []
        self.existing = {"Issue 2"}

    def issue_exists(self, title: str) -> bool:
        return title in self.existing

    def create_issue(self, issue: Issue) -> None:
        self.created.append(issue)


def test_import_issues_dry_run():
    config = Config(
        repository="owner/repository",
        csv_file="data/tasks.csv",
        dry_run=False,
        skip_duplicates=True,
        project_name="Demo",
        github_owner="owner",
        github_project="Demo Project",
    )

    reader = FakeReader()
    client = FakeGitHubClient()
    project_manager = FakeProjectManager()

    manager = IssueManager(
        config=config,
        reader=reader,
        github_client=client,
        project_manager=project_manager,
    )

    result = manager.import_issues()

    assert result.total == 3
    assert result.created == 0
    assert result.would_create == 2
    assert result.skipped == 1
    assert result.failed == 0
    assert result.dry_run is True

    assert len(client.created) == 0