#!/usr/bin/python2.7
import RPi.GPIO as GPIO
import time

# GPIO CONSTANTS
BUZZER = 7
LED = 8

# GPIO PIN SETUP
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER, GPIO.OUT) # BUZZER
GPIO.setup(LED, GPIO.OUT) # LED

# NOTE FREQUENCY CONSTANTS
RE = 288
MI = 324
FA_DIEZE = 369
SOL = 384
LA = 432
SI = 493 

# HIGHER OCTAVE NOTE FREQUENCY CONSTANTS
DO_HIGH = 523
RE_HIGH = 587


def silent(s_time, pwm):
	GPIO.output(LED, False)
	pwm.stop()
	time.sleep(s_time)

def note_loop(iteration, note, time_silent, note_duration):
	tmp = 0

	while tmp < iteration:
		timeout = time.time() + note_duration 
		pwm = GPIO.PWM(BUZZER, note)

		GPIO.output(LED, True)
		pwm.start(1)
		while True:
			if timeout < time.time():
				silent(time_silent, pwm)
				tmp += 1
				break

def first_phase():
	note_loop(3, RE, .05, .1)
	note_loop(2, SOL, .3, .1)
	note_loop(2, LA, .3, .1)
	note_loop(1, RE_HIGH, .1, .5) 
	note_loop(1, SI, .05, .1)
	note_loop(2, SOL, .1, .12)
	note_loop(1, SI, .05, .1)
	note_loop(1, SOL, .1, .1)
	note_loop(1, MI, .1, .4)
	note_loop(1, DO_HIGH, .3, .5)
	note_loop(1, LA, .1, .15)
	note_loop(1, FA_DIEZE, .05, .1)
	note_loop(1, SOL, .05, .15)

def play():
	first_phase()
	GPIO.cleanup()

play()
