class Calendar(object):
    """
    This is a simple calendar application the enables users to
     create calendar,adds events, views events
    """
    def __init__(self):
        self._calender_data = {}
        self._days = []

    def create_calendar(self, calendar_month, calendar_year):
        import calendar
        calendar1 = [item for item in calendar.month(calendar_year, calendar_month).split()]
        for item in calendar1[9:]:
            self._days.append(int(item))

    def add_event(self):
        pass


    def view_events(self):
        pass


    def view_last_event(self):
        pass
