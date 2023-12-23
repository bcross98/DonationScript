#Import
import pyautogui
import pytesseract
from PIL import ImageGrab
import subprocess
import time

#Open chat function
def OpenChat():
    chat = pyautogui.locateCenterOnScreen("Resources/Buttons/chat.png", confidence=0.6)

    pyautogui.moveTo(chat, duration=0.1)
    pyautogui.click(button="left", clicks=2, interval=0.25)

    time.sleep(1)

#Capture and process function
def CaptureAndProcess():

    #Look for Donate Button and start the capture process
    if pyautogui.locateCenterOnScreen("Resources/Buttons/Donate.png", confidence=0.6) == None:
        print("No requests found")
    else:
        capture=ImageGrab.grab(bbox = None)
        tess = pytesseract.image_to_string(capture)

        #Search for 45 troop weight donation
        if (tess.find("0") != -1) and (tess.find("45") != -1):

            #Search for what troop
            if (tess.find("CandyCorn") != -1):
                subprocess.run(["python", "Library/45/SuperArcher45.py"])
            
            elif (tess.find("CaramelCorn") != -1):
                subprocess.run(["python", "Library/45/Yeti45.py"])
            
            elif (tess.find("ButterCorn") != -1):
                subprocess.run(["python", "Library/45/Balloon45.py"])
            
            else:
                print("cc request isn't supported yet")
        
        #Search for 50 troop weight donation
        elif (tess.find("0") != -1) and (tess.find("50") != -1):

            #Search for what troop
            if (tess.find("CandyCorn") != -1):
                subprocess.run(["python", "Library/50/SuperArcher50.py"])
            
            elif (tess.find("CaramelCorn") != -1):
                subprocess.run(["python", "Library/50/Yeti50.py"])
            
            elif (tess.find("ButterCorn") != -1):
                subprocess.run(["python", "Library/50/Balloon50.py"])
            
            else:
                print("cc request isn't supported yet")
        
        else:
            print("cc isn't supported yet")


#Main loop
OpenChat()
CaptureAndProcess()
