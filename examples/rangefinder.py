
#import Pubnub, GPIO and time libraries

from Pubnub import Pubnub 
import RPi.GPIO as GPIO
import time
import sys

import picamera

spicam = picamera.PiCamera()

loopcount = 0

## www.pubnub.com - PubNub Real-time push service in the cloud.
# coding=utf8

## PubNub Real-time Push APIs and Notifications Framework
## Copyright (c) 2010 Stephen Blum
## http://www.pubnub.com/

##Put in Pub/Sub and Secret keys
publish_key = len(sys.argv) > 1 and sys.argv[1] or 'demo'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'demo'
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'
cipher_key = len(sys.argv) > 4 and sys.argv[4] or ''
ssl_on = len(sys.argv) > 5 and bool(sys.argv[5]) or False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
channel = 'Rangefinder'
def callback(message, channel):
    print(message)
    #pubnub.unsubscribe(channel)


def error(message):
    print("ERROR : " + str(message))


def connect(message):
    print("CONNECTED")


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")


#pubnub.subscribe(channel, callback=callback, error=callback,
                 #connect=connect, reconnect=reconnect, disconnect=disconnect)



#Now to interacting with the hardware:

GPIO.setmode(GPIO.BCM)

#Set GPIO pins used on breadboard.

TRIG = 20
ECHO = 26

#Connect the libraries to your GPIO pins 
print("Distance Measurement in Progess")
GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

#Settle the trigger and wait 
GPIO.output(TRIG,False)
print("Waiting for sensor to settle.")

time.sleep(2)

#Send a pulse for 10 microseconds.

while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    #GPIO.cleanup()
    #sys.exit()

#Instatiate a time stamp for when a signal is detected by setting beginning + end values.
#Then subtract beginning from end to get duration value.

    print("before pulse start")
    pulse_start = time.time()
    while GPIO.input(ECHO)==0:
        #print("waiting for pulse signal")
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    print("after pulse")
    pulse_duration = pulse_end - pulse_start

    #Speed of sound at sea-level is 343 m/s.
    #34300 = Distance/(Time/2) >>> speed of sound = distance/one-way time
    #Simplify + Flip it: distance = pulse_duration x 17150

    distance = pulse_duration*17150

#Round out distance for simplicity and print.

    distance = round(distance, 2)
    loopcount+=1
    print('shot #'+str(loopcount))
    

    if distance <= 10:
        print("Distance:",distance,"cm")
        print("Proximity Detected")
        spicam.capture("spicam"+str(loopcount)+".jpg")
        
        message = {'distance': distance, 'Proximal?': "Proximal!"}
        print pubnub.publish(channel, message)
        time.sleep(1)
        #pubnub.unsubscribe(channel)
        break
    
    else:
        print("Time", pulse_duration)
        print("Distance", distance, "cm")
        print("Too Far")

        message = {'distance': distance, 'Proximal?' : 'Nope'}
        print pubnub.publish(channel, message)
        
    time.sleep(1)

#Subscribe to messages on the channel; Asynchronous usage
#time.sleep(10)


#Clean up GPIO pins + reset
GPIO.cleanup()
sys.exit()
#next step:
#while loop around detection
#reporting distance and/or proximity alarm based on distance value

