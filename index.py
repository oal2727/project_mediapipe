import numpy as np
import cv2
import HandleDetection as pm
################################
cap = cv2.VideoCapture(0)

detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img,False)
    cv2.imshow('screen', img)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
