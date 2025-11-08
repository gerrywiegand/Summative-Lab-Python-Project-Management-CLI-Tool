class User:
    all = []

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.all.append(self)
        self.projects = []

    @property
    def tasks(self):
        tasks = []
        for project in self.projects:
            for task in project.tasks:
                if task.assigned_to == self:
                    tasks.append(task)
        return tasks

    @tasks.setter
    def tasks(self, tasks):
        for task in tasks:
            task.assigned_to = self
            if task.project and self not in task.project.users:
                task.project.users.append(self)

    @property
    def projects(self):
        projects = set()
        for task in self.tasks:
            if task.project:
                projects.add(task.project)
        return list(projects)

    @projects.setter
    def projects(self, projects):
        for project in projects:
            if self not in project.users:
                project.users.append(self)
            for task in project.tasks:
                if task.assigned_to == self:
                    if task not in self.tasks:
                        self.tasks.append(task)

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
