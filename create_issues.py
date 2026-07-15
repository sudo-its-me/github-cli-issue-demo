import csv
import subprocess

CSV_FILE = "tasks.csv"

with open(CSV_FILE, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"]
        body = row["body"]

        print(f"Creating issue: {title}")

        command = [
            "gh",
            "issue",
            "create",
            "--title",
            title,
            "--body",
            body,
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Success")
            print(result.stdout)
        else:
            print("❌ Failed")
            print(result.stderr)