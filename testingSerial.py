import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
print('Serial Port open')         # check which port was really used

while True:
    a = ser.readline()
    b = a.split(',')
    print a
    print b
    temp = b[1]
    print 'temperature is ',temp

#ser.write(b'hello')     # write a string
#ser.close()     
