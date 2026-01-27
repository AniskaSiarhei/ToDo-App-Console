from todo.database import Database


class ToDoManager:
    """
    Класс отвечает за управление задачами:
    добавление, получение списка, завершение и удаление.
    """

    def __init__(self):
        # Создаём объект базы данных
        self.db = Database()

    def add_task(self, title):
        """
        Добавляет новую задачу в базу данных.

        :param title: текст задачи
        """
        # Открываем соединение с БД
        with self.db._connect() as conn:
            # Добавляем задачу, done = 0 (не выполнена)
            conn.execute(
                "INSERT INTO tasks (title, done) VALUES (?, ?)",
                (title, 0)
            )

    def list_tasks(self):
        """
        Возвращает список всех задач.
        Каждая задача — словарь.
        """
        with self.db._connect() as conn:
            cursor = conn.execute(
                "SELECT id, title, done FROM tasks"
            )

            # Преобразуем строки БД в список словарей
            return [
                {
                    "id": row[0],
                    "title": row[1],
                    "done": bool(row[2]) # 0/1 → False/True
                }
                for row in cursor.fetchall()
            ]

    def complete_task(self, task_id):
        """
        Помечает задачу как выполненную.

        :param task_id: ID задачи
        :return: True если задача найдена и обновлена
        """
        with self.db._connect() as conn:
            cursor = conn.execute(
                "UPDATE tasks SET done = 1 WHERE id = ?",
                (task_id,)
            )
            # rowcount > 0 означает, что строка была обновлена
            return cursor.rowcount > 0

    def delete_task(self, task_id):
        """
        Удаляет задачу по ID.

        :param task_id: ID задачи
        :return: True если задача была удалена
        """
        with self.db._connect() as conn:
            cursor = conn.execute(
                "DELETE FROM tasks WHERE id = ?",
                (task_id,)
            )
            return cursor.rowcount > 0