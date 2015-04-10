# proximity sensor

This project builds over the range finder example by modifying it. The rangefinder calculates the distance between itself and an object in front of it. The proximity sensor on the other hand has only two outputs - closer or further away with respect to a set distance. Proximity sensors are commonly used on smartphones to detect (and skip) accidental touchscreen taps when held to the ear during a call. Using this sensor, you can detect if an object is next to you or not without having to touch it. 

With this proximity sensor, Raspberry Pi and PubNub, you can build amazing real life applications. The sensor measures the distance between itself and an object. Say this is set up on the entrance of a coffee store, to know when customers are close to the store. When a customer is close to the store, the device smartly sends out a notification to him saying there is a sale. The moment he steps out of the range, the message goes away. This kind of smart marketing can be used in big supermarkets and malls to attract customers with good deals when they are close by. You can check it out here. [Lego man Coffee sale](http://codyjb.github.io/pubnub-proximity/).
 
## How the code works : 


For the most part, this program is the same as the [rangefinder.py](../range-finder/rangefinder.py). Here we'll explain the parts that are different.

The following code takes the distance measured by the range finder and puts it in a loop. You can set a minimum distance (we have it at 10cm), below which, it sends out a message saying proximity detected to PubNub. You can use this to trigger more actions in the real world instead of just sending a message. 


    
  ```python   
    if distance <= 10:
        print("Distance:",distance,"cm")
        print("Proximity Detected")
        
        message = {'distance': distance, 'Proximity': "True"}
        print pubnub.publish(channel, message)
        time.sleep(1)
        
   ```  

If the object is further than the minimum distance set, you still publish it to PubNub, and do any action you want based on it. 

```python 

    # If nothing is detected, the sensor continuously sends and listens for a signal, and 	publishes the distance to your PubNub channel.
    
    else:
        print("Time", pulse_duration)
        print("Distance", distance, "cm")
        print("Too Far")
        
        message = {'distance': distance, 'Proximity' : 'False'}
        print pubnub.publish(channel, message)

		time.sleep(1)
```



