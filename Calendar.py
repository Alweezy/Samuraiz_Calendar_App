import calendar, json

calendar_dict = {}

class Calendar(object):
    """
    This is a simple calendar application that enables users to
     create calendar,adds events, views events
    """
    def __init__(self):
        self._days = [] # stores all days with events, used to a check against double booking
        self._picked_days = []
        self.events = []

    def create_calendar(self, calendar_year, calendar_month):
        self.calendar_year = calendar_year 
        self.calendar_month = calendar_month         
        import calendar as new_calendar
        calendar1 = [item for item in new_calendar.month(self.calendar_year, self.calendar_month).split()]
        for item in calendar1[9:]:
            self._days.append(int(item))
        return ''

    def add_event(self, event_day, event_name, event_desc):
        """
            Function makes use of the calendar to book various dates to event.
            :param event_date:
            :param event_month:
            :param event_day:
            :param event_name:
            :return: dictionary{"date": "event"}
        """

        self.event_day = int(event_day)
        self.event_desc = event_desc
        self.event_name = event_name
        event = [self.event_name, self.event_desc]
        self.date = str(self.calendar_month) + '/' + str(self.event_day) + '/' + str(self.calendar_year)
        if self.event_day not in self._picked_days:
                #self._calender_data[self.event_day] = event
                self._picked_days.append(self.event_day) # checks that dates used are not reused
                print('\n Event successfully added')
        else:
            return ("\n Sorry date already booked, view events")
        #removed line of code checking a dictionary, was bugging code
        event_details = {}  # handles all event details
        event_details['Date'] = self.date
        event_details['Details'] = event
        self.events.append(event_details)
        return ''

    def view_last_event(self):
        """
        The method returns the last event in the list of events.
        """
        if self.events: # Handles error when no events have been scheduled.
            len_of_list = len(self.events) - 1
            events = self.events[len_of_list]
            # Handles printing for last event
            print("{:<30} {:<20} {:<15}".format('Event Date', 'Event Name', 'Event Details' ))
            print("{:<30} {:<20} {:<15}".format(events['Date'], events['Details'][0], events['Details'][1]))
        else:
            return ('No events Scheduled Yet')
        return ''
    def view_events(self):
        if self.events:
            print("{:<30} {:<20} {:<15}".format('Event Date', 'Event Name', 'Event Details' ))
            for events in self.events:
                print("{:<30} {:<20} {:<15}".format(events['Date'], events['Details'][0], events['Details'][1]))
        else:
            return 'No events Scheduled yet'
        return ''

def save(name, obj):
    """
    Function creates a json file and saves the calendar_dict to it. 
    """
    calendar_dict[name] = obj.events 
    save_file = open("test.json", "w")
    json.dump(calendar_dict,save_file, indent=4)
    save_file.close()

def open_file():
    """
    Function loads the json file created in save() and prints the content.
    """
    read_file = open("test.json", "r")
    new_dict = json.load(read_file)
    read_file.close()
    print("{:<20} {:<30} {:<20} {:<15}".format('Dictionary Name','Event Date', 'Event Name', 'Event Details' ))
    for key, value in new_dict.iteritems():
        for items in value:
            print("{:<20} {:<30} {:<20} {:<15}".format(key, items['Date'], items['Details'][0], items['Details'][1]))


