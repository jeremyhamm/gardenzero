#!/usr/bin/python3

"""
Raspberry Pi Zero heartbeat 
https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2
"""

import sys
import os
import time
sys.path.append(os.path.abspath('./services'))
import mqtt

client = mqtt.get_connection()
interval = int(os.environ.get("INTERVAL_SECONDS"))
while True:
  client.publish("garden/heartbeat", "Powered")
  time.sleep(interval)