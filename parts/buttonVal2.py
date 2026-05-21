from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pinin = 3
pinout = 40
GPIO.setup(pinin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinout, GPIO.OUT)

try:
    while True:
            Value= GPIO.input(pinin)
            print(Value)
            if Value == 1:
                  GPIO.output(pinout, 0)
            if Value == 0:
                  GPIO.output(pinout, 1)
            sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

