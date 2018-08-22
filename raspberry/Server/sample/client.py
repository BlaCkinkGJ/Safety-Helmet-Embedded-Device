import socket
import keyboard

def Main():
    host='127.0.0.1'
    port = 12345

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    soc.connect((host, port))

    msg = 'run'

    while True:
        soc.send(msg.encode('ascii'))
        data = soc.recv(1024)
        print(str(data.decode('ascii')))
        if keyboard.is_pressed('q'):
            soc.close()

if __name__=='__main__':
    Main()
