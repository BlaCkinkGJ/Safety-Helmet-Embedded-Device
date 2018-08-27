import socket
from _thread import *

class Server:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host   = host
        self.port   = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connect = None
        self.address = None

    def connection(self, callback, MAX_SIZE=1024):
        print('connected    > ', self.address[0], ':', self.address[1])
        if self.connect is None or self.address is None:
            return -1
        try:
            while True:
                data = self.connect.recv(MAX_SIZE)
                if not data: break
                recv = callback(data.decode('ascii'))
                if recv is not None: self.connect.send(recv.encode('ascii'))
        except InterruptedError:
            print('INTERRUPT OCCUR')
        finally:
            print('disconnected > ', self.address[0], ':', self.address[1])
            return 0

    def run(self, callback, backlog = 5):
        print('READY')
        self.socket.bind((self.host, self.port))
        self.socket.listen(backlog)

        while True:
            try:
                con, addr = self.socket.accept()
                self.connect = con
                self.address = addr
                start_new_thread(self.connection, (callback,))
            except InterruptedError:
                print("Disconnected")
                self.socket.close()
                return 0
