import DB
import Serial
import subprocess


def getSSID():
    args = ['/sbin/iwgetid', '-r']
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    (output, dummy) = proc.communicate()
    return output.split()[0]


class Connector:
    SUCCESS = 1
    FAIL = 0

    def __init__(self, ip='localhost', port=27017, table="employees"):
        self.db = DB.DB(ip, port, table)
        self.serial = Serial.Serial()
        self.serial.setData(self.serial.ALERT_OFF)

    def pushToSerial(self, sleep=False):
        """
        OFF INVALID
        BECAUSE THE ONLY OFF THE ALARM CAN USE RESET BUTTON
        """
        temp = self.serial.getData()
        if len(temp) == 2:
            if temp[1] == '0' or sleep:
                self.serial.setData(self.serial.ALERT_ON)
        else:
            if sleep:
                self.serial.setData(self.serial.ALERT_ON)

    def pushToBuffer(self, id, name, sleep):
        dataArray = []

        dataArray.append(id)
        dataArray.append(name)
        dataArray.append(sleep)
        for temp in self.serial.getData():
            dataArray.append(temp)
        dataArray.append(getSSID())

        if len(dataArray) == 6:
            data = {
                '_id': dataArray[0],
                'name': dataArray[1],
                'sleep': dataArray[2],
                'temper': dataArray[3],
                'connected': dataArray[4],
                'WiFi': dataArray[5]
            }
            self.db.setBuffer(data)
            return self.SUCCESS
        else:
            return self.FAIL

    def pushToDB(self, id, name, sleep):
        if self.pushToBuffer(id, name, sleep) == self.SUCCESS:
            self.db.upload()
