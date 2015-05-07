#Monitoring Data, and Remote-Controlling the Pi from Web Interface

When you are programming your Pi and sending the data to PubNub network, you probably want to have some visual display to read the data, or dashboard interface that lets you control your Pi remotly.

The examples here uses PubNub JavaScript APIs to make this happen on web browsers.

First, include the latest pubnub.js in your HTML:

```
<script src="http://cdn.pubnub.com/pubnub-3.7.1.min.js"></script>
```

## Monitoring data with Subscribe API

In this repo, you find examples of web interface to display data from
the excersises:

- [Hello World](../projects-python/helloworld) ([Web interface](http://pubnub.github.io/workshop-raspberrypi/web/hello.html))
- [Motion detctor](../projects-python/motion-sensor) ([Web interface](http://pubnub.github.io/workshop-raspberrypi/web/motion.html))
- [Range finder](../projects-python/range-finder) ([Web interface](http://pubnub.github.io/workshop-raspberrypi/web/motion.html))

They all have different user interfaces, however, the way to grab the data from PubNub network is the same.

First, initialize PubNub stream:

```javascript
var channel = 'motionsensor';

var p = PUBNUB.init({
  subscribe_key: 'your-sub-key',
  publish_key:   'your-pub-key'
});
```

To stream the data that you published from a sensor (or just an object with strings that you published from the *Hello World* example), you must use the same channel name for both publishing and subscribing.

*Note: You suppose to use your own sub/pub keys, however you may have used 'demo' keys at the workshop. No matter what you used, use the same keys when you are subscribing the data!*

When the connection is succesful, the success `callback` is called. You can display or visualize, or whatever you would like to do with the data, upon the callback call.

For an easy example, let's just display the data you send from the motion sensor, in DOM as text.

```javascript
p.subscribe({
  channe: channel,
  error: function(e) {
    console.log(e);
  },
  callback: function(m) { 
    console.log(m);
    // Display in DOM
    document.getElementById('output').textContent = m.motion;
  }
});
```

In this case, your HTML should contain the corresponding DOM tree:

```
<div id="output"></div>
```


## Remote-Controlling with Publish API

The [disco.html](disco.html) ([Web Interface](http://pubnub.github.io/workshop-raspberrypi/web/disco.html)) is an example to blink a LED remotely.
Unlike the previous examples, this web interface does not display any data coming from sensors, instead it sends on/off message to PubNub network. (Then, [remote-led.py](https://github.com/pubnub/workshop-raspberrypi/tree/master/projects-python/remote-led) that communicate with your Pi programmatically blink the LED as new data is received.)

There are more sophisticated ways to send the state of the LED, but for this excersize, let's just simply send a trigger each time a user press a button.

Initialize PubNub:

```javascript
var channel = 'disco';

var p = PUBNUB.init({
  subscribe_key: 'your-sub-key',
  publish_key:   'your-pub-key'
});
```

Once initialized, you can just publish the trigger (*"Button is pressed!"*):

```javascript
document.querySelector('button').addEventListener('click', function() {
  p.publish({
    channel : channel, 
    message : {led: 1} // trigger
  });
}, false);

```

Your HTML has a button UI:
```
<button>Disco on!</button>
```

