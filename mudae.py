import os
import time
import pyautogui
from rich.console import Console
from rich.markdown import Markdown
console = Console()
TEXTBAR = []
TEXTBAR.append(730)
TEXTBAR.append(1023)
LINK = []
LINK.append(818)
LINK.append(802)
FIREFOX = []
FIREFOX.append(13)
FIREFOX.append(109)
VOTEBUTTON = [881, 634]
CONFIRM = [924, 907]
FINALVOTE = [955, 568]
MD_TITLE = Markdown("# Mudae Autoplayer")
os.system("clear")
console.print(MD_TITLE)
entered = ""
enteredList = []
while True:
    entered = input("Command: ")
    enteredList = entered.split()
    if entered == "quit" or entered == "exit":
        exit()
    elif entered == "dk":
        pyautogui.hotkey("alt", "tab")
        pyautogui.moveTo(TEXTBAR[0], TEXTBAR[1])
        pyautogui.click()
        pyautogui.write("$dk")
        pyautogui.press("enter")
    elif entered == "b" or entered == "start":
        print("Starting in 5 seconds")
        time.sleep(5)
        pyautogui.moveTo(TEXTBAR[0], TEXTBAR[1])
        pyautogui.click()
        for x in range(1, 15):
            pyautogui.write("$w")
            pyautogui.press("enter")
            time.sleep(1.1)
        pyautogui.write("$tu")
        pyautogui.press("enter")
    elif entered == "d" or entered == "dk":
        pyautogui.hotkey("alt", "tab")
        pyautogui.moveTo(TEXTBAR[0], TEXTBAR[1])
        pyautogui.click()
        pyautogui.write("$dk")
        pyautogui.press("enter")
        pyautogui.hotkey("alt", "tab")
    elif entered == "vote":
        pyautogui.hotkey("alt", "tab")
        pyautogui.moveTo(TEXTBAR[0], TEXTBAR[1])
        pyautogui.click()
        pyautogui.write("$rolls")
        pyautogui.press("enter")
        time.sleep(1.5)
        pyautogui.moveTo(LINK[0], LINK[1])
        pyautogui.click()
        pyautogui.moveTo(FIREFOX[0], FIREFOX[1])
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(VOTEBUTTON[0], VOTEBUTTON[1])
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(CONFIRM[0], CONFIRM[1])
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(FINALVOTE[0], FINALVOTE[1])
        pyautogui.click()
        



