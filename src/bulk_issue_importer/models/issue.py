from dataclasses import dataclass, field


@dataclass(slots=True)
class Issue:
    """
    Represents a GitHub Issue.

    Attributes:
        title: Issue title.
        body: Issue description/body.
        labels: List of GitHub labels.
    """

    title: str
    body: str
    labels: list[str] = field(default_factory=list)