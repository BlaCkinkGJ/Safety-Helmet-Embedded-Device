import Detector as det
import cv2
import threading



class MyThread(threading.Thread):
    def __init__(self, threadID, func):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.func = func

    def run(self):
        self.func()


def EyeDetection():
    try:
        eye = det.Eye(cascade_path="/home/pi/opencv/opencv-3.4.1/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml")
        for frame in eye.getFrame():
            eye.analyze(frame)
            state = eye.isExist()
            print(state)
            cv2.imshow("Fuck", eye.img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"): break
    except KeyboardInterrupt:
        return 0;


if __name__=="__main__":
    thread1 = MyThread(1, EyeDetection)
    thread1.start()
    thread1.join()
