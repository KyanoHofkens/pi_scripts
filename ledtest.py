import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def blink(pin):
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, 1)
    time.sleep(0.5)
    GPIO.output(24, 0)
    time.sleep(0.5)

for i in range(0,10):
    blink(24)

GPIO.cleanup()
print