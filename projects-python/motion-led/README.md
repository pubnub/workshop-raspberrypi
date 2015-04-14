<<<<<<< HEAD
# Motion sensor with a visual indicator

Here we will modify the circuit from the [motion sensor](../motion-sensor/motionsensor.py) to add an LED that will only light up when motion is detected. 

## Hardware

ADD A PICTURE HERE OF THE HW WITH THE TINY KIT

Wire up the circuit in the following manner. The LED will blink for 30 seconds or so when the Raspberry Pi is powering on. Wait for it to settle, and run the program as explained below. You will notice how everytime motion is detected, the LED turns on and when there is nothing in front of the motion sensor, it turns off. At the same time motion is detected, a message is published to PubNub as well. 

### What you need 

## Running the program

Open Python 2 IDE.
=======
# Adding an LED to the Motion Detector

This project is an add-on for the [PIR Motion detector project](README.md)).
The LED is used as a visual indicator of the motion sensor: when a motion is detected, the LED turns on.

## Wiring up PIR Sensor and LED

### What You Need:

- Raspberry Pi 2 (Set up properly. See [Setting up Raspberry Pi](../README.md))
- [PIR sensor](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview)
- LED (1.9 - 3.2V)
- Resistor (~200Ω)
- Breadboard
- 7x M-to-F jumper wires, 3 colors with 2 of each, and 1 extra color


### Assemble the Circuit

Addition to the circuit you have wired a PIR sensor, you connect a LED output to another GPIO (We are using GPIO-17 / Pin 11 for the diagram and the code) with an appropriate resistor. We are using 200Ω to be safe. (also, we have a lot of them for everybody!)

Circuit on Mini breadboard:
>>>>>>> origin/master

 ![image](../../images/PIR-LED/fritzing-pir-led-mini.png)
 
[If you are using a 400-pin, the circuit should look something like this.](../../images/PIR-LED/fritzing-pir-led-400.png)


## Running the program

1. Open Python 2 IDE

2. Then, in Python Shell,  **File** > **New Window**

3. In the new window, copy and paste [motion-led.py](https://github.com/pubnub/workshop-raspberrypi/blob/master/projects-python/motion-led/motion-led.py), and save as `motion-led.py`

4. Run the script

On terminal:
`$ sudo python motion-led.py`

This will run the program to detect motion and switch on an LED when motion is detected.



## What is happening behind the scenes

This project builds on the existing Motion sensor project, by adding the LED element. When motion is detected, not only a message is sent to PubNub, but also a message to the LED to light up. 

### The code 


We want to switch on the LED when motion is detected, but switch off when there is nothing moving. For this we need to monitor the pin receiving the output from the sensor, and see if its **RISING**. GPIO.RISING lets you detect this change. The hardware circuit associated with the Pi and the LED will ensure that it switches on only motion is detected, but not otherwise.

`GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)`

Once in the callback function, we actually check if it RISING in which case we switch on the LED. And if its FALLING, we switch it off. 

```python
def MOTION(PIR_PIN):
    if PIR_PIN:
        print 'Motion Detected!'
        print 'Light on'
        pubnub.publish(channel, message, callback=callback, error=callback)
```