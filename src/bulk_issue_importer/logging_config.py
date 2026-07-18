import logging
from pathlib import Path


def configure_logging() -> None:
    """
    Configure application logging.
    """

    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    log_file = log_directory / "bulk_issue_importer.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )