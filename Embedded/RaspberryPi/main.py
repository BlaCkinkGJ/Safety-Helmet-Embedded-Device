import Detector as det, Connector
import sys
import re
import os
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse

def DataProcessing(con, sleep, account):
    if account is None or con is None or sleep is None:
        return -1
    try:
        con.pushToSerial(sleep)
        con.pushToTarget(account['id'], account['name'], sleep)
    except ValueError or KeyboardInterrupt:
        con.serial.setData(con.serial.ALERT_ON)
        return 0

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
        print("start")
        eye = det.Eye(cascade_path="./opencv/haarcascades/haarcascade_eye_tree_eyeglasses.xml")
        for frame in eye.getFrame():
            eye.analyze(frame)

            percent = float(eye.sleepPercentage())

            if percent > 0.8 : counter += 1
            else             : counter = 0

            if   counter > 30 : sleep = True
            # This statement just test statement
            elif counter == 0 : sleep = False

            if DataProcessing(con, sleep, account) == -1:
                return -1

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
    if operateCommand(sys.argv, len(sys.argv)) == -1:
        if len(sys.argv) > 1:
            print('''[ Invalid Command ]
You have to use like
python main.py (--host 127.0.0.1) (--port 3000)\n''')
        print("Operates in Default Setting")
        MY_IP   = '127.0.0.1'
        MY_PORT = 3000

    account = getAccount()

    if account['id'] is not None and account['name'] is not None:
        EyeDetection(account)
