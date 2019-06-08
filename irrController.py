#Water Irrigator with PubNub
#TO DO:
#1. Update to communicate with google sheets and google app script
#2. Scrape for weather data
#3. Add library to start program -10 minutes from first task

import sys
import Adafruit_DHT
from gpiozero import LED, Button
from time import sleep
import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNOperationType, PNStatusCategory

pump = LED(4)

flag = 1
pump.on()

class MySubscribeCallback(SubscribeCallback) :
    def status(self, pubnub, status) :
        pass
        if status.operation == PNOperationType.PNSubscribeOperation
            or status.operation == PNOperationType.PNUnsubscribeOperation :
            if status.category == PNStatusCategory.PNConnectedCategory :
                pass
            elif status.category == PNStatusCateory.PNReconnectedCategory :
                pass
            elif status.category == PNStatusCategory.PNDisconnectedCategory :
                pass
            elif status.category == PNStatusCategory.PNAccessDeniedCategory :
                pass
            else :
                pass
        elif status.operation == PNOperationType.PNSubscribeOperation :
            if status.is_error() :
                pass
            else : 
                pass
        else :
            pass

    def presence(self, pubnub, presence) :
        pass

    def message(self, pubnub, message) :
        if message.message == 'ON' :
            global flag
            flag = 1
        elif message.message == 'OFF' :
            global flag 
            flag = 0
        else:
            message.message == 'WATER' :
            pump.off()
            sleep(5)
            pump.on()
            pubnub.add_listener(MySubscribeCallback())
            pubnub.subscribe().channels('ch1').execute()

    def publish_callback(result, status) :
        pass