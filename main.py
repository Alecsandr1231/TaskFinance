from task_manager.views import display_tasks, add_task, update_task_status
from finance.views import add_finance_record, show_finance_summary, show_finance_records
from history.views import show_history, filter_history


def main():
    while True:
        print("\n---- Меню ----")
        print("1. Управление задачами")
        print("2. Финансовые записи")
        print("3. История изменений")
        print("4. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            print("\n1. Показать все задачи")
            print("2. Добавить задачу")
            print("3. Обновить статус задачи")
            task_choice = input("Выберите опцию: ")

            if task_choice == '1':
                display_tasks()
            elif task_choice == '2':
                add_task()
            elif task_choice == '3':
                update_task_status()

        elif choice == '2':
            print("\n1. Добавить финансовую запись")
            print("2. Показать сводку по финансам")
            print("3. Показать все финансовые записи")
            finance_choice = input("Выберите опцию: ")

            if finance_choice == '1':
                add_finance_record()
            elif finance_choice == '2':
                show_finance_summary()
            elif finance_choice == '3':
                show_finance_records()

        elif choice == '3':
            print("\n1. Показать историю изменений")
            print("2. Фильтровать историю по дате")
            history_choice = input("Выберите опцию: ")

            if history_choice == '1':
                show_history()
            elif history_choice == '2':
                filter_history()

        elif choice == '4':
            print("Выход из приложения.")
            break


if __name__ == "__main__":
    main()
