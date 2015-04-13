# Hello World with PubNub Python APIs

## Running the program

Open Python 2 IDE

![image](../../images/python-ide.png)

Then, in Python Shell,  **File** > **New Window**

In the new window, copy and paste [motion-led.py](https://github.com/pubnub/workshop-raspberrypi/blob/master/projects-python/motion-led/motion-led.py), and save as `motion-led.py`

Run the script

On terminal:
`$ sudo python motion-led.py`

This will run the program to detect motion and switch on an LED when motion is detected.

### Monitoring PubNub Data Stream on Console

1. On web browser, go to [http://www.pubnub.com/console/](http://www.pubnub.com/console/)
2. Type `motionsensor-led` into the **Channel** field, `demo` into both **publish key** and **subscribe key**
3. Click **Subscribe**

![image](../../images/pubnub-console.png)

## What is happening behind the scenes

This project builds on the existing Motion sensor project, by adding the LED element. When motion is detected, not only a message is sent to PubNub, but also a message to the LED to light up. 

### The code 


We want to switch on the LED when motion is detected, but switch off when there is nothing moving. For this we need to monitor the pin receiving the output from the sensor, and see if its **RISING** or **FALLING**. GPIO.BOTH lets you detect edges in either changing direction(rising or falling). 

`GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=MOTION)`

Once in the callback function, we actually check if it RISING in which case we switch on the LED. And if its FALLING, we switch it off. 

```python
def MOTION(PIR_PIN):
    if PIR_PIN:
        print 'Motion Detected!'
        print 'Light on'
        GPIO.output(LED_PIN, True)
        pubnub.publish(channel, message, callback=callback, error=callback)
    else:
        print 'No Motion!'
        GPIO.output(LED_PIN, False)
```