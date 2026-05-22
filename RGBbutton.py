from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

red=38
green=37
blue=40
RGBcolors=[red, green, blue]

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

pinin = 7
GPIO.setup(pinin, GPIO.IN)

buttonDefault=1
colornum=0

#outputVal = False

try:
    while True:
        buttonVal= GPIO.input(7)
        print(buttonVal)
        if buttonVal != buttonDefault:
            GPIO.output(RGBcolors[colornum % 3], False)
            colornum += 1
            GPIO.output(RGBcolors[colornum % 3], True)


        sleep(0.4)

except: KeyboardInterrupt
