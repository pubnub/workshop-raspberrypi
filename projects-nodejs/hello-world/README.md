## Hello World with PubNub


Open Python 2 IDE (although it is not the ideal IED for JavaScript. Let's use it for now!)

![image](../../images/python-ide.png)

Then, in Python Shell,  **File** > **New Window**

In the new window, copy and paste [hello.js](https://github.com/pubnub/workshop-raspberrypi/blob/master/examples-nodejs/hello.js), and save as `hello.js`

Run the script

On terminal:

`$ sudo node hello.js`

This sends a Hello World message to PubNub data stream.

### Monitoring PubNub Data Stream on Console

1. On web browser, go to [http://www.pubnub.com/console/](http://www.pubnub.com/console/)
2. Type `hello` into the **Channel** field, `demo` into both **publish key** and **subscribe key**
3. Click **Subscribe**

![image](../../images/pubnub-console.png)

