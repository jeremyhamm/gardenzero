import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
import time

def load_env():
  load_dotenv()

def get_client():
  return mqtt.Client()

def on_connect(client, userdata, flags, rc):
  if rc==0:
    print("Good MQTT connection")
  else:
    print("Bad MQTT connection")

def get_connection():
  load_env()

  username = os.environ.get("MQTT_USER")
  password = os.environ.get("MQTT_PASSWORD")
  host = os.environ.get("MQTT_BROKER_HOST")
  
  client = get_client()
  client.on_connect=on_connect
  client.username_pw_set(username, password)
  client.connect(host)
  client.loop_start()
  time.sleep(1)

  return client
