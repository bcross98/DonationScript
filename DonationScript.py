#Import
import pyautogui
import pytesseract
from PIL import ImageGrab
import subprocess
import time

#Variables
chat = pyautogui.locateCenterOnScreen("Resources/Buttons/chat.png", confidence=0.7)

#Open chat function
def OpenChat():
    pyautogui.moveTo(chat, duration=0.1)
    pyautogui.click(button="left", clicks=2, interval=0.25)

    time.sleep(1)

#Capture and process function
def CaptureAndProcess():
    capture=ImageGrab.grab(bbox = None)

    tess = pytesseract.image_to_string(capture)

    if (tess.find("Super Archer") != -1):
        subprocess.run(["python", "Library/SuperArcher.py"])

    #Issue finding Yeti
    elif (tess.find("Yeti") != -1):
        subprocess.run(["python", "Library/Yeti.py"])

    elif (tess.find("Balloon") != -1):
        subprocess.run(["python", "Library/Balloon.py"])
        
    else:
        print("Nothing found")


#Main loop
OpenChat()
CaptureAndProcess()
