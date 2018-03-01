from flask import Flask,render_template
from  datetime import datetime
import time
import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()
app=Flask(__name__)
@app.route("/")
def hello():
    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()
    altitude= sensor.read_altitude()
    sea_level_p = sensor.read_sealevel_pressure()
    print temp
    print pressure
    print altitude
    print sea_level_p
    time.sleep(1)
    now=datetime.now()
    timestring=now.strftime("%Y-%m-%d %H:%M:%S")
    templateData={
    'title':'BMP180',
    'time':timestring,
    'value1':temp,
    'value2':pressure,
    'value3':altitude,
    'value4':sea_level_p
     
            }
    return render_template('main1.html',**templateData)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
