# Communication between 2 Pis

As a next step, what if you could do more when motion is detected, than just send an alarm to a user. One possibility is to send a message to a range finder (also connected to a Pi - [Range Finder Pi](../motion-and-range/RF+Motion Detector.py)). The other is to click a picture using the Pi camera module when motion is detected - [Spicam](../Spicam/SpiCamMotion.py). Here, the former project has been described in detail with the code.

## Step 1 : The idea behind it 

 - So far we have a device publishing data to the internet. But in an ideal case, you want it to be able to subscribe/receive data as well, and to consume  that data. 
 - So say have two Raspberry Pis(you can collaborate with the person next to you and become friends); one which powers the [motion sensor](../motion-sensor/Motionsensor.py) and one for the [range finder](../range-finder/rangefinder.py).
 - Your motion sensor code detects motion and publishes a message to "motionrange" channel to notify the range finder to capture the distance between the moving object and itself.
 - This way, the range finder is listening to data from one device, and acting upon the received data. 
 - In a real world scenario, think of how you can have several devices all talking to each other, and making smart decisions based on the information. 
 - This is where PubNub comes in, providing you with the ability to send messages instaneously. With PubNub, you don't have to limit yourself to just the Raspberry Pi; we support 70+ SDKs and platforms and easy to use APIs.

## Step 2 : The software

 - This code just builds on the previous basic example.
 - The publish key, subscribe key and the channel for both the Pis have to be the same so they can bidirectionally talk to each other. 
 - This is the only change to make. (line 17 and 18 in the [Motionsensor_rangefinder.py](../motion-and-range/Motionsensor_rangefinder.py)) 

### Breaking up the code

#### Line by line explanation of what the code does:

**Accesing the code from other modules. The following modules are used in the code:**

 - GPIO to access the GPIO(general purpose input output)pins on the Raspberry Pi. This library lets handles the interfacing with the pins.
 - sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
 - Pubnub allows you to access the PubNub APIs to publish the messages over the internet.
 
 ```python
import RPi.GPIO as GPIO
import sys
from Pubnub import Pubnub
```

**Setting up the keys for Pubnub**

Every one who signs up for PubNub, gets a unique set of keys. This way, you can choose the devices that can send and receive messages from your device. 

Once you have a [PubNub account](https://www.pubnub.com/get-started/), replace the string 'demo' in Publish_key and subscribe_key, with your own keys. If not, you can use 'demo,' but common use of this key may result in throttled message speeds.


```python
publish_key = len(sys.argv) > 1 and sys.argv[1] or 'demo'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'demo'
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'
cipher_key = len(sys.argv) > 4 and sys.argv[4] or ''
ssl_on = len(sys.argv) > 5 and bool(sys.argv[5]) or False
```

**Initiate Pubnub State**

 - In order to use the PubNub APIs, it is necessary to create a PubNub object using the keys we got above. 
 - The channel variable can be named whatever you like. **This is where you set the channel, pub key and sub key to be the same as in the in the [RF+Motion Detector.py](../motion-and-range/RF+Motion Detector.py)**
 - The message argument can contain any JSON serializable data, including: Objects, Arrays, Ints and Strings. Message data should not contain special python classes or functions as these will not serialize. String content can include any single-byte or multi-byte UTF-8 character.

```python
pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key, secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
channel = 'motionsensor'
message = {['Motion', 1]}
```

**Setting up variables for the pins on Pi**

The sensor module communicates with the Pi by sending electrical signals to specific pins. When recieving no signal, a pin is read as LOW. When a signal is recieved, that pin switches to HIGH. This binary operation is at the heart of any digital I/O device, including LEDs and stepper motors. For now, we'll deal with it in its simplest form.

First, we have to point our code to the pins we're using. To do so, add the following to your code:

```python
GPIO.setmode(GPIO.BCM)
```
The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number, rather than to the pin number. The BCM numbers are those after the "GPIO" in the board overview diagram: 
![image](https://camo.githubusercontent.com/ca1ff23008fb7000828355b50768ae7ce2b83936/687474703a2f2f7777772e72617370626572727970692d7370792e636f2e756b2f77702d636f6e74656e742f75706c6f6164732f323031322f30362f5261737062657272792d50692d4750494f2d4c61796f75742d4d6f64656c2d422d506c75732d726f74617465642d32373030783930302d31303234783334312e706e67)

In our code, we have set up pin 7 (GPIO 4) to be the input pin receiving the sensor information.  

```python
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
```

**The logic that determines when the sensor has sensed motion**

The event_detected() function is designed to be used in a loop with other things, and it wont miss the change in state of an input while the CPU is busy working on other things. 

The GPIO library has built in a rising-edge function. A rising-edge is defined by the time the pin changes from low to high, but it only detects the change.

We want the Pi to publish a message when motion is detected. This is done by adding the callback function. 

```python
try:
  GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
  while 1:
    time.sleep(100)
except KeyboardInterrupt:
  print “ Quit”
```

**Asynchronous usage of Pubnub publish API**

The callback function, MOTION, calls pubnub.publish which sends the message over the channel, and also prints the message that is sent so you can see this on your screen as well. 

```python
def callback(message):
  print(message)
def MOTION(PIR_PIN):
  pubnub.publish(channel, message, callback=callback, error=callback)
```

**Some print statements when the code is run, just to enhance the user experience**

```python
print “PIR Module Test (CTRL+C to exit)”
time.sleep(2)
print “Ready”
```

**Exiting your program cleanly**

RPi.GPIO provides a built-in function GPIO.cleanup() to clean up all the ports you’ve used. It only affects any ports you have set in the current program. It resets any ports you have used in this program back to input mode. 

```python
GPIO.cleanup()
```

