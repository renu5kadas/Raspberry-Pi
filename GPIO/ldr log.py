import RPi.GPIO as GPIO
import datetime
import time 
GPIO.setmode(GPIO.BCM)
log=open("LDR.csv","a")
sr=1
log.write("Sr no.,Count,Seconds,Minutes,Hour,Date,Month,Year\n")
while True:
    count=0
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    while(GPIO.input(4)==False):
        count=count+1
    log=open("LDR.csv","a")
    mytime=datetime.datetime.now()
    abc=str(sr)+','+str(count)+','+str(mytime.second)+','+str(mytime.minute)+','+str(mytime.hour)+','+str(mytime.day)+','+str(mytime.month)+','+str(mytime.year)+'\n'
    log.write(abc+'\n')
    time.sleep(2)
    log.flush()
    log.close
    sr=sr+1
    print count
    print abc
    
    
    
    
