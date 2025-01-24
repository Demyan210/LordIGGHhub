import pygetwindow as gw
import time
import os

class Window:
    def __init__(self, window_name):
        self.window_name = window_name
        self.window = self.find_window(window_name)
        if self.window:
            self.client_area = self.get_client_area(self.window)
        else:
            self.client_area = None

    def find_window(self, window_name):
        windows = [win for win in gw.getAllWindows() if window_name.lower() in win.title.lower()]
        if not windows:
            print(f"Окно с названием '{window_name}' не найдено!")
            return None
        print(f"Найдено окно: {windows[0].title}")
        windows[0].activate()
        return windows[0]

    def get_client_area(self, window):
        x, y = window.left, window.top
        width, height = window.width, window.height

        border_width = 8
        title_bar_height = 30

        client_width = width - 2 * border_width
        client_height = height - title_bar_height

        return {
            "x": x + border_width,
            "y": y + title_bar_height,
            "width": client_width,
            "height": client_height
        }

    def close(self):
        if self.window:
            print(f"Закрытие окна: {self.window.title}")
            try:
                self.window.close()
            except AttributeError:
                os.system(f"taskkill /f /im {self.window_name}.exe")
        else:
            print("Окно не найдено. Нечего закрывать.")
