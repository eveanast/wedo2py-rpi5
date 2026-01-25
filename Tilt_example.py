#!/usr/bin/env python3

from wedo2python.app import WeDo2Python
import time
from time import sleep

# Initialize the program
device_wedo2 = WeDo2Python("04:EE:03:16:ED:1D") # replace with your MAC
device_wedo2.connect()

try:
    device_wedo2.tilt_sensor(device_wedo2.port('A'))

    # Continuously read and print the tilt direction
    while True:
        time.sleep(1)

        tilt = device_wedo2.read_tilt_value()
        tilt_any = device_wedo2.print_tilt_any(tilt)
        """
        if tilt_any is not None:
            print("Tilt Any")

        """
        if tilt is not None:
            if tilt == device_wedo2.TILT_HORIZONTAL:
                print("HORIZONTAL")
            elif tilt == device_wedo2.TILT_DOWN:
                print("DOWN")
                device_wedo2.motor_off(device_wedo2.port('B'))
            elif tilt == device_wedo2.TILT_RIGHT:
                print("RIGHT")
                device_wedo2.motor_that_way(device_wedo2.port('B'))
                device_wedo2.motor_on(device_wedo2.port('B'))
            elif tilt == device_wedo2.TILT_LEFT:
                print("LEFT")
                device_wedo2.motor_this_way(device_wedo2.port('B'))
                device_wedo2.motor_on(device_wedo2.port('B'))
            elif tilt == device_wedo2.TILT_UP:
                print("UP")
                device_wedo2.motor_on(device_wedo2.port('B'))
            else:
                print(f"UNKNOWN({tilt})")

except KeyboardInterrupt:
    print("Program interrupted by user.")

finally:
    device_wedo2.disconnect()