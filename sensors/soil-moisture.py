"""
Measure soil moisture with the Kuman soil moisture sensor
https://www.amazon.com/gp/product/B071F4RDHY/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=piddlerinther-20&linkId=77f1c0f9c67c51d76b687628afa62ce1&language=en_US
"""

import sys
import os
import time
from dotenv import load_dotenv
sys.path.append(os.path.abspath('../services'))
import mqtt
import RPi.GPIO as GPIO
 
def callback(channel):  
	if GPIO.input(channel):
		print("Need Water")
	else:
		print("I am watered!")

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)
channel = 11
GPIO.setup(channel, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(channel, callback)

# This is an infinte loop to keep our script running
while True:
	# This line simply tells our script to wait 0.1 of a second, this is so the script doesnt hog all of the CPU
	time.sleep(1)

