import sqlite3
from datetime import datetime

class Event:
    def __init__(self, description, start_time, end_time):
        self.description = description
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.description} from {self.start_time} to {self.end_time}"

class CalendarDatabase:
    def __init__(self, db_name="calendar.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY,
                    description TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT NOT NULL
                )
            """)

    def add_event(self, event):
        with self.conn:
            self.conn.execute("""
                INSERT INTO events (description, start_time, end_time)
                VALUES (?, ?, ?)
            """, (event.description, event.start_time.isoformat(), event.end_time.isoformat()))
        print(f"Event '{event.description}' added.")

    def remove_event(self, description):
        with self.conn:
            self.conn.execute("""
                DELETE FROM events WHERE description = ?
            """, (description,))
        print(f"Event '{description}' removed.")

    def list_events(self):
        cursor = self.conn.execute("SELECT description, start_time, end_time FROM events")
        events = []
        for row in cursor:
            event = Event(row[0], datetime.fromisoformat(row[1]), datetime.fromisoformat(row[2]))
            events.append(event)
        return events