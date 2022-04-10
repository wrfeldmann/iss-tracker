#!/usr/bin/env python3

import argparse
import platform
import time

from datetime import datetime

from classes.colors import Colors
from classes.date_utils import DateUtils
from classes.iss_utils import ISSUtils
from classes.lights_utils import LightsUtils
from classes.print_utils import PrintUtils
from classes.sunrise_sunset_utils import SunriseSunsetUtils
from classes.utilities import Utilities

colors = Colors()
date_utils = DateUtils()
lights_utils = LightsUtils()
iss_utils = ISSUtils()
print_utils = PrintUtils()
sunrise_sunset_utils = SunriseSunsetUtils()
utilities = Utilities()


class ISSTracker():

    def __init__(self):
        return

    def get_args(self):
        parser = argparse.ArgumentParser(description="ISS Tracker Command Line Arguments")
        parser.add_argument("--latitude",
                            help="[REQUIRED] Latitude of the location you would like to know when the ISS is near.",
                            required=True,
                            action="store",
                            type=float)
        parser.add_argument("--longitude",
                            help="[REQUIRED] Longitude of the location you would like to know when the ISS is near.",
                            action="store",
                            type=float)
        self.args = parser.parse_args()

    def track_iss(self):
        self.get_args()
        column_headings = dict()
        column_headings[1] = "Current Time"
        column_headings[2] = "ISS Latitude"
        column_headings[3] = "ISS Longitude"
        column_headings[4] = "Latitude Range"
        column_headings[5] = "Longitude Range"
        column_headings[6] = "Overhead"
        column_headings[7] = "Visible"
        column_widths = dict()
        column_widths[1] = 23
        column_widths[2] = 12
        column_widths[3] = 13
        column_widths[4] = 24
        column_widths[5] = 24
        column_widths[6] = 8
        column_widths[7] = 7
        print("")
        heading_printed = False
        while True:
            now = datetime.now().astimezone()
            display_now = now.strftime("%Y-%m-%d %H:%M:%S %Z")

            iss_latitude, iss_longitude = iss_utils.current_ISS_location()
            str_iss_latitude, str_iss_longitude, latitude_range, longitude_range = \
                iss_utils.get_latitude_longitude_messages(self.args, iss_latitude, iss_longitude)
            is_near, overhead_message = iss_utils.near_ISS(self.args, iss_latitude, iss_longitude)

            is_visible = False
            visible_message = ""
            if sunrise_sunset_utils.is_dark(now, self.args) and is_near:
                visible_message = "Visible"
                is_visible = True

            row_data = dict()
            row_data[1] = "{0}".format(display_now)
            row_data[2] = "{0}".format(str_iss_latitude)
            row_data[3] = "{0}".format(str_iss_longitude)
            row_data[4] = "{0}".format(latitude_range)
            row_data[5] = "{0}".format(longitude_range)
            row_data[6] = "{0}".format(overhead_message)
            row_data[7] = "{0}".format(visible_message)
            if not heading_printed:
                print_utils.print_headings(column_headings, column_widths)
            print_utils.print_message(row_data, column_widths)
            heading_printed = True
            if platform.system() != "Darwin":
                if is_near:
                    if is_visible:
                        lights_utils.chase(colors.green, 60, 0.1)
                    else:
                        lights_utils.chase(colors.blue, 60, 0.1)
                else:
                    time.sleep(60)
            else:
                time.sleep(60)
        print("")


if __name__ == '__main__':
    ISS_Tracker = ISSTracker()
    ISS_Tracker.track_iss()
