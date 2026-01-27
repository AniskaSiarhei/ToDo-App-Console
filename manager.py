import json
import os


class ToDoManager:
    def __init__(self, filename="storage.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

        self.next_id = 1
        if self.tasks:
            self.next_id = max(task["id"] for task in self.tasks) + 1

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
        task = {
            "id": self.next_id,
            "title": title,
            "done": False
        }
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                return True
        return False

    def list_tasks(self):
        return self.tasks