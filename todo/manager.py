from todo.database import Database


class ToDoManager:
    def __init__(self):
        self.db = Database()

    def add_task(self, title):
        with self.db._connect() as conn:
            conn.execute(
                "INSERT INTO tasks (title, done) VALUES (?, ?)",
                (title, 0)
            )

    def list_tasks(self):
        with self.db._connect() as conn:
            cursor = conn.execute(
                "SELECT id, title, done FROM tasks"
            )

            return [
                {"id": row[0], "title": row[1], "done": bool(row[2])}
                for row in cursor.fetchall()
            ]

    def complete_task(self, task_id):
        with self.db._connect() as conn:
            cursor = conn.execute(
                "UPDATE tasks SET done = 1 WHERE id = ?",
                (task_id,)
            )
            return cursor.rowcount > 0

    def delete_task(self, task_id):
        with self.db._connect() as conn:
            cursor = conn.execute(
                "DELETE FROM tasks WHERE id = ?",
                (task_id,)
            )
            return cursor.rowcount > 0