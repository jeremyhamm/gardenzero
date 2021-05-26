#!/bin/sh

(python3 /home/pi/apps/garden-zero/sensors/soil-temperature.py;python3 /home/pi/apps/garden-zero/sensors/soil-moisture.py;python3 /home/pi/apps/garden-zero/metrics/heartbeat.py)&