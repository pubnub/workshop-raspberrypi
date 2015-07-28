## Hello World, PubNub

import sys
from pubnub import Pubnub

# Initiate Pubnub State
pubnub = Pubnub(publish_key='demo', subscribe_key='demo')

channel = 'hello-pi'

username = 'Your name'
message = 'Hello World from Pi!'

data = {
    'username': username,
    'message': message
}

# Asynchronous usage
def callback(m):
    print(m)

pubnub.publish(channel, data, callback=callback, error=callback)
