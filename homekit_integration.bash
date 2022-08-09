#!/bin/bash

iss_location=$( tail -n 1 /home/pi/iss-tracker/logs/iss-tracker.log )

case "$iss_location" in
	*Visible* )
		echo "Visible"
		echo "`date +"%Y/%m/%d %H:%M:%S"` | Visible" >> /home/pi/iss-tracker/logs/homebridge-access.log
		;;
	*Overhead* )
		echo "Overhead"
		echo "`date +"%Y/%m/%d %H:%M:%S"` | Overhead" >> /home/pi/iss-tracker/logs/homebridge-access.log
		;;
	* )
	 	echo ""
		echo "`date +"%Y/%m/%d %H:%M:%S"` | Not Near Me" >> /home/pi/iss-tracker/logs/homebridge-access.log
esac
