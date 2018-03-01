import RPi.GPIO as GPIO
import urllib2
import Adafruit_DHT
import smtplib
import time
GPIO.setmode(GPIO.BCM)
sensor=Adafruit_DHT.DHT11
pin=17
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
link='https://thingspeak.com/update?key=X2TUC97OEM6D3DK6'
server.login("varad.joshi5299@gmail.com","varad123")
while True:
    count=0
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    while (GPIO.input(4)==False):
        count=count+1
    humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        print "\nLIGHT is=",count
        print "\nHUMIDITY is=",humidity
        print "\nTEMPERATURE is=",temperature
    link=link+'&field1='+str(count)+'&field2='+str(humidity)+'&field3='+str(temperature)
    response=urllib2.urlopen(link)
    print 'Sending Email...'
    mesg='Hi\nLDR='+str(count)+'\nHUMIDITY='+str(humidity)+'\nTEMPERATURE='+str(temperature)
    server.sendmail("varad.joshi5299","renukadasnb5@gmail.com",mesg)
    print 'Email Sent'
    print response.code
    time.sleep(15)
    
    
    
    

