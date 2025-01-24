import pyautogui as py
import time

def Scroll(amount, times):
    for _ in range(times):
        py.scroll(amount)
        time.sleep(0.1)

def smooth_drag(x, y, steps=10):
    start_x, start_y = py.position() 
    delta_x = (x - start_x) / steps
    delta_y = (y - start_y) / steps

    py.mouseDown()
    for _ in range(steps):
        start_x += delta_x
        start_y += delta_y
        py.moveTo(start_x, start_y)
        time.sleep(0.01)
    time.sleep(1)
    py.mouseUp()