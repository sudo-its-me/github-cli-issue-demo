# Bulk Issue Importer

A Python-based command-line tool for importing GitHub Issues in bulk from a CSV file using the GitHub CLI (`gh`).

The goal of this project is to evolve from a simple CSV importer into a production-ready automation tool capable of managing GitHub Issues, Labels, Milestones, and GitHub Projects.

---

# Project Goals

* Import GitHub Issues from CSV
* Prevent duplicate issue creation
* Automatically manage labels
* Support multiple assignees
* Support milestones
* Automatically add issues to GitHub Projects
* Support dry-run mode
* Generate import reports
* Keep the code modular, maintainable, and easy to extend

---

# Current Status

## ✅ Completed

* Project structure
* GitHub CLI setup
* Repository creation
* Initial CSV import prototype
* Basic project documentation

## 🚧 In Progress

* Configuration system
* CSV reader
* GitHub client abstraction
* Issue manager

## 📌 Planned

* Duplicate detection
* Label management
* Milestone management
* GitHub Projects integration
* Logging
* Reporting
* Command-line interface
* Unit tests

---

# Project Structure

```text
github-cli-issue-demo/
│
├── main.py                     # Application entry point
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── config.json
│
├── data/
│   ├── tasks.csv               # Working CSV
│   └── sample_tasks.csv        # Example CSV
│
├── logs/
│   └── .gitkeep
│
├── reports/
│   └── .gitkeep
│
├── src/
│   └── bulk_issue_importer/
│       │
│       ├── app.py              # Application orchestration
│       ├── constants.py
│       ├── utils.py
│       ├── __init__.py
│       │
│       ├── clients/
│       │   ├── github_client.py
│       │   └── __init__.py
│       │
│       ├── exceptions/
│       │   ├── github_exceptions.py
│       │   └── validation_exceptions.py
│       │
│       ├── managers/
│       │   ├── issue_manager.py
│       │   ├── label_manager.py
│       │   ├── project_manager.py
│       │   └── __init__.py
│       │
│       ├── models/
│       │   ├── config.py
│       │   ├── issue.py
│       │   └── __init__.py
│       │
│       └── readers/
│           ├── csv_reader.py
│           └── __init__.py
│
└── tests/
    ├── test_csv_reader.py
    └── test_issue_manager.py
```

---

# Architecture

```
                main.py
                    │
                    ▼
                 app.py
                    │
        ┌───────────┼────────────┐
        ▼           ▼            ▼
   CSVReader   IssueManager   GitHubClient
                    │
        ┌───────────┼────────────┐
        ▼           ▼            ▼
 LabelManager  ProjectManager   Config
```

---

# Module Responsibilities

## `main.py`

* Application entry point.
* Starts the application.
* Should remain very small.

---

## `app.py`

* Coordinates the application's workflow.
* Creates and connects the required objects.
* Contains no business logic.

---

## `models`

### `Config`

Represents the application configuration loaded from `config.json`.

### `Issue`

Represents a GitHub Issue throughout the application.

---

## `readers`

### `CSVReader`

Responsible for:

* Reading CSV files
* Validating rows
* Converting rows into `Issue` objects

---

## `clients`

### `GitHubClient`

Responsible for all communication with GitHub through the GitHub CLI.

Examples:

* List issues
* Create issues
* Create labels
* Create milestones
* Add issues to projects

No other module should directly execute `gh` commands.

---

## `managers`

### `IssueManager`

Contains the application's business logic.

Responsibilities include:

* Import issues
* Skip duplicates
* Coordinate issue creation
* Generate import summary

### `LabelManager`

Responsible for label creation and management.

### `ProjectManager`

Responsible for GitHub Project operations.

---

## `exceptions`

Contains custom exceptions used throughout the application.

---

## `utils`

Contains reusable helper functions that don't belong to any specific module.

---

# Configuration

Configuration is stored in `config.json`.

Example:

```json
{
    "repository": "owner/repository",
    "csv_file": "data/tasks.csv",
    "dry_run": false,
    "skip_duplicates": true,
    "project_name": "My Project"
}
```

---

# Development Roadmap

## Version 0.1.0

* [x] Project skeleton
* [x] Folder structure
* [x] Documentation

---

## Version 0.2.0

* [ ] Configuration system

---

## Version 0.3.0

* [ ] CSV Reader

---

## Version 0.4.0

* [ ] GitHub Client

---

## Version 0.5.0

* [ ] Issue Manager

---

## Version 1.0.0

* [ ] Bulk Issue Import

---

## Version 1.1.0

* [ ] Duplicate Detection

---

## Version 1.2.0

* [ ] Label Support

---

## Version 1.3.0

* [ ] Milestone Support

---

## Version 1.4.0

* [ ] GitHub Projects Integration

---

## Version 2.0.0

Production-ready Bulk Issue Importer

Features planned:

* Dry-run mode
* Import reports
* Logging
* Retry mechanism
* Validation
* CLI commands
* Improved testing

---

# Requirements

* Python 3.10+
* GitHub CLI (`gh`)
* GitHub account
* Authenticated GitHub CLI

---

# Development Philosophy

This project is being built incrementally.

Each module will be:

1. Designed
2. Implemented
3. Tested
4. Integrated
5. Committed

before moving to the next module.

The objective is not only to build a useful automation tool but also to demonstrate clean software architecture, modular design, and maintainable Python code.

---

# Future Improvements

* Support multiple CSV formats
* Import from Excel
* Import from JSON
* Support GitHub Enterprise
* Interactive CLI
* Progress bars
* Colored console output
* Configuration profiles
* Packaging and PyPI distribution

---

# License

This project is licensed under the MIT License.
