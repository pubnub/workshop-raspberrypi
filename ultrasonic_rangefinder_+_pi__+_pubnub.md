# Ultrasonic Rangefinder + Pi  + PubNub
## Section 1: Building the Hardware 
*Measure distances and trigger an alarm using PubNub Pub/Sub Messaging and Raspberry Pi*

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Full%20View.jpg)

### What You'll Need:

1. Raspberry Pi 2, set-up, with accessories (power, wifi, m+kb, monitor, or setup via SSH) (See ReadMe)
2. An HC-SR04 ultrasonic rangefinder
3. 8 jumper wires in 4 colors, with 2 of each color 
4. 1 1k Ohm resistor
5. 1 2.2k Ohm resistor
5. A browser or internet-capable smartphone 

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%200.jpg?raw=true)
### What You're Building and How It Works:

In this project, you'll build Pi-based ultrasonic rangefinder, which can be easily turned into a proximity alert with PubNub.

This system has two main elements: A Raspberry Pi and the rangefinder module itself. From a hardware perspective, this is a relatively simple system. Upon trigger from the Pi, the module emits a 40kHz pulse for 8-10 microseconds. This signal, beyond the range of human hearing, will bounce off of solid objects, and some of those bounced waves will return to the rangefinder. An element on the module is sensitive to this frequency, and when the reflected pulse is detected, it sends a signal back to the Pi. In code, the time elapsed between signal emission and reception can be put through simple math to find the distance of the reflecting object.

Electronically, there are a few quirks to be aware of when building our circuit. First, while many of the jumper wires *could* be connected directly from Pi to Module, we've used a solderless breadboard partially for ease of use.

Second, we have to pay attention to voltage. The ECHO signal comes at **5 volts** but the GPIO pin it will be transmitted through on the Pi is only rated at **3.3v**. Sending this higher voltage into an unprotected pin can damage our Pi, so our circuit design will have to adjust the voltage of the signal with a voltage divider.

### Step 1: Wiring up the Range Finder

Here is the circuit diagram for the whole device:
![image](https://www.modmypi.com/image/data/tutorials/hc-sr04/hc-sr04-tut-2.png)

Paying attention only to the top section for now, you'll see that the rangefinder sensor has four pins: Vcc (power), TRIG, ECHO, and GND  (ground).  
Vcc powers the module, and GND is used to ground it. 

TRIG allows the sensor to recieve a signal from the Pi, which then triggers the emission of an ultrasound pulse.
ECHO transmits back a signal when the sensor detects the reflected pulse. 

For now, pick four male-female jumper wires, each a different color, and attach them to the sensor. It should look similar to this: 

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step1.jpg?raw=true)

### Step 2: Wiring Power and Ground Pins on the Pi 

Leaving the sensor alone for a moment, let's wire up the system from the Pi side. 

First, attach a wire each to the **5v** and **GND** GPIO pins. In our case, we used Pin 2 for power and Pin 6 for ground. To keep things organized, your power wire should be the same color as that attached to the sensor's Vcc pin, and likewise for your GND wires. 

This is a useful diagram for reading the Pi's pin layout: 
![image](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900-1024x341.png)

One configuration may look like this: 
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%202.jpg)

### Step 3: Wiring Input and Output Pins on the Pi

Next, we will attach wires to two GPIO pins in order to send and recieve signals from the sensor module. 
Select a wire that matches that attached to the sensor's ECHO pin, and attach it to pin 37 (GPIO26). Next, match your TRIG wire and attach it to pin 38 (GPIO20).

It should look something like this (ECHO = grey; GPIO26, TRIG = violet; GPIO20):
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%203.jpg)

#### After steps 2 and 3, check to make sure your Pi's GPIO pins resemble this layout:
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%202+3.jpg?raw=true)

### Step 4: Linking PWR and Ground from the Pi to the Sensor 

First, connect your Pi's **Power** to the space in the first row of the breadboard's positive rail. In the second-row space on that rail, connect the sensor's Vcc cable. 

Once that's done, connect your Pi's **Ground wire** to the first row of the negative rail. In the second-row space on this rail, connect the sensor's GND wire. 

It should look something like this: 

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%205.jpg)

### Step 5: Linking TRIG to GPIO

Find a blank rail on the breadboard, and plug in your TRIG wire (from the sensor) and GPIO20 wire (from the Pi). These should be the same color. 

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%206.jpg)

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
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%207c.jpg?raw=true)


##That's the entirety of our hardware construction. Now, you're ready to write some code!##

*Based on ["HC-SR04 Ultrasonic Range Sensor on the Raspberry Pi"](http://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)*
