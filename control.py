#PYNPUT
#controlling your mouse
#listening your mouse
#controlling your keyboard
#listening to your keyboard

from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController

def controlMouse():
    mouse = MouseController()
    mouse.position = (10, 20)  # Move the mouse to (10, 20) pixels on the screen
    # This moves the mouse to 10 pixels from the left and 20 pixels from the top.

def controlKeyboard():
    keyboard = KeyboardController()
    keyboard.type("I'M smriti")  # Types out the text "I'M smriti"

# Call the functions
controlMouse()
controlKeyboard()
