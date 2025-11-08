# Project Management CLI

A command-line tool for managing projects, users, and tasks.

## How It Works

The tool manages three types of data that work together:

- **Users**: Store username and email. Users can be assigned to tasks.
- **Projects**: Store title and due date. Projects can contain multiple tasks.
- **Tasks**: Store title, status, and assigned user. Tasks can optionally belong to a project.

**Relationships:**

- Tasks are assigned to Users
- Tasks can belong to Projects (optional)
- Projects track how many tasks they contain

Data is automatically saved to `data/data.json` after each operation.

## Setup

Install dependencies with pipenv:

```bash
pipenv install
```

Or with pip:

```bash
pip install -r requirements.txt
```

Run with:

```bash
pipenv run python main.py <command> [arguments]
```

Or if using pip:

```bash
python main.py <command> [arguments]
```

## Commands

### Users

```bash
# Add a user
python main.py add-user <username> <email>

# List users
python main.py list-users
```

### Projects

```bash
# Add a project (date format: YYYY-MM-DD)
python main.py add-project <title> <due_date>

# List projects
python main.py list-projects
```

### Tasks

```bash
# Add a task (project is optional)
python main.py add-task <title> <status> <assigned_to> [project]

# List tasks
python main.py list-tasks
```

## Example

```bash
python main.py add-user alice alice@example.com
python main.py add-project "Website Redesign" 2025-12-15
python main.py add-task "Design homepage" pending alice "Website Redesign"
python main.py add-task "Code review" done alice
python main.py list-tasks
```

## packages used

- Python 3
- argparse (CLI)
- JSON (data storage)
- tabulate (tables)
- rich (colored output)
