#!/usr/bin/python

"""
Measure soil moisture with the Kuman soil moisture sensor
https://www.amazon.com/gp/product/B071F4RDHY/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=piddlerinther-20&linkId=77f1c0f9c67c51d76b687628afa62ce1&language=en_US
"""

import sys
import os
import time
import RPi.GPIO as GPIO
from dotenv import load_dotenv
sys.path.append(os.path.abspath('./services'))
import mqtt

def callback(channel):
  if GPIO.input(channel):
    print("I AM WATERED!")
    client.publish("garden/soil-moisture", True)
  else:
    print("I NEED WATER!")
    client.publish("garden/soil-moisture", False)

# MQTT
client = mqtt.get_connection()
client.publish("garden/soil-moisture", True) # Set initial mode to watered

#GPIO SETUP
channel = int(os.environ.get("SOIL_MOISTURE_GPIO"))
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)


while True:
  time.sleep(1)