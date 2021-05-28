#!/usr/bin/python3

"""
Camera functionality for Garden Zero
https://picamera.readthedocs.io
"""

from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
