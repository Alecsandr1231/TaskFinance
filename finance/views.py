from task_manager.controllers import TaskController

def display_tasks():
    """
    Отображает все задачи.

    Получает список всех задач через контроллер задач и выводит их на экран,
    включая идентификатор задачи, заголовок и статус.
    """
    tasks = TaskController.get_all_tasks()
    for task in tasks:
        print(f"[{task.task_id}] {task.title} - {task.status}")

def add_task():
    """
    Добавляет новую задачу.

    Запрашивает у пользователя название и описание задачи, затем создает новую задачу
    через контроллер задач и выводит сообщение об успешном добавлении.
    """
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    TaskController.create_task(title, description)
    print("Задача добавлена!")

def update_task_status():
    """
    Обновляет статус существующей задачи.

    Запрашивает у пользователя идентификатор задачи и новый статус, затем обновляет
    статус задачи через контроллер задач и выводит сообщение об успешном обновлении.
    """
    task_id = int(input("Введите ID задачи: "))
    new_status = input("Введите новый статус: ")
    TaskController.update_task(task_id, new_status)
    print("Статус задачи обновлён!")
