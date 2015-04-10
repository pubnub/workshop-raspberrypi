# Spy cam

All of us have imagined having a spy cam in our rooms as kids, and this project lets you build one with a Raspberry Pi, a camera module for the Pi, a PIR (motion) sensor and PubNub for realtime notifications about prowlers in your room.

The PIR sensor measures the IR radiation emitted by objects. The sensor is able to measure changes in the IR signature around it(when an object moves) and hence detect motion. This message can be sent to any device in the world using PubNub. With PubNub, all you need to do is to **publish** on a channel to the PubNub network, which can be **subscribed** to by any other device any where else in the world.

##How to run this program

In case you want to jump to the exciting part and run the program, then just follow the below steps. 

Open Python 2 IDE

![image](../../images/python-ide.png)

Then, in Python Shell,  **File** > **New Window**

In the new window, copy and paste [spycam.py](../spycam/spycam.py), and save as `Motionsensor.py`

Run the script

On terminal:
`$ sudo python Motionsensor.py`

This sends a message to PubNub data stream when motion is detected.

### Monitoring PubNub Data Stream on Console

1. On web browser, go to [http://www.pubnub.com/console/](http://www.pubnub.com/console/)
2. Type `proximitysensor`(or the name of your channel in the Motionsensor.py) into the **Channel** field, `demo` into both **publish key** and **subscribe key** (unless you registered for a PubNub account, in which case you use your personal pub and sub keys)
3. Click **Subscribe**

![image](../../images/pubnub-console.png)

# Description of the project

## Using a Pyroelectric IR Motion Detector


![image](../../images/PIR/pir-fullview.jpg)



## Step 1 : The hardware

The hardware set up is the same as the motion sensor, with an additional camera module attached to the Raspberry Pi. 

NEED A PHOTO OF THE ENTIRE SETUP HERE.

### A

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

If you are using a mini breadborad, your circuit should look similar to this:

![image](../../images/PIR/fritzing-pir-sm.png)

If you are using 400-point breadboard as seen in the photo below, [see this diagram](../../images/PIR/fritzing-pir-400.png).

## Step 2 : The software


The motion sensor is designed to send a web based alarm, when it detects motion. To do this, the overall setup has to detect motion and then publish a message using PubNub.

### Breaking up the code

#### Line by line explanation of what the code does: