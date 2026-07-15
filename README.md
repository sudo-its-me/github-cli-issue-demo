\# GitHub CLI Bulk Issue Creator



A beginner-friendly Python project that demonstrates how to create GitHub Issues in bulk from a CSV file using the GitHub CLI (`gh`).



This project was built as a learning exercise and will gradually evolve into a production-ready automation tool.



\## Features



\* Read issues from a CSV file

\* Create GitHub Issues using the GitHub CLI

\* Simple and easy to understand Python code

\* Works on Windows

\* Great starting point for GitHub automation



\## Project Structure



```text

github-cli-issue-demo/

│

├── create\_issues.py      # Python script

├── tasks.csv             # Input data

├── README.md

└── .gitignore

```



\## Requirements



\* Python 3.10 or later

\* GitHub CLI (`gh`)

\* GitHub account

\* Authenticated GitHub CLI



\## Installation



Clone the repository:



```bash

git clone https://github.com/sudo-its-me/github-cli-issue-demo.git

cd github-cli-issue-demo

```



Verify GitHub CLI is installed:



```bash

gh --version

```



Authenticate:



```bash

gh auth login

```



\## CSV Format



The script expects a CSV file named `tasks.csv`.



Example:



```csv

title,body,labels

Create Login Screen,Design and implement the login UI,frontend

Implement Authentication,Authenticate users using GitHub OAuth,backend

```



Current columns:



| Column | Description              |

| ------ | ------------------------ |

| title  | GitHub Issue title       |

| body   | GitHub Issue description |

| labels | Reserved for future use  |



\## Running the Script



```bash

python create\_issues.py

```



The script will read every row in `tasks.csv` and create a GitHub Issue.



\## Current Status



Implemented:



\* ✅ Read CSV

\* ✅ Create GitHub Issues



Planned:



\* Duplicate detection

\* Automatic label creation

\* Multiple labels

\* Assignees

\* Milestones

\* GitHub Projects integration

\* Dry-run mode

\* Summary report

\* Configuration file support



\## License



This project is for learning purposes.



