import subprocess

from bulk_issue_importer.models.config import Config
from bulk_issue_importer.models.issue import Issue


class GitHubClient:
    """
    Wrapper around the GitHub CLI.
    """

    def __init__(self, config: Config):
        self.config = config

    def create_issue(self, issue: Issue) -> None:
        """
        Create a GitHub issue using the GitHub CLI.
        """

        command = [
            "gh",
            "issue",
            "create",
            "--repo",
            self.config.repository,
            "--title",
            issue.title,
            "--body",
            issue.body,
        ]

        if issue.labels:
            command.extend(
                [
                    "--label",
                    ",".join(issue.labels),
                ]
            )

        subprocess.run(command, check=True)