import socket

from _thread import *
import threading

print_lock = threading.Lock()

def Thread(con):
    try:
        while True:
            data = con.recv(1024)
            if not data:
                print_lock.release()
                break
            data = data[::-1]
            print(data)
            con.send(data)
        if print_lock.locked():
            print_lock.release()
        con.close()
    except KeyboardInterrupt:
        print_lock.release()
        con.close()

def Main():
    host = ""
    port = 12345
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((host, port))

    print('socket binded to post', port)

    soc.listen(5)
    print('socket is listening')

    while True:
        try:
            con, addr = soc.accept()
            print_lock.acquire()
            print('Connected to : ', addr[0], ':', addr[1])

            start_new_thread(Thread, (con,))
        except InterruptedError or KeyboardInterrupt:
            soc.close()

if __name__=='__main__':
    Main()
