import RPi.GPIO as GPIO
import smtplib
import datetime
import time
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('varad.joshi5299@gmail.com','varad123')
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
while True:
    t=datetime.datetime.now()
    mesg="alarm worked\n"+str(t)
    server.sendmail("varad.joshi5299","renukadasnb5@gmail.com",mesg)
    print t
    for i in range (60):
        if (GPIO.input(6)==True):
            break
        GPIO.output(18,GPIO.HIGH)
        print "ALARM...\n UTH NA BHAVA...."
        time.sleep(1)
    print 'EMAIL SENT'
    GPIO.output(18,GPIO.LOW)
    time.sleep(60-i)

    
