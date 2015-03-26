# Motion Sensor with Raspberry Pi and PubNub
## Section 1: Building the Hardware

*The motion sensor detects changes in the IR signature around it and triggers a message/alarm using PubNub*

### What you needing

1. Raspberry Pi 2, set-up, with accessories (power, wifi, m+kb, monitor, or setup via SSH) (See ReadMe)
2. A PIR sensor
3. 8 jumper wires in 4 colors, with 2 of each color 
4. A browser or internet-capable smartphone 

### What you are building and how it works

The PIR sensor measures the IR radiation emitted by objects. The sensor is able to measure changes in the IR signature around it(when an object moves) and hence detect motion. This message can be sent to any device in the world using PubNub. With PubNub, all you need to do is to **publish** on a channel to the PubNub network, which can be **subscribed** to by any other device any where else in the world.


