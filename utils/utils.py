from rich.console import Console
from tabulate import tabulate

from models.projects import Project
from models.tasks import Task
from models.users import User

from .persistence import save_data

console = Console()


def add_user(args):
    user = User(username=args.username, email=args.email)
    console.print(f"✓ User '{user.username}' added successfully.", style="bold green")
    save_data()
    return user


def add_project(args):
    project = Project(title=args.title, due_date=args.due_date)
    console.print(
        f"✓ Project '{project.title}' added successfully.", style="bold green"
    )
    save_data()
    return project


def add_task(args):
    assigned_user = next((u for u in User.all if u.username == args.assigned_to), None)
    if not assigned_user:
        console.print(f"✗ User '{args.assigned_to}' not found.", style="bold red")
        return None

    task = Task(title=args.title, status=args.status, assigned_to=assigned_user)

    # Optionally link to a project
    if args.project:
        project = next((p for p in Project.all if p.title == args.project), None)
        if project:
            task.project = project
            console.print(
                f"✓ Task '{task.title}' added to project '{project.title}' and assigned to '{assigned_user.username}'.",
                style="bold green",
            )
        else:
            console.print(
                f"✗ Project '{args.project}' not found. Task created without project.",
                style="bold yellow",
            )
    else:
        console.print(
            f"✓ Task '{task.title}' added successfully and assigned to '{assigned_user.username}'.",
            style="bold green",
        )

    save_data()
    return task


def list_users(args):
    if not User.all:
        console.print("No users found.", style="yellow")
        return

    data = [[user.username, user.email] for user in User.all]
    console.print(
        "\n" + tabulate(data, headers=["Username", "Email"], tablefmt="grid"),
        style="cyan",
    )
    print()


def list_projects(args):
    if not Project.all:
        print("No projects found.")
        return

    data = [
        [project.title, project.due_date, len(project.tasks)] for project in Project.all
    ]
    print(
        "\n" + tabulate(data, headers=["Title", "Due Date", "Tasks"], tablefmt="grid")
    )
    print()


def list_tasks(args):
    if not Task.all:
        print("No tasks found.")
        return

    data = []
    for task in Task.all:
        assigned = task.assigned_to.username if task.assigned_to else "Unassigned"
        project_name = task.project.title if task.project else "No project"
        data.append([task.title, task.status, assigned, project_name])

    print(
        "\n"
        + tabulate(
            data, headers=["Title", "Status", "Assigned To", "Project"], tablefmt="grid"
        )
    )
    print()


def find_user_by_username(username):
    return next((u for u in User.all if u.username == username), None)


def find_project_by_title(title):
    return next((p for p in Project.all if p.title == title), None)


def find_task_by_title(title):
    return next((t for t in Task.all if t.title == title), None)
