import RPi.GPIO as GPIO
import time
import urllib2
link='https://thingspeak.com/update?key=87W59A9NJIITDPDF'
GPIO.setmode(GPIO.BCM)
while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    count=0
    while(GPIO.input(4)==False):
        count=count+1
    x=count*10
    y=count/5
    link=link+'&field1='+str(count)+'&field2='+str(x)+'&field3='+str(y)
    response = urllib2.urlopen(link)
    print response.code
    print count
    print x
    print y
    time.sleep(15)
