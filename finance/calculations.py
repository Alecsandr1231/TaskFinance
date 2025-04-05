from finance.models import FinanceRecord
from datetime import datetime
from collections import defaultdict


class FinanceCalculator:
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
    def get_total(cls, category=None):
        """
        Возвращает сумму всех операций, с фильтрацией по категории (если указана).

        @param category: (необязательный) Категория для фильтрации.
        @return: Сумма всех операций или сумма операций по указанной категории.
        """
        if category:
            return sum(record.amount for record in cls.records if record.category.lower() == category.lower())
        return sum(record.amount for record in cls.records)

    @classmethod
    def get_balance(cls):
        """
        Возвращает текущий баланс (Доход - Расход).

        @return: Текущий баланс.
        """
        total_income = cls.get_total("Доход")
        total_expense = cls.get_total("Расход")
        return total_income - total_expense

    @classmethod
    def get_records(cls, category=None, start_date=None, end_date=None):
        """
        Возвращает список финансовых записей с фильтрацией по категории и дате.

        @param category: (необязательный) Категория для фильтрации.
        @param start_date: (необязательный) Начальная дата для фильтрации.
        @param end_date: (необязательный) Конечная дата для фильтрации.
        @return: Список отфильтрованных финансовых записей.
        """
        filtered_records = cls.records

        if category:
            filtered_records = [record for record in filtered_records if record.category.lower() == category.lower()]

        if start_date and end_date:
            filtered_records = [
                record for record in filtered_records
                if start_date <= record.timestamp <= end_date
            ]

        return filtered_records

    @classmethod
    def get_monthly_summary(cls):
        """
        Возвращает суммарные доходы и расходы по месяцам.

        @return: Словарь с суммарными доходами и расходами по месяцам.
        """
        monthly_summary = defaultdict(lambda: {"Доход": 0, "Расход": 0})

        for record in cls.records:
            month = record.timestamp[:7]  # Группировка по ГГГГ-ММ
            monthly_summary[month][record.category] += record.amount

        return dict(monthly_summary)

    @classmethod
    def get_top_expenses(cls, top_n=5):
        """
        Возвращает топ-N самых крупных расходов.

        @param top_n: Количество самых крупных расходов для возврата.
        @return: Список топ-N самых крупных расходов.
        """
        expenses = [record for record in cls.records if record.category == "Расход"]
        sorted_expenses = sorted(expenses, key=lambda x: x.amount, reverse=True)
        return sorted_expenses[:top_n]

    @classmethod
    def get_category_distribution(cls):
        """
        Возвращает распределение расходов по категориям.

        @return: Словарь с распределением расходов по категориям.
        """
        category_distribution = defaultdict(float)

        for record in cls.records:
            if record.category == "Расход":
                category_distribution[record.task_id] += record.amount

        return dict(category_distribution)
