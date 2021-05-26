#!/bin/sh

# Sensors
nohup python3 /home/pi/apps/garden-zero/sensors/soil-temperature.py &
nohup python3 /home/pi/apps/garden-zero/sensors/soil-moisture.py &

# Metrics
nohup python3 /home/pi/apps/garden-zero/metrics/heartbeat.py &