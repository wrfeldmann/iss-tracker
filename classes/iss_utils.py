import requests

from geopy import distance

class ISSUtils():

    def __init__(self):
        return

    def near_ISS(self, args, iss_latitude, iss_longitude, distance):
        message = ""
        true_false = False
        if args.latitude - 12.5 <= iss_latitude <= args.latitude + 12.5 and \
                args.longitude - 12.5 <= iss_longitude <= args.longitude + 12.5:
            message = "Overhead"
            true_false = True
        if distance <= args.radius:
            message = "Overhead"
            true_false = True
        return true_false, message

    def current_ISS_location(self):
        try:
            response = requests.get(url="http://api.open-notify.org/iss-now.json")
            data = response.json()
            iss_latitude = float(data["iss_position"]["latitude"])
            iss_longitude = float(data["iss_position"]["longitude"])
        except:
            iss_latitude = 0.0
            iss_longitude = 0.0
        return iss_latitude, iss_longitude

    def get_latitude_longitude_ranges(self, args):
        start_latitude = args.latitude - 12.5
        end_latitude = args.latitude + 12.5
        start_longitude = args.longitude - 12.5
        end_longitude = args.longitude + 12.5
        return start_latitude, end_latitude, start_longitude, end_longitude

    def get_latitude_longitude_messages(self, args, iss_latitude, iss_longitude):
        start_latitude, end_latitude, start_longitude, end_longitude = self.get_latitude_longitude_ranges(args)
        my_latitude = "{0:.5f} N".format(args.latitude)
        if args.latitude < 0:
            my_latitude = "{0:.5f} S".format(args.latitude)
        my_longitude = "{0:.5f} E".format(abs(args.longitude))
        if args.longitude < 0:
            my_longitude = "{0:.5f} W".format(abs(args.longitude))
        start_latitude_range = "{0:.5f} N".format(start_latitude)
        if start_latitude < 0:
            start_latitude_range = "{0:.5f} S".format(start_latitude)
        end_latitude_range = "{0:.5f} N".format(end_latitude)
        if end_latitude < 0:
            end_latitude_range = "{0:.5f} S".format(end_latitude)
        start_longitude_range = "{0:.5f} E".format(abs(start_longitude))
        if start_longitude < 0:
            start_longitude_range = "{0:.5f} W".format(abs(start_longitude))
        end_longitude_range = "{0:.5f}E".format(abs(end_longitude))
        if end_longitude < 0:
            end_longitude_range = "{0:.5f} W".format(abs(end_longitude))

        str_iss_latitude = "{0:.5f} N".format(abs(iss_latitude))
        if iss_latitude < 0:
            str_iss_latitude = "{0:.5f} S".format(abs(iss_latitude))
        str_iss_longitude = "{0:.5f} E".format(abs(iss_longitude))
        if iss_longitude < 0:
            str_iss_longitude = "{0:.5f} W".format(abs(iss_longitude))

        latitude_range_message = "{0} -> {1}".format(start_latitude_range, end_latitude_range)
        longitude_range_message = "{0} -> {1}".format(start_longitude_range, end_longitude_range)
        return str_iss_latitude, str_iss_longitude, latitude_range_message, longitude_range_message, my_latitude, my_longitude

    def iss_distance(self, args, iss_latitude, iss_longitude):
        center_point = [{'lat': iss_latitude, 'lng': iss_longitude}]
        test_point = [{'lat': args.latitude, 'lng': args.longitude}]
        center_point_tuple = tuple(center_point[0].values())
        test_point_tuple = tuple(test_point[0].values())
        return distance.distance(center_point_tuple, test_point_tuple).miles