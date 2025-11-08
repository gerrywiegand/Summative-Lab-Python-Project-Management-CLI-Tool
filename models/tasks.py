class Task:
    all = []

    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        Task.all.append(self)
        self.project = None

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, project):
        self._project = project
        if project:
            project.tasks.append(self)

    @property
    def assigned_to(self):
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, user):
        self._assigned_to = user
        if user:
            if not hasattr(user, "tasks"):
                user.tasks = []
            user.tasks.append(self)

    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to.username if self.assigned_to else None,
            "project": self.project.title if self.project else None,
        }

    @classmethod
    def from_dict(cls, data, users, projects):
        # Find the user by username
        user = next((u for u in users if u.username == data["assigned_to"]), None)
        # Find the project by title
        project = next((p for p in projects if p.title == data["project"]), None)

        task = cls(title=data["title"], status=data["status"], assigned_to=user)
        if project:
            task.project = project
        return task

    def __str__(self):
        assigned = self.assigned_to.username if self.assigned_to else "Unassigned"
        project_name = self.project.title if self.project else "No project"
        return f"Task(title='{self.title}', status='{self.status}', assigned_to='{assigned}', project='{project_name}')"

    def __repr__(self):
        return self.__str__()
