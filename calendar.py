class Calendar(object):
    """
    This is a simple calendar application the enables users to
     create calendar,adds events, views events
    """
    def __init__(self):
        self._calender_data = {}

    def create_calendar(self):
        pass


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
