import paho.mqtt.client as mqtt
import time

##print("okay")
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected ok")
        results, mid = client.subscribe("#")
        print(results,mid)
def on_message(client, userdata, message):
    msg=str(message.payload.decode("utf-8"))
    print("message =",msg)
    topic=message.topic
    messages.append([topic, msg])        
##
broker = "localhost"    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker)
client.loop_start() #start the loop
time.sleep(4) # wait
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")
time.sleep(4) # wait
client.loop_stop() #stop the loop##client.subscribe("zrvz/#",qos=1)

##client.loop_forever()
