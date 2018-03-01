count =0
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.LOW)
sleep(0.5)
GPIO.setup(4,GPIO.IN)
while(GPIO.input(4)==False):
    count=count+1
print count
count = 0
