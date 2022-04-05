"""
DateUtils.py

DateUtils is a utility class that can be used for generic date functions that might
be used by other Swarley modules or utilities.
"""
# Copyright (c) 1999 - 2015, Salesforce.com, San Francisco, CA, All rights reserved.

from datetime import datetime

class DateUtils():
    def __init__(self):
        return

    def getDateTimeString(self,):
        """
        Returns the current date time in the format 2015-08-21 14:52:30

        @return String containing the current date and time
        """
        str_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return str_date

    def unixToDateString(self,unix_time_stamp):
        """
        Returns the date and time from the specified unix timestamp

        @param unix_time_stamp: The unix timestamp to convert.
                              Timestamps coming from idb will need to be divided by 1000 before calling

        @return String containing the formatted data and time from the unix timestamp
        """
        if isinstance(unix_time_stamp, int):
            date_to_string = datetime.fromtimestamp(unix_time_stamp)
        else:
            date_to_string = datetime.fromtimestamp(int(unix_time_stamp))
        str_date = date_to_string.strftime('%Y-%m-%d %H:%M:%S')
        return str_date

    def getDateTimeForFileName(self):
        """
        Returns the current date time in the format 2015-08-21 14:52:30

        @return String containing the current date and time
        """
        str_date = datetime.now().strftime('%Y%m%d-%H%M%S')
        #logger.debug("Exit getDateTimeString - {0}".format(str_date))
        return str_date

    def getTimestamp(self, dt):
        return datetime.timestamp(datetime.fromisoformat(dt))