import pyautogui as py
import numpy as np
import time
import cv2
import mss
import sys
import os

def get_res(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def get_scr(window_coords):
    win_x, win_y, win_width, win_height = window_coords
    with mss.mss() as sct:
        monitor = {
            "top": win_y,
            "left": win_x,
            "width": win_width,
            "height": win_height,
        }
        screenshot = np.array(sct.grab(monitor))
    return screenshot

def find(path, window_coords, confidence, rate):
    win_x, win_y, win_width, win_height = window_coords
    screenshot = get_scr(window_coords)

    template_path = get_res(path)

    if not os.path.exists(template_path):
        print(f"Шаблон {template_path} не найден!")
        return []
    else:
        template = cv2.imread(template_path, 0)
        # print(f"Шаблон {template_path} успешно загружен!")

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= confidence)  # Correctly get the positions

    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print(f"Res: {max_val}")

    click_positions = []
    if loc[0].size > 0:  # Check if any locations are found
        all_boxes = [(int(pt[0]), int(pt[1]), w, h) for pt in zip(*loc[::-1])]
        filtered_boxes = non_max_suppression(np.array(all_boxes), overlap_thresh=0.5)

        for idx, (x, y, w, h) in enumerate(filtered_boxes):
            if rate:
                py.click((x + w // 2) + win_x, (y + h // 2) + win_y)
            else:
                click_positions.append(((x + w // 2) + win_x, (y + h // 2) + win_y))

            #Обводка шаблона на скриншоте
        #     cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 0, 0), 2)

        # timestamp = time.time()
        # filename = f"nfind_single_{idx}_{int(timestamp)}.jpg"
        # cv2.imwrite(filename, screenshot)

    return click_positions

def non_max_suppression(boxes, overlap_thresh=0.5):
    if len(boxes) == 0:
        return []
    boxes = np.array(boxes)
    pick = []

    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 0] + boxes[:, 2]
    y2 = boxes[:, 1] + boxes[:, 3]

    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)

    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[idxs[:last]]
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlap_thresh)[0])))

    return boxes[pick].astype("int")