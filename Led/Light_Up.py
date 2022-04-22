#!/usr/bin/python2.7
import RPi.GPIO as GPIO # Import GPIO lib
import time

GPIO.setmode(GPIO.BOARD) # Use pin number instead of BCM number
GPIO.setup(8, GPIO.OUT) # Setup GPIO pin 8 To OUT

GPIO.output(8, True) # Turn on GPIO pin 8
time.sleep(5) # Wait 5 seconds
GPIO.cleanup() # Clean GPIO
