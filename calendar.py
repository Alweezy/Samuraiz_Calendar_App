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
            :param date:
            :param month:
            :param day:
            :param event:
            :return dictionary{"date": "event"}
        """

        self.event_date = event_date
        self.event_month = event_month
        self.event_day = event_day
        self.event_name = event_name


    def view_events(self):
        pass


    def view_last_event(self):
        pass
