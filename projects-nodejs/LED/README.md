# Using LED: Hello World of Hardware

## Wiring an LED

To get started with wires and breadboard, let's make an LED light up by simply wiring to the 3.3V.

### What You Need

- Raspberry Pi 2 (Set up properly. See [Setting up Raspberry Pi](../README.md))
- 1 LED light (Somewhere around 1.9V - 3.2V)
- 1 Resistor 200Ω ~ 270Ω
- Breadboard
- 2 M-to-F jumper wires, 2 colors

(need an image)

### Assemble the Circuit

(need a better photo here!)
![image](../../images/LED/led-simple.jpg)



## Controlling the LED with Node.js using Johnny-Five

When you program the LED, re-connect the 3.3V wire into a one of GPIO pin. In this example,
I am using the GPIO-4 (Pin 7).


(need a photo)


### Installing Johnny-Five

Intro Johnny-Five

blah

### Installing Raspi-io

Intro
https://github.com/bryan-m-hughes/raspi-io

blah

### Strobe.js - Lighting up LED

```
var raspi = require('raspi-io');
var five = require('johnny-five');
var board = new five.Board({
  io: new raspi()
});

board.on('ready', function() {

  // Create an Led on pin 7 (GPIO4) on P1 and strobe it on/off
  var led = new five.Led('P1-7'));
  
  led.strobe();

});
```