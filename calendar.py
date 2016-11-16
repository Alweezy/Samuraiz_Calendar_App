class Calendar(object):
    """
    This is a simple calendar application the enables users to
     create calendar,adds events, views events
    """
    def __init__(self):
        self._calender_data = {}
        self._days = []

    def create_calendar(self, calendar_year, calendar_month):
        import calendar as new_calendar
        calendar1 = [item for item in new_calendar.month(calendar_year, calendar_month).split()]
        for item in calendar1[9:]:
            self._days.append(int(item))

    def add_event(self, event_date, event_month, event_day, event_name):
        """
            Function makes use of the calendar to book various dates to event.
            :param event_date:
            :param event_month:
            :param event_day:
            :param event_name:
            :return: dictionary{"date": "event"}
        """

        self.event_day = event_day
        self.event_month = event_month
        self.event_desc = event_desc
        self.event_name = event_name
        event = [event_name, event_desc]
        date = str(self.event_month) + str(self.event_day)
        if self.event_day in self._days:
            for day in self._days:
                self._calender_data[days] = event
                self._days.remove(day)
        else:
            return "Sorry date already booked, view events"

    def view_events(self):
        pass


    def view_last_event(self, list_of_events):
        """
        The method returns the last event in the list of events.
        """
        len_of_list = len(list_of_events) - 1
        print list_of_events[len_of_list]
