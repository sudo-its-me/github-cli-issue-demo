# GitHub Bulk Issue Importer - Setup & Usage Guide

This guide walks through the complete setup and usage of the GitHub Bulk Issue Importer.

---

# What This Tool Does

The application automates the process of importing GitHub Issues from a CSV file.

For every issue in the CSV, the importer can:

* Check if the issue already exists.
* Skip duplicate issues.
* Automatically create missing GitHub labels.
* Create the GitHub Issue.
* Add the newly created issue to a GitHub Project (Project V2).

---

# Prerequisites

Before using the application, ensure you have:

* Python 3.12 or later
* GitHub CLI (`gh`)
* GitHub account
* Authenticated GitHub CLI

Verify:

```bash
python --version
gh --version
gh auth status
```

If you have not authenticated:

```bash
gh auth login
```

---

# Grant Project Permissions

If you plan to add issues to GitHub Projects, your GitHub CLI token must include the **project** scope.

Grant the required permission:

```bash
gh auth refresh -s project
```

Verify:

```bash
gh auth status
```

---

# Repository Setup

The importer creates issues inside the repository specified in the configuration.

Example:

```json
"repository": "sudo-its-me/test-repo"
```

This repository **must already exist**.

The importer does **not** create repositories.

---

# GitHub Project Setup

If you want imported issues to be automatically added to a GitHub Project:

1. Create a GitHub Project (Project V2).
2. Note its name.
3. Configure:

```json
"github_owner": "sudo-its-me",
"github_project": "CAD-Android"
```

The importer automatically:

* Looks up the project.
* Retrieves its Project Number.
* Adds every newly created issue to that project.

If the project cannot be found, the application stops before importing any issues.

---

# Label Configuration

The importer uses:

```text
data/labels.json
```

as the master list of supported labels.

Example:

```json
{
    "bug": "#d73a4a",
    "feature": "#0e8a16",
    "documentation": "#0075ca",
    "frontend": "#1d76db",
    "backend": "#5319e7"
}
```

Each entry consists of:

* Label name
* Label color

---

# Why labels.json exists

The application validates labels before creating them.

This prevents accidental labels such as:

* FrontEnd
* frontend
* front-end
* Front End

Only labels defined in `labels.json` are allowed.

If a label exists in the CSV but not in `labels.json`, the importer stops and reports the unknown label.

---

# CSV Format

Example:

```csv
title,body,labels
Implement Login,Create authentication page,"feature,frontend"
Fix API Error,Handle null response,"bug,backend"
Update README,Improve project documentation,"documentation"
```

Multiple labels are comma-separated.

---

# Configuration

Example:

```json
{
    "repository": "sudo-its-me/test-repo",
    "csv_file": "data/tasks.csv",
    "dry_run": false,
    "skip_duplicates": true,
    "github_owner": "sudo-its-me",
    "github_project": "CAD-Android"
}
```

Configuration fields:

| Field           | Description                                             |
| --------------- | ------------------------------------------------------- |
| repository      | Repository where issues are created                     |
| csv_file        | CSV containing the issues                               |
| dry_run         | Preview import without creating anything                |
| skip_duplicates | Skip issues whose title already exists                  |
| github_owner    | Owner of the GitHub Project                             |
| github_project  | GitHub Project that should receive newly created issues |

---

# Running the Importer

Execute:

```bash
python main.py
```

---

# Import Workflow

The importer performs the following steps:

```text
Load Configuration
        │
        ▼
Read CSV
        │
        ▼
Locate GitHub Project
        │
        ▼
Read Issues
        │
        ▼
Check Duplicate
        │
 ┌──────┴───────┐
 │              │
Exists        Doesn't Exist
 │              │
 ▼              ▼
Skip      Validate Labels
                 │
                 ▼
        Create Missing Labels
                 │
                 ▼
         Create GitHub Issue
                 │
                 ▼
     Add Issue to GitHub Project
                 │
                 ▼
          Print Import Summary
```

---

# Expected Output

Example:

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

Checking: Fix API Error
Skipped duplicate: Fix API Error

=============================================
Import Summary
=============================================
Total Issues : 3
Created      : 2
Skipped      : 1
Failed       : 0
=============================================

Import completed.
```

---

# What Happens on GitHub?

For every new issue:

1. The issue is created in the configured repository.
2. Any missing labels are automatically created.
3. The issue receives all configured labels.
4. The issue is automatically added to the configured GitHub Project.

No manual interaction with GitHub is required.

---

# Common Errors

## Unknown Label

Example:

```text
Unknown label 'frontend'
```

### Solution

Add the label to:

```text
data/labels.json
```

Example:

```json
"frontend": "#1d76db"
```

---

## Project Not Found

Example:

```text
Project 'CAD-Android' not found.
```

### Solution

Verify:

* The project exists.
* The project name matches exactly.
* The project belongs to the configured owner.

---

## Missing GitHub Project Permission

Example:

```text
your authentication token is missing required scopes [project]
```

### Solution

Refresh GitHub CLI authentication:

```bash
gh auth refresh -s project
```

---

## Duplicate Issues

If an issue with the same title already exists, the importer skips it.

Example:

```text
Checking: Implement Login
Skipped duplicate: Implement Login
```

This prevents creating duplicate issues across multiple imports.

---

# Typical Usage

A typical workflow is:

1. Create or choose a GitHub repository.
2. Create a GitHub Project (optional but recommended).
3. Configure the application.
4. Define allowed labels in `data/labels.json`.
5. Prepare `data/tasks.csv`.
6. Run:

```bash
python main.py
```

7. Review the import summary.
8. Verify the created issues and project board on GitHub.

---

# Notes

* The application never creates repositories.
* GitHub Projects must already exist.
* Labels are created automatically only if they are defined in `labels.json`.
* Duplicate issues are skipped based on their title.
* The importer is designed to be safely re-run multiple times without creating duplicate issues.
