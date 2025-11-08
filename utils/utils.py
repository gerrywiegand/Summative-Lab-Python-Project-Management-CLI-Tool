from models.projects import Project
from models.tasks import Task
from models.users import User


def add_user(args):
    user = User(username=args.username, email=args.email)
    print(f"User '{user.username}' added successfully.")
    return user


def add_project(args):
    project = Project(title=args.title, due_date=args.due_date)
    print(f"Project '{project.title}' added successfully.")
    return project


def add_task(args):
    assigned_user = next((u for u in User.all if u.username == args.assigned_to), None)
    if not assigned_user:
        print(f"User '{args.assigned_to}' not found.")
        return None
    task = Task(title=args.title, status=args.status, assigned_to=assigned_user)
    print(
        f"Task '{task.title}' added successfully and assigned to '{assigned_user.username}'."
    )
    return task


def list_users():
    if not User.all:
        print("No users found.")
        return
    print("\nUsers:")
    for user in User.all:
        print(f"  - {user.username} ({user.email})")


def list_projects():
    if not Project.all:
        print("No projects found.")
        return
    print("\nProjects:")
    for project in Project.all:
        print(f"  - {project.title} (Due: {project.due_date})")


def list_tasks():
    if not Task.all:
        print("No tasks found.")
        return
    print("\nTasks:")
    for task in Task.all:
        assigned = task.assigned_to.username if task.assigned_to else "Unassigned"
        print(f"  - {task.title} | Status: {task.status} | Assigned to: {assigned}")


def find_user_by_username(username):
    return next((u for u in User.all if u.username == username), None)


def find_project_by_title(title):
    return next((p for p in Project.all if p.title == title), None)


def find_task_by_title(title):
    return next((t for t in Task.all if t.title == title), None)
