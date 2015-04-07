# Pi-Light LED: A "Hello World" of Hardware

## Wiring an LED

To get started with wires and breadboard, let's make an LED light up by simply wiring to the 3.3V.

### What You Need

- Raspberry Pi 2 (Set up properly. See [Setting up Raspberry Pi](../README.md))
- 1 LED light (Somewhere around 1.9V - 3.2V)
- 1 Resistor 200Ω ~ 270Ω
- Breadboard
- 2 M-to-F jumper wires, 2 colors

![image](../../images/LED tutorial/led_01.jpg)

### Assemble the Circuit

  1. First, designate one of the jumper wires as power, and plug it into the Pi's 3.3v pin. Plug the other into one       of the Pi's GND pins. 
  
    *In the abstract, you could use one of the Pi's 5v pins to power an LED. However, the Pi's GPIO pins, which we  will use later to actually control the LED, output to 3.3v- so using the basic 3.3v pin in this step will allow you to accurately calibrate your circuit for later use.*  

    The pins aren't labeled on the Pi directly, so this diagram will prove useful for any Pi + Hardware experiment       you work on:
    ![image](https://camo.githubusercontent.com/ca1ff23008fb7000828355b50768ae7ce2b83936/687474703a2f2f7777772e72617370626572727970692d7370792e636f2e756b2f77702d636f6e74656e742f75706c6f6164732f323031322f30362f5261737062657272792d50692d4750494f2d4c61796f75742d4d6f64656c2d422d506c75732d726f74617465642d32373030783930302d31303234783334312e706e67)

    Here's how it looks on a Pi:
    [need image]

2. Connect your GND wire to the first row of the breadboard. On a nearby row, plug in your 3.3v power wire.
    ![image](../../images/LED tutorial/led_02)
    We'll be building a circuit from the 3.3v pin, through the breadboard, and back to the GND pin. 

3. Connect the long pin of your LED to the same row as your power wire. Plug the short pin into the last row on a blank rail, preferably that between your power and GND rows.
    ![image](../../images/LED_tutorial/led_04) 

4. With your resistor, connect one pin to the LED and the other to the GND wire's row, completing the circuit.
    ![image](../../images/LED_tutorial/led_05)

When you simply power on your Pi, your light will turn on, like so:
![image](../../images/LED_tutorial/led_06)



## Controlling the LED with Python

####A Word About pins
Now that we've built a complete circuit using the Pi's GND and 3.3v PWR pins, it's time to make modifications and build some modest hardware control.

To make the LED programmable, we will use one of the Pi's many GPIO pins. Through code, we can designate these pins as either digital inputs or outputs. When a pin turns  from LOW (0) to HIGH (1), it supplies a 3.3v signal. This functionality is used to trigger, or respond to, sensors and actuators. 

The Raspberry Pi's pins, and those for GPIO in particular, have two designations: Pin number (the numbers inside the circles on the diagram), and a BCM (Broadcom SOC Channel) designation (the numbers in the boxes alongside the diagram). 

When using pins in code, you have to pick a designation. Throughout the code in our workshop, we will refer to pins by their **BCM designation.** 

Here's the diagram again:
![image](https://camo.githubusercontent.com/ca1ff23008fb7000828355b50768ae7ce2b83936/687474703a2f2f7777772e72617370626572727970692d7370792e636f2e756b2f77702d636f6e74656e742f75706c6f6164732f323031322f30362f5261737062657272792d50692d4750494f2d4c61796f75742d4d6f64656c2d422d506c75732d726f74617465642d32373030783930302d31303234783334312e706e67)

###Building the Circuit

In this case, we simply want to write code that, when executed, will blink the LED 7 times.

To change the circuit to be controllable, we simply unplug the power wire from the Pi's 3.3v pin and attach it to one of the GPIO pins, as below:
[Need image]

Referencing the diagram above, you'll see that this is GPIO-4, or Pin 7. 

###Writing the Code

[Full Code Here]()

