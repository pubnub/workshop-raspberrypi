import os
import time
import sys
from pubnub import Pubnub
import Adafruit_DHT as dht

pubnub = Pubnub(publish_key='pub-c-156a6d5f-22bd-4a13-848d-b5b4d4b36695', subscribe_key='sub-c-f762fb78-2724-11e4-a4df-02ee2ddab7fe')
channel = 'tempeon'

def callback(message):
    print(message)

#published in this fashion to comply with Eon
while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h)
    pubnub.publish('tempeon', {
        'columns': [
            ['x', time.time()],
            ['temperature_celcius', t]
            ]

        })
    pubnub.publish('humeon', {
        'columns': [
            ['humidity', h]
            ]

        })