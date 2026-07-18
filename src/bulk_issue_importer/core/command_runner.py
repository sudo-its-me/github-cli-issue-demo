import subprocess

from bulk_issue_importer.exceptions.github_exceptions import GitHubCLIError
from bulk_issue_importer.models.command_result import CommandResult


class CommandRunner:
    """
    Executes shell commands.
    """

    @staticmethod
    def run(command: list[str]) -> CommandResult:

        try:

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
            )

            return CommandResult(
                stdout=result.stdout,
                stderr=result.stderr,
                return_code=result.returncode,
            )

        except FileNotFoundError as error:

            raise GitHubCLIError(
                "GitHub CLI (gh) was not found.\n"
                "Please install GitHub CLI and ensure it is available in PATH."
            ) from error

        except subprocess.CalledProcessError as error:

            raise GitHubCLIError(
                f"""
GitHub CLI command failed.

Command:
{' '.join(error.cmd)}

Error:
{error.stderr.strip()}
"""
            ) from error