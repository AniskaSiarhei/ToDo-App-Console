from todo.database import Database
from todo.repository import TaskRepository


class ToDoManager:

    def __init__(self):
        # Создаём объект базы данных
        db = Database()
        self.repository = TaskRepository(db)

    def add_task(self, title: str):
        """
        Добавляет новую задачу в базу данных.

        :param title: текст задачи
        """
        if not title.strip():
            raise ValueError("Задача не может быть пустой!")
        self.repository.create(title)

    def list_tasks(self):
        """
        Возвращает список всех задач.
        Каждая задача — словарь.
        """
        rows = self.repository.find_all()

        # Преобразуем строки БД в список словарей
        return [
            {
                "id": row[0],
                "title": row[1],
                "done": bool(row[2])  # 0/1 → False/True
            }
            for row in rows
        ]

    def complete_task(self, task_id: int) -> bool:
        """
        Помечает задачу как выполненную.

        :param task_id: ID задачи
        :return: True если задача найдена и обновлена
        """
        return self.repository.mark_done(task_id)


    def delete_task(self, task_id: int) -> bool:
        """
        Удаляет задачу по ID.

        :param task_id: ID задачи
        :return: True если задача была удалена
        """
        return self.repository.delete(task_id)











