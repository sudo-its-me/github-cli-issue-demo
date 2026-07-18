from bulk_issue_importer.models.issue import Issue


def test_issue_creation():
    issue = Issue(
        title="Test Issue",
        body="This is a test issue."
    )

    assert issue.title == "Test Issue"
    assert issue.body == "This is a test issue."
    assert issue.labels == []