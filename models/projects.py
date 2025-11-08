class Project:
    all = []

    def __init__(self, title, due_date):
        self.title = title
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

    def add_task(self, task):
        task.project = self
