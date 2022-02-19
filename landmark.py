import cv2
import numpy as np
import math
import cvzone.HandTrackingModule as htm



wCam, hCam = 1280, 720
smooth = 7
plocX,plocY = 0,0
clocX,clocY = 0,0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.HandDetector(detectionCon=0.8, maxHands=1)


while True:
    key = cv2.waitKey(1)
    success, img = cap.read()
    img = cv2.flip(img, 1)
    #HAND DETECTION
    Hands, img = detector.findHands(img,flipType=False)
    if Hands:
        hand1 = Hands[0]
        lmList = hand1["lmList"]
        if len(lmList) != 0:
            x1, y1 = lmList[4][0], lmList[4][1]
            x2, y2 = lmList[8][0], lmList[8][1]
            #distance between
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            length = math.hypot(x2 - x1, y2 - y1)
            length = np.interp(length, (50, 400), (0, 100))
            print(int(length))
    

    #SHOW WINDOW
    cv2.imshow("Image", img)
    if key == 27 or key == 113:
        break
cv2.destroyAllWindows()
