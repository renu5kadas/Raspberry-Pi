import Adafruit_DHT
import time
sensor=Adafruit_DHT.DHT11
pin = 17

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        print "Humidity is",humidity
        print "temperature is",temperature
    time.sleep(1)
