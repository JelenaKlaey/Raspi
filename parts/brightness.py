from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
pinout = 40
frequency=50
GPIO.setup(pinout, GPIO.OUT)
brightness=GPIO.PWM(pinout, frequency)
try:
	GPIO.output(pinout, True)
	brightness.start(frequency)
	brightness.ChangeDutyCycle(100)
		
		
except KeyboardInterrupt:
	brightness.stop()
	GPIO.cleanup()