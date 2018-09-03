import DB
import subprocess
import socket
import json


def getSSID():
    args = ['/sbin/iwgetid', '-r']
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    (output, dummy) = proc.communicate()
    return output.split()[0]

class Socket:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def run(self, data):
        self.socket.send(data.encode('utf8'))
        """
        # No use now
        recv = self.socket.recv(1024)
        if recv : return recv
        else    : return None
        """

    def close(self):
        self.socket.close()

    def __del__(self):
        self.close()

CONNECTED_TCP = 0
CONNECTED_DB  = 1

class Connector:
    SUCCESS = 1
    FAIL = 0

    def __init__(self, ip='localhost', port=27017, table="employees", method = CONNECTED_DB):
        if   method == CONNECTED_DB : self.db = DB.DB(ip, port, table)
        elif method == CONNECTED_TCP: self.socket = Socket(host=ip, port=port)
        self.method = method
        self.data   = None



    def pushToSerial(self, sleep=False):
        if sleep : self.serial.setData(self.serial.ALERT_ON)
        else     : self.serial.setData(self.serial.ALERT_OFF)

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
            if self.method == CONNECTED_DB  :
                self.db.setBuffer(data)
                self.data = data
            elif self.method == CONNECTED_TCP :
                self.data = data
            return self.SUCCESS
        else:
            return self.FAIL

    def pushToTarget(self, id, name, sleep):
        data = json.dumps(self.data)
        self.socket.run(data)
        self.data = None

    # Make push to TCP/IP
    # Use the producer, consumer Threading
    # func(IP addr, data)
