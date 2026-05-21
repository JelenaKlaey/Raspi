import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

blink_amount=int(input())
for i in range(blink_amount):
        GPIO.output(11,True)
        GPIO.sleep(1)
        GPIO.output(11,False)
        GPIO.sleep(1)
