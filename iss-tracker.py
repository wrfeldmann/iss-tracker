#!/usr/bin/env python3

import argparse
import platform
import time

if platform.system() != "Darwin":
    import board
    import neopixel


from datetime import datetime

import requests

from classes.colors import Colors
from classes.date_utils import DateUtils
from classes.print_utils import PrintUtils
from classes.utilities import Utilities

colors = Colors()
date_utils = DateUtils()
print_utils = PrintUtils()
utilities = Utilities()


class ISSTracker():

    def __init__(self):
        if platform.system() != "Darwin":
            self.leds = 20
            self.lights = neopixel.NeoPixel(board.D18, self.leds)

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

    def near_ISS(self):
        if self.args.latitude - 5 <= self.iss_latitude <= self.args.latitude + 5 and \
                self.args.longitude - 5 <= self.iss_longitude <= self.args.longitude + 5:
            return True
        else:
            return False

    def current_ISS_location(self):
        try:
            response = requests.get(url="http://api.open-notify.org/iss-now.json")
            data = response.json()
            self.iss_latitude = float(data["iss_position"]["latitude"])
            self.iss_longitude = float(data["iss_position"]["longitude"])
        except:
            self.iss_latitude = 0.0
            self.iss_longitude = 0.0

    def is_dark(self, now):
        sunrise_sunset_base_url = "https://api.sunrise-sunset.org/json"
        sunrise_sunset_url = "{0}?lat={1}&lng={2}&formatted=0".format(sunrise_sunset_base_url,
                                                                      self.args.latitude,
                                                                      self.args.longitude)
        try:
            response = requests.get(sunrise_sunset_url)
            data = response.json()
            astronomical_twilight_begin_timestamp = date_utils.getTimestamp(data["results"]["astronomical_twilight_begin"])
            sunrise_timestamp = date_utils.getTimestamp(data["results"]["sunrise"])
            sunset_timestamp = date_utils.getTimestamp(data["results"]["sunset"])
            astronomical_twilight_end_timestamp = date_utils.getTimestamp(data["results"]["astronomical_twilight_end"])
        except:
            astronomical_twilight_begin_timestamp = 0
            sunrise_timestamp = 0
            sunset_timestamp = 0
            astronomical_twilight_end_timestamp = 0
        timezone_offset = float(now.isoformat().split("T")[1][-6:].replace(":", "."))
        time_now = date_utils.getTimestamp(now.isoformat())
        astronomical_twilight_begin_timestamp = astronomical_twilight_begin_timestamp + (timezone_offset * 3600)
        sunrise_timestamp = sunrise_timestamp + (timezone_offset * 3600)
        sunset_timestamp = sunset_timestamp + (timezone_offset * 3600)
        astronomical_twilight_end_timestamp = astronomical_twilight_end_timestamp + (timezone_offset * 3600)
        if (time_now >= astronomical_twilight_begin_timestamp and time_now <= sunrise_timestamp) or \
                (time_now >= sunset_timestamp and time_now <= astronomical_twilight_end_timestamp):
            return True
        return False

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
        last_latitude = 0
        last_longitude = 0
        heading_printed = False
        while True:
            now = datetime.now().astimezone()
            display_now = now.strftime("%Y-%m-%d %H:%M:%S %Z")
            self.current_ISS_location()
            if last_latitude == 0 and last_longitude == 0:
                latitude_diff = 0.0
                longitude_diff = 0.0
            else:
                latitude_diff = last_latitude - self.iss_latitude
                longitude_diff = last_longitude - self.iss_longitude
            last_latitude = self.iss_latitude
            last_longitude = self.iss_longitude
            iss_latitude = "{0:.5f} N".format(abs(self.iss_latitude))
            if self.iss_latitude < 0:
                iss_latitude = "{0:.5f} S".format(abs(self.iss_latitude))
            iss_longitude = "{0:.5f} E".format(abs(self.iss_longitude))
            if self.iss_longitude < 0:
                iss_longitude = "{0:.5f} W".format(abs(self.iss_longitude))
            start_latitude = self.args.latitude - 5
            end_latitude = self.args.latitude + 5
            start_latitude_range = "{0:.5f} N".format(start_latitude)
            if start_latitude < 0:
                start_latitude_range = "{0:.5f} S".format(start_latitude)
            end_latitude_range = "{0:.5f} N".format(end_latitude)
            if end_latitude < 0:
                end_latitude_range = "{0:.5f} S".format(end_latitude)
            start_longitude = self.args.longitude - 5
            end_longitude = self.args.longitude + 5
            start_longitude_range = "{0:.5f} E".format(abs(start_longitude))
            if start_longitude < 0:
                start_longitude_range = "{0:.5f} W".format(abs(start_longitude))
            end_longitude_range = "{0:.5f}E".format(abs(end_longitude))
            if end_longitude < 0:
                end_longitude_range = "{0:.5f} W".format(abs(end_longitude))
            latitude_range_message = "{0} -> {1}".format(start_latitude_range, end_latitude_range)
            longitude_range_message = "{0} -> {1}".format(start_longitude_range, end_longitude_range)

            iss_location_message = "| {0} | {1} | {2} |".format(display_now,
                                                                      iss_latitude.rjust(len("ISS Latitude "), " "),
                                                                      iss_longitude.rjust(len("ISS Longitude "), " ")
                                                                      )
            iss_location_message = "{0} {1} | {2}".format(iss_location_message,
                                                          latitude_range_message.rjust(len(latitude_range_message), " "),
                                                          longitude_range_message.rjust(len(longitude_range_message)))
            is_near = False
            overhead_message = ""
            if self.near_ISS():
                overhead_message = "Overhead"
                is_near = True
            visible_message = ""
            if  self.is_dark(now) and is_near:
                for led in range(0, self.leds):
                    self.lights[led] = colors.red
                    time.sleep(0.1)
                    self.lights[led] = colors.black
                visible_message = "Visible"
            row_data = dict()
            row_data[1] = "{0}".format(display_now)
            row_data[2] = "{0}".format(iss_latitude)
            row_data[3] = "{0}".format(iss_longitude)
            row_data[4] = "{0}".format(latitude_range_message)
            row_data[5] = "{0}".format(longitude_range_message)
            row_data[6] = "{0}".format(overhead_message)
            row_data[7] = "{0}".format(visible_message)
            if not heading_printed:
                print_utils.print_headings(column_headings, column_widths)
            print_utils.print_message(row_data, column_widths)
            heading_printed = True
            if platform.system() != "Darwin":
                if is_near:
                    if self.is_dark(now):
                        for duration in range(0, 600):
                            for led in range(0, self.leds):
                                self.lights[led] = colors.green
                                time.sleep(0.1)
                                self.lights[led] = colors.black
                    else:
                        for duration in range(0, 600):
                            for led in range(0, self.leds):
                                self.lights[led] = colors.blue
                                time.sleep(0.1)
                                self.lights[led] = colors.black
            else:
                time.sleep(60)
        print("")

if __name__ == '__main__':
    ISS_Tracker = ISSTracker()
    ISS_Tracker.track_iss()
