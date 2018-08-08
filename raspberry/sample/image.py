
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np


def detect(img, cascade):
    rects = cascade.detectMultiScale(img,
                                     scaleFactor=1.3,
                                     minNeighbors=3,
                                     minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0: return []

    rects[:, 2:] += rects[:, :2]
    return rects


def draw_rects(img, rects, color):
    for lx, ly, rx, ry in rects:
        cv2.rectangle(img, (lx, ly), (rx, ry), color, 2)


if __name__ == "__main__":
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32

    rawCapture = PiRGBArray(camera, size=(640, 480))
    path = "/home/pi/opencv/opencv-3.4.1/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml"
    # lower  grade : haarcascade_eye.xml
    # mid    grade : haarcascade_eye_tree_eyeglasses.xml
    # higher grade : haarcascade_lefteye_2splits.xml
    cascade = cv2.CascadeClassifier(path)

    time.sleep(0.1)  # For camera warmup

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        img = frame.array

        gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray  = cv2.equalizeHist(gray)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        gray  = clahe.apply(gray)

        rects = detect(gray, cascade)
        out = gray.copy()

        draw_rects(out, rects, (0, 255, 0))

        if len(rects) == 0:
            print(0)
        else:
            print(1)

        cv2.imshow("Frame", out)
        key = cv2.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        # if pressed q then stop the program
        if key == ord("q"): break
