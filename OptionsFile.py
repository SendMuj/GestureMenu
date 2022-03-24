import sys
import cv2
import time
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import numpy as np
import autopy


modeFlag = True
modeTracker = 0

#Action Functions
def OpenMenu(fingersup, handData): 
    #Open GUI before match statement
    global modeFlag
    global modeTracker
    
    #flag system to go to and remain in correct state
    if modeFlag:
        if fingersup==[1,1,0,0,0]:
            modeTracker = 1
            modeFlag = False
        if fingersup==[1,1,1,0,0]:
            modeTracker = 2
            modeFlag = False 
        if fingersup==[1,1,1,1,0]:
            modeTracker = 3
            modeFlag = False
        if fingersup==[1,1,1,1,1]:
            modeTracker = 4
            modeFlag = False
        if fingersup==[0,1,1,1,1]:
            modeTracker = 5
            modeFlag = False 
        if fingersup==[0,0,0,0,1]:
            modeTracker = 6
    
    if modeTracker == 0:
        print("base menu")
    if modeTracker == 1:
        MouseOption(fingersup, handData)
    if modeTracker == 2:
        AudioOption(fingersup)
    if modeTracker == 3:
        AppsOption(fingersup)
    if modeTracker == 4:
        ExtraOption(fingersup)
    if modeTracker == 5:
        ReturnMainMenu(fingersup)
    if modeTracker == 6:
        QuitOption(fingersup)
    
    
###############################################################
#for use in python 3.10 if autopy/rust gets an update to work
    # match modeTracker:
    #     case 0: print("base menu")
    #     case 1: MouseOption(fingersup, handData)  #only index finger is up
    #     case 2: AudioOption(fingersup)            #index and middle fingers up
    #     case 3: AppsOption(fingersup)             #index, middle and ring fingers up
    #     case 4: ExtraOption(fingersup)            #four fingers up
    #     case 5: ReturnMainMenu(fingersup)         #five fingers up
    #     case 6: QuitOption(fingersup)             #thumb and pinky fingers are up      
###############################################################
    




def MouseOption(fingersup, handData): #action to begin mouse control
    global modeFlag
    global modeTracker
    iX, iY = handData["lmList"][6][:2]
    
    if fingersup==[1,1,0,0,0]:     #move the mouse
        autopy.mouse.move(iX, iY)
    if fingersup==[1,1,1,0,0]:     #left click when middle and index finger are raised
        autopy.mouse.click()
        time.sleep(5)
    if fingersup==[1,1,1,1,0]:     #double click when three fingers are raised
        autopy.mouse.click()
        time.sleep(0.1)
        autopy.mouse.click()
        time.sleep(5)
    if fingersup==[0,0,0,0,1]: 
        modeFlag = True
        modeTracker = 0
        print("returning to menu from mouse")
        return True
        

def AudioOption(fingersup): #action to gain volume change control
    global modeFlag
    global modeTracker
    
    if fingersup==[1,1,0,0,0]:
        print("base form in audio")
    if fingersup==[1,1,1,0,0]:
        print("clicker form in audio")
    if fingersup==[0,1,1,1,1]:
        modeFlag = True
        modeTracker = 0
        print("returning to menu from audio")
        return True


def AppsOption(fingersup): #action to open applications menu
    global modeFlag
    global modeTracker
    
    if fingersup==[1,1,0,0,0]:
        print("base form in Apps")
    if fingersup==[1,1,1,0,0]:
        print("clicker form in Apps")
    if fingersup==[0,1,1,1,1]:
        modeFlag = True
        modeTracker = 0
        print("returning to menu from Apps")
        return True


def ExtraOption(fingersup): #rickroll for now, can't think of another option
    global modeFlag
    global modeTracker
    if fingersup==[1,1,0,0,0]:
        print("base form in Extra")
    if fingersup==[1,1,1,0,0]:
        print("clicker form in Extra")
    if fingersup==[0,1,1,1,1]:
        modeFlag = True
        modeTracker = 0
        print("returning to menu from Extra")
        return True

def ReturnMainMenu(fingersup): #action to go back to first menu
    global modeFlag
    global modeTracker
    if fingersup==[1,1,0,0,0]:
        print("base form in Return")
    if fingersup==[1,1,1,0,0]:
        print("clicker form in Return")
    if fingersup==[0,1,1,1,1]:
        modeFlag = True
        modeTracker = 0
        print("returning to menu from Return")
        return True

def QuitOption(fingersup): #action to quit app entirely
    global modeFlag
    global modeTracker
    if fingersup==[1,1,0,0,0]:
        print("base form in Quit")
    if fingersup==[1,1,1,0,0]:
        print("clicker form in Quit")
    if fingersup==[0,1,1,1,1]:
        modeFlag = True
        modeTracker = 0
        print("returning to menu from Quit")
        return True