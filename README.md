# iss-tracker
Python/Raspberry Pi based ISS Tracker that will light up some leds when overhead/visible.

This project uses the adafruit libraries to control a strip of WS2812b leds.
Depending on where the ISS is located, it will light up the strip either green or blue.
If it is during twilight and the ISS is close by, it will light up green.
All other times it will light up blue when it is over head.

On the Raspberry Pi you have to run it as root to get access to the 
proper pins for controlling the lights.

It was written using Python3.9.10.  I typically create individual python
virtual environments for all of my projects so you might consider doing that
as well.

The WS2812b led strip is connected to the Raspberry Pi on pin GPIO 18 (green) and GND.
The ground (blsck) is also connect to the ground on the 5V power supply along with the
power (red).

Eventually I'll put some photos on here so you can see the setup.

I did this project so I could light up a Lego ISS model when the ISS is close by.

To run the ISS tracker requires 2 command line parameters

`./iss-tracker.py --latitude <latitude of your location as a float> --longitude <longitude of your location as a float>`

"Close by" is defined as latitude + and - 5 and the longitude + and - 5.

Installation of iss-tracker.service file on raspberry pi:

sudo su -
copy the iss-tracker.service file to /etc/systemd/system/iss-tracker.service
systemctl enable iss-tracker.service
systemctl daeemon-reload
systemctl status iss-tracker.service
