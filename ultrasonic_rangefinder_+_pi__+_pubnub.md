# Ultrasonic Rangefinder + Pi  + PubNub
## Section 1: Building the Hardware 
*Measure distances and trigger an alarm using PubNub Pub/Sub Messaging and Raspberry Pi*

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Full%20View.jpg)

### What You'll Need:

1. Raspberry Pi 2, set-up, with accessories (power, wifi, m+kb, monitor, or setup via SSH) (See ReadMe)
2. An HC-SR04 Ultrasonic Rangefinder
3. 8 Jumper Wires in 4 colors, with 2 of each color 
4. 3 1k Ohm Resistors 
5. A browser or internet-capable smartphone 


### Step 1: Wiring up the Range Finder 
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%201.jpg)

### Step 2: Wiring Power and Ground Pins on the Pi 

Attach a wire each to the **5v** and **GND** GPIO pins.
![image](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900-1024x341.png)

One configuration may look like this: 
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%202.jpg)

### Step 3: Wiring Input and Output Pins on the Pi
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%203.jpg)

#### After steps 2 and 3, your Pi should look something like this:
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%202+3.jpg?raw=true)

### Step 4: Linking PWR and Ground from the Pi to the Sensor 

First, connect your Pi's **Power** to the space in the first row of the breadboard's positive rail. In the second-row space on that rail, connect the sensor's Power (labeled VCC). 

Once that's done, connect your Pi's **Ground wire** to the first row of the negative rail. In the second-row space on this rail, connect the sensor's GND wire. 

It should look something like this: 

![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%205.jpg)

### Step 5: Linking ECHO to GPIO
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%206.jpg)

### Step 6: Linking TRIG to GPIO 
![image](https://github.com/pubnub/workshop-raspberrypi/blob/master/images/Rangefinder%20Images/Rangefinder.Step%207.jpg)


*Based on ["HC-SR04 Ultrasonic Range Sensor on the Raspberry Pi"](http://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)*
