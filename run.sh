#!/bin/sh

# Sensors
nohup /home/pi/apps/garden-zero/sensors/soil-temperature.py &
nohup /home/pi/apps/garden-zero/sensors/soil-moisture.py &

# Metrics
nohup /home/pi/apps/garden-zero/metrics/heartbeat.py