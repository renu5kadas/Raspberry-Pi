import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(6,GPIO.IN)
GPIO.input(GPIO.LOW)
while True:
    if 6 == GPIO.HIGH :
        GPIO.output(24,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
    if 6 == GPIO.LOW :
        GPIO.output(24,GPIO.HIGH)
        GPIO.output(25,GPIO.HIGH)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(21,GPIO.HIGH)
     

    