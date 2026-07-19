import json
import logging
from pathlib import Path

from bulk_issue_importer.clients.github_client import GitHubClient
from bulk_issue_importer.models.config import Config


class LabelManager:
    """
    Handles GitHub label management.
    """

    def __init__(
        self,
        config: Config,
        github_client: GitHubClient,
    ):
        self.config = config
        self.github_client = github_client
        self.logger = logging.getLogger(__name__)

        self.available_labels = {}
        self.github_labels = set()

    def load(self) -> None:
        """
        Load allowed labels from labels.json.
        """

        with open(
            Path("data") / "labels.json",
            encoding="utf-8",
        ) as file:

            self.available_labels = json.load(file)

    def initialize(self) -> None:
        """
        Load labels from configuration and GitHub.
        """

        self.load()

        self.github_labels = self.github_client.get_labels()

    def ensure_label(self, label: str) -> None:

        if label not in self.available_labels:

            raise ValueError(
                f"Unknown label '{label}'."
            )

        if label in self.github_labels:
            return

        color = self.available_labels[label]

        self.logger.info("Creating label: %s", label)

        self.github_client.create_label(
            label,
            color,
        )

        self.github_labels.add(label)