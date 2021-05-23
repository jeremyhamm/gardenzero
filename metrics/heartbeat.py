import sys
import os
import time
sys.path.append(os.path.abspath('../services'))
import mqtt

client = mqtt.get_connection()
while True:
  client.publish("garden/heartbeat", True)
  time.sleep(300)