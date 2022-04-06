import PySimpleGUI as sg


#Main Menu GUI
def MainMenu():
 
    layout = [ [sg.Text("""Gestures:                Options: 
                        \nIndex Up                  Mouse Control
                        \nIndex and Middle Up    Audio Control
                        \nFirst Three Up          App Launcher
                        \nFour Up                   WAH!
                        \nIndex+Thumb+Pinky Shutdown
                        \n""")]
        
    ]
    
    menu = sg.Window("Main Menu", layout, location =(0,0), no_titlebar=True, size=(250,200))
    menu.read(timeout=0)
    
#Mouse Control GUI
def MouseMenu():

    layout = [ [sg.Text("""Gestures:             Options: 
                        \nIndex Up               Move Mouse
                        \nIndex and Middle Up Left Click
                        \nFirst Three Up       Double Left Click
                        \nThumb+Pinky   Quit to Main Menu
                        \n""")]
        
    ]
    menu = sg.Window("Move Mouse", layout, location =(0,0), no_titlebar=True, size=(250,200))
    menu.read(timeout=0)
    
#Audio Control GUI
def AudioMenu():
    layout = [ [sg.Text("""Move index finger and thumb
                        \n to adjust volume.""")]
        
    ]
    
    menu = sg.Window("AudioLVL", layout, location =(0,0), no_titlebar=True, size=(250,200))
    menu.read(timeout=0)
    
#Apps Opening GUI
def AppsMenu():
    
    layout = [ [sg.Text("""Gestures:             Options: 
                        \nIndex Up               Spotify
                        \nIndex and Middle Up Steam
                        \nFirst Three Up       League
                        \nFour Up                Firefox
                        \nThumb+Pinky   Shutdown""")]
        
    ]
    
    menu = sg.Window("Apps Menu", layout, location =(0,0), no_titlebar=True, size=(250,200))
    menu.read(timeout=0)


#Quitting UI
def QuitMenu():
    layout = [ [sg.Text("""Gestures:             Options: 
                        \nIndex and Middle Up Return to Main Menu
                        \nAll Up   Shutdown""")]
        
    ]
    
    menu = sg.Window("Quit Menu", layout, location =(0,0), no_titlebar=True, size=(250,200))
    menu.read(timeout=0)

