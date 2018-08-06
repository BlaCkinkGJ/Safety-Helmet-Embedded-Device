import serial as SERIAL
import glob as PATH


class Serial:
    def __init__(self, idx=0, rate=9600):
        self.ttyUSBList = PATH.glob('/dev/ttyUSB*')
        self.serial = SERIAL.Serial(self.ttyUSBList[idx], rate)
        if not self.serial.isOpen():
            self.serial.open()

    def getData(self):
        data = None
        try:
            data = self.serial.readline()
            data = (str(data.decode('utf-8'))).split()
        except AssertionError or KeyboardInterrupt:
            print("HART SEQUENCE DETECTED")
        finally:
            self.__del__()
        return data

    def setData(self, data=b'0'):
        self.serial.write(data)

    def __del__(self):
        self.serial.close()
