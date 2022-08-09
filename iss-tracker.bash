#!/bin/bash
#
# Copyright (c) 1999 - 2022, Rick Feldmann
#
# maintainer: Rick Feldmann
# email     : wrfeldmann@me.com
# version   : 1.0
#
# iss-tracker.bash
#
# This script starts the iss-tracker.py script but will source the correct python virtual environment
# depending on the operating system (Mac OS or raspberry pi linux)
#
# You will want to change the settings of the locations based on your specific setup.
#
echo "Running on $OSTYPE"

if [[ "$OSTYPE" == "darwin"* ]]; then
  source $HOME/Documents/Software_Development/virtualenvs/iss-tracker/bin/activate
  cd /Users/rickfeldmann/Documents/Software_Development/git/iss-tracker
else
  cd /home/pi/iss-tracker
  source /home/pi/virtualenvs/iss-tracker/bin/activate
fi
./iss-tracker.py --latitude 33.39231 --longitude -86.76309 --radius 1500
