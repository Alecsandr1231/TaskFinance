from finance.calculations import FinanceCalculator
from datetime import datetime


def add_finance_record():
    task_id = int(input("Введите ID задачи: "))
    amount = float(input("Введите сумму: "))
    category = input("Введите категорию (Доход/Расход): ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    FinanceCalculator.add_record(task_id, amount, category, timestamp)
    print("Финансовая запись добавлена!")


def show_finance_summary():
    total_income = FinanceCalculator.get_total("Доход")
    total_expense = FinanceCalculator.get_total("Расход")
    balance = total_income - total_expense

    print(f"Доход: {total_income}")
    print(f"Расход: {total_expense}")
    print(f"Баланс: {balance}")


def show_finance_records():
    records = FinanceCalculator.get_records()
    for record in records:
        print(f"[{record.record_id}] Task {record.task_id}: {record.amount} {record.category} at {record.timestamp}")
