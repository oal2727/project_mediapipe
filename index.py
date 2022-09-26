import numpy as np
import cv2
import HandleDetection as pm
from PIL import ImageGrab
################################
# cap = cv2.VideoCapture(0)

video = "video.mp4"
cap = cv2.VideoCapture(video)
detector = pm.poseDetector()
# grab = ImageGrab.grab()

while True:
    success, img = cap.read()
    img = cv2.resize(img, (500, 400))
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        result = detector.findAngleAndDrawLandmark(img,27,28)
        # frame = np.array(img)
        print(result)
        if(80 <= result): # requried only screen
            print("save image")
        # cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)


    cv2.imshow('screen', img)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
