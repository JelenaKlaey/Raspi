from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pinin = 3
pinout = 40
GPIO.setup(pinin, GPIO.IN)
GPIO.setup(pinout, GPIO.OUT)

buttonDefault=1
LEDstate= False

try:
    while True:
        buttonVal= GPIO.input(3)
        if buttonVal != buttonDefault:
            buttonVal= GPIO.input(3)
            LEDstate= not LEDstate
            print(LEDstate)
            GPIO.output(40, LEDstate)
        else:
            pass
        sleep(0.2)

except: KeyboardInterrupt