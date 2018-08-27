import Detector as det, Connector
import sys
import re


def DataProcessing(con, sleep, account):
    if account is None or con is None or sleep is None:
        return -1
    try:
        con.pushToSerial(sleep)
        con.pushToTarget(account['id'], account['name'], sleep)
    except ValueError or KeyboardInterrupt:
        con.serial.setData(con.serial.ALERT_ON)
        return 0

MY_IP = None
MY_PORT = None


def EyeDetection(account):
    global MY_IP, MY_PORT
    sleep   = False
    counter = 0

    # AWS Public Key
    con = Connector.Connector(ip = MY_IP, port=MY_PORT, method=Connector.CONNECTED_TCP)
    print("Connected to "+MY_IP+':'+str(MY_PORT))

    try:
        print("start")
        eye = det.Eye(cascade_path="/home/pi/opencv/opencv-3.4.1/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml")
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


if __name__=="__main__":
    if operateCommand(sys.argv, len(sys.argv)) == -1:
        if len(sys.argv) > 1:
            print('''[ Invalid Command ]
You have to use like
python main.py (--host 127.0.0.1) (--port 3000)\n''')
        print("Operates in Default Setting")
        MY_IP   = '127.0.0.1'
        MY_PORT = 3000

    account = {
        'id' : 1,
        'name' : "오기준"
    }
    EyeDetection(account)
