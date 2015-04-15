# Communication between 2 Raspberry Pis

As a next step, what if you could do more when motion is detected, than just send an alarm to a user. One possibility is to send a message to a range finder (also connected to a Pi - [Range Finder Pi](../motion-and-range/RF+Motion Detector.py)). The other is to click a picture using the Pi camera module when motion is detected - [Spicam](../Spicam/SpiCamMotion.py). Here, the former project has been described in detail with the code.

## Step 1 : The idea behind it 

 - So far we have a device publishing data to the internet. But in an ideal case, you want it to be able to subscribe/receive data as well, and to consume  that data. 
 - So say have two Raspberry Pis (you can collaborate with the person next to you and become friends); one which powers the [motion sensor](../motion-sensor/Motionsensor.py) and one for the [range finder](../range-finder/rangefinder.py).
 - Your motion sensor code detects motion and publishes a message to "motionrange" channel to notify the range finder to capture the distance between the moving object and itself.
 - This way, the range finder is listening to data from one device, and acting upon the received data. 
 - In a real world scenario, think of how you can have several devices all talking to each other, and making smart decisions based on the information. 
 - This is where PubNub comes in, providing you with the ability to send messages instaneously. With PubNub, you don't have to limit yourself to just the Raspberry Pi; we support 70+ SDKs and platforms and easy to use APIs.

## Step 2 : The code
 

### Modifications to the *Motion sensor* code

 - This code just builds on the previous basic example.
 - **The publish key, subscribe key and the channel for both the Pis have to be the same so they can bidirectionally talk to each other.**
 - This is the only change to make. (line 17 and 18 in the [motion.py](../motion-and-range/motion.py))


**Setting up the keys for the combined project**
You have to set up the following keys with your keys or simply use 'demo'. Also, set the channel name. 

```python
publish_key = 'demo'
subscribe_key = 'demo'
secret_key = 'demo'
cipher_key = ''
ssl_on = False
channel = 'motionsensor'
```


### Modifications to the *Rangefinder sensor* code

When the motion sensor detects motion, the rangefinder will fire, sending an alert when an object gets too close.

Whereas in the above code [(Simple Range Finder)](../range-finder/rangefinder.py) we run the rangefinding code automatically and only *published* to a PubNub channel, we now want to detect range **only** after receiving a flagged message from another device. 


###1. Setting up subscription###

Leave the library import code and the setup of pins as it was. 
In the PubNub setup code block, you'll need the subscribe key of the device you want to 'listen' to.

From the *dashboard*, pick a motion detector's data stream. Copy the device's *Subscribe Key,* and paste it in your code:

```python
publish_key = len(sys.argv) > 1 and sys.argv[1] or 'demo'
subscribe_key = len(sys.argv) > 2 and sys.argv[2] or 'PASTE MOTION DETECTOR SUBKEY HERE'
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




