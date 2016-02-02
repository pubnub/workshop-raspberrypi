## Web-controlled LED

import RPi.GPIO as GPIO
import time
import sys
from pubnub import Pubnub

GPIO.setmode (GPIO.BCM)

LED_PIN = 4

GPIO.setup(LED_PIN,GPIO.OUT)


pubnub = Pubnub(publish_key='pub-c-156a6d5f-22bd-4a13-848d-b5b4d4b36695', subscribe_key='sub-c-f762fb78-2724-11e4-a4df-02ee2ddab7fe')

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

