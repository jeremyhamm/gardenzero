import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

def load_env():
  load_dotenv()

def get_client():
  return mqtt.Client()

def on_connect(client, userdata, flags, rc):
  if rc==0:
    print("connected OK Returned code=",rc)
  else:
    print("Bad connection Returned code=",rc)

def get_connection():
  load_env()

  username = os.environ.get("MQTT_USER")
  password = os.environ.get("MQTT_PASSWORD")
  host = os.environ.get("MQTT_BROKER_HOST")
  
  client = get_client()
  client.on_connect=on_connect
  client.username_pw_set(username, password)
  client.connect(host)

  return client
