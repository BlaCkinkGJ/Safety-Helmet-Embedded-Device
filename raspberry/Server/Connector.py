import socket
from _thread import *

class Server:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host   = host
        self.port   = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connection(self, callback, accept, MAX_SIZE=1024):
        connect, address = accept
        print('connected    > ', address[0], ':', address[1])
        if connect is None or address is None:
            return -1
        try:
            while True:
                data = connect.recv(MAX_SIZE)
                if not data: break
                recv = callback(data.decode('utf8'))
                if recv is not None: connect.send(recv.encode('utf8'))
        except InterruptedError:
            print('INTERRUPT OCCUR')
        finally:
            print('disconnected > ', address[0], ':', address[1])
            return 0

    def run(self, callback, backlog = 5):
        print('READY')
        self.socket.bind((self.host, self.port))
        self.socket.listen(backlog)

        while True:
            try:
                con, addr = self.socket.accept()
                start_new_thread(self.connection, (callback,(con, addr)))
            except InterruptedError:
                print("Disconnected")
                self.socket.close()
                return 0
