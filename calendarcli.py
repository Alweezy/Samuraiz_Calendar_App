from Calendar import Calendar, save, open_file
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
    count = 0 

    while True:
        now = datetime.datetime.now()
        if count <= 1: # Checks if there are more than one calendar created.
            print(" 1. Create calendar\n 2. Add Event\n 3. View Events \n 4. View Last Entry \n 5. Exit \n \n")
        else: 
            print(" 1. Create calendar\n 2. Add Event\n 3. View Events \n 4. View Last Entry \n 4.5. View other calendar's events \n 5. Exit \n\n")
        action = input('Enter your choice: ')
        if action == '1':
            month = input("Enter month (e.g 7 for 'July') : ")
            try:
                if int(month) in range(1, 13):
                    year = input('Enter year (e.g 2016) : ')
                    if int(year) >= now.year:
                        calendar_name = input('Enter your calendar name: ')
                        name = calendar_name
                        calendar_name = Calendar()
                        calendar_name.create_calendar(int(year), int(month))
                        count += 1 #increments every time a new calendar is created.
                        print('\n')
                        print('Calendar created.')
                        print('\n')
                    else:
                        print ('You can only create events for future dates')
                else:
                    print ('Sorry month entered should be between 1 to 12')
                    print ('\n')
            except:
                print('Please key in month in numbers.')
                print('\n')
        elif action == '2':
            try:
                if calendar_name._days:
                    event_day = int(input("Add Event day: "))
                    if event_day in calendar_name._days:
                        event_name = input("Add Event name: ")
                        event_desc = input("Add Event description: ")
                        print(calendar_name.add_event(event_day, event_name, event_desc))
                        save(name, calendar_name) # calls the save function in Calendar.py. This creates a json file. 
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
        elif action == '4.5':  
            """
            Prints all the events in all the calendars created.
            Option only available if more than one calendar created.
            Calls except when no event has been added to any calendar thus no json file was created.
            """
            try: 
                open_file()  
                print("\n \n")
            except:
                print('No event added to any calendar')
                print('\n')  
        elif action == '5':
            break
        else:
            print("Invalid choice: select again")


if __name__ == '__main__': main()
