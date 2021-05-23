#!/usr/bin/python3

"""

https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2
"""

import sys
import os
import glob
import time
sys.path.append(os.path.abspath('../services'))
import mqtt

class DS18B20(object):
  def __init__(self):        
    self.client = mqtt.get_connection()
    self.device_file = glob.glob("/sys/bus/w1/devices/28*")[0] + "/w1_slave"
      
  def read_temp_raw(self):
    f = open(self.device_file, "r")
    lines = f.readlines()
    f.close()
    return lines
      
  def crc_check(self, lines):
    return lines[0].strip()[-3:] == "YES"
      
  def read_temp(self):
    temp_c = -255
    attempts = 0
    
    lines = self.read_temp_raw()
    success = self.crc_check(lines)
    
    while not success and attempts < 3:
      time.sleep(.2)
      lines = self.read_temp_raw()            
      success = self.crc_check(lines)
      attempts += 1
    
    if success:
      temp_line = lines[1]
      equal_pos = temp_line.find("t=")            
      if equal_pos != -1:
        temp_string = temp_line[equal_pos+2:]
        temp_c = float(temp_string)/1000.0
        temp_f = round((temp_c * 1.8) + 32, 1)

        self.client.publish("garden/soil-temperature", temp_f)
    
    return temp_f

if __name__ == "__main__":
  obj = DS18B20()
  while True:
    print("Temp: %s F" % obj.read_temp())
    time.sleep(300)