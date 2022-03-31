import PySimpleGUI as sg



#Main Menu GUI
def MainMenu():
    layout = [ [sg.Text("""Gestures:          Options:
                         \nIndex Up          Mouse Control
                    Index and Ring Up Audio Control
                    First Three Up    App Launcher
                    Four Up           WAH!
                    Index+Thumb+Pinky Shutdown""")]
        
    ]
    
    menu = sg.Window("Main Menu", layout, location =(0,0), no_titlebar=True)
    menu.read(timeout=0)


#Mouse Control GUI

#Audio Control GUI

#Apps Opening GUI

#GUI for adding own apps?

#Ayylmao UI

#Quitting UI

#Closing Existing UI
