#Accessing the code from other modules
import RPi.GPIO as GPIO
import time
import sys
import picamera
from Pubnub import Pubnub

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
channel = 'proximitysensor'
message = {columns: [['data', 1]]}


# Asynchronous usage
def callback(message):
    print(message)

# setting the pins and creating camera instance
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
camera = picamera.PiCamera()

# When motion is detected, a message is sent to the user as well as a video is recorded

def MOTION(PIR_PIN):
    pubnub.publish(channel, message, callback=callback, error=callback)
    camera.start_recording('video.h264')
    sleep(5)
    camera.stop_recording()

print “PIR Module Test (CTRL+C to exit)”
time.sleep(2)
print “Ready”

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
        while 1:
time.sleep(100)

except KeyboardInterrupt:
    print “ Quit”

GPIO.cleanup()

