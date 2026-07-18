from bulk_issue_importer.exceptions.application_exception import ApplicationError


class GitHubCLIError(ApplicationError):
    """
    Raised when a GitHub CLI command fails.
    """

    pass


class ProjectNotFoundError(ApplicationError):
    """
    Raised when the configured GitHub Project cannot be found.
    """

    pass


class LabelNotFoundError(ApplicationError):
    """
    Raised when an invalid label is used.
    """

    pass