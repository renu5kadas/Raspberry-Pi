import RPi.GPIO as GPIO
import time
from flask import Flask
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello Renukadas!"
@app.route("/ledon")
def hello1():
    GPIO.output(24,GPIO.LOW)
    return "LED is ON"
@app.route("/ledoff")
def hello2():
    GPIO.output(24,GPIO.HIGH)
    return "LED is off"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
    
