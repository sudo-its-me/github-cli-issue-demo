from bulk_issue_importer.exceptions.application_exception import ApplicationError


class CSVValidationError(ApplicationError):
    """
    Raised when the CSV file is invalid.
    """

    pass


class ConfigurationError(ApplicationError):
    """
    Raised when the application configuration is invalid.
    """

    pass