#!/usr/bin/env bash

# Sensors
python3 ./sensors/soil-temperature.py &
python3 ./sensors/soil-moisture.py &

# Metrics
python3 ./metrics/heartbeat.py