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
                         \nThumb+Pinky   Shutdown""")]
        
    ]
    
    menu = sg.Window("Move Mouse", layout, location =(0,0), no_titlebar=True)
    menu.read(timeout=0)

#Audio Control GUI

#Apps Opening GUI

#GUI for adding own apps?

#Ayylmao UI

#Quitting UI

#Closing Existing UI




#make menu class, have default menu active, with ways of closing it. then have functions that replace it when going into other menus/states
#call the class in the main menu function, then call the functions that replace the main menu in subsequent menu changes
#this way can make a function that closes the menu, regardless of which is up