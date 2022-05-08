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
        max_duration = int(duration * sleep)
        for duration in range(0, max_duration):
            for led in range(0, self.leds):
                self.lights[led] = color
                time.sleep(sleep)
                self.lights[led] = colors.black

    def fill(self, color, duration, sleep):
        self.lights.fill((color))
        time.sleep(duration * sleep) 

    def blink(self, color, duration, sleep):
        max_duration = int(duration * sleep)
        print("blink - color={0}, duration={1}, sleep={2}, max_duration={3}".format(color, duration, sleep, max_duration))
        for duration in range(0, max_duration):
            self.lights.fill((color))
            time.sleep(sleep)
            self.lights.fill((colors.black))

    def red_white_blue_blink(self, duration, sleep):
        max_duration = int(duration * sleep)
        for duration in range(0, max_duration):
            self.lights.fill((colors.red))
            time.sleep(sleep)
            self.lights.fill((colors.white))
            time.sleep(sleep)
            self.lights.fill((colors.blue))
            time.sleep(sleep) 
        self.lights.fill((colors.black)) 
