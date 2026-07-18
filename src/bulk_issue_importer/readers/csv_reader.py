import csv
from pathlib import Path

from bulk_issue_importer.models.issue import Issue


class CSVReader:
    """
    Reads a CSV file and converts each row into an Issue object.
    """

    def __init__(self, csv_file: str | Path):
        self.csv_file = Path(csv_file)

    def read(self) -> list[Issue]:
        """
        Read all issues from the CSV file.

        Returns:
            A list of Issue objects.
        """

        issues: list[Issue] = []

        with self.csv_file.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                labels = []

                if row.get("labels"):
                    labels = [
                        label.strip()
                        for label in row["labels"].split(",")
                        if label.strip()
                    ]

                issue = Issue(
                    title=row["title"],
                    body=row["body"],
                    labels=labels,
                )

                issues.append(issue)

        return issues