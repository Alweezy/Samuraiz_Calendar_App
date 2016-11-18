from Calendar import Calendar
import datetime 

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
        now = datetime.datetime.now
        print(" 1. Create calendar\n 2. Add Event\n 3. View Events \n 4. View Last Entry \n 5. Exit \n \n")
        action = input('Enter your choice: ')
        if action == '1':
            month = input("Enter month e.g 7 for 'July': ")
            if int(month) in range(1, 13):
                year = input('Enter year e.g 2016: ')
                if int(year) >= datetime.year:
                    calendar_name = input('Enter your calendar name: ')
                    calendar_name = Calendar()
                    calendar_name.create_calendar(int(year), int(month))
                    print('\n')
                    print('Calendar created.')
                    print('\n')
                else:
                    print ('You can only create events for future dates')
            else:
                print ('Sorry month entered should be between 1 and 12')
                print ('\n')
        elif action == '2':
            try:
                if calendar_name._days:
                    event_day = int(input("Add Event day: "))
                    if event_day in calendar_name._days:
                        event_name = input("Add Event name: ")
                        event_desc = input("Add Event description: ")
                        print(calendar_name.add_event(event_day, event_name, event_desc))
                        print('Event successfully added')
                        print('\n')
                    else:
                        print('No such day in the {} month'.format(calendar_name.calendar_month))
                        print('\n')
            except UnboundLocalError:
                print('No calendars created yet, Create a Calendar first')
                print("\n")
        elif action == '3':
            try:
                if calendar_name._days:
                    print(calendar_name.view_events())
            except UnboundLocalError:
                print('No calendars created yet, Create a Calendar first')
                print("\n")
        elif action == '4':
            try:
                if calendar_name._days:
                    print(calendar_name.view_last_event())
            except UnboundLocalError:
                print('No calendars created yet, Create a Calendar first')
                print("\n")
        elif action == '5':
            break
        else:
            print("Invalid choice: select again")

if __name__ == '__main__': main()
