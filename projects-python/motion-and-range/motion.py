#Accessing the code from other modules
import RPi.GPIO as GPIO
import time
import sys
from pubnub import Pubnub

#Setting up the keys for Pubnub
publish_key = len(sys.argv) > 1 and sys.argv[1] or 'demo'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'demo'
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'
cipher_key = len(sys.argv) > 4 and sys.argv[4] or ''
ssl_on = len(sys.argv) > 5 and bool(sys.argv[5]) or False

## -----------------------------------------------------------------------
## Initiate Pubnub State
## -----------------------------------------------------------------------
pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key, secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
channel = 'MotionDetector'
message = {'motion' : 1}


# Asynchronous usage
def callback(message):
  print(message)

# Setting the pin number as a variable so its easier to use, and setting it to receive an input.
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

# calling publish, which sends a message over the channel onto the internet
def MOTION(PIR_PIN):
  pubnub.publish(channel, message, callback=callback, error=callback)

print “PIR Module Test (CTRL+C to exit)”
time.sleep(2)
print “Ready”

# calling the publish only when the sensor detects motion
try:
  GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
  while 1:
    time.sleep(100)

except KeyboardInterrupt:
  print “ Quit”
  
GPIO.cleanup()
