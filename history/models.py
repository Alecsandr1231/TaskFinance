class HistoryRecord:
    def __init__(self, record_id, task_id, action, timestamp):
        """
        Инициализирует новый объект записи истории.

        @param record_id: Идентификатор записи истории.
        @param task_id: Идентификатор задачи, с которой связана запись.
        @param action: Описание действия, которое было выполнено.
        @param timestamp: Временная метка, когда действие было выполнено.
        """
        self.record_id = record_id
        self.task_id = task_id
        self.action = action
        self.timestamp = timestamp

    def __repr__(self):
        """
        Возвращает строковое представление записи истории.

        @return: Строка, представляющая объект записи истории.
        """
        return f"HistoryRecord({self.record_id}, Task {self.task_id}, {self.action}, {self.timestamp})"
