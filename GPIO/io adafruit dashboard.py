import RPi.GPIO as GPIO
from time import *
from Adafruit_IO import *
import Adafruit_DHT
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
aio=Client('5fd87cf912324ff8b2753489a69a56c8')
sensor=Adafruit_DHT.DHT11
pin=17
GPIO.setup(4,GPIO.IN)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.LOW)
sleep(0.1)
while True:
    count=0
    while(GPIO.input(4)==False):
        count=count+1
    humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        aio.send('temperature',temperature)
        sleep(0.4)
        aio.send('humidity',humidity)
        sleep(0.4)
        print "Humidity=",humidity
        print "Temperature",temperature
    sleep(0.4)
    aio.send('L',count);
    print"LDR",count
    sleep(0.4)
    s1=aio.receive('switch1')
    sleep(0.4)
    s2=aio.receive('switch2')
    sleep(0.4)
    r=aio.receive('relay')
    sleep(0.4)
    print "led1",s1.value
    print "led2",s2.value
    print "relay",r.value
    if s1.value=='ON':
        GPIO.output(24,GPIO.LOW)
    else:
        GPIO.output(24,GPIO.HIGH)    
    if s2.value=='ON':
        GPIO.output(25,GPIO.LOW)
    else:
        GPIO.output(25,GPIO.HIGH)
    if r.value=='ON':
        GPIO.output(27,GPIO.HIGH)
    else:
        GPIO.output(27,GPIO.LOW)
    sleep(0.1)

