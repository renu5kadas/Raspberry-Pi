import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
count=0
while True:
    inputvalue=GPIO.input(6)
    if(inputvalue ==True):
        count=count+1
        print("count "+str(count)+"times")
    sleep(0.1)

