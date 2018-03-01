
import Adafruit_BMP.BMP085 as BMP085
from time import sleep
sensor = BMP085.BMP085()

while True:
    temperature = sensor.read_temperature()
    print temperature
    pressure = sensor.read_pressure()
    print "Pressure is " +str(pressure) + " Pa"

    altitude = sensor.read_altitude()
    altitude = round(altitude,2)
    print altitude

    sea_level = sensor.read_sealevel_pressure()
    print sea_level
    sleep(1)
#print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
#print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
#print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
#rint('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
