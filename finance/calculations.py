from task_manager.models import Task

class TaskController:
    tasks = []
    task_counter = 1

    @classmethod
    def create_task(cls, title, description):
        task = Task(cls.task_counter, title, description)
        cls.tasks.append(task)
        cls.task_counter += 1

    @classmethod
    def get_all_tasks(cls):
        return cls.tasks

    @classmethod
    def update_task(cls, task_id, new_status):
        for task in cls.tasks:
            if task.task_id == task_id:
                task.update_status(new_status)
                return True
        return False
