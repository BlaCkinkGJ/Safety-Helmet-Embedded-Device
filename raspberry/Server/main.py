import Connector
import DB as database
import json
import threading
import queue
import random

queueLock = threading.Lock()
waitList  = queue.Queue()
DB        = None
TIMER_GAP = 0.25


def processing(data):
    data = json.loads(data)
    # print("push ", data['_id'])
    queueLock.acquire()
    waitList.put(data)
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
                DB.setBuffer(post=data)
                DB.upload()
        queueLock.release()
        threading.Timer(TIMER_GAP+random.random(), self.flushing).start()

MY_IP = '172.31.18.210'

if __name__ == "__main__":
    pushProcessing().flushing()
    DB = database.DB(ip = MY_IP, port = 27017, table='employees')
    getProcessing = Connector.Server(host=MY_IP, port=3000)
    getProcessing.run(processing)

