class HistoryRecord:
    def __init__(self, record_id, task_id, action, timestamp):
        self.record_id = record_id
        self.task_id = task_id
        self.action = action
        self.timestamp = timestamp

    def __repr__(self):
        return f"HistoryRecord({self.record_id}, Task {self.task_id}, {self.action}, {self.timestamp})"
