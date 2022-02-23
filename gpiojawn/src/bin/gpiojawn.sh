#!/bin/bash

set -e

GPIO=23

# trap ctrl-c and turn the light off
trap lights_out INT

function lights_out() {
	echo "0" >/sys/class/gpio/gpio${GPIO}/value
}

if [ "(cat /sys/class/gpio/gpio${GPIO}/direction)" != "out" ]
then
	echo out >/sys/class/gpio/gpio${GPIO}/direction
fi

while true; do
	echo "1" >/sys/class/gpio/gpio${GPIO}/value
	sleep 1
	echo "0" >/sys/class/gpio/gpio${GPIO}/value
	sleep 1
done
