import pyautogui
import time
screenWidth, screenHeight = pyautogui.size()
session = "y"
notif = input("Hitting ENTER will begin session ")
while session == "y":
    for x in range(0, 11):
        x, y = pyautogui.position()
        print("Mouse Position: {}, {}".format(x, y))
        time.sleep(1)
    session = input("Continue? [y/n]  ")
stop = input("Press ENTER to terminate ")
