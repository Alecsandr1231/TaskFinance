from history.models import HistoryRecord
from datetime import datetime

class HistoryTracker:
    records = []
    record_counter = 1

    @classmethod
    def add_record(cls, task_id, action):
        """
        Добавляет новую запись истории действий.

        @param task_id: Идентификатор задачи, с которой связана запись.
        @param action: Описание действия, которое было выполнено.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = HistoryRecord(cls.record_counter, task_id, action, timestamp)
        cls.records.append(record)
        cls.record_counter += 1

    @classmethod
    def get_records(cls, start_date=None, end_date=None):
        """
        Возвращает список записей истории действий с фильтрацией по дате.

        @param start_date: (необязательный) Начальная дата для фильтрации.
        @param end_date: (необязательный) Конечная дата для фильтрации.
        @return: Список записей истории действий, отфильтрованных по дате.
        """
        if start_date and end_date:
            return [record for record in cls.records if start_date <= record.timestamp <= end_date]
        return cls.records
