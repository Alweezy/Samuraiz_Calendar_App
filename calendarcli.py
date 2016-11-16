from calendar import Calendar

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
	print "Welcome to your Personal Calendar\n\n"

	while True:
		print " 1. Create calendar\n 2. Add Event\n 3. View Events \n 4. View Last Entry \n 5. Exit \n \n"
		action = raw_input('Enter your choice: ')
		if action.lower() == '1':
			month = raw_input('Enter month: ')
			year = raw_input('Enter year: ')
			Calendar.create_calendar(int(year), int(month))
		elif action.lower() == '2':
			event_day = raw_input("Add Event day: ")
			event_month = raw_input("Add Event month: ")
			event_name = raw_input("Add Event name: ")
			event_desc = raw_input("Add Event description: ")
			print Calendar.add_event(event_day, event_month, event_name, event_desc)
		elif action.lower() == '3':
			print Calendar.view_events()
		elif action.lower() == '4':
			print Calendar.view_last_event()
		else:
			print "Invalid choice: select again"
			

if __name__ == '__main__': main()
