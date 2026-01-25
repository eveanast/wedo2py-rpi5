#!/usr/bin/env python3

from wedo2python.app import WeDo2Python
import time
from time import sleep
    
try:
    device_wedo2 = WeDo2Python("04:EE:03:16:ED:1D") # replace with your MAC
    device_wedo2.connect()
    device_wedo2.distance_sensor(device_wedo2.port('A'))
        
    while True:
        time.sleep(0.1)
        distance = device_wedo2.read_distance_value()
        if distance is not None:
            if distance < 20:
                print(f"OBSTACLE!\n")
                device_wedo2.set_color("red")
                device_wedo2.sound()
                print("Low Speed and Back")
                device_wedo2.motor_this_way(device_wedo2.port('B'))
                device_wedo2.motor_on(device_wedo2.port('B'))
                device_wedo2.set_motor_power(device_wedo2.port('B'), 20)
                sleep(1)
                print("CRASH! MOTOR OFF!")
                device_wedo2.motor_off(device_wedo2.port('B'))
            else:
                print("FREE ROAD!\n")
                device_wedo2.set_color("green")
                device_wedo2.sound_off()
                device_wedo2.set_motor_power(device_wedo2.port('B'), 40)
                device_wedo2.motor_on(device_wedo2.port('B'))
                device_wedo2.motor_that_way(device_wedo2.port('B'))
                sleep(1)
        print(f"Distance {distance} cm\n")
                    
                
except KeyboardInterrupt:
    print("Program interrupted by user ...")
finally:
    device_wedo2.disconnect()