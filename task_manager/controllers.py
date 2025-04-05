from finance.models import FinanceRecord
from datetime import datetime

class FinanceController:
    records = []
    record_counter = 1

    @classmethod
    def add_record(cls, task_id, amount, category):
        """
        Добавляет новую финансовую запись, связанную с задачей.

        @param task_id: Идентификатор задачи, с которой связана запись.
        @param amount: Сумма финансовой операции.
        @param category: Категория финансовой операции (например, "Доход" или "Расход").
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = FinanceRecord(cls.record_counter, task_id, amount, category, timestamp)
        cls.records.append(record)
        cls.record_counter += 1

    @classmethod
    def get_all_records(cls):
        """
        Возвращает список всех финансовых записей.

        @return: Список всех финансовых записей.
        """
        return cls.records

    @classmethod
    def get_total_by_category(cls, category):
        """
        Возвращает сумму всех операций в указанной категории (Доход/Расход).

        @param category: Категория для фильтрации (например, "Доход" или "Расход").
        @return: Сумма всех операций в указанной категории.
        """
        return sum(record.amount for record in cls.records if record.category == category)

    @classmethod
    def get_balance(cls):
        """
        Возвращает текущий баланс (Доход - Расход).

        @return: Текущий баланс.
        """
        total_income = cls.get_total_by_category("Доход")
        total_expense = cls.get_total_by_category("Расход")
        return total_income - total_expense
