from kod.Find import *
import keyboard
import time

def prize(window_coords):
    find("res/Profile.jpg", window_coords, confidence=0.9, rate=True)
    time.sleep(5)
    find("res/Take.jpg", window_coords, confidence=0.9, rate=True)
    time.sleep(6)
    find("res/Take1.jpg", window_coords, confidence=0.9, rate=True)
    time.sleep(1)
    find("res/Entry.jpg", window_coords, confidence=0.9, rate=True)
    time.sleep(1)
    keyboard.send("Esc")
    time.sleep(2)