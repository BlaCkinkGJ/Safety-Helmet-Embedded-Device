import serial as SERIAL
import glob as PATH


class Serial:
    ALERT_ON  = b'2'
    ALERT_OFF = b'0'

    def __init__(self, idx=0, rate=9600):
        self.ttyUSBList = PATH.glob('/dev/ttyUSB*')
        self.serial = SERIAL.Serial(port         = self.ttyUSBList[idx],
                                    baudrate     = rate,
                                    bytesize     = SERIAL.EIGHTBITS,
                                    parity       = SERIAL.PARITY_NONE,
                                    stopbits     = SERIAL.STOPBITS_ONE)
        if not self.serial.isOpen():
            self.serial.open()

    def getData(self):
        data = None
        isChanged = False
        try:
            data = self.serial.readline()
            if data is not None:
                temp = (str(data.decode('utf-8'))).split()
                if len(temp) > 1:
                    parity = int(temp[-1])
                    # except '\r', '\t', '\n'
                    dataLength = len(data) - len(temp[-1]) - 3
                    if dataLength == parity:
                        data = temp[:-1]
                        isChanged = True
        except AssertionError or KeyboardInterrupt:
            print("HART SEQUENCE DETECTED")
        self.serial.flushOutput()
        if not isChanged:
            data = []
        return data

    def setData(self, data=b'0'):
        self.serial.write(data)
        self.serial.flushInput()

    def __del__(self):
        self.serial.close()
