## Web-controlled LED

import RPi.GPIO as GPIO
import time
import sys
from pubnub import Pubnub

GPIO.setmode (GPIO.BCM)

LED_PIN = 4

GPIO.setup(LED_PIN,GPIO.OUT)


pubnub = Pubnub(publish_key='demo', subscribe_key='demo')

channel = 'disco'

def _callback(m, channel):
	print(m)
	if m['led'] == 1:
		for i in range(6):
		    GPIO.output(LED_PIN,True)
		    time.sleep(0.5)
		    GPIO.output(LED_PIN,False)
		    time.sleep(0.5)
		    print('blink')

def _error(m):
	print(m)
 
pubnub.subscribe(channels=channel, callback=_callback, error=_error)

