## Setting up PubNub Node.js Lib


Open LXTerminal:

![image](../images/LXTerminal.png)

Make sure your Pi is up-to-date:

`pi@raspberrypi ~$ sudo apt-get update`

then,

`pi@raspberrypi ~$ sudo apt-get upgrade`

Download Node:

`pi@raspberrypi ~$ wget http://node-arm.herokuapp.com/node_latest_armhf.deb`

once downloaded, install Node:

`pi@raspberrypi ~$ sudo dpkg -i node_latest_armhf.deb`

Check if node is successfully installed:

`pi@raspberrypi ~$ node -v`

You should see the Node version number, if it is installed correctly.

Then, install PubNub:

`pi@raspberrypi ~$ npm install pubnub`

### Hello World

- [Publishing messages using PubNub](helloworld/)

---

## Projects

Now, let's connect some sensors to Raspberry Pi, and learn more about sending and receiving data to/from the sensors using PubNub APIs!

### Using Motion Sensor

Using a IR motion sensor to detect when some object is near the sensor.

- [Sending realtime data using a motion sensor](motion.md)

### Using Ultrasonic Rangefinder Sensor

Measure distances and trigger an alarm using PubNub Pub/Sub Messaging and Raspberry Pi


- [Project page: Ultrasonic Rangefinder + Pi + PubNub](../examples/ultrasonic_rangefinder_+_pi__+_pubnub.md)

etc.