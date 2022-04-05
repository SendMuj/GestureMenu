import PySimpleGUI as sg


#Main Menu GUI
def MainMenu():
 
    layout = [ [sg.Text("""Gestures:                Options: 
                        \nIndex Up                  Mouse Control
                        \nIndex and Ring Up    Audio Control
                        \nFirst Three Up          App Launcher
                        \nFour Up                   WAH!
                        \nIndex+Thumb+Pinky Shutdown""")]
        
    ]
    
    menu = sg.Window("Main Menu", layout, location =(0,0), no_titlebar=True)
    menu.read(timeout=0)
    
#Mouse Control GUI
def MouseMenu():

    layout = [ [sg.Text("""Gestures:             Options: 
                        \nIndex Up               Move Mouse
                        \nIndex and Ring Up Left Click
                        \nFirst Three Up       Double Left Click
                        \nFour Up                Open/Close UI
                        \nThumb+Pinky   Quit to Main Menu""")]
        
    ]
    menu = sg.Window("Move Mouse", layout, location =(0,0), no_titlebar=True)
    menu.read(timeout=0)
    
#Audio Control GUI
def AudioMenu(audiolvl):
    layout = [ [sg.Text("""Move index finger and thumb
                        \n to adjust volume.""")]
        
    ]
    
    menu = sg.Window("Move Mouse", layout, location =(0,0), no_titlebar=True)
    menu.read(timeout=0)
    
#Apps Opening GUI
def AppsMenu():
    layout = [ [sg.Text("""Gestures:             Options: 
                        \nIndex Up               Move Mouse
                        \nIndex and Ring Up Left Click
                        \nFirst Three Up       Double Left Click
                        \nFour Up                Open/Close UI
                        \nThumb+Pinky   Shutdown""")]
        
    ]
    
    menu = sg.Window("Move Mouse", layout, location =(0,0), no_titlebar=True)
    menu.read(timeout=0)

#GUI for adding own apps?

#Ayylmao UI
def WAH():
    layout = [ [sg.Text("""Gestures:             Options: 
                        \nIndex Up               Move Mouse
                        \nIndex and Ring Up Left Click
                        \nFirst Three Up       Double Left Click
                        \nFour Up                Open/Close UI
                        \nThumb+Pinky   Shutdown""")]
        
    ]
    
    menu = sg.Window("Move Mouse", layout, location =(0,0), no_titlebar=True)
    menu.read(timeout=0)

#Quitting UI
def QuitMenu():
    layout = [ [sg.Text("""Gestures:             Options: 
                        \nIndex Up               Move Mouse
                        \nIndex and Ring Up Left Click
                        \nFirst Three Up       Double Left Click
                        \nFour Up                Open/Close UI
                        \nThumb+Pinky   Shutdown""")]
        
    ]
    
    menu = sg.Window("Move Mouse", layout, location =(0,0), no_titlebar=True)
    menu.read(timeout=0)

