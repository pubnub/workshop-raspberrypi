#Accessing the code from other modules
import RPi.GPIO as GPIO
import time
import sys
from pubnub import Pubnub

#Setting up the keys for Pubnub
publish_key = len(sys.argv) > 1 and sys.argv[1] or 'pub-c-156a6d5f-22bd-4a13-848d-b5b4d4b36695'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'sub-c-f762fb78-2724-11e4-a4df-02ee2ddab7fe'


## -----------------------------------------------------------------------
## Initiate Pubnub State
## -----------------------------------------------------------------------
pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key)
channel = 'motionsensor'
message = {'motion': 1}


# Asynchronous usage
def callback(message):
  print(message)

 
GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)
  
def MOTION(PIR_PIN):
  pubnub.publish(channel, message, callback=callback, error=callback)

print 'PIR Module Test (CTRL+C to exit)'
time.sleep(2)
print 'Ready'

try:
  GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
  while 1:
    time.sleep(100)

except KeyboardInterrupt:
  print 'Quit'
  
GPIO.cleanup()
