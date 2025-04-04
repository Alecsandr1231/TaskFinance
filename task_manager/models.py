class FinanceRecord:
    def __init__(self, record_id, task_id, amount, category, timestamp):
        self.record_id = record_id
        self.task_id = task_id
        self.amount = amount
        self.category = category  # Например: "Доход", "Расход"
        self.timestamp = timestamp

    def __repr__(self):
        return f"FinanceRecord({self.record_id}, Task {self.task_id}, {self.amount} {self.category}, {self.timestamp})"
