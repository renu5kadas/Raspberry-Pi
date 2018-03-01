import RPi.GPIO as GPIO
import time
from flask import Flask
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello Renukadas!"
@app.route("/l1on")
def hello1():
    GPIO.output(24,GPIO.LOW)
    return "LED1 is ON"
@app.route("/l1off")
def hello2():
    GPIO.output(24,GPIO.HIGH)
    return "LED1 is off"
@app.route("/l2on")
def hello3():
    GPIO.output(25,GPIO.LOW)
    return "LED2 is ON"
@app.route("/l2off")
def hello4():
    GPIO.output(25,GPIO.HIGH)
    return "LED2 is off"
@app.route("/on")
def hello5():
    GPIO.output(27,GPIO.HIGH)
    return "relay is ON"
@app.route("/off")
def hello6():
    GPIO.output(27,GPIO.LOW)
    return "relay is off"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
    
