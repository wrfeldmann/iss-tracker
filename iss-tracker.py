#!/usr/bin/env python3

import argparse
import logging
import logging.handlers
import os
import sys
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
        self.platform = utilities.get_platform()
        return

    def log_setup(self):
        logger = logging.getLogger("issLogger")
        logger.setLevel(logging.INFO)
        current_directory = os.getcwd()
        if self.platform == "OS X":
            if not os.path.exists("{0}/logs".format(current_directory)):
                os.mkdir("{0}/logs".format(current_directory))
            handler = logging.handlers.RotatingFileHandler("{0}/logs/iss-tracker.log".format(current_directory),
                                                           maxBytes=1048576,
                                                           backupCount=10)
        else:
            if not os.path.exists("{0}/logs".format(current_directory)):
                os.mkdir("{0}/logs".format(current_directory))
            handler = logging.handlers.RotatingFileHandler("{0}/logs/iss-tracker.log".format(current_directory),
                                                           maxBytes=1048576,
                                                           backupCount=10)
        formatter = logging.Formatter("%(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
    
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
        parser.add_argument("--radius",
                            help="[OPTIONAL] Radius from the ISS that the lattitude and longitude must be within to count as Overhead",
                            action="store",
                            type=float,
                            default=1500.0)
        self.args = parser.parse_args()

    def track_iss(self):
        logger = self.log_setup()
        logger.info("Starting iss-tracker.py")
        self.get_args()
        column_headings = dict()
        column_headings[1] = "Current Time"
        column_headings[2] = "ISS Latitude"
        column_headings[3] = "ISS Longitude"
        column_headings[4] = "My Latitude"
        column_headings[5] = "My Longitude"
        column_headings[6] = "Distance"
        column_headings[7] = "Overhead"
        column_headings[8] = "Visible"
        column_widths = dict()
        column_widths[1] = 23
        column_widths[2] = 12
        column_widths[3] = 13
        column_widths[4] = 11
        column_widths[5] = 12
        column_widths[6] = 8
        column_widths[7] = 8
        column_widths[8] = 7
        #print("")
        heading_printed = False
        if not self.platform == "OS X":
            lights_utils.red_white_blue_blink(50, 0.2)
        while True:
            now = datetime.now().astimezone()
            display_now = now.strftime("%Y-%m-%d %H:%M:%S %Z")
            iss_latitude, iss_longitude = iss_utils.current_ISS_location()
            str_iss_latitude, str_iss_longitude, latitude_range, longitude_range, my_latitude, my_longitude = \
                iss_utils.get_latitude_longitude_messages(self.args, iss_latitude, iss_longitude)
            distance = iss_utils.iss_distance(self.args, iss_latitude, iss_longitude)
            is_near, overhead_message = iss_utils.near_ISS(self.args, iss_latitude, iss_longitude, distance)
            is_visible = False
            visible_message = ""
            if sunrise_sunset_utils.is_dark(now, self.args) and is_near:
                visible_message = "Visible"
                is_visible = True
            row_data = dict()
            row_data[1] = "{0}".format(display_now)
            row_data[2] = "{0}".format(str_iss_latitude)
            row_data[3] = "{0}".format(str_iss_longitude)
            row_data[4] = "{0}".format(my_latitude)
            row_data[5] = "{0}".format(my_longitude)
            row_data[6] = "{0}".format("{0:.2f}".format(distance))
            row_data[7] = "{0}".format(overhead_message)
            row_data[8] = "{0}".format(visible_message)
            if not heading_printed:
                if self.platform == "OS X":
                    print_utils.print_headings(column_headings, column_widths)
                logger.info("{0} | {1} | {2} | {3} | {4} | {5} | {6}".format(column_headings[1].ljust(column_widths[1], " "),
                                                                 column_headings[2].rjust(column_widths[2], " "),
                                                                 column_headings[3].rjust(column_widths[3], " "),
                                                                 column_headings[4].rjust(column_widths[4], " "),
                                                                 column_headings[5].rjust(column_widths[5], " "),
                                                                 column_headings[6].rjust(column_widths[6], " "),
                                                                 column_headings[7].ljust(column_widths[6], " "),
                                                                 column_headings[8].ljust(column_widths[7], " ")))
            if self.platform == "OS X":
                print_utils.print_message(row_data, column_widths)
            logger.info("{0} | {1} | {2} | {3} | {4} | {5} | {6}".format(row_data[1].ljust(column_widths[1], " "),
                                                             row_data[2].rjust(column_widths[2], " "),
                                                             row_data[3].rjust(column_widths[3], " "),
                                                             row_data[4].ljust(column_widths[4], " "),
                                                             row_data[5].ljust(column_widths[5], " "),
                                                             row_data[6].rjust(column_widths[6], " "),
                                                             row_data[7].rjust(column_widths[7], " "),
                                                             row_data[8].ljust(column_widths[8], " ")))
            heading_printed = True
            if is_near:
                if is_visible:
                    #lights_utils.chase(colors.green, 60, 0.1)
                    if not self.platform == "OS X":
                        lights_utils.fill(colors.green, 60, 0.1)
                else:
                    #lights_utils.chase(colors.blue, 60, 0.1)
                    if not self.platform == "OS X":
                        lights_utils.fill(colors.blue, 60, 0.1)
                time.sleep(5)
            else:
                if not self.platform == "OS X":
                    lights_utils.fill(colors.black, 1, 0.1)
                time.sleep(30)


if __name__ == '__main__':
    ISS_Tracker = ISSTracker()
    ISS_Tracker.track_iss()
