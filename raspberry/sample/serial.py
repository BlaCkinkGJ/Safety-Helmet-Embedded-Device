import serial
import glob

value = glob.glob('/dev/ttyUSB*')
ser = serial.Serial(value[0], 9600)
ser.xonxoff = 1

if not ser.isOpen():
    ser.open()

try:
    while True:
        line = ser.readline()
        if line is not []:
            data = (str(line.decode("utf-8"))).split()
        #ser.write(b'I will kill you mother fucker')
        print(data)

except KeyboardInterrupt:
    print("Keyboard Interrupt Occured!!")

finally:
    ser.close()
