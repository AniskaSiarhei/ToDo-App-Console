def show_menu():
    print("\n📌 МЕНЕДЖЕР ЗАДАЧ")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу выполненной")
    print("4. Удалить задачу")
    print("5. Выйти")

def show_task(tasks):
    if not tasks:
        print("📭 Список задач пуст")
        return

    for task in tasks:
        status = "✅" if task["done"] else "❌"
        print(f'{task["id"]}. {task["title"]} [{status}]')