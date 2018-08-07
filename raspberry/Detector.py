from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class Detect:
    def __init__(self, camera: object = PiCamera(), resolution: object = (640, 480), framerate: object = 32) -> object:
        self.camera = camera
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self.camera, size=self.camera.resolution)

    @staticmethod
    def find(img, cascade, scale=1.3, nbr=3, sz=(30, 30), flg=cv2.CASCADE_SCALE_IMAGE):
        rects = cascade.detectMultiScale(img, scaleFactor=scale, minNeighbors=nbr, minSize=sz, flags=flg)

        if len(rects) == 0: return []  # If you cannot find the img then return empty list

        rects[:, 2:] += rects[:, :2]
        return rects

    @staticmethod
    def draw(img, rects, color=(0, 255, 0)):
        for lx, ly, rx, ry in rects:
            cv2.rectangle(img, (lx, ly), (rx, ry), color, 2)


class Eye(Detect):
    def __init__(self, cascade_path = "", climit = 2.0, tgsize = (8, 8)):
        super().__init__()

        self.path    = cascade_path
        self.cascade = cv2.CascadeClassifier(self.path)
        self.clahe   = cv2.createCLAHE(clipLimit=climit, tileGridSize=tgsize)
        self.img     = []  # Only use the debug
        self.pos     = []

        time.sleep(0.1)  # camera warm-up

    def analyze(self, frame):
        img = frame.array

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        gray = self.clahe.apply(gray)

        rects    = self.find(gray, self.cascade)
        self.img = gray.copy()  # Only use the debug
        self.pos = rects.copy()

        self.draw(self.img, self.pos)  # Only use the debug
        self.rawCapture.truncate(0)

    def isExist(self):
        if len(self.pos) == 0:
            return False
        else:
            return True

    def getFrame(self):
        return self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)


