# Setting up PubNub Python Lib


Open LXTerminal

![image](../images/LXTerminal.png)

Install Python
`pi@raspberrypi ~$ sudo apt-get install python-dev`

Install pip
`pi@raspberrypi ~$ sudo apt-get install python-pip`

Then, install PubNub
`pi@raspberrypi ~$ sudo pip install pubnub`

### Using Python IDE


Open Python 2 IDE

![image](../images/python-ide.png)

### Running a Script


On terminal:
`$ sudo python your-script.py`

OK, now you are ready to code on Pi.
Let's learn how to use PubNub next!

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
  * [Motion Sensor](motion-sensor/) This lets you detect motion and send a notification to a browser or a mobile phone.
  * [Motion Sensor with an LED indicator](motion-led/) Adding an LED to the motion sensor project to include a visual indicator when motion is detected.
  * [Motion Sensor and Range Finder](motion-and-range) This program lets you notify a range finder when you detect motion, to detect the distance between the moving object and yourself.
- [Ultrasonic Rangefinder](range-finder/) Using HC-SR04 ultrasonic rangefinder to sense a nearby object's proximity range.
- Temperature and Humidity Sensor
  * [Data Visualization using DHT22 sensor](dht22) 
