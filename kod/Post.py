from kod.Scroll import *
import pyautogui as py
from kod.Find import *
import subprocess
import keyboard
import time

def post(window_coords, point):
    for i in range(5):
        pos = find("res/Follow.jpg", window_coords, confidence=0.9, rate=False)
        if pos:
            if len(pos) > 1:
                pos[::-1]

            py.click((pos[0][0] - 60), pos[0][1])
            time.sleep(3)
            find("res/Like.jpg", window_coords, confidence=0.9, rate=True)
            time.sleep(1)
            if point == 1:
                point =-1
                find("res/Share.jpg", window_coords, confidence=0.9, rate=True)
                time.sleep(1)
                keyboard.send("Esc")
                time.sleep(1)
            keyboard.send("Esc")
            time.sleep(1)
            py.moveTo(pos[0][0], pos[0][1])
            smooth_drag(pos[0][0], 145)
            time.sleep(1)
    time.sleep(3)
