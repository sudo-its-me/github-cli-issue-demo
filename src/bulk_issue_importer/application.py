import logging

from bulk_issue_importer.clients.github_client import GitHubClient
from bulk_issue_importer.config_loader import load_config
from bulk_issue_importer.core.command_runner import CommandRunner
from bulk_issue_importer.logging_config import configure_logging
from bulk_issue_importer.managers.issue_manager import IssueManager
from bulk_issue_importer.readers.csv_reader import CSVReader
from bulk_issue_importer.managers.project_manager import ProjectManager
from bulk_issue_importer.exceptions.application_exception import ApplicationError

class Application:

    def __init__(self):

        configure_logging()

        self.logger = logging.getLogger(__name__)

        self.logger.info("Loading configuration...")

        self.config = load_config()

        self.logger.info("Reading CSV...")

        self.reader = CSVReader(
            self.config.csv_file
        )

        self.runner = CommandRunner()

        self.github_client = GitHubClient(
            config=self.config,
            runner=self.runner,
        )

        self.project_manager = ProjectManager(
            config=self.config,
            github_client=self.github_client,
        )

        self.project_manager.initialize()

        self.issue_manager = IssueManager(
            config=self.config,
            reader=self.reader,
            github_client=self.github_client,
            project_manager=self.project_manager,
        )
        

    def run(self):

        try:

            self.logger.info("Starting import...")

            result = self.issue_manager.import_issues()

            print()
            print("=" * 45)
            print("Import Summary")
            print("=" * 45)
            print(f"Total Issues : {result.total}")
            print(f"Created      : {result.created}")
            print(f"Skipped      : {result.skipped}")
            print(f"Failed       : {result.failed}")

            if result.dry_run:
                print(f"Would Create : {result.would_create}")

            print("=" * 45)

            self.logger.info("Import completed.")

        except ApplicationError as error:

            self.logger.error(error)

            print()
            print("=" * 45)
            print("APPLICATION ERROR")
            print("=" * 45)
            print(error)
            print("=" * 45)

        except Exception:

            self.logger.exception("Unexpected error")

            raise