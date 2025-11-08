class Project:
    all = []

    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        Project.all.append(self)
        self.tasks = []
