import pytest
from todo.manager import ToDoManager


class FakeTaskRepository:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create(self, title: str):
        self.tasks.append((self.next_id, title, 0))
        self.next_id += 1

    def find_all(self):
        return self.tasks

    def mark_done(self, task_id: int) -> bool:
        for i, (id_, title, done) in enumerate(self.tasks):
            if id_ == task_id:
                self.tasks[i] = (id_, title, 1)
                return True
        return False

    def delete(self, task_id: int) -> bool:
        for task in self.tasks:
            if task[0] == task_id:
                self.tasks.remove(task)
                return True
        return False


@pytest.fixture
def manager():
    repo = FakeTaskRepository()
    return ToDoManager(repo)
