# Communication between 2 Pis

As a next step, what if you could do more when motion is detected, than just send an alarm to a user. One possibility is to send a message to a range finder (also connected to a Pi - [Range Finder Pi](../motion-and-range/RF+Motion Detector.py)). The other is to click a picture using the Pi camera module when motion is detected - [Spicam](../Spicam/SpiCamMotion.py). Here, the former project has been described in detail with the code.

## Step 1 : The idea behind it 

 - So far we have a device publishing data to the internet. But in an ideal case, you want it to be able to subscribe/receive data as well, and to consume  that data. 
 - So say have two Raspberry Pis(you can collaborate with the person next to you and become friends); one which powers the [motion sensor](../motion-sensor/Motionsensor.py) and one for the [range finder](../range-finder/rangefinder.py).
 - Your motion sensor code detects motion and publishes a message to "motionrange" channel to notify the range finder to capture the distance between the moving object and itself.
 - This way, the range finder is listening to data from one device, and acting upon the received data. 
 - In a real world scenario, think of how you can have several devices all talking to each other, and making smart decisions based on the information. 
 - This is where PubNub comes in, providing you with the ability to send messages instaneously. With PubNub, you don't have to limit yourself to just the Raspberry Pi; we support 70+ SDKs and platforms and easy to use APIs.

## Step 2 : The code

 - This code just builds on the previous basic example.
 - The publish key, subscribe key and the channel for both the Pis have to be the same so they can bidirectionally talk to each other. 
 - This is the only change to make. (line 17 and 18 in the [Motionsensor_rangefinder.py](../motion-and-range/Motionsensor_rangefinder.py)) 

### Modifications to the Motion sensor code




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


### Modifications to the Rangefinder sensor code

 - The rangefinder code has to have the same keys and channel to receive the messages sent over PubNub.
 
 ```python
publish_key = 'demo'
subscribe_key = 'demo'
secret_key = 'demo'
cipher_key = ''
ssl_on = False
channel = 'Rangefinder'
```

- The other is the subscribe function (**TO BE FILLED BY ERIC**)