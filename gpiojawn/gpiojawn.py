#  Blink an LED with the RPi.GPIO library
#  Author: William 'jawn-smith' Wilson

import time
import RPi.GPIO as gpio

LED = 18

gpio.setmode(gpio.BCM)
gpio.setup(LED, gpio.OUT)

def main():
    try:
        while True:
            # Turn the GPIO pin on
            gpio.output(LED, gpio.HIGH)
            time.sleep(1)
    
            # Turn the GPIO pin off
            gpio.output(LED, gpio.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        gpio.output(LED, gpio.LOW)


if __name__ == "__main__":
    main()
