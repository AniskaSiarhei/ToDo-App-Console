import pytest

from todo.manager import ToDoManager


class FakeTaskRepository:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create(self, title):
        self.tasks.append((self.next_id, title, 0))
        self.next_id += 1

    def find_all(self):
        return self.tasks

    def mark_done(self, task_id):
        for i, (id_, title, done) in enumerate(self.tasks):
            if id_ == task_id:
                self.tasks[i] = (id_, title, 1)
                return True
        return False

    def delete(self, task_id):
        for task in self.tasks:
            if task[0] == task_id:
                self.tasks.remove(task)
                return True
        return False


def test_add_task():
    repo = FakeTaskRepository()
    manager = ToDoManager(repo)

    manager.add_task("Выучить pytest")

    tasks = manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Выучить pytest"
    assert tasks[0]["done"] is False


def test_add_empty_task():
    repo = FakeTaskRepository()
    manager = ToDoManager(repo)

    with pytest.raises(ValueError):
        manager.add_task("   ")


def test_complete_task():
    repo = FakeTaskRepository()
    manager = ToDoManager(repo)

    manager.add_task("Сделать тесты")
    result = manager.complete_task(1)

    tasks = manager.list_tasks()
    assert result is True
    assert tasks[0]["done"] is True


def test_delete_task():
    repo = FakeTaskRepository()
    manager = ToDoManager(repo)

    manager.add_task("Удалить меня")
    result = manager.delete_task(1)

    assert result is True
    assert manager.list_tasks() == []
