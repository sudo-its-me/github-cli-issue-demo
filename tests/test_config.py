from bulk_issue_importer.config_loader import load_config


def test_load_config():
    config = load_config()

    assert config.repository == "sudo-its-me/github-cli-issue-demo"
    assert config.csv_file == "data/tasks.csv"
    assert config.dry_run is False
    assert config.skip_duplicates is True
    assert config.project_name == "GitHub CLI Demo"