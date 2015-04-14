# Hello World with PubNub Python APIs

Open Python 2 IDE

![image](../../images/python-ide.png)

Then, in Python Shell,  **File** > **New Window**

In the new window, copy and paste [hello.py](hello.py), and save as `hello.py`

Run the script

On terminal:
`$ sudo python hello.py`

This sends a Hello World message to PubNub data stream.

## The Quick Code Walk-though 

Now we’ll quickly walk through using the PubNub API for Python SDK. Just follow the steps…

Include the Python SDK in your code.

```python
from Pubnub import Pubnub
```

`init()`: Get a new Pubnub instance with publish and subscribe key


```python
pubnub = Pubnub(publish_key="demo", subscribe_key="demo")
```


`publish()`: Publish a message!


```python
def callback(message):
     print(message)
 pubnub.publish('hello_world', 'Hello PubNub', callback=callback, error=callback)
```
 
Also, you can `subscribe1 all messages that have been published, although this block of code is not included in the `hello.py`.

Try creating a new file, and subscribe all other messages coming to the channel, **hello_world**.

```python
def _callback(message, channel):
   print(message)
 
 def _error(message):
     print(message)
 
 pubnub.subscribe(channels='hello_world', callback=_callback, error=_error)
```
 
# Initialize with Publish & Subscribe Keys
 
 pubnub = Pubnub(publish_key="demo", subscribe_key="demo")
```

## Monitoring PubNub Data Stream on Console

1. On web browser, go to [http://www.pubnub.com/console/](http://www.pubnub.com/console/)
2. Type `hello_world` into the **Channel** field, `demo` into both **publish key** and **subscribe key**
3. Click **Subscribe**

![image](../../images/pubnub-console.png)