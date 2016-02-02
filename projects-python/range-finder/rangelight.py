#import Pubnub, GPIO and time libraries

from pubnub import Pubnub 
import RPi.GPIO as GPIO
import time
import sys


loopcount = 0

##------------------------------
## Set up PubNub
## Put in Pub/Sub (Use your own keys!)
## Define your PubNub channel
##------------------------------
publish_key = len(sys.argv) > 1 and sys.argv[1] or 'pub-c-156a6d5f-22bd-4a13-848d-b5b4d4b36695'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'sub-c-f762fb78-2724-11e4-a4df-02ee2ddab7fe'


pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
channel = 'Rangefinder'



#Now to interacting with the hardware:

GPIO.setmode(GPIO.BCM)

#Set GPIO pins used on breadboard.

TRIG = 20
ECHO = 26
LIGHT = 16
#Connect the libraries to your GPIO pins 
print("Distance Measurement in Progess")
GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(LIGHT,GPIO.OUT)

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

    ##Speed of sound at sea-level is 343 m/s.
    ##34300 cm/s = Distance/Time; 34300 cm/s = Speed of sound;
    ##"Time" is there and back; divide by 2 to get time-to-object only.
    ##So: 34300 = Distance/(Time/2) >>> speed of sound = distance/one-way time
    
    
    ##Simplify + Flip it: distance = pulse_duration x 17150
    distance = pulse_duration*17150

##Round out distance for simplicity and print.

    distance = round(distance, 2)
    loopcount+=1
    print('shot #'+str(loopcount))
    
##Use the distance measurement as a proximity alarm.
##Set 'distance' in if-loop to desired alarm distance.
##When the alarm is tripped, the distance and a note are sent as a dictionary in a PubNub message, and the sensor stops searching.

    if distance <= 10:
        print("Distance:",distance,"cm")
        print("Proximity Detected")

        for i in range(6):
            GPIO.output(LIGHT,True)
            time.sleep(0.03)
            GPIO.output(LIGHT,False)
            time.sleep(0.03)
        message = {'distance': distance, 'Proximity': "True"}
        print pubnub.publish(channel, message)
        time.sleep(.3)
       

##If nothing is detected, the sensor continuously sends and listens for a signal, and publishes the distance to your PubNub channel.    
    else:
        print("Time", pulse_duration)
        print("Distance", distance, "cm")
        print("Too Far")

        message = {'distance': distance, 'Proximity' : 'False'}
        print pubnub.publish(channel, message)
        
    time.sleep(.3)



#Clean up GPIO pins + reset
GPIO.cleanup()
sys.exit()

