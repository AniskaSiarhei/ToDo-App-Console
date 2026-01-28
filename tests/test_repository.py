import pytest


def test_add_task(manager):
    manager.add_task("Выучить pytest")

    tasks = manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Выучить pytest"
    assert tasks[0]["done"] is False


def test_add_empty_task(manager):
    with pytest.raises(ValueError):
        manager.add_task("   ")


def test_complete_task(manager):
    manager.add_task("Сделать тесты")

    result = manager.complete_task(1)
    tasks = manager.list_tasks()

    assert result is True
    assert tasks[0]["done"] is True


def test_complete_nonexistent_task(manager):
    result = manager.complete_task(999)
    assert result is False


def test_delete_task(manager):
    manager.add_task("Удалить меня")

    result = manager.delete_task(1)
    tasks = manager.list_tasks()

    assert result is True
    assert tasks == []


def test_delete_nonexistent_task(manager):
    result = manager.delete_task(123)
    assert result is False
