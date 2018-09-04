import Connector
import sys
import re
import os
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse
import time
from random import *
S = True
C = '1'
def DataProcessing(con, sleep, account):
    global S, C
    con.data = {
        '_id' : account['id'],
        'name' : account['name'],
        'temper' : round(uniform(-10.0,45.0),2),
        'connected' : C,
        'sleep' : S,
        'WiFi' : 'sample'+str(account['id']),
        'Time' : time.time()
    }
    if random() > 0.5:
        S = True
    else:
        S = False
    if C == '1': C = '0'
    else: C = '1'
    con.pushToTarget(account['id'], account['name'], sleep)

MY_IP = '127.0.0.1'
MY_PORT = 3000


def EyeDetection(account):
    global MY_IP, MY_PORT
    sleep   = False
    counter = 0

    # AWS Public Key
    con = Connector.Connector(ip = MY_IP, port=MY_PORT, method=Connector.CONNECTED_TCP)
    print("Connected to "+MY_IP+':'+str(MY_PORT))

    try:
        while True:
            DataProcessing(con, sleep, account)
            time.sleep(uniform(0.1, 10.0))

    except KeyboardInterrupt:
        print("end")
        return 0

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

def getAccount():
    result = {
        'id': None,
        'name': None
    }
    if not os.path.exists('data.xml'):
        data = Element("LoginData")

        while True:
            result['id'] = input("ID 값을 입력해주십시오 : ")
            result['name'] = input("이름을 입력해주십시오 : ")
            if result['id'].isdecimal():
                break
            else:
                print("잘못된 ID 값입니다. 다시 수행해주십시오.")

        SubElement(data, "id").text = result['id']
        SubElement(data, "name").text = result['name']

        ElementTree(data).write("data.xml")
    else:
        tree = parse("data.xml")
        data = tree.getroot()
        result['id'] = data.findtext("id")
        result['name'] = data.findtext("name")

    if result['id'] is not None:
        result['id'] = int(result['id'])

    return result

if __name__=="__main__":
    MY_IP   = '34.214.27.59'
    MY_PORT = 3000

    account = {
        'id' : int(sys.argv[1]),
        'name' : sys.argv[2]
        }

    if account['id'] is not None and account['name'] is not None:
        EyeDetection(account)
