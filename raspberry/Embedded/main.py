from Embedded import Detector as det, Connector


def DataProcessing(con, sleep, account):
    if account is None or con is None or sleep is None:
        return -1
    try:
        con.pushToSerial(sleep)
        con.pushToTarget(account['id'], account['name'], sleep)
    except ValueError or KeyboardInterrupt:
        con.serial.setData(con.serial.ALERT_ON)
        return 0


def EyeDetection(account):
    sleep   = False
    counter = 0

    # default : '13.124.96.176'
    con = Connector.Connector(ip = '192.168.1.13', port=3000, method=Connector.CONNECTED_TCP)

    try:
        eye = det.Eye(cascade_path="/home/pi/opencv/opencv-3.4.1/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml")
        for frame in eye.getFrame():
            eye.analyze(frame)

            percent = float(eye.sleepPercentage())

            if percent > 0.8 : counter += 1
            else             : counter = 0

            if   counter > 10 : sleep = True
            elif counter == 0 : sleep = False

            print(sleep)

            if DataProcessing(con, sleep, account) == -1:
                return -1

    except KeyboardInterrupt:
        return 0


if __name__=="__main__":
    account = {
        'id' : 1,
        'name' : "오기준"
    }
    EyeDetection(account)
