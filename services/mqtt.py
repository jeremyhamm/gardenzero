import paho.mqtt.client as mqtt
from dotenv import load_dotenv

def loadEnv():
  dotenv_path = join(dirname(__file__), '.env')
  load_dotenv(dotenv_path)

def getClient():
  return mqtt.Client()

def authenticate():
  loadEnv()

  token = os.environ.get("MQTT_BROKER_PORT")

  print(token)
  
  client = getClient()
  client.username_pw_set("", "")

authenticate()