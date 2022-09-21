import os
import time
from pynput.keyboard import Key, Controller
import random

os.system("open -a Messages")

time.sleep(3)

keyboard = Controller()


with open ("PickupLines.txt", "r") as f:
    data = f.readlines()

    clean_data = []
    for line in data:
        line = line.replace("\n","")
        clean_data.append(line)
        
    
    random_phrase = random.choice(clean_data)



def typing(phrase):
    keyboard.type(phrase)
    time.sleep(3)
    keyboard.press(Key.enter)


typing(random_phrase)