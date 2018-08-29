import socket
import keyboard
import json
import time

def Main():
    host='34.214.27.59'
    port = 3000

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    soc.connect((host, port))
    data = {
        '_id': 2,
        'name': "서희재",
        'sleep': False,
        'temper': "32.14",
        'connected': "1",
        'WiFi': "Sample"
    }
    while True:
        temp = json.dumps(data)
        print(temp)
        soc.send(temp.encode('utf8'))
        time.sleep(1)

    soc.close()

if __name__=='__main__':
    Main()
