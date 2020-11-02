import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

try:
	while True:
		if GPIO.input(25) == True:
			print("Sensor on!")
			time.sleep(0.2)
		if GPIO.input(25) == False:
			print("Sensor off!")
			time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()
