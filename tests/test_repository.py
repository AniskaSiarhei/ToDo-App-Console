import os
import pytest
from todo.database import Database
from todo.repository import TaskRepository

TEST_DB = "test_tasks.db"


@pytest.fixture
def db_session():
    """Фикстура для создания и удаления тестовой БД."""
    # Удаляем файл, если он остался от прошлых запусков
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    db = Database(TEST_DB)
    yield db  # Передаем объект базы в тест

    # После завершения теста удаляем ссылку и файл
    del db
    if os.path.exists(TEST_DB):
        try:
            os.remove(TEST_DB)
        except PermissionError:
            # На Windows файл может освободиться не мгновенно
            pass


def test_create_and_find(db_session):
    """Тест создания и поиска задачи."""
    # Используем объект db_session, созданный фикстурой
    repo = TaskRepository(db_session)
    repo.create("SQLite task")

    tasks = repo.find_all()
    assert len(tasks) == 1
    assert tasks[0][1] == "SQLite task"
    assert tasks[0][2] == 0