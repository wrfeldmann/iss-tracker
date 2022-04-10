import platform
import time

if platform.system() != "Darwin":
    import board
    import neopixel

from classes.colors import Colors
colors = Colors()

class LightsUtils():

    def __init__(self):
        if platform.system() != "Darwin":
            self.leds = 20
            self.lights = neopixel.NeoPixel(board.D18, self.leds)

    def chase(self, color, duration, sleep):
        max_duration = duration * sleep
        for duration in range(0, max_duration):
            for led in range(0, self.leds):
                self.lights[led] = color
                time.sleep(sleep)
                self.lights[led] = colors.black

    def fill(self, color, duration, sleep):
        self.lights.fill((color))
        time.sleep = duration * sleep

    def flash(self, color, duration, sleep):
        max_duration = duration * sleep
        for duration in range(0, max_duration):
            self.lights.fill((color))
            time.sleep(sleep)
            self.lights.fill((colors.black))
