from bulk_issue_importer.config import load_config
from bulk_issue_importer.models.issue import Issue
from bulk_issue_importer.clients.github_client import GitHubClient

config = load_config()

client = GitHubClient(config)

issue = Issue(
    title="Test From GitHubClient",
    body="This issue was created using the GitHubClient class."
)

client.create_issue(issue)