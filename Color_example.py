#!/usr/bin/env python3

from wedo2python.app import WeDo2Python
import time
from time import sleep

try:
    device_wedo2 = WeDo2Python("04:EE:03:16:ED:1D") # replace with your MAC
    device_wedo2.connect()
        
    while True:
        time.sleep(0.1)

        device_wedo2.colors()
        sleep(2)
        device_wedo2.set_color('off')
            
except KeyboardInterrupt:
    print("Program interrupted by user ...")
finally:
    device_wedo2.disconnect()