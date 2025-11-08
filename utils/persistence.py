import json
import os

from models.projects import Project
from models.tasks import Task
from models.users import User


def save_data(filename="data/data.json"):
    """Save all users, projects, and tasks to JSON file."""
    try:
        data = {
            "users": [user.to_dict() for user in User.all],
            "projects": [project.to_dict() for project in Project.all],
            "tasks": [task.to_dict() for task in Task.all],
        }

        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)

        # Write to file
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        print(f"✓ Data saved to {filename}")
    except Exception as e:
        print(f"✗ Error saving data: {e}")


def load_data(filename="data/data.json"):
    """Load users, projects, and tasks from JSON file."""
    if not os.path.exists(filename):
        print(f"No data file found at {filename}. Starting fresh.")
        return

    try:
        with open(filename) as f:
            data = json.load(f)

        # Clear existing data
        User.all.clear()
        Project.all.clear()
        Task.all.clear()

        # Recreate objects in order
        users = [User.from_dict(u) for u in data.get("users", [])]
        projects = [Project.from_dict(p) for p in data.get("projects", [])]
        tasks = [Task.from_dict(t, users, projects) for t in data.get("tasks", [])]

        print(
            f"✓ Loaded {len(users)} users, {len(projects)} projects, {len(tasks)} tasks"
        )
    except json.JSONDecodeError:
        print(f"✗ Error: {filename} contains invalid JSON. Starting fresh.")
    except Exception as e:
        print(f"✗ Error loading data: {e}")
