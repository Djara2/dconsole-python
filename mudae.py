import os
import time
import pyautogui
from rich.console import Console
from rich.markdown import Markdown
import dtools
console = Console()
mode = input("Mode: ")
TEXTBAR = [730, 1023, 810, 1154, 782, 960]
# for TEXTBAR, indices 0 and 1 are for the HP laptop and 2 and 3 are for the virtual machine. 4 and 5 are for the zorin VM on scale mode set to 200%
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
def focusChatbar():
    global mode
    if mode == "zorin 200":
        time.sleep(0.3)
        pyautogui.moveTo(TEXTBAR[4], TEXTBAR[5])
        time.sleep(0.3)
        pyautogui.click()
    else:
        time.sleep(0.3)
        pyautogui.moveTo(TEXTBAR[0], TEXTBAR[1])
        time.sleep(0.3)
        pyautogui.click()
    time.sleep(0.3)

def goToMarry():
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "k")
    time.sleep(0.3)
    pyautogui.write("psycho")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(0.3)

while True:
    entered = input("Command: ")
    enteredList = entered.split()
    if entered == "quit" or entered == "exit":
        exit()
    elif entered == "dk":
        pyautogui.hotkey("alt", "tab")
        goToMarry()
        focusChatbar()
        pyautogui.write("$dk")
        pyautogui.press("enter")
        time.sleep(0.3)
        pyautogui.hotkey("alt", "tab")
    elif entered == "b" or entered == "start":
        pyautogui.hotkey("alt", "tab")
        goToMarry()
        focusChatbar()
        for x in range(1, 15):
            pyautogui.write("$w")
            pyautogui.press("enter")
            time.sleep(1.5)
        pyautogui.write("$tu")
        pyautogui.press("enter")
    elif entered == "d" or entered == "dk":
        pyautogui.hotkey("alt", "tab")
        goToMarry()
        focusChatbar()
        pyautogui.write("$dk")
        pyautogui.press("enter")
        pyautogui.hotkey("alt", "tab")
    elif entered == "tu" or entered == "t":
        pyautogui.hotkey("alt", "tab")
        goToMarry()
        focusChatbar()
        pyautogui.write("$tu")
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.hotkey("alt", "tab")
    elif entered == "nav":
        pyautogui.hotkey("win", "4")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "k")
        time.sleep(0.5)
        pyautogui.write("psycho")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        dtools.engageTextbar()
        time.sleep(0.5)
        pyautogui.hotkey("alt", "tab")
        pyautogui
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

