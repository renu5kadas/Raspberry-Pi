from Adafruit_IO import *
import time
aio = Client('5fd87cf912324ff8b2753489a69a56c8')
temp = 30

while True:
    aio.send('temp',temp)
    data = aio.receive('sw')
    print data.value
    time.sleep(0.1)
    temp = temp + 2
