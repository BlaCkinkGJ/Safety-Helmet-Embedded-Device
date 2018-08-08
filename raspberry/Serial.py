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
        try:
            data = self.serial.readline()
            self.serial.flushInput()
            if data is not None:
                data = (str(data.decode('utf-8'))).split()
        except AssertionError or KeyboardInterrupt:
            print("HART SEQUENCE DETECTED")
        return data

    def setData(self, data=b'0'):
        self.serial.write(data)

    def __del__(self):
        self.serial.close()
