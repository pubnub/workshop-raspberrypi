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



## Step 2 : The software


The motion sensor is designed to send a web based alarm, when it detects motion. To do this, the overall setup has to detect motion and then publish a message using PubNub.

### Breaking up the code

#### Line by line explanation of what the code does: