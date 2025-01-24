from kod.window import Window
from kod.Switch import switch
from kod.Entry import entry
from kod.Prize import prize
from kod.Post import post
from kod.Launch import *
import time

launch()

wj = Window("LordHub")
window_coords = (wj.client_area['x'], wj.client_area['y'], wj.client_area['width'], wj.client_area['height'])

time.sleep(2)

# print("entry")
entry(window_coords)
time.sleep(2)
# print("post")
post(window_coords, point=1)
time.sleep(2)
# print("prize")  
prize(window_coords)
time.sleep(2)
# print(" ")

wj.close()

