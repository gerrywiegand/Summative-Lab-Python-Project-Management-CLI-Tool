import argparse

import utils as u

# Load existing data at startup
u.load_data()

parser = argparse.ArgumentParser(description="Project Management CLI Tool")
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser("add-user", help="Add a new user")
add_parser.add_argument("username", type=str, help="Username of the user")
add_parser.add_argument("email", type=str, help="Email of the user")
add_parser.set_defaults(func=u.add_user)
add_parser = subparsers.add_parser("list-users", help="List all users")
add_parser.set_defaults(func=u.list_users)


add_parser = subparsers.add_parser("add-project", help="Add a new project")
add_parser.add_argument("title", type=str, help="Title of the project")
add_parser.add_argument(
    "due_date", type=str, help="Due date of the project (format: YYYY-MM-DD)"
)
add_parser.set_defaults(func=u.add_project)
add_parser = subparsers.add_parser("list-projects", help="List all projects")
add_parser.set_defaults(func=u.list_projects)


add_parser = subparsers.add_parser("add-task", help="Add a new task")
add_parser.add_argument("title", type=str, help="Title of the task")
add_parser.add_argument(
    "status", type=str, help="Status of the task (e.g., 'todo', 'in-progress', 'done')"
)
add_parser.add_argument("assigned_to", type=str, help="User assigned to the task")
add_parser.add_argument(
    "project", type=str, nargs="?", default=None, help="Project title (optional)"
)
add_parser.set_defaults(func=u.add_task)
add_parser = subparsers.add_parser("list-tasks", help="List all tasks")
add_parser.set_defaults(func=u.list_tasks)


if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)
