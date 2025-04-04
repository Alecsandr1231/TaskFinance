class FinanceRecord:
    def __init__(self, record_id, task_id, amount, category, timestamp, currency="RUB", source=None, note=None):
        """
        :param record_id: Уникальный ID записи
        :param task_id: ID связанной задачи
        :param amount: Сумма операции
        :param category: Категория (например: 'Доход', 'Расход')
        :param timestamp: Время создания записи (строка в формате '%Y-%m-%d %H:%M:%S')
        :param currency: Валюта (по умолчанию 'RUB')
        :param source: Источник дохода или статьи расходов (например: 'Зарплата', 'Аренда', 'Еда')
        :param note: Комментарий к записи
        """
        self.record_id = record_id
        self.task_id = task_id
        self.amount = amount
        self.category = category
        self.timestamp = timestamp
        self.currency = currency
        self.source = source
        self.note = note

    def __repr__(self):
        return (f"FinanceRecord(ID={self.record_id}, Task={self.task_id}, "
                f"{self.amount} {self.currency} [{self.category}] @ {self.timestamp}, "
                f"Source='{self.source}', Note='{self.note}')")

    def to_dict(self):
        """Возвращает словарь с данными записи (например, для экспорта)."""
        return {
            "record_id": self.record_id,
            "task_id": self.task_id,
            "amount": self.amount,
            "category": self.category,
            "timestamp": self.timestamp,
            "currency": self.currency,
            "source": self.source,
            "note": self.note
        }
