# IoT-fying Your LED: Remote-controlling LED from Web Interface

Let's create a super simple remote-controllable LED with PubNub APIs.

## Wiring an LED & Assemble the Circuit

You are using the same circuit you have created at [the previous exercise with LED](../led).

## Writing Code

There are two independently operated programs:

1. Web/Mobile interface to remotely turn the LED on. Written in HTML with JavaScript. [disco.html](https://github.com/pubnub/workshop-raspberrypi/blob/master/web/disco.html)
2. Python code to blink the LED physically. [remote-led.py](remote-led.py)

The [remote-led.py](remote-led.py) uses the same code as the previous example [led.py](../led/led.py), however, it contans PubNub `subscribe` API to take signals from the web interface.

### Publishing Data from Web

You are creating a simple web UI that contains a button for this exercise.

Using JavaScript, add a click event handler to the button, and when the event is fired, send the data to PubNub, so the python code to talk to Raspberry Pi gets the signal.

```javascript

// Init PubNub

var p = PUBNUB.init({
  subscribe_key: 'demo',
  publish_key:   'demo'
});
	
// Sending data
	
function disco() {
  p.publish({
    channel : 'disco', // This is the channel name you are subscribing in remote-led.py
    message : {led: 1}
  });
}
    
// Click event
document.querySelector('button').addEventListener('click', disco);

```

### Subscribing Data Using PubNub

Whenever a button is clicked by a user, browser sends `{led: 1}` to PubNub server, then a python code to talk to Pi receive the data and triggers the LED.


```python

# Init PubNub
pubnub = Pubnub(publish_key='demo', subscribe_key='demo')

pubnub.subscribe(channels='disco', callback=_callback, error=_error)
```

At the success callback (`_callback`), the function to blink LED is called. 

It is that easy.

## Disco!

If you use `demo` for both publish and subscribe keys, with the same channel name used in this example, [try the demo here](http://pubnub.github.io/workshop-raspberrypi/web/disco.html).



