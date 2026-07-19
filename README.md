# GitHub CLI Bulk Issue Importer

A production-ready Python application that bulk imports GitHub Issues from a CSV file using the GitHub CLI (`gh`).

The application automatically detects duplicate issues, creates missing labels, and adds newly created issues to a GitHub Project (Project V2).

Beyond solving a practical automation problem, this project demonstrates clean software architecture, dependency injection, command abstraction, structured logging, and unit testing.

---

# Why This Project?

Creating and organizing a large number of GitHub Issues manually is repetitive and time-consuming. This tool automates the complete workflow by reading issues from a CSV file, ensuring required labels exist, creating the issues, and placing them into a GitHub Project.

The project was also developed as a portfolio project to demonstrate good software engineering practices rather than simply scripting GitHub CLI commands.

---

# Features

* Bulk import GitHub Issues from CSV
* Skip duplicate issues
* Automatically create missing labels
* Add issues to GitHub Projects (Project V2)
* Dry-run mode
* Structured logging
* Clean modular architecture
* Dependency Injection
* Unit tested with pytest

---

# Tech Stack

* Python 3.12
* GitHub CLI (`gh`)
* pytest
* GitHub Projects (Project V2)
* src-layout project structure

---

# Project Architecture

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

The application uses the GitHub CLI instead of directly interacting with the GitHub REST or GraphQL APIs. Authentication is therefore managed by the GitHub CLI, eliminating the need to store or manage Personal Access Tokens within the application.

---

# Project Structure

```text
github-cli-issue-demo/
│
├── data/
│   ├── labels.json
│   ├── sample_tasks.csv
│   └── tasks.csv
│
├── logs/
├── reports/
│
├── src/
│   └── bulk_issue_importer/
│       │
│       ├── application.py
│       ├── config_loader.py
│       ├── logging_config.py
│       │
│       ├── clients/
│       │   └── github_client.py
│       │
│       ├── core/
│       │   └── command_runner.py
│       │
│       ├── exceptions/
│       │   ├── application_exception.py
│       │   ├── github_exceptions.py
│       │   └── validation_exceptions.py
│       │
│       ├── managers/
│       │   ├── issue_manager.py
│       │   ├── label_manager.py
│       │   └── project_manager.py
│       │
│       ├── models/
│       │   ├── command_result.py
│       │   ├── config.py
│       │   ├── import_result.py
│       │   └── issue.py
│       │
│       └── readers/
│           └── csv_reader.py
│
├── tests/
├── main.py
├── pyproject.toml
├── README.md
└── LICENSE
```

---

# Module Responsibilities

## `main.py`

* Application entry point.
* Starts the application.
* Delegates execution to the `Application` class.

---

## `application.py`

Responsible for:

* Loading configuration
* Initializing dependencies
* Coordinating the application's workflow

Contains no business logic.

---

## `CSVReader`

Responsible for:

* Reading CSV files
* Validating CSV rows
* Converting rows into `Issue` objects

---

## `IssueManager`

Contains the application's business logic.

Responsibilities include:

* Import issues
* Skip duplicate issues
* Coordinate label creation
* Coordinate issue creation
* Generate import summary

---

## `LabelManager`

Responsible for:

* Checking whether labels exist
* Automatically creating missing labels

---

## `ProjectManager`

Responsible for:

* Looking up the configured GitHub Project
* Adding newly created issues to the project

---

## `GitHubClient`

Responsible for all communication with GitHub through the GitHub CLI.

Examples include:

* List issues
* Create issues
* List labels
* Create labels
* List projects
* Add issues to projects

No other module directly executes `gh` commands.

---

## `CommandRunner`

Provides an abstraction over subprocess execution, making GitHub CLI interactions easier to test.

---

# Prerequisites

Before running the application, install:

* Python 3.12 or later
* GitHub CLI (`gh`)

Verify installation:

```bash
python --version
gh --version
```

Authenticate with GitHub:

```bash
gh auth login
```

Verify authentication:

```bash
gh auth status
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/sudo-its-me/github-cli-issue-demo.git
cd github-cli-issue-demo
```

Create a virtual environment.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project:

```bash
pip install -e .
```

---

# Configuration

The application loads its configuration through the configuration loader.

Example configuration:

| Setting         | Description            |
| --------------- | ---------------------- |
| Repository      | GitHub repository      |
| CSV File        | CSV containing issues  |
| GitHub Owner    | GitHub Project owner   |
| GitHub Project  | GitHub Project name    |
| Dry Run         | Preview mode           |
| Skip Duplicates | Ignore existing issues |

---

# CSV Format

Example:

```csv
title,body,labels
Implement Login,Create login page,"feature,frontend"
Fix API Error,Handle null response,"bug,backend"
Update README,Improve documentation,"documentation"
```

Labels may contain multiple comma-separated values.

---

# Workflow

For every issue in the CSV:

1. Read CSV data.
2. Check whether the issue already exists.
3. Skip duplicate issues.
4. Ensure all required labels exist.
5. Create missing labels.
6. Create the GitHub Issue.
7. Add the issue to the configured GitHub Project.
8. Print the import summary.

---

# Running the Application

```bash
python main.py
```

---

# Example Output

```text
Loading configuration...
Reading CSV...
Looking up project 'CAD-Android'...
Project found (2)

Starting import...
Loaded 3 issues.

Checking: Implement Login
Created: Implement Login
Added issue to project.

=============================================
Import Summary
=============================================
Total Issues : 3
Created      : 3
Skipped      : 0
Failed       : 0
=============================================

Import completed.
```

---

# Running Tests

Run all unit tests:

```bash
pytest
```

---

# Current Status

## ✅ Implemented

* CSV import
* Duplicate detection
* Automatic label creation
* GitHub Project (Project V2) integration
* Dry-run mode
* Structured logging
* Dependency Injection
* Command abstraction
* Custom exception hierarchy
* Unit tests

---

# Development Philosophy

This project was built incrementally, with each module being:

1. Designed
2. Implemented
3. Tested
4. Integrated
5. Committed

The focus throughout development was on clean architecture, modular design, maintainability, and testability rather than simply achieving the required functionality.

---

# Future Improvements

Potential future enhancements include:

* Support for additional import formats (JSON, Excel)
* Retry policies for transient GitHub CLI failures
* Enhanced import reporting
* GitHub Actions CI workflow

---

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

# Author

**sudo-its-me** & Thank you **ChatGPT** for helping me out

If you found this project useful, consider giving it a ⭐ on GitHub.
