import json
import os


class ToDoManager:
    def __init__(self, filename="storage.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        task = {
            "id": task_id,
            "title": title,
            "done": False
        }
        self.tasks.append(task)
        self.save_tasks()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self.save_tasks()
                return True
        return False

    def list_tasks(self):
        return self.tasks

def show_menu():
        print("\n📌 МЕНЕДЖЕР ЗАДАЧ")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Отметить задачу выполненной")
        print("4. Выйти")

def main():
    to_do_manager = ToDoManager()

    while True:
        show_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            tasks = to_do_manager.list_tasks()
            if not tasks:
                print("📭 Список задач пуст")
            else:
                for task in tasks:
                    status = "✅" if task["done"] else "❌"
                    print(f'{task["id"]}. {task["title"]} [{status}]')

        elif choice == "2":
            title = input("Введите текст задачи: ")
            if title.strip():
                to_do_manager.add_task(title)
                print("✅ Задача добавлена")
            else:
                print("⚠️ Задача не может быть пустой")

        elif choice == "3":
            try:
                task_id = int(input("Введите ID задачи: "))
                if to_do_manager.complete_task(task_id):
                    print("✅ Задача отмечена как выполненная")
                else:
                    print("❗ Задача с таким ID не найдена")
            except ValueError:
                print("⚠️ ID должен быть числом")

        elif choice == "4":
            print("👋 Выход из программы")
            break

        else:
            print("❗ Неверный пункт меню")

if __name__ == "__main__":
    main()
