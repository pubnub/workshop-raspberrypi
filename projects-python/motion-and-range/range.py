#This code subcsribes to a PIR Motion Detector's PubNub channel, ##
##activating a rangefinder when the PIR detects an object.##
#import Pubnub, GPIO and time libraries##

from pubnub import Pubnub
import RPi.GPIO as GPIO
import time
import sys

##Set up variables and RF##
i = 0


#Set GPIO pins used on breadboard.

GPIO.setmode(GPIO.BCM)
TRIG = 20
ECHO = 26

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

##------------------------------
## Set up PubNub
## Put in Pub/Sub and Secret keys (replace 'demo')
## Define your PubNub channel
##------------------------------

publish_key = len(sys.argv) > 1 and sys.argv[1] or 'demo'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'demo'
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'
cipher_key = len(sys.argv) > 4 and sys.argv[4] or ''
ssl_on = len(sys.argv) > 5 and bool(sys.argv[5]) or False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)

##Define Pub and Sub channels. Pub channel can be anything; Sub channel must match that of the device you're listening to, in this case from the motion detector.
channel = 'Rangefinder'
subchannel = 'MotionDetector'

##Define parameters PN will use to subscribe to another channel
##"Callback" is where you process the message, and it will hold most of our code.

# Asynchronous usage
def callback(submessage, channel):
    print(submessage)
    ##Check to see if motion has been detected##
    ##This line will depend on the nature of the message recieved.
    ##This demo code assumes that the motion detector will send a dicitonary with one item: 
    ##a key "motion" with a value of either true (1) or false(0)
    
    if submessage["motion"] == 1:
    
    ##If so, run Rangefinder code##
        print("Object detected! Distance Measurement in Progress")
        #Send a pulse for 10 microseconds.
        while True:
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

        #Instatiate a time stamp for when a signal is detected by setting beginning + end values.
        #Then subtract beginning from end to get duration value.

            pulse_start = time.time()
            while GPIO.input(ECHO)==0:
                #print("waiting for pulse signal")
                pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start

            ##Simplify + Flip it: distance = pulse_duration x 17150
            distance = pulse_duration*17150

        ##Round out distance for simplicity and print.

            distance = round(distance, 2)

        ##Use the distance measurement as a proximity alarm.
        ##Set 'distance' in if-loop to desired alarm distance.
        ##When the alarm is tripped, the distance and a note are sent as a dictionary in a PubNub message, and the sensor keeps searching.

            if distance <= 20:
                print("Distance:",distance,"cm")
                print("Proximity Detected")

                message = {'distance': distance, 'Proximity': 1}
                print pubnub.publish(channel, message)
                time.sleep(1)


        ##If nothing is detected, the sensor continuously sends and listens for a signal, and publishes the distance to your PubNub channel.
            else:
                print("Time:", pulse_duration)
                print("Distance:", distance, "cm")
                print("Object is far.")

                message = {'distance': distance, 'Proximity' : 0}
                print pubnub.publish(channel, message)

            time.sleep(1)

        #Clean up GPIO pins + reset
        GPIO.cleanup()
        sys.exit()
    else:
        print("Nothing detected.")

##These allow PN to communicate connection states and keep you notified. 
def error(message):
    print("ERROR : " + str(message))


def connect(message):
    print("CONNECTED")
    print(message)


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")

##______________________________##


#Settle the trigger and wait
GPIO.output(TRIG,False)
print("Waiting for sensor to settle.")

time.sleep(2)

print("Now subscribing.")

##Actually subscribe to the channel to receive the messages:##
pubnub.subscribe(subchannel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)

