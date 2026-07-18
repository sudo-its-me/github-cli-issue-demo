import json

from bulk_issue_importer.models.config import Config


def load_config(config_file: str = "config.json") -> Config:
    """
    Load application configuration from a JSON file.

    Args:
        config_file: Path to the configuration file.

    Returns:
        Config object.
    """

    with open(config_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Config(**data)