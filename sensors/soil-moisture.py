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
sys.path.append(os.path.abspath('../services'))
import mqtt

i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr=0x36)

# MQTT
client = mqtt.get_connection()

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()

    # read temperature from the temperature sensor
    temp = ss.get_temp()

    print("temp: " + str(temp) + "  moisture: " + str(touch))

    client.publish("garden/soil-moisture", str(touch))
    time.sleep(1)
