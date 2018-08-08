import Detector as det
import cv2
import Connector
import time


def DataProcessing(con, sleep):
    try:
        con.pushToSerial(sleep)
        con.pushToDB(1, '오기준', sleep)
    except ValueError or KeyboardInterrupt:
        con.serial.setData(con.serial.ALERT_ON)
        return 0


def EyeDetection():
    sleep = False
    con = Connector.Connector(ip = '13.124.96.176')
    try:
        eye = det.Eye(cascade_path="/home/pi/opencv/opencv-3.4.1/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml")
        for frame in eye.getFrame():
            eye.analyze(frame)

            percent = float(eye.sleepPercentage())

            if percent > 0.7 : sleep = True
            else :             sleep = False
            print(percent)
            DataProcessing(con, sleep)

    except KeyboardInterrupt:
        return 0

if __name__=="__main__":
    EyeDetection()
