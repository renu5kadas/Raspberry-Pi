import RPi.GPIO as GPIO
from espeak import espeak
import time
def speak():
    if(GPIO.input(26)==True):
        es='distance is'+str(distance1)+'cm'
        espeak.synth(es)
        time.sleep(3)
GPIO.setmode(GPIO.BCM)
trig=14
echo=15
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
espeak.synth("Welcome to distance meter using ultrasonic sensor HC-SR-04")
espeak.synth("press swich on 26 to listen distance in cm")
distance1=0
while True:
    GPIO.output(trig,GPIO.LOW)
    speak()
    print 'Waiting'
    speak()
    time.sleep(0.01)
    speak()
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.00001)
    speak()
    GPIO.output(trig,GPIO.LOW)
    speak()
    while GPIO.input(echo)==False:
        start=time.time()
        speak()
    while GPIO.input(echo)==True:
        end=time.time()
        speak()
    t=end-start 
    distance=17150*t
    if(distance<195 and distance>0):
        distance1=distance
    distance1=round(distance1,2)
    print 'distance is ',distance1,'cm'
    time.sleep(0.1)

            
