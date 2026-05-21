from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
pinin = 3
pinout = 40
frequency = 1
buttonDefault = 1


GPIO.setup(pinout, GPIO.OUT)
GPIO.setup(pinin, GPIO.IN)
brightness = GPIO.PWM(pinout, frequency)

try:
    while True:
        buttonVal = GPIO.input(3)
        GPIO.output(pinout, True)
        if buttonVal != buttonDefault:
            if frequency < 100:
                frequency += 10
                print(frequency)
            else:
                print("max brightness")
            brightness.start(1)
            brightness.ChangeDutyCycle(frequency)

except KeyboardInterrupt:
    brightness.stop()
    GPIO.cleanup()
