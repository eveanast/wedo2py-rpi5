#!/usr/bin/env python3
from wedo2python.app import WeDo2Python
import time
from time import sleep

try:
    device_wedo2 = WeDo2Python("04:EE:03:16:ED:1D") # replace with your MAC000000000
    device_wedo2.connect()

    while True:
        time.sleep(0.1)
        
        print("RIGHT AND 50% POWER\n")
        device_wedo2.motor_this_way(device_wedo2.port('B'))
        device_wedo2.set_motor_power(device_wedo2.port('B'), 50)
        sleep(1)
            
        print("MOTOR ON\n")
        device_wedo2.motor_on(device_wedo2.port('B'))
        sleep(1)
            
        device_wedo2.motor_reverse(device_wedo2.port('B'))
        print("MOTOR REVERSED")
        sleep(1)
            
        device_wedo2.motor_on(device_wedo2.port('B'))
        print("MOTOR ON")
        sleep(1)
            
        print("LEFT AND 30% POWER\n")
        device_wedo2.motor_that_way(device_wedo2.port('B'))
        device_wedo2.set_motor_power(device_wedo2.port('B'), 30)
        sleep(1)
            
        print("MOTOR ON\n")
        device_wedo2.motor_on(device_wedo2.port('B'))
        sleep(1)
            
        print("MOTOR OFF\n")
        device_wedo2.motor_off(device_wedo2.port('B'))
        sleep(1)
            
except KeyboardInterrupt:
    print("Program interrupted by user ...")
finally:
    device_wedo2.disconnect()

