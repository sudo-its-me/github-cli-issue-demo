from bulk_issue_importer.config_loader import load_config
from bulk_issue_importer.readers.csv_reader import CSVReader


def test_csv_reader():
    config = load_config()

    reader = CSVReader(config.csv_file)

    issues = reader.read()

    assert len(issues) > 0

    first_issue = issues[0]

    assert first_issue.title != ""
    assert first_issue.body != ""