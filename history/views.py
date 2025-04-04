from history.tracker import HistoryTracker


def show_history():
    records = HistoryTracker.get_records()
    for record in records:
        print(f"[{record.record_id}] Task {record.task_id}: {record.action} at {record.timestamp}")


def filter_history():
    start_date = input("Введите начальную дату (YYYY-MM-DD HH:MM:SS): ")
    end_date = input("Введите конечную дату (YYYY-MM-DD HH:MM:SS): ")
    records = HistoryTracker.get_records(start_date, end_date)

    if records:
        for record in records:
            print(f"[{record.record_id}] Task {record.task_id}: {record.action} at {record.timestamp}")
    else:
        print("Записей за данный период нет.")
