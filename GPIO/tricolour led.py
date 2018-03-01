import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
while True:
    GPIO.output(4,GPIO.LOW)
    GPIO.output(2,GPIO.HIGH)
    sleep(0.2)
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(2,GPIO.LOW)
    sleep(0.2)
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(3,GPIO.LOW)
    sleep(0.2)
    
