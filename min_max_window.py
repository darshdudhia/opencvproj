import cv2
import numpy as np
import pyautogui
import cvzone.HandTrackingModule as htm

wCam, hCam = 1280, 720
plocX,plocY = 0,0
clocX,clocY = 0,0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.HandDetector(detectionCon=0.8, maxHands=1)
min = True

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
            fingers = detector.fingersUp(hand1)
            if (fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and min == False):
                pyautogui.hotkey('win','d')
                min = True
            if (fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1 and min == True):
                pyautogui.hotkey('win','d')
                min = False
    #SHOW WINDOW
    cv2.imshow("Image", img)
    if key == 27 or key == 113:
        break
cv2.destroyAllWindows()
