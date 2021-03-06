#!/usr/bin/python3

"""
Measure soil moisture with the Adafruit stemma soil sensor i2c
https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/
"""

import sys
import os
import time
import board
from adafruit_seesaw.seesaw import Seesaw
from dotenv import load_dotenv
sys.path.append(os.path.abspath('./services'))
import mqtt

i2c_bus = board.I2C()
sensor = Seesaw(i2c_bus, addr=0x36)

# MQTT
client = mqtt.get_connection()

while True:
    # read moisture level through capacitive touch pad
    touch = sensor.moisture_read()

    # read temperature from the temperature sensor
    temp = sensor.get_temp()

    # Publish to MQTT
    client.publish("garden/soil-moisture", str(touch))

    interval = int(os.environ.get("INTERVAL_SECONDS"))
    time.sleep(interval)
