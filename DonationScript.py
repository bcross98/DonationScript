#Import
import pyautogui
import pytesseract
from PIL import ImageGrab

#Variables
chat = pyautogui.locateCenterOnScreen("Resources/Buttons/chat.png", confidence=0.7)

#Open chat
pyautogui.moveTo(chat, duration=0.1)
pyautogui.click(button="left", clicks=2, interval=0.25)

#Capture and process function
def CaptureAndProcess():
    capture=ImageGrab.grab(bbox = None)

    tess = pytesseract.image_to_string(capture)

    print(tess)

CaptureAndProcess()

#Main loop
