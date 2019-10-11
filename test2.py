import sys
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)    
    msg=str(message.payload.decode("utf-8"))
    topic=message.topic    
    messages.append([topic, msg])
    i=0
########################################
i=1
messages = []
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
print("value is ",GPIO.input(4))  
broker_address="localhost"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","zrvz/pi4/control/#")
client.subscribe("zrvz/pi4/control/#")
##print("Publishing message to topic","zrvz/pi4/control/4")
##client.publish("zrvz/pi4/control/4","0")
##GPIO.output(4,1)
 # wait
while(True):
##    time.sleep(10)    
    if len(messages)>0:    
        m=messages.pop(0)
        print("recieved control = ", m)
        GPIO.output(4,int(m[1]))
        print("value is ",GPIO.input(4))
##    i=0
##    time.sleep(4)
print("value is ",GPIO.input(4))  
client.loop_stop() #stop the loop