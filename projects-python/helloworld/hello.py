## Hello World, PubNub

import sys
from pubnub import Pubnub

# Initiate Pubnub State - Get your own keys at admin.pubnub.com
pubnub = Pubnub(publish_key='pub-c-156a6d5f-22bd-4a13-848d-b5b4d4b36695', subscribe_key='sub-c-f762fb78-2724-11e4-a4df-02ee2ddab7fe')

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
