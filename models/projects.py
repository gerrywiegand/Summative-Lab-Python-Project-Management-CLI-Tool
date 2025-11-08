import datetime  # noqa: F401


class Project:
    all = []

    def __init__(self, title, due_date):
        self.title = title
        self._due_date = None
        self.due_date = due_date
        Project.all.append(self)
        self.tasks = []

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        self._tasks = tasks
        for task in tasks:
            task.project = self

    @property
    def users(self):
        users = set()
        for task in self.tasks:
            if task.assigned_to:
                users.add(task.assigned_to)
        return list(users)

    @property
    def due_date(self):
        if self._due_date and not isinstance(self._due_date, str):
            return self._due_date.strftime("%Y-%m-%d")
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
        if isinstance(self._due_date, str):
            return self._due_date
        return self._due_date.strftime("%Y-%m-%d")

    def add_task(self, task):
        task.project = self

    def add_user(self, user):
        for task in self.tasks:
            if task.assigned_to == user:
                if user not in self.users:
                    self.users.append(user)

    def to_dict(self):
        return {"title": self.title, "due_date": self.due_date}

    @classmethod
    def from_dict(cls, data):
        return cls(title=data["title"], due_date=data["due_date"])

    def __str__(self):
        return f"Project(title='{self.title}', due_date='{self.due_date}', tasks={len(self.tasks)})"

    def __repr__(self):
        return self.__str__()
