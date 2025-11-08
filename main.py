import argparse  # noqa: F401, I001
from models.users import User  # noqa: F401
from models.projects import Project  # noqa: F401
from models.tasks import Task  # noqa: F401

parser = argparse.ArgumentParser(description="Project Management CLI Tool")
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser("add-user", help="Add a new user")
add_parser.add_argument("username", type=str, help="Username of the user")
add_parser.add_argument("email", type=str, help="Email of the user")

add_parser = subparsers.add_parser("add-project", help="Add a new project")
add_parser.add_argument("title", type=str, help="Title of the project")
add_parser.add_argument("due_date", type=str, help="Due date of the project")
