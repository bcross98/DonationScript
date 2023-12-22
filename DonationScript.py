#Import
import pyautogui
import pytesseract
from PIL import ImageGrab

#Variables
chat = pyautogui.locateCenterOnScreen("Resources/Buttons/chat.png", confidence=0.7)

#Open chat function
def OpenChat():
    pyautogui.moveTo(chat, duration=0.1)
    pyautogui.click(button="left", clicks=2, interval=0.25)

#Capture and process function
def CaptureAndProcess():
    capture=ImageGrab.grab(bbox = None)

    tess = pytesseract.image_to_string(capture)

    if (tess.find("Super Archers") != -1):
        print("Found SA")
    elif (tess.find("Yeti") != -1):
        print("Found Yet")
    elif (tess.find("Balloons") != -1):
        print("Found Bal")
    else:
        print("Didn't find")

#Main loop
OpenChat()
CaptureAndProcess()