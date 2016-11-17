from Calendar import Calendar

import calendar as new_calendar


def main():
    """
	Samuraiz Calendar App

	Usage:
		calendar -h| --help
		calendar --version

	Options:
		-h --help
		--version

	Examples:
		calendar create

	"""
    print("\n\n")
    print("Welcome to your Personal Calendar\n\n")

    while True:
        print(" 1. Create calendar\n 2. Add Event\n 3. View Events \n 4. View Last Entry \n 5. Exit \n \n")
        action = input('Enter your choice: ')
        if action.lower() == '1':
            Mycal = Calendar()
            month = input('Enter month: ')
            year = input('Enter year: ')
            Mycal.create_calendar(int(year), int(month))
            print('\n')
        elif action.lower() == '2':
            try:
                if Mycal._days:
                    event_day = input("Add Event day: ")
                    event_name = input("Add Event name: ")
                    event_desc = input("Add Event description: ")
                    print(Mycal.add_event(event_day, event_name, event_desc))
            except UnboundLocalError:
                print('No calendars created yet, Create a Calendar first')
                print("\n")
        elif action.lower() == '3':
            try:
                if Mycal._days:
                    print(Mycal.view_events())
            except UnboundLocalError:
                print('No calendars created yet, Create a Calendar first')
                print("\n")
        elif action.lower() == '4':
            try:
                if Mycal._days:
                    print(Mycal.view_last_event())
            except UnboundLocalError:
                print('No calendars created yet, Create a Calendar first')
                print("\n")
        elif action.lower() == '5':
            break
        else:
            print("Invalid choice: select again")


if __name__ == '__main__': main()
