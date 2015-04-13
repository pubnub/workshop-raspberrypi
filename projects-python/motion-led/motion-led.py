import RPi.GPIO as GPIO
import time
import sys
from Pubnub import Pubnub

pubnub = Pubnub(publish_key='demo', subscribe_key='demo')
channel = 'motionsensor'
message = 'Motion detected'

def callback(message):
    print(message)


GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)

LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

def MOTION(PIR_PIN):
    print 'Motion Detected!'
        GPIO.output(LED_PIN, True)
            pubnub.publish(channel, message, callback=callback, error=callback)
# GPIO.output(LED_PIN, False)

def STILL(PIR_PIN):
    print 'No Motion Detected!'
        GPIO.output(LED_PIN, False)
# GPIO.output(LED_PIN, False)

print 'PIR Module Test (CTRL+C to exit)'
time.sleep(2)
print 'Ready'

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
        while 1:
time.sleep(100)

except KeyboardInterrupt:
    print ' Quit'



try:
    GPIO.add_event_detect(PIR_PIN, GPIO.FALLING, callback=STILL)
        while 1:
time.sleep(100)

except KeyboardInterrupt:
    print ' Quit'
GPIO.cleanup()