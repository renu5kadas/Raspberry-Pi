import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
while True:
    GPIO.output(24,GPIO.HIGH)
    sleep(1)
    GPIO.output(24,GPIO.LOW)
    sleep(1)
