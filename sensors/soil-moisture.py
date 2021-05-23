"""
Measure soil moisture with the Kuman soil moisture sensor
https://www.amazon.com/gp/product/B071F4RDHY/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=piddlerinther-20&linkId=77f1c0f9c67c51d76b687628afa62ce1&language=en_US
"""

import sys
import os
import time
from dotenv import load_dotenv
sys.path.append(os.path.abspath('./services'))
import mqtt
import RPi.GPIO as GPIO
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
  if GPIO.input(channel):
    print("No Water Detected!")
  else:
    print("Water Detected!")
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
  time.sleep(1)
