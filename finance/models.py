class Task:
    def __init__(self, task_id, title, description, status="pending"):
        """
        Инициализирует новый объект задачи.

        @param task_id: Идентификатор задачи.
        @param title: Заголовок задачи.
        @param description: Описание задачи.
        @param status: Статус задачи (по умолчанию "pending").
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def update_status(self, new_status):
        """
        Обновляет статус задачи.

        @param new_status: Новый статус задачи.
        """
        self.status = new_status

    def __repr__(self):
        """
        Возвращает строковое представление задачи.

        @return: Строка, представляющая объект задачи.
        """
        return f"Task({self.task_id}, {self.title}, {self.status})"
