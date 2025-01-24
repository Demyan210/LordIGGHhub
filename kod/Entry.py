from datetime import datetime
from kod.Scroll import *
import pyautogui as py
from kod.Find import *
import keyboard
import time
    
def entry(window_coords):
    today = datetime.now().day
    # print(f"Сегодня: {today}")
    time.sleep(1)
    find("res/Vxod.jpg", window_coords, confidence=0.9, rate=True)
    time.sleep(7)
    pos = find(f"day/{today}.jpg", window_coords, confidence=0.95, rate=False)
    if pos:
        py.click(pos[0][0], pos[0][1])
        time.sleep(2)
        keyboard.send("Esc")
        time.sleep(3)
    else:
        Scroll(-300, 4)
        time.sleep(2)
        find(f"day/{today}.jpg", window_coords, confidence=0.95, rate=True)
        time.sleep(2)
        keyboard.send("Esc")
        time.sleep(3)