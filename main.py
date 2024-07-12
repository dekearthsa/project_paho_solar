import paho.mqtt.client as mqtt
import json
## IPv4 192.168.1.107

HOST_MQTT = "localhost"
PORT_MQTT = 1883
PUB_MQTT = "test/pub/topic"
SUB_MQTT = "test/topic"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(SUB_MQTT)

def on_message(client, userdata, msg):
    load_json_data = json.loads(msg.payload)
    print(load_json_data['deviceID'])
    if load_json_data['deviceID'] == "test":
        client.publish(PUB_MQTT, "Hello MQTT")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()


