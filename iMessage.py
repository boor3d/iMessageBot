import os
import time
from pynput.keyboard import Key, Controller

os.system("open -a Messages")

time.sleep(3)

keyboard = Controller()





test = "My name is iTod. I think I have been created to win PubG"



for i in range(1, 5):
    keyboard.type(test)
    time.sleep(3)
    keyboard.press(Key.enter)
    test += '!'