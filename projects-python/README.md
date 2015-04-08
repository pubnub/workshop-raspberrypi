# Setting up PubNub Python Lib


Open LXTerminal

![image](../images/LXTerminal.png)

Install Python
`pi@raspberrypi ~$ sudo apt-get install python-dev`

Install pip
`pi@raspberrypi ~$ sudo apt-get install python-pip`

Then, install PubNub
`pi@raspberrypi ~$ sudo pip install pubnub`

---

## "Hello World" with PubNub

Learn how to use PubNub Python APIs by publishing simple messages.

- [Publishing messages using PubNub](helloworld/)

## "Hello World" of Hardware

Learn how to assemble circuit with wires and breadboard using a LED.

- The first project: [Blinking LED](led/)



## Pi Projects with Sensors

Now, let's connect some sensors to Raspberry Pi, and learn more about sending and receiving data to/from the sensors using PubNub APIs!

- Motion Sensor
  * [Motion Sensor](motion-sensor/) The basic code that detects motion and sends a notification to a browser or a mobile phone.
  * [Motion Sensor and Range Finder](motion-and-range) This program lets you notify a range finder when you detect motion.
  * [Spicam](Spicam/) This example switches on the camera to capture a picture when motion is detected.
- [Ultrasonic Rangefinder](range-finder/) Using HC-SR04 ultrasonic rangefinder to sense a nearby object's proximity range.
