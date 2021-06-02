#!/usr/bin/python3

"""
Measure humidity with the DHT11 sensor
https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
"""

import RPi.GPIO as GPIO
import time

data = []

GPIOPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIOPin,GPIO.OUT)
GPIO.output(GPIOPin,GPIO.HIGH)
time.sleep(0.025)
GPIO.output(GPIOPin,GPIO.LOW)
time.sleep(0.02)
GPIO.setup(GPIOPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def bin2dec(string_num):
  return str(int(string_num, 2))

for i in range(0,500):
  data.append(GPIO.input(GPIOPin))


bit_count = 0
tmp = 0
count = 0
HumidityBit = ""
crc = ""

try:
  for i in range(0, 8):
    bit_count = 0

    while data[count] == 0:
      tmp = 1
      count = count + 1

    while data[count] == 1:
      bit_count = bit_count + 1
      count = count + 1

    if bit_count > 3:
      crc = crc + "1"
    else:
      crc = crc + "0"
except:
  print("ERR_RANGE")
  exit(0)

Humidity = bin2dec(HumidityBit)

if int(Humidity) - int(bin2dec(crc)) == 0:
  print(Humidity)

else:
  print("ERR_CRC")

