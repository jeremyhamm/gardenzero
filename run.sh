#!/bin/bash

# Sensors
python3  /home/pi/apps/garden-zero/sensors/soil-temperature.py &
python3  /home/pi/apps/garden-zero/sensors/soil-moisture.py &

# Metrics
python3  /home/pi/apps/garden-zero/metrics/heartbeat.py