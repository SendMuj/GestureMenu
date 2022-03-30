from math import sqrt
import sys
import cv2
import time
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import numpy as np
import autopy
from pywinauto import application
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


modeFlag = True
modeTracker = 0
unsmoothX, unsmoothY = 0,0
smoothX, smoothY = 0,0
unsmoothD = 0
smoothD = 0
smoother = 3.5

#Action Functions
def OpenMenu(fingersup, handData, detector): 
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
        if fingersup==[0,1,0,0,1]:
            modeTracker = 6
            modeFlag = False
    
    if modeTracker == 0:
        print("base menu")
    if modeTracker == 1:
        MouseOption(fingersup, handData)
    if modeTracker == 2:
        AudioOption(fingersup, handData)
    if modeTracker == 3:
        AppsOption(fingersup)
    if modeTracker == 4:
        ExtraOption(fingersup)
    if modeTracker == 5:
        ChillingMainMenu(fingersup)
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
    #     case 5: ChillingMainMenu(fingersup)       #five fingers up
    #     case 6: QuitOption(fingersup)             #thumb and pinky fingers are up      
###############################################################
    




def MouseOption(fingersup, handData): #action to begin mouse control
    global modeFlag
    global modeTracker
    global smoother
    global unsmoothX, unsmoothY
    global smoothX, smoothY
    
    rawX, rawY = handData["lmList"][8][:2]
    baseX = np.interp(rawX, (250,830), (0,1919))
    baseY = np.interp(rawY, (250,470), (0,1079))
    

    
    if fingersup==[1,1,0,0,0]:     #move the mouse
        smoothX = unsmoothX + (baseX - unsmoothX)/smoother
        smoothY = unsmoothY + (baseY - unsmoothY)/smoother
        unsmoothX = smoothX
        unsmoothY = smoothY
        
        autopy.mouse.move(smoothX, smoothY)
        

        
    if fingersup==[1,1,1,0,0]:     #left click when middle and index finger are raised
        autopy.mouse.click()
        time.sleep(0.75)
        
    if fingersup==[1,1,1,1,0]:     #double click when three fingers are raised
        autopy.mouse.click()
        time.sleep(0.1)
        autopy.mouse.click()
        time.sleep(0.75)
        
    if fingersup==[0,0,0,0,1]: 
        modeFlag = True
        modeTracker = 0
        print("returning to menu from mouse")
        time.sleep(1.5)
        return True
        

def AudioOption(fingersup, handData): #action to gain volume change control
    global modeFlag
    global modeTracker
    global unsmoothD
    global smoothD
    
    tX, tY = handData["lmList"][4][:2]
    iX, iY = handData["lmList"][8][:2]
    
    ##########
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    ##########
    
    if fingersup==[0,1,0,0,0]:
        length = sqrt(((iX-tX)**2)+((iY-tY)**2))
        distance = np.interp(length, (30,175), (-65.25,1))
        smoothD = unsmoothD + (distance - unsmoothD)/smoother
        unsmoothD = smoothD
        volume.SetMasterVolumeLevel(int(smoothD), None)
        
    if fingersup==[0,0,0,0,1]:
        modeFlag = True
        modeTracker = 0
        print("returning to menu from audio")
        return True


def AppsOption(fingersup): #action to open applications menu
    global modeFlag
    global modeTracker
    apps = application.Application()
    
    if fingersup==[1,1,0,0,0]: #Launching Spotify
        apps.start(r"C:\Users\itach\AppData\Roaming\Spotify\Spotify.exe")
        modeFlag = True
        modeTracker = 0
        return True

    if fingersup==[1,1,1,0,0]: #Launching Steam
        apps.start(r"C:\Program Files (x86)\Steam\Steam.exe")
        modeFlag = True
        modeTracker = 0
        return True

    if fingersup==[1,1,1,1,0]: #Launching League
        apps.start(r"C:\Riot Games\Riot Client\RiotClientServices.exe")
        modeFlag = True
        modeTracker = 0
        return True

    if fingersup==[1,1,1,1,1]: #Launching Firefox
        apps.start(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        modeFlag = True
        modeTracker = 0
        return True

    if fingersup==[0,0,0,0,1]:
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

def ChillingMainMenu(fingersup): #action to go back to first menu
    global modeFlag
    global modeTracker

    if fingersup==[0,1,1,1,1]:
        modeFlag = True
        modeTracker = 0
        print("just out here chillin")
        return True

def QuitOption(fingersup): #action to quit app entirely
    global modeFlag
    global modeTracker
    
    if fingersup==[1,1,1,0,0]:
        modeFlag = True
        modeTracker = 0
        print("returning to menu from Quit")
        return True
    
    if fingersup==[0,1,1,1,1]:
        sys.exit(0)
