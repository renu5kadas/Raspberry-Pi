led = 24
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
while True:
    GPIO.output(led,GPIO.HIGH)
    sleep(1)
    GPIO.output(led,GPIO.LOW)
    sleep(1)
