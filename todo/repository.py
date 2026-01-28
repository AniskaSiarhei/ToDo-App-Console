from todo.database import Database


class TaskRepository:
    def __init__(self, db: Database):
        self.db = db

    def create(self, title: str):
        with self.db._connect() as conn:
            conn.execute(
                "INSERT INTO tasks(title, done) VALUES (?, ?)",
                (title, 0)
            )

    def find_all(self):
        with self.db._connect() as conn:
            cursor = conn.execute(
                "SELECT id, title, done FROM tasks"
            )
            return cursor.fetchall()

    def mark_done(self, task_id: int) -> bool:
        with self.db._connect() as conn:
            cursor = conn.execute(
                "UPDATE tasks SET done = 1 WHERE id = ?",
                (task_id,)
            )
            return cursor.rowcount > 0

    def delete(self, task_id: int) -> bool:
        with self.db._connect() as conn:
            cursor = conn.execute(
                "DELETE FROM tasks WHERE id = ?",
                (task_id,)
            )
            return cursor.rowcount > 0




































