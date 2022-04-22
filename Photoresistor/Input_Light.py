#!/usr/bin/python2.7
import RPi.GPIO as GPIO
import time

PHOTO_RESISTOR_PIN = 7

def main():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PHOTO_RESISTOR_PIN, GPIO.IN)
	
	while True:
		print GPIO.input(PHOTO_RESISTOR_PIN)

if __name__ == "__main__":
	main()
