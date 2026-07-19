# GitHub CLI Bulk Issue Importer

This is a Python application that bulk imports GitHub Issues from a CSV file using the GitHub CLI (`gh`).

The application automatically detects duplicate issues, creates missing labels, and adds newly created issues to a GitHub Project (Project V2).

---

# Features

* Bulk import GitHub Issues from a CSV file
* Skip duplicate issues automatically
* Automatically create missing labels
* Add newly created issues to GitHub Projects (Project V2)
* Dry-run mode
* Structured logging
* Dependency Injection
* Command abstraction for GitHub CLI
* Unit tested with pytest

---

# Tech Stack

* Python 3.12
* GitHub CLI (`gh`)
* pytest
* GitHub Projects (Project V2)
* src-layout project structure

---

# Architecture

```text
                  main.py
                      │
                      ▼
               Application
                      │
                      ▼
                IssueManager
        ┌───────────┼────────────┐
        ▼           ▼            ▼
   CSVReader   LabelManager  GitHubClient
                                     │
                                     ▼
                             ProjectManager
                                     │
                                     ▼
                              GitHub CLI (gh)
```

The application communicates exclusively through the GitHub CLI rather than directly using the GitHub REST or GraphQL APIs. Authentication is therefore handled by the GitHub CLI, eliminating the need to manage Personal Access Tokens within the application.

---

# Project Structure

```text
github-bulk-issue-importer/
│
├── data/
├── logs/
├── reports/
├── src/
│   └── bulk_issue_importer/
├── tests/
├── main.py
├── pyproject.toml
├── README.md
├── LICENSE
└── docs/
    └── USAGE.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/sudo-its-me/github-bulk-issue-importer.git
cd github-bulk-issue-importer
```

Create a virtual environment.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project:

```bash
pip install -e .
```

Authenticate GitHub CLI:

```bash
gh auth login
```

---

# Quick Start

 Define allowed labels in `data/labels.json`.
 Prepare `data/tasks.csv`.

Run the importer:

```bash
python main.py
```

For complete setup instructions, configuration, CSV format, troubleshooting, and usage examples, see:

**📖 [docs/USAGE.md](docs/USAGE.md)**

---

# Running Tests

Execute all unit tests:

```bash
pytest
```

---

---

# Future Improvements

Potential future enhancements include:

* Typer-based CLI
* Rich terminal output
* Progress bars
* Enhanced reporting
* Support for additional import formats (JSON, Excel)
* Retry policies for transient GitHub CLI failures
* GitHub Actions CI workflow
* PyPI packaging

---

# License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

---

# Author

**`sudo-its-me`** & Thank you **ChatGPT** for helping me out.



If you found this project useful, consider giving it a ⭐ on GitHub.
