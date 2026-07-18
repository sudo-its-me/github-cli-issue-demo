import logging

from bulk_issue_importer.clients.github_client import GitHubClient
from bulk_issue_importer.models.config import Config
from bulk_issue_importer.exceptions.github_exceptions import ProjectNotFoundError

class ProjectManager:
    """
    Handles GitHub Project operations.
    """

    def __init__(
        self,
        config: Config,
        github_client: GitHubClient,
    ):
        self.config = config
        self.github_client = github_client
        self.logger = logging.getLogger(__name__)

        self.project_id = None

    def initialize(self) -> None:
        """
        Resolve the GitHub Project ID.
        """

        self.logger.info(
            "Looking up project '%s'...",
            self.config.github_project,
        )

        self.project_id = self.github_client.get_project_id(
            self.config.github_owner,
            self.config.github_project,
        )

        if self.project_id is None:
            raise ProjectNotFoundError(
                f"Project '{self.config.github_project}' not found."
            )

        self.logger.info(
            "Project found (%s)",
            self.project_id,
        )

    def add_issue(self, issue_url: str) -> None:
        """
        Add an issue to the configured project.
        """

        if self.project_id is None:
            raise RuntimeError("ProjectManager not initialized.")

        self.github_client.add_issue_to_project(
            self.project_id,
            issue_url,
        )

        self.logger.info(
            "Added issue to project."
        )