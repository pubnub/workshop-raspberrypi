# Pi-o-T: Prototyping IoT Devices with PubNub Data Streams and Raspberry Pi 

Thanks to its open software and hardware designs, the Raspberry Pi is well-suited to demonstrating the core tenants of the IoT. On a Pi, a tinkerer has full control. They can connect actuators and sensors, process data, and send information over a wi-fi connection. 


The key to the pi is initial simplicity with a high tolerance for increasing complexity. For IoT applications, PubNub Data Streams bring this same usability to inter-device communication, enabling even a beginner to create realtime, bidirectional communication between their own embedded devices. 

From bare board to functioning system, this tutorial will walk through the construction of a simple proximity alarm that sends data over a Pubnub Data Stream to a webpage. In the last step, we show how you can easily upgrade this basic device to communicate with a [motion detector](), stepping into the world of bi-directional IoT communication.

Before you start, you'll want to check out some resources for getting started with the Raspberry Pi, as this tutorial assumes a machine already running Raspbian:

*Tomomi's Getting Started* 

*Getting Started on Raspberrypi.org*

**Let's Build.**

# Description of the project

## Section 1: Building the Hardware 
*Measure distances and trigger an alarm using PubNub Pub/Sub Messaging and Raspberry Pi*

### What You'll Need:
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Rangefinder.Full%20View.jpg)

1. Raspberry Pi 2, set-up, with accessories (power, wifi, m+kb, monitor, or setup via SSH) (See ReadMe)
2. An HC-SR04 ultrasonic rangefinder
3. 8 jumper wires in 4 colors, with 2 of each color 
4. 1 1k Ohm resistor
5. 1 2.2k Ohm resistor
5. A browser or internet-capable smartphone 

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Rangefinder.Step%200.jpg)
### What You're Building and How It Works:

In this project, you'll build Pi-based ultrasonic rangefinder, which can be easily turned into a proximity alert with PubNub. We'll get to that later.

This system has two main elements: A Raspberry Pi and the rangefinder module itself. From a hardware perspective, this is a relatively simple system. 

Upon trigger from the Pi, the module emits a 40kHz pulse for 8-10 microseconds. This signal, beyond the range of human hearing, will bounce off of solid objects, and some of those bounced waves will return to the rangefinder.

 An element on the module is sensitive to this frequency, and when the reflected pulse is detected, it sends a signal back to the Pi. In code, the time elapsed between signal emission and reception can be put through simple math to find the distance of the reflecting object.

Electronically, there are a few quirks to be aware of when building our circuit. First, while many of the jumper wires *could* be connected directly from Pi to Module, we've used a solderless breadboard partially for ease of use.

**We have to pay attention to voltage.** The ECHO signal comes at **5 volts** but the GPIO pin it will be transmitted through on the Pi is only rated at **3.3v**. Sending this higher voltage into an unprotected pin can damage our Pi, so our circuit design will have to adjust the voltage of the signal with a voltage divider.

### Step 1: Wiring up the Range Finder

Take a bit to check out the circuit diagram for the whole device:
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Circuit%20Diagram.png)

Paying attention only to the top section for now, you'll see that the rangefinder sensor has four pins: Vcc (power), TRIG, ECHO, and GND  (ground).  

**Vcc** powers the module, and **GND** is used to ground it. 

**TRIG** allows the sensor to recieve a signal from the Pi, which then triggers the emission of an ultrasound pulse.

**ECHO** transmits back a signal when the sensor detects the reflected pulse. 

For now, pick four male-female jumper wires, each a different color, and attach them to the sensor. It should look similar to this: 

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Rangefinder.Step1.jpg)

### Step 2: Wiring Power and Ground Pins on the Pi 

Leaving the sensor alone for a moment, let's wire up the system from the Pi side. 

First, attach a wire each to the **5v** and **GND** GPIO pins. In our case, we used Pin 2 for power and Pin 6 for ground. To keep things organized, your power wire should be the same color as that attached to the sensor's Vcc pin, and likewise for your GND wires. 

This is a useful diagram for reading the Pi's pin layout: 
![image](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900-1024x341.png)

One configuration may look like this: 
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Rangefinder.Step%202.jpg)

### Step 3: Wiring Input and Output Pins on the Pi

Next, we will attach wires to two GPIO pins in order to send and recieve signals from the sensor module. 
Select a wire that matches that attached to the sensor's ECHO pin, and attach it to pin 37 (GPIO26). Next, match your TRIG wire and attach it to pin 38 (GPIO20).

It should look something like this (ECHO = blue; GPIO26, TRIG = green; GPIO20):
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Rangefinder.Step%203.jpg)

#### After steps 2 and 3, check to make sure your Pi's GPIO pins resemble this layout:
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Rangefinder.Step%202%2B3.jpg)

### Step 4: Linking PWR and Ground from the Pi to the Sensor 

First, connect your Pi's **Power** to the space in the first row of the breadboard's positive rail. In the second-row space on that rail, connect the sensor's Vcc cable. 

Once that's done, connect your Pi's **Ground wire** to the first row of the negative rail. In the second-row space on this rail, connect the sensor's GND wire. 

It should look something like this: 

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Rangefinder.Step%205.jpg)

### Step 5: Linking TRIG to GPIO

Find a blank rail on the breadboard, and plug in your TRIG wire (from the sensor) and GPIO20 wire (from the Pi). These should be the same color. 

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Rangefinder%20Step%206.jpg)

### Step 6: Linking ECHO to GPIO

This is the trickiest step of this construction, but it isn't too difficult.

We can't simply attach the sensor's ECHO wire to the Pi's GPIO pin, as the sensor module would be outputting a 5v signal to a pin rated only for 3.3v, and this could result in damage to the Pi.

With resistors, we can create a voltage divider to bring the voltage down to an acceptable level.
A voltage divider consists of two resistors (R1 and R2) in series connected to an input voltage (Vin), which needs to be reduced to our output voltage (Vout). In our circuit, Vin will be ECHO, which needs to be decreased from 5V to our Vout of 3.3V.

![image](https://www.modmypi.com/image/data/tutorials/hc-sr04/hc-sr04-tut-1.png)

For our purposes, we will use a 1k oHm resistor for R1 and a 2.2k oHm resistor for R2. Should you be interested, the inspiration for this tutorial, linked at the bottom, has a good explanation of the math involved.  

Actually building the voltage divider:
  1. Plug your ECHO wire into a blank rail
  2. Use your R1 resistor (1k) to link that rail to another blank rail. 
  3. Link this rail to the breadboard's Ground with your R2 resistor (2.2k), leaving at least one space between your R1 and R2 elements. 
  4. In the blank space between resistors, plug in the Pi's GPIO26 wire, linking ECHO to your Pi. 
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/rangefinder/Rangefinder.Step%207c.jpg)


**That's the entirety of our hardware construction. Now, you're ready to write some code!**

*Based on ["HC-SR04 Ultrasonic Range Sensor on the Raspberry Pi"](http://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)*

If you are using a mini breadboard, your circuit should look like this:

![image](../../images/rangefinder/fritzing-ultrasonic-mini.png)


##Section 2: Writing the Code##

Our device, when completed, will act as a proximity alarm by publishing alert data and distance to a webpage, which can be accessed on any browser-capable device. 

###A Word About PubNub###



To get there, the overall design of our device has to accomplish 3 main tasks:

  1. Find the range of an object with a pulse of ultrasonic waves
  2. Keep track of when an object enters its proximity 
  3. Publish range and alarm data over a PubNub channel

With PubNub and GPIO libraries, this is simpler than it seems. 

**Full Code can be found [here.](https://github.com/pubnub/workshop-raspberrypi/blob/master/projects-python/range-finder/rangefinder.py)**

####1. Setting up the Code####

a. Libraries 

  We'll be importing three libraries to build our device's functionality: GPIO, PubNub, and time. We'll also take   the opportuntiy to create a global variable that we'll use to track the number of rangefinding "shots" fired as the program runs.

```python
from Pubnub import Pubnub 
import RPi.GPIO as GPIO
import time
import sys


loopcount = 0
```

b. PubNub setup

  With the libraries imported, we can now call and calibrate them as we need for our device. 

  To set up PubNub Pub-Sub messaging, the project's communication infrastructure, start by adding this code:

```python
Publish_key = len(sys.argv) > 1 and sys.argv[1] or 'demo'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'demo'
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'
cipher_key = len(sys.argv) > 4 and sys.argv[4] or ''
ssl_on = len(sys.argv) > 5 and bool(sys.argv[5]) or False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
channel = 'Rangefinder'
```

If you have a [PubNub account](http://www.pubnub.com/get-started/), replace the string 'demo' in *Publish_key* and *subscribe_key*, with your own keys. If not, you can use 'demo,' but common use of this key may result in throttled message speeds. 

The *channel* variable can be named whatever you like. Your Pub key, sub key, and channel name will all be used to transmit and keep track of the data from your Pi. 

c. GPIO Pin Setup

  The sensor module communicates with the Pi by sending electrical signals to specific pins. When recieving no     signal, a pin is read as LOW. When a signal is recieved, that pin switches to HIGH. This binary operation is at the heart of any digital I/O device, including LEDs and stepper motors. For now, we'll deal with it in its simplest form. 

First, we have to point our code to the pins we're using. To do so, add the following to your code:

```python
GPIO.setmode(GPIO.BCM)
```

The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number, rather than to the pin number. The BCM numbers are those after the "GPIO" in the board overview diagram:
![image](https://camo.githubusercontent.com/ca1ff23008fb7000828355b50768ae7ce2b83936/687474703a2f2f7777772e72617370626572727970692d7370792e636f2e756b2f77702d636f6e74656e742f75706c6f6164732f323031322f30362f5261737062657272792d50692d4750494f2d4c61796f75742d4d6f64656c2d422d506c75732d726f74617465642d32373030783930302d31303234783334312e706e67)

In our hardware construction, we plugged our TRIG cable into pin 38 (GPIO 20) and our ECHO cable into pin 37 (GPIO 26). So, in our code, we'll add variables to easily reference these values:

```python
TRIG = 20
ECHO = 26
```

And then we'll configure the correct pins for input and output:

```python
print("Distance Measurement in Progess")
GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)`
```

"TRIG" will be the pin on which a signal is sent to the sensor module, which will trigger the ultrasonic pulse. It's an Output.

"ECHO" receives a signal when the module detects the reflected soundwave, flipping from LOW to HIGH. It's an Input.

####2. Sending the Pulse####

Each shot works by sending a 10-microsecond pulse at around 40khz, marking the time at which the pulse is sent and then, subsequentially, when the reflected signal is detected. To ensure accuracy, we must first settle the trigger and wait:

```python
GPIO.output(TRIG,False)
print("Waiting for sensor to settle.")

time.sleep(2)
```
We then send the pulse.    
Because we want to continuously check for range, we nest the entirety of the rangefinding functionality within a 'While' loop:

```python
while True:
   GPIO.output(TRIG, True)
   time.sleep(0.00001)
   GPIO.output(TRIG, False)
```
Here, we're calling GPIO.output to control a previously defined output pin. In this case, we first pass 'TRIG' as an argument to the function. By calling "True" as the second argument, we turn the pin to HIGH and send a signal.

After waiting for 10 microseconds, we call GPIO.output again, but this time set the second argument to False, halting the signal and turning the pin to LOW. 

####3. Waiting for the Echo And Recording the Signal####

Just after we send the pulse, we will create the variable "pulse_start" and set it equal to the current time, all in order to mark the beginning of the time between signal sent and recieved. 

```python
    print("before pulse start")  # debug statement
    pulse_start = time.time()  
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
```

```python
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    print("after pulse")  # debug statement
    pulse_duration = pulse_end - pulse_start
```
    
When the signal is recieved, our ECHO pin flips to HIGH, reading out as '1' rather than '0' in our code. 
At this point, we take another time.time reading with a variable named "pulse_end." We find the final duration by subracting pulse_start from pulse_end. 

####4. Calculating Distance and Sending Data####

Using known values, we can easily turn our pulse_duration value into a measure of distance.

At sea-level, the speed of sound is 34300 centimeters/second, Or:
**Speed = Distance/Time**. Our time, contained in **pulse_duration**, actually represents the time to *and* back from the detected object. To get the distance from the sensor to that object, we'll need to divide our time in half.
So:

**34,300 = Distance/Time/2**, or, simplified and flipped: **Distance = 17,150 * time**

In code:
```python
  distance = pulse_duration*17150
```
  
We then round out the value, for neatness, and print it with the current "shot" number:

```python
  distance = round(distance, 2)
  loopcount+=1
```

Finally, we publish the distance data over our PubNub channel, which was defined in Step 1. At this point, we can easily integrate the functionality of a proximity alarm and send two types of messages, depending on the final value of "distance."  

```python
  print("Distance:",distance,"cm")
  print("Measured distance")
  message = {['distance', distance]}
  print pubnub.publish(channel, message)
  time.sleep(1)
```

We publish distance to our own log.

We use the function pubnub.publish to publish to our channel, which is passed via the variable we created as an argument. 

The very, very last step is to clean out the pins and halt the process:

```python
GPIO.cleanup()
sys.exit()
```

On the Pi terminal, run the code with the command:
`sudo python your-program-name.py`.

Watch for your message data. If a reading takes too long, or if a number seems too high, there may be a few problems. Check your wiring, and make sure the object you're measuring is within 4 meters- the effective range of this particular sensor.



##Section 3: Connecting to the IoT##

So far, we've turned a Raspberry Pi into a local range-finder, which can measure the distance between a sensor module and an object fairly accurately within a moderate vicinity. 

It uses PubNub to send data over the internet to an end-user device, allowing you to monitor a space watched by the device.

But, this doesn't realize the full promise of the IoT. To do that, our proximity alarm would have to communicate with other devices. Their statuses and outputs would have to be readable and actionable by our device.

Luckily, with PubNub, we can do this with **less than 20 lines of code.** By adding a subscription function to our code, we can easily reconfigure this device to communicate bi-directionally with other connected machines.

For the purposes of this tutorial, we'll connect our rangefinder through PubNub to a [motion detector](link to Motion Detector tutorial). When that machine detects motion, the rangefinder will fire, sending an alert when an object gets too close.

Whereas in the above code we run the rangefinding code automatically and only *published* to a PubNub channel, we now want to detect range **only** after receiving a flagged message from another device. 

[Full Code](rangefinder.py)

###1. Setting up subscription###

Leave the library import code and the setup of pins as it was. 
In the PubNub setup code bloc, you'll need the subscribe key of the device you want to 'listen' to.

From the *dashboard*, pick a motion detector's data stream. Copy the device's *Subscribe Key,* and paste it in your code:

```python
publish_key = len(sys.argv) > 1 and sys.argv[1] or 'demo'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'PASTE SUBKEY HERE'
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'
cipher_key = len(sys.argv) > 4 and sys.argv[4] or ''
ssl_on = len(sys.argv) > 5 and bool(sys.argv[5]) or False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
```

Under your variable 'channel,' add another channel variable (with a human-readable name!):

```python
subchannel = 'MotionDetector'
```

###2. Connecting RF Code to Motion Detection###

The PubNub subscription API requires the definition of 5 functions: callback, error, connect, reconnect, and disconnect. In general, using the data in a PubNub message will mean putting code in the Callback function. 


Inside of 
```python
def callback(submessage, channel):
```
Add a conditional statement waiting for the proper flag. In this case, we assume a motion detector will publish
a message with a key "motion" set to either 0 or 1, depending on whether it detects motion.

```python
 if submessage["motion"] == 1:
```

*Check the dashboard to see what kind of values your chosen device is publishing.*

Then, nested within that conditional statment, **paste the entirety of the While Loop created in Section 2.** 

###3. Instantiating Subscription###

Skip down several lines, past the definition of the **disconnect** function. 
Here, we're now at the beginning of the code that will actually be run. 

As before, settle the sensor and wait.

```python
GPIO.output(TRIG,False)
print("Waiting for sensor to settle.")

time.sleep(2)
```

Then, call the pubnub.subscribe function, passing in the variable for your subscription channel:

```python
print("Now subscribing.")

##Actually subscribe to the channel to receive the messages:##
pubnub.subscribe(subchannel, callback=callback, error=callback, connect=connect, reconnect=reconnect, disconnect=disconnect)
```

If the subscribe key and message formatting match, you should soon see your rangefinder react and detect *only* when motion is detected. As before, a webpage subscribing to your rangefinder's channel can still act as an alarm if an object comes too close. Try placing the two sensors in a specific area in order to keep tabs on your personal space.




