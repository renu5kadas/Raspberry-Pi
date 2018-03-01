import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.OUT)
while True:
    inputvalue=GPIO.input(6)
    if(inputvalue ==True):
        GPIO.output(24,GPIO.LOW)
    else:
        GPIO.output(24,GPIO.HIGH)
     

