#!usr/bin/python3
import Connector
import DB as database
import json
import threading
import queue
import random
import time
import sys
import re

queueLock = threading.Lock()
waitList  = queue.Queue()
DB        = None
TIMER_GAP = 0.25

def processing(data):
    try:
        data = json.loads(data)
    except ValueError:
        return
    # print("push ", data['_id'])
    queueLock.acquire()
    try:
        waitList.put(data)
    except InterruptedError or KeyboardInterrupt:
        if queueLock.locked(): queueLock.release()
    queueLock.release()
    return None


class pushProcessing:
    def __init__(self):
        pass

    def flushing(self):
        # print("flushing all data")
        queueLock.acquire()
        while not waitList.empty():
            data = waitList.get()
            if DB is not None:
                data['Time'] = time.time() # For check the last modification
                DB.setBuffer(post=data)
                DB.upload()
        queueLock.release()
        threading.Timer(TIMER_GAP+random.random(), self.flushing).start()

    def __del__(self):
        if queueLock.locked() == True:
            queueLock.release()

MY_IP = '127.0.0.1' # AWS Private Key
MY_PORT = 3000
MONGO_PORT = 27017

def command(opcode, operand):
    global MY_IP, MY_PORT
    returnVal = -1
    if type(opcode) == str and type(operand) == str:
        if opcode == '--host':
            ipRegex = re.compile(r'^(\d{1,4}.\d{1,4}.\d{1,4}.\d{1,4})$')
            result = ipRegex.search(operand)
            if result is not None:
                MY_IP = result.group()
                returnVal = 0
            else:
                print("[--host] You have to write IPv4(xxx.xxx.xxx.xxx)")
        elif opcode == '--port':
            if operand.isdecimal():
                MY_PORT = int(operand)
                returnVal = 0
            else:
                print("[--port] Decimal only command")
        return returnVal

def operateCommand(argv, argc):
    commandStatus = 0
    if argc == 3:
        commandStatus |= command(argv[1], argv[2])
    elif argc == 5:
        commandStatus |= command(argv[1], argv[2])
        commandStatus |= command(argv[3], argv[4])
    else:
        commandStatus |= -1

    return commandStatus


if __name__=="__main__":
    if operateCommand(sys.argv, len(sys.argv)) == -1:
        if len(sys.argv) > 1:
            print('''[ Invalid Command ]
You have to use like
python main.py (--host 127.0.0.1) (--port 3000)\n''')
        print("Operates in Default Setting")
        MY_IP   = '127.0.0.1'
        MY_PORT = 3000

    pushProcessing().flushing()
    DB = database.DB(ip = MY_IP, port = MONGO_PORT, table='employees')
    getProcessing = Connector.Server(host=MY_IP, port=MY_PORT)
    getProcessing.run(processing)

