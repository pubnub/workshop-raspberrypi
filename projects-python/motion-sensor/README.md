# Motion Sensor with Raspberry Pi and PubNub


The PIR sensor measures the IR radiation emitted by objects. The sensor is able to measure changes in the IR signature around it(when an object moves) and hence detect motion. This message can be sent to any device in the world using PubNub. With PubNub, all you need to do is to **publish** on a channel to the PubNub network, which can be **subscribed** to by any other device any where else in the world.


## Using a Pyroelectric IR Motion Detector


![image](../../images/PIR/pir-fullview.jpg)



## Step 1 : The hardware

### What You Need:

- Raspberry Pi 2 (Set up properly. See [Setting up Raspberry Pi](../README.md))
- [PIR sensor](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview)
- Breadboard
- 6x M-to-F jumper wires, 3 colors with 2 of each


### Wiring up PIR Sensor

Your PIR sensor should have 3-pin connection. 
Wire up to the sensor as following:

- Red wire to PIR-VCC (3-5VDC voltage power)
- Black wire to PIR-GND (ground power)
- Brown wire to PIR-OUT (signal out)

Note that not all sensor has thr 3-pin connection in the same order, so make sure you wire in the correct pins. The easy way to find out is that look for a power protection IC (looks red in the picture), and one pin next to it should be VCC.
 
![image](../../images/PIR/pir-sensor.jpg)

Now, plus the other ends of the wires to a breadborad:

- Red wire (PIR-VCC) to a positive rail (in the photo below, row 7, but you can use any positive rail)
- Black wire (PIR-GND) to a negative rail, next to the red wire
- Brown wire (PIR-OUT) to any blank rail (row 7, column b, but you can pick any blank)

![image](../../images/PIR/pir-breadboard.jpg)

### Wiring up Pi

Take another pair of red, black and brown wire.

First, plug into one end to Pi:

- Red wire to GPIO 5V (Pin 4)
- Black wire to GPIO GND (Pin 6)
- Brown wire to GPIO 4 (Pin 7)

![image](../../images/pi-modelb-gpio.png)


Then, plug into one end to the breadborad:

- Red wire (GPIO 5V) to a positive rail (in the photo below, raw 1, but you can use any positive rail)
- Black wire (GPIO GND) to a negative rail, next to the red wire
- Brown wire (GPIO 4) to the same rail as your PIR-OUT

![image](../../images/PIR/pir-breadboard-pi.jpg)

## Step 2 : The software


The motion sensor is designed to send a web based alarm, when it detects motion. To do this, the overall setup has to do detect motion and then publish a message using PubNub.

### The code

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

```python
publish_key = len(sys.argv) > 1 and sys.argv[1] or 'demo'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'demo'
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'
cipher_key = len(sys.argv) > 4 and sys.argv[4] or ''
ssl_on = len(sys.argv) > 5 and bool(sys.argv[5]) or False
```

**Initiate Pubnub State**

```python
pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key, secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
channel = 'motionsensor'
message = {['Motion', 1]}
```

**Setting up variables for the pins on Pi**


**Asynchronous usage of Pubnub publish API**

```python
def callback(message):
  print(message)
def MOTION(PIR_PIN):
  pubnub.publish(channel, message, callback=callback, error=callback)
```

print “PIR Module Test (CTRL+C to exit)”
time.sleep(2)
print “Ready”

**The logic that determines when the sensor has sensed motion**

```python
try:
  GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
  while 1:
    time.sleep(100)
except KeyboardInterrupt:
  print “ Quit”
GPIO.cleanup()
```

