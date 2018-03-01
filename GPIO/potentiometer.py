import RPi.GPIO as GPIO
import time
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23,GPIO.IN)  
    inputvalue=GPIO.input(23)
    print inputvalue
