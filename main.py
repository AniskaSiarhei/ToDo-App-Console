from todo.database import Database
from todo.manager import ToDoManager
from todo.menu import show_menu, show_task
from todo.repository import TaskRepository


def main():
    db = Database()
    repo = TaskRepository(db)
    manager = ToDoManager(repo)

    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            show_task(manager.list_tasks())

        elif choice == "2":
            title = input("Введите текст задачи: ")
            if title.strip():
                manager.add_task(title)
                print("✅ Задача добавлена")
            else:
                print("⚠️ Задача не может быть пустой")

        elif choice == "3":
            try:
                task_id = int(input("Введите ID задачи: "))
                print(
                    "✅ Задача отмечена как выполненная" if manager.complete_task(task_id)
                    else "❗ Задача с таким ID не найдена"
                )
            except ValueError:
                print("⚠️ ID должен быть числом")

        elif choice == "4":
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                print(
                    "🗑 Задача удалена" if manager.delete_task(task_id)
                    else "❗ Задача с таким ID не найдена"
                )
            except ValueError:
                print("⚠️ ID должен быть числом")

        elif choice == "5":
            print("👋 Выход из программы")
            break

        else:
            print("❗ Неверный пункт меню")


if __name__ == "__main__":
    main()
