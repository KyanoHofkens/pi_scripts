from re import I
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

def blink(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)


while I != 0:
    blink(24)
    I + 1

GPIO.cleanup()
print("program executed")