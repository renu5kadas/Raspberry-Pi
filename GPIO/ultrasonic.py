import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trig=14
echo=15
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
distance1=0
while True:
    GPIO.output(trig,GPIO.LOW)
    print 'Waiting'
    time.sleep(1)
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig,GPIO.LOW)
    while GPIO.input(echo)==False:
        start=time.time()
    while GPIO.input(echo)==True:
        end=time.time()
    t=end-start
    distance=17150*t
    if(distance<195 and distance>0):
        distance1=distance
    distance1=round(distance1,2)
    print 'distance is ',distance1,'cm'
    time.sleep(1)
    
