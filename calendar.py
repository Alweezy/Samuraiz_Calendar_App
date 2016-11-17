class Calendar(object):
    """
    This is a simple calendar application the enables users to
     create calendar,adds events, views events
    """
    def __init__(self):
        self._calender_data = {}

    def create_calendar(self):
        pass


    def add_event(self, date, month, day, event):
        pass


    def view_events(self):
        pass


    def view_last_event(self, list_of_events):
        """
        The method returns the last event in the list of events.
        """
        len_of_list = len(list_of_events) - 1
        return list_of_events[len_of_list]
