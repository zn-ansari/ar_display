import sys
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.IN)

#GPIO.setoutput(4,1)

pin5 = GPIO.input(5)
pin4 = GPIO.input(4)

print("using ",sys.version) #what version of python
mode=GPIO.getmode()
print("mode is ",mode)
GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
print("mode is ",mode)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,1)
print("value is ",GPIO.input(4))
GPIO.output(4,0)
print("value is ",GPIO.input(4))
GPIO.setup(5,GPIO.IN)
print("input value is ",GPIO.input(5))
#GPIO.cleanup()
print("board ",GPIO.BOARD)
print("bcm ",GPIO.BCM)

#settin up mqtt
messages = []
sub_topic = 'zrvz/pi/control/4'
##print("okay")
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected ok")
        results, mid = client.subscribe("test")
        print(results,mid)
##        client.connected_flag=True
def on_mess(client, userdata, message):
    msg=str(message.payload.decode(utf-8))
    print("message =",msg)
    topic=message.topic
    messages.append([topic, msg])

client = mqtt.Client()
client.on_connect= on_connect
client.on_message= on_mess
broker = "127.0.0.1"
client.loop_start()
client.connect(broker)
##print("connected to broker")

i = 0
while i<5:
    #client.publish("zrvz","Hello From Python")
##    client.loop_start()
    client.publish("zrvz/pi/GPIO4",GPIO.input(4))
##    client.loop()
    time.sleep(4)
##    print(len(messages))
    if len(messages)>0:
        m=messages.pop(0)
        print("recieved control = ", m)
        GPIO.ouput(4,int(m[1]))
        print("value is ",GPIO.input(4))        
        time.sleep(4)
    i=i+1

client.loop_stop()
sys.exit()









