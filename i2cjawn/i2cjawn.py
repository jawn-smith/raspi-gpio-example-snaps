#  Raspberry Pi Leader for Arduino Follower
#  Connects to Arduino via I2C and periodically blinks an LED
#  Author: William 'jawn-smith' Wilson

import smbus
import time

addr = 0x8 # bus address
channel = 1

def main():
    bus = smbus.SMBus(channel)
    while True:
        try:
            bus.write_byte(addr, 0x0) # switch it off
            time.sleep(1)
            bus.write_byte(addr, 0x1) # switch it on
            time.sleep(1)
        except KeyboardInterrupt:
            bus.write_byte(addr, 0x0) # switch it off
            break

if __name__ == "__main__":
    main()
