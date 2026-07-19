from bulk_issue_importer.core.command_runner import CommandRunner
from bulk_issue_importer.models.config import Config
from bulk_issue_importer.models.issue import Issue
import json


class GitHubClient:
    """
    Client responsible for interacting with GitHub through the GitHub CLI.
    """

    def __init__(
        self,
        config: Config,
        runner: CommandRunner,
    ):
        self.config = config
        self.runner = runner

    def create_issue(self, issue: Issue) -> str:
        """
        Create a GitHub issue and return its URL.
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
            for label in issue.labels:
                command.extend(["--label", label])

        result = self.runner.run(command)

        return result.stdout.strip()

    def issue_exists(self, title: str) -> bool:
        """
        Check whether a GitHub issue with the given title already exists.
        """

        command = [
            "gh",
            "issue",
            "list",
            "--repo",
            self.config.repository,
            "--state",
            "all",
            "--json",
            "title",
        ]

        result = self.runner.run(command)

        issues = json.loads(result.stdout)

        return any(issue["title"] == title for issue in issues)
   
    def get_project_number(
        self,
        owner: str,
        project_name: str,
    ) -> int | None:
        """
        Get the ID of a GitHub Project V2 by its name.
        """

        command = [
            "gh",
            "project",
            "list",
            "--owner",
            owner,
            "--format",
            "json",
        ]

        result = self.runner.run(command)

        data = json.loads(result.stdout)

        for project in data["projects"]:

            if project["title"] == project_name:
                return project["number"]

        return None
    
    def add_issue_to_project(
        self,
        project_number: int,
        issue_url: str,
    ) -> None:

        command = [
            "gh",
            "project",
            "item-add",
            str(project_number),
            "--owner",
            self.config.github_owner,
            "--url",
            issue_url,
        ]

        self.runner.run(command)

    def get_labels(self) -> set[str]:

        command = [
            "gh",
            "label",
            "list",
            "--repo",
            self.config.repository,
            "--json",
            "name",
        ]

        result = self.runner.run(command)

        labels = json.loads(result.stdout)

        return {label["name"] for label in labels}
    
    def create_label(
        self,
        name: str,
        color: str,
    ) -> None:

        command = [
            "gh",
            "label",
            "create",
            name,
            "--repo",
            self.config.repository,
            "--color",
            color.lstrip("#"),
        ]

        self.runner.run(command)