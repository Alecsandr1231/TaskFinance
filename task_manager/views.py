from finance.calculations import FinanceCalculator
from datetime import datetime


def add_finance_record():
    """
    Добавляет новую финансовую запись.

    Запрашивает у пользователя ID задачи, сумму и категорию (Доход/Расход),
    затем добавляет запись через FinanceCalculator и выводит сообщение об успешном добавлении.
    """
    task_id = int(input("Введите ID задачи: "))
    amount = float(input("Введите сумму: "))
    category = input("Введите категорию (Доход/Расход): ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    FinanceCalculator.add_record(task_id, amount, category, timestamp)
    print("Финансовая запись добавлена!")


def show_finance_summary():
    """
    Отображает сводку финансовых данных.

    Выводит общую сумму доходов, расходов и текущий баланс.
    """
    total_income = FinanceCalculator.get_total("Доход")
    total_expense = FinanceCalculator.get_total("Расход")
    balance = total_income - total_expense

    print(f"Доход: {total_income}")
    print(f"Расход: {total_expense}")
    print(f"Баланс: {balance}")


def show_finance_records():
    """
    Отображает все финансовые записи.

    Получает список всех финансовых записей через FinanceCalculator и выводит их на экран,
    включая идентификатор записи, идентификатор задачи, сумму, категорию и временную метку.
    """
    records = FinanceCalculator.get_records()
    for record in records:
        print(f"[{record.record_id}] Task {record.task_id}: {record.amount} {record.category} at {record.timestamp}")
