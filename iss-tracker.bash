#!/bin/bash
#
# Maryland - ./iss-tracker.py --latitude 39.14179 --longitude -77.14780
# Alabama - ./iss-tracker.py --latitude 33.39231 --longitude -86.76309
cd /home/pi/iss-tracker
source /home/pi/virtualenvs/iss-tracker/bin/activate
./iss-tracker.py --latitude 33.39231 --longitude -86.76309

