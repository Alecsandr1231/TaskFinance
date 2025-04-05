from history.tracker import HistoryTracker


def show_history():
    """
    Отображает все записи истории действий.

    Выводит на экран все записи истории, включая идентификатор записи, идентификатор задачи,
    описание действия и временную метку.
    """
    records = HistoryTracker.get_records()
    for record in records:
        print(f"[{record.record_id}] Task {record.task_id}: {record.action} at {record.timestamp}")


def filter_history():
    """
    Фильтрует записи истории действий по заданному диапазону дат.

    Запрашивает у пользователя начальную и конечную дату, затем отображает записи истории,
    которые попадают в указанный диапазон.

    Если записей за данный период нет, выводит соответствующее сообщение.
    """
    start_date = input("Введите начальную дату (YYYY-MM-DD HH:MM:SS): ")
    end_date = input("Введите конечную дату (YYYY-MM-DD HH:MM:SS): ")
    records = HistoryTracker.get_records(start_date, end_date)

    if records:
        for record in records:
            print(f"[{record.record_id}] Task {record.task_id}: {record.action} at {record.timestamp}")
    else:
        print("Записей за данный период нет.")
