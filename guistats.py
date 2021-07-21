import pyautogui
import time
screenWidth, screenHeight = pyautogui.size()
for x in range(0, 12):
    x, y = pyautogui.position()
    print("{}, {}".format(x, y))
    time.sleep(1)

