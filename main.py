import paho.mqtt.client as mqtt
import json
## IPv4 192.168.1.107

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    # print(f"{msg.topic} {msg.payload}")
    load_json_data = json.loads(msg.payload)
    # print("load_json_data => ", load_json_data)
    print(load_json_data['deviceID'])
    if load_json_data['deviceID'] == "test":
        client.publish("test/pub/topic", "Hello MQTT")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.on_publish = on_publish
client.connect("localhost", 1883, 60)
client.loop_forever()


