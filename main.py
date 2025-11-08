import argparse  # noqa: F401, I001
from models.users import User  # noqa: F401
from models.projects import Project  # noqa: F401
from models.tasks import Task  # noqa: F401

parser = argparse.ArgumentParser(description="Project Management CLI Tool")
subparses = parser.add_subparsers()
