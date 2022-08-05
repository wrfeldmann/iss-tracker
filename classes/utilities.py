import sys

class Utilities():
    def __init__(self):
        return

    def getLongest(self, field, longest):
        if len(field) > longest:
            longest = len(field)
        return longest
        return longest

    def get_platform(self):
        platforms = {
            "linux1": "Linux",
            "linux2": "Linux",
            "darwin": "OS X",
            "win32": "Windows"
        }
        if sys.platform not in platforms:
            return sys.platform
        return platforms[sys.platform]