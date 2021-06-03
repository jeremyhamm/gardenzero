#!/bin/sh

# Sensors
/home/pi/apps/garden-zero/sensors/environment.py &
/home/pi/apps/garden-zero/sensors/soil-temperature.py &
/home/pi/apps/garden-zero/sensors/soil-moisture.py &

# Metrics
/home/pi/apps/garden-zero/metrics/heartbeat.py &
