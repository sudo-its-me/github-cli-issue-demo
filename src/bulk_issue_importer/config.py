import json
from pathlib import Path

from bulk_issue_importer.models.config import Config


def load_config(config_path: str | Path = "config.json") -> Config:
    """
    Load the application configuration from a JSON file.

    Args:
        config_path: Path to the configuration file.

    Returns:
        Config: The loaded configuration.
    """

    config_path = Path(config_path)

    with config_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return Config(**data)