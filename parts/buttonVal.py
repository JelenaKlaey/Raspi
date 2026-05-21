import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(40, GPIO.OUT)

try:
    while True:
        buttonVal = GPIO.input(3)
        print(buttonVal)
        GPIO.sleep(1)
        if buttonVal == 1:
            GPIO.output(40, False)
        else:
            GPIO.output(40, True)

        
except KeyboardInterrupt:
    GPIO.cleanup

