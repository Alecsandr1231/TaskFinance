from task_manager.controllers import TaskController

def display_tasks():
    tasks = TaskController.get_all_tasks()
    for task in tasks:
        print(f"[{task.task_id}] {task.title} - {task.status}")

def add_task():
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    TaskController.create_task(title, description)
    print("Задача добавлена!")

def update_task_status():
    task_id = int(input("Введите ID задачи: "))
    new_status = input("Введите новый статус: ")
    TaskController.update_task(task_id, new_status)
    print("Статус задачи обновлён!")
