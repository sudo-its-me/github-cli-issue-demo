import csv

from bulk_issue_importer.models.issue import Issue


class CSVReader:
    """
    Reads issues from a CSV file.
    """

    def __init__(self, csv_file: str):
        self.csv_file = csv_file

    def read(self) -> list[Issue]:
        issues: list[Issue] = []

        with open(self.csv_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Normalize header names (Title -> title, BODY -> body, etc.)
                row = {
                    key.strip().lower(): (value.strip() if value else "")
                    for key, value in row.items()
                }

                labels = []

                if row.get("labels"):
                    labels = [
                        label.strip()
                        for label in row["labels"].split(",")
                        if label.strip()
                    ]

                issues.append(
                    Issue(
                        title=row.get("title", ""),
                        body=row.get("body", ""),
                        labels=labels,
                    )
                )

        return issues