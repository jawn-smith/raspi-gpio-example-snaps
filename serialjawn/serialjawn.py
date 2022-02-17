#  Raspberry Pi UART communication
#  Takes an argument to either send or receive data over UART
#  Author: William 'jawn-smith' Wilson

import serial
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--mode", type=str, choices=["listen", "send"], help="Mode to use, either \"listen\" or \"send\"")
parser.add_argument("--message", type=str, help="The message to send. Can only be used with \"send\" mode")

def listen():
    port = serial.Serial("/dev/ttyAMA0", 115200)
    while True:
        data = port.read()
        time.sleep(0.05)
        data_remaining = port.inWaiting()
        data += port.read(data_remaining)
        print(data.decode())

def send(message):
    port = serial.Serial("/dev/ttyAMA0", 115200)
    encoded_message = str.encode(message)
    port.write(encoded_message)
    time.sleep(0.5)

def main():
    args = parser.parse_args()
    if args.mode == "listen":
        if args.message != None:
            print("Cannot specify a message in listen mode!")
            return 1
        else:
            listen()
    elif args.mode == "send":
        if args.message == "":
            print("Send mode must have a message specified!")
            return 1
        else:
            send(args.message)

if __name__ == "__main__":
    main()
