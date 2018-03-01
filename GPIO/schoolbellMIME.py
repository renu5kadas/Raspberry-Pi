import RPi.GPIO as GPIO
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime
import time
fromaddr="varad.joshi5299@gmail.com"
toaddr='renukadasnb5@gmail.com'
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
while True:
    t=datetime.datetime.now()
    mesg="alarm worked\n"+str(t)
    msg=MIMEMultipart()
    msg['From']="varad.joshi5299"
    msg['To']="renukadasnb5"
    msg['Subject']="ALARM"
    msg.attach(MIMEText(mesg,'plain'))
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("varad.joshi5299","varad123")
    text=msg.as_string() 
    server.sendmail("varad.joshi5299","renukadasnb5@gmail.com",text)
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

    
