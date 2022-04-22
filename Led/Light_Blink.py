#!/usr/bin/python2.7
import RPi.GPIO as GPIO # Import GPIO lib
import time

GPIO.setmode(GPIO.BOARD) # Use pin number instead of BCM number
GPIO.setup(8, GPIO.OUT) # Setup GPIO pin 3 To OUT

def blink(numTimes, speed):
	for i in range(0, numTimes): # For x times
		GPIO.output(8, True) # Light up the led
		time.sleep(speed) # sleep y seconds
		GPIO.output(8, False) # Light off the led
		time.sleep(speed) # sleep y seconds
	GPIO.cleanup() # Clean up GPIO

blink(5, 1)
