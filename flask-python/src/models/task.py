from collections.abc import Iterable


class Task():
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    @staticmethod
    def total_tasks(tasks):
        if isinstance(tasks, Iterable):
            return len(tasks)
        return 0
    

