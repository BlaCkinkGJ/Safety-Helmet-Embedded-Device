import serial
import glob

value = glob.glob('/dev/ttyUSB*')
ser = serial.Serial(value[0], 9600)

if not ser.isOpen():
    ser.open()

try:
    while True:
        line = ser.readline()
        data = (str(line.decode("utf-8"))).split()
        #ser.write(b'I will kill you mother fucker')
        print(data)

except KeyboardInterrupt:
    ser.close()
