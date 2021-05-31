#!/usr/bin/python3

"""
Camera functionality for Garden Zero
https://picamera.readthedocs.io
"""

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

sleep(2)
#my_file = open('/dev/sda1/test.jpg', 'wb')
camera.capture('~/apps/photos/test.jpg')
