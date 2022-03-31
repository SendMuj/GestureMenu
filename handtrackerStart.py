import cv2
from cvzone.HandTrackingModule import HandDetector
import OptionsFile as opf



#Video Visual Feed
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

#Setup variables
fingers = []
handTracker = HandDetector(maxHands=1, detectionCon=0.85)
sTime = 0

#Main Function
while True:
    
    #Setting up video feed and hand detection
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = handTracker.findHands(img, flipType=False)
    cv2.imshow("Video", img)
    
    #Adjusting the array depending on what fingers are being held up
    if hands:
        hand1 = hands[0]
        fingers = handTracker.fingersUp(hand1)
    else:
        fingers = []   

        
    #Do actions based on what gestures are made
    if len(fingers)==5:
        opf.OpenMenu(fingers, hand1)
    

    
    #Method of quitting application    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break