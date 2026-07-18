import json

from bulk_issue_importer.clients.github_client import GitHubClient
from bulk_issue_importer.models.config import Config
from bulk_issue_importer.models.issue import Issue


class FakeCommandRunner:

    def __init__(self):
        self.command = None
        self.stdout = "[]"

    def run(self, command):
        self.command = command

        class Result:
            pass

        result = Result()
        result.stdout = self.stdout

        return result


def create_client():
    config = Config(
        repository="owner/repository",
        csv_file="data/tasks.csv",
        dry_run=False,
        skip_duplicates=True,
        project_name="Demo",
        github_owner="owner",
        github_project="Demo Project",
    )

    runner = FakeCommandRunner()

    client = GitHubClient(config, runner)

    return client, runner


def test_create_issue_command():

    client, runner = create_client()

    issue = Issue(
        title="Create Dashboard",
        body="Implement dashboard",
        labels=["frontend", "ui"],
    )

    client.create_issue(issue)

    assert runner.command == [
        "gh",
        "issue",
        "create",
        "--repo",
        "owner/repository",
        "--title",
        "Create Dashboard",
        "--body",
        "Implement dashboard",
        "--label",
        "frontend,ui",
    ]


def test_issue_exists_returns_true():

    client, runner = create_client()

    runner.stdout = json.dumps([
        {"title": "Create Dashboard"},
        {"title": "Fix Navbar"},
    ])

    assert client.issue_exists("Create Dashboard") is True


def test_issue_exists_returns_false():

    client, runner = create_client()

    runner.stdout = json.dumps([
        {"title": "Fix Navbar"},
    ])

    assert client.issue_exists("Create Dashboard") is False