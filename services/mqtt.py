import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

def loadEnv():
  load_dotenv()

def getClient():
  return mqtt.Client()

def getConnection():
  loadEnv()

  username = os.environ.get("MQTT_USER")
  password = os.environ.get("MQTT_PASSWORD")
  host = os.environ.get("MQTT_BROKER_HOST")
  port = os.environ.get("MQTT_BROKER_PORT")
  
  client = getClient()
  client.username_pw_set(username, password)
  client.connect('http://192.168.1.151')

  return client
