import sqlite3


class Database:
    """
    Класс отвечает за работу с базой данных SQLite:
    - подключение
    - создание таблицы
    """

    def __init__(self, db_name="tasks.db"):
        # Имя файла базы данных
        self.db_name = db_name

        # При создании объекта сразу проверяем,
        # существует ли таблица, и создаём её при необходимости
        self._create_table()

    def _connect(self):
        """
        Создаёт и возвращает соединение с базой данных.
        Каждый вызов — новое соединение.
        """
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        """
        Создаёт таблицу tasks, если она ещё не существует.
        """
        with self._connect() as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
            )
            """)










