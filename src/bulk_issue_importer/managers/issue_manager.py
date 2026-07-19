import logging

from bulk_issue_importer.clients.github_client import GitHubClient
from bulk_issue_importer.models.config import Config
from bulk_issue_importer.models.import_result import ImportResult
from bulk_issue_importer.readers.csv_reader import CSVReader


class IssueManager:

    def __init__(
        self,
        config,
        reader,
        github_client,
        project_manager,
        label_manager,
    ):
        self.config = config
        self.reader = reader
        self.github_client = github_client
        self.project_manager = project_manager
        self.label_manager = label_manager

        self.logger = logging.getLogger(__name__)

    def import_issues(self) -> ImportResult:

        issues = self.reader.read()

        self.logger.info("Loaded %d issues.", len(issues))

        result = ImportResult(
            total=len(issues),
            dry_run=self.config.dry_run,
        )

        for issue in issues:

            self.logger.info("Checking: %s", issue.title)

            if self.github_client.issue_exists(issue.title):

                self.logger.info("Skipped duplicate: %s", issue.title)

                result.skipped += 1
                continue

            if self.config.dry_run:

                self.logger.info("Dry Run -> Would create: %s", issue.title)

                result.would_create += 1
                continue

            for label in issue.labels:
                self.label_manager.ensure_label(label)

            issue_url = self.github_client.create_issue(issue)

            self.logger.info("Created: %s", issue.title)

            self.project_manager.add_issue(issue_url)

            result.created += 1
        return result