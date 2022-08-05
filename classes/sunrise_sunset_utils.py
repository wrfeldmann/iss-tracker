import requests

from classes.date_utils import DateUtils

date_utils = DateUtils()

class SunriseSunsetUtils():

    def __init__(self):
        return

    def is_dark(self, now, args):
        sunrise_sunset_base_url = "https://api.sunrise-sunset.org/json"
        sunrise_sunset_url = "{0}?lat={1}&lng={2}&formatted=0".format(sunrise_sunset_base_url,
                                                                      args.latitude,
                                                                      args.longitude)
        try:
            response = requests.get(sunrise_sunset_url)
            data = response.json()
            astronomical_twilight_begin_timestamp = date_utils.getTimestamp(
                data["results"]["astronomical_twilight_begin"])
            sunrise_timestamp = date_utils.getTimestamp(data["results"]["sunrise"])
            sunset_timestamp = date_utils.getTimestamp(data["results"]["sunset"])
            astronomical_twilight_end_timestamp = date_utils.getTimestamp(data["results"]["astronomical_twilight_end"])
        except:
            astronomical_twilight_begin_timestamp = 0
            sunrise_timestamp = 0
            sunset_timestamp = 0
            astronomical_twilight_end_timestamp = 0
            true_false = False
        timezone_offset = float(now.isoformat().split("T")[1][-6:].replace(":", "."))
        time_now = date_utils.getTimestamp(now.isoformat())
        astronomical_twilight_begin_timestamp = astronomical_twilight_begin_timestamp + (timezone_offset * 3600)
        sunrise_timestamp = sunrise_timestamp + (timezone_offset * 3600)
        sunset_timestamp = sunset_timestamp + (timezone_offset * 3600)
        astronomical_twilight_end_timestamp = astronomical_twilight_end_timestamp + (timezone_offset * 3600)
        true_false = False
        if (time_now >= astronomical_twilight_begin_timestamp and time_now <= sunrise_timestamp) or \
                (time_now >= sunset_timestamp and time_now <= astronomical_twilight_end_timestamp):
            true_false = True
        return true_false

