from finance.models import FinanceRecord
from datetime import datetime

class FinanceController:
    records = []
    record_counter = 1

    @classmethod
    def add_record(cls, task_id, amount, category):
        """Добавляет новую финансовую запись, связанную с задачей."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = FinanceRecord(cls.record_counter, task_id, amount, category, timestamp)
        cls.records.append(record)
        cls.record_counter += 1

    @classmethod
    def get_all_records(cls):
        """Возвращает список всех финансовых записей."""
        return cls.records

    @classmethod
    def get_total_by_category(cls, category):
        """Возвращает сумму всех операций в указанной категории (Доход/Расход)."""
        return sum(record.amount for record in cls.records if record.category == category)

    @classmethod
    def get_balance(cls):
        """Возвращает текущий баланс (Доход - Расход)."""
        total_income = cls.get_total_by_category("Доход")
        total_expense = cls.get_total_by_category("Расход")
        return total_income - total_expense
