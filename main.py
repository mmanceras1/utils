from datetime import datetime
from database import Event, CalendarDatabase

def print_menu():
    print("\nCalendar Menu:")
    print("1. Add Event")
    print("2. Remove Event")
    print("3. List Events")
    print("4. Exit")

def main():
    calendar_db = CalendarDatabase()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter event description: ")
            start_time_str = input("Enter start time (YYYY-MM-DD HH:MM): ")
            end_time_str = input("Enter end time (YYYY-MM-DD HH:MM): ")
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
            event = Event(description, start_time, end_time)
            calendar_db.add_event(event)
        elif choice == '2':
            description = input("Enter event description to remove: ")
            calendar_db.remove_event(description)
        elif choice == '3':
            print("\nCurrent events in the calendar:")
            events = calendar_db.list_events()
            for event in events:
                print(event)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()