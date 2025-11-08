class User:
    all = []

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.all.append(self)
        self.projects = []
