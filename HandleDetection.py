import cv2
import mediapipe as mp
import time
import math

class poseDetector():

    def __init__(self, mode=False, upBody=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        # self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth,
        #                              self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # inversion de colores
        self.results = self.pose.process(imgRGB) # devuelve los puntos de referencia de las poses
        # output : mediapipe.python.solution_base.SolutionOutputs
        # if self.results.pose_landmarks: # punto de referencia de las poses
        #     if draw: # dibujo default True
        #         #Dibuja los puntos de referencia y las conexiones en la imagen.
        #         self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
        #                                    self.mpPose.POSE_CONNECTIONS)
        return imgRGB
    
    def findPosition(self, img, draw=True):
        self.lmList = [] ##   [id,cx,cy]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark): 
                h, w, c = img.shape # [w,y]
                cx, cy = int(lm.x * w), int(lm.y * h) #
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED) # dibujar las posiciones actuales con puntos
        return self.lmList

    def findAngleAndDrawLandmark(self, img, p1, p2, draw=True):
        
        # get coordinates cx,cy for id landmarks 

        # Get the landmarks
        
        # [id,cx,cy]
        x1, y1 = self.lmList[p1][1:] # cx1,cy1
        x2, y2 = self.lmList[p2][1:] # cx2,cy2
        # Draw
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 7, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 7, (0, 0, 255), 2)

        # 1.distancia entre 2 puntos a mano
        # 2.distance entre  2 puntos con numpy
        valuePotentialX = math.pow(x2-x1,2)
        valuePotentialY = math.pow(y2-y1,2)
        finalResult = math.sqrt(valuePotentialX + valuePotentialY)
        return finalResult
        # # res = False
        # if(80 <= finalResult): # requried only screen
        #     # res = True
        #     cv2.imwrite("images/",img)
            # cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        # cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

