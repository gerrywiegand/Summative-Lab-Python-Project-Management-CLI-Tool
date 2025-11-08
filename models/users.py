class User:
    all = []

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.all.append(self)
        self._projects = []

    @property
    def tasks(self):
        """Get all tasks assigned to this user across all projects"""
        tasks = []
        for project in self._projects:
            for task in project.tasks:
                if task.assigned_to == self:
                    tasks.append(task)
        return tasks

    @tasks.setter
    def tasks(self, tasks):
        for task in tasks:
            task.assigned_to = self
            if task.project and task.project not in self._projects:
                self._projects.append(task.project)

    @property
    def projects(self):
        """Get all projects this user is involved in"""
        return self._projects

    @projects.setter
    def projects(self, projects):
        self._projects = projects if isinstance(projects, list) else list(projects)
        for project in self._projects:
            if self not in project.users:
                project.users.append(self)

    def add_task(self, task):
        task.assigned_to = self
        if task.project and self not in task.project.users:
            task.project.users.append(self)

    def add_project(self, project):
        if self not in project.users:
            project.users.append(self)
        for task in project.tasks:
            if task.assigned_to == self:
                if task not in self.tasks:
                    self.tasks.append(task)

    def to_dict(self):
        return {"username": self.username, "email": self.email}

    @classmethod
    def from_dict(cls, data):
        return cls(username=data["username"], email=data["email"])

    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}')"

    def __repr__(self):
        return self.__str__()
