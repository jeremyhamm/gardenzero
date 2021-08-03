#!/usr/bin/python3

"""
Measure humidity with the DHT11 sensor
https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
"""

import sys
import os
import RPi.GPIO as GPIO
import dht11
import time
import datetime
from dotenv import load_dotenv
sys.path.append(os.path.abspath('./services'))
#import services.mqtt

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 21
instance = dht11.DHT11(pin = 21)
result = instance.read()
client = mqtt.get_connection()

def formatTemperature(temp):
  return str(round((temp * 1.8) + 32, 1)) + '°F'

def formatHumidity(humidity):
  return str(round(humidity, 1)) + '%';


while True:
  result = instance.read()
  if result.is_valid():
    temp = formatTemperature(result.temperature)
    humidity = formatHumidity(result.humidity)
    interval = int(os.environ.get("INTERVAL_SECONDS"))

    client.publish("garden/equipment/temperature", temp)
    client.publish("garden/equipment/humidity", humidity)

    time.sleep(interval)

