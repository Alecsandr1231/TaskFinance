from history.models import HistoryRecord
from datetime import datetime

class HistoryTracker:
    records = []
    record_counter = 1

    @classmethod
    def add_record(cls, task_id, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = HistoryRecord(cls.record_counter, task_id, action, timestamp)
        cls.records.append(record)
        cls.record_counter += 1

    @classmethod
    def get_records(cls, start_date=None, end_date=None):
        if start_date and end_date:
            return [record for record in cls.records if start_date <= record.timestamp <= end_date]
        return cls.records
