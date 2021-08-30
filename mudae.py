import os
import time
import pyautogui
from rich.console import Console
from rich.markdown import Markdown
import dtools
console = Console()
mode = input("Mode: ")
TEXTBAR = [730, 1023, 810, 1154, 782, 960, 858, 1896]
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
DURATION = 0.3
if mode.lower() == "lm" or mode.lower() == "lmvm":
    DURATION = 0.6
console.print(MD_TITLE)
entered = ""
enteredList = []
def wait():
    global DURATION
    time.sleep(DURATION)

def focusChatbar():
    global mode
    if mode == "zorin 200":
        wait()
        pyautogui.moveTo(TEXTBAR[4], TEXTBAR[5])
        wait()
        pyautogui.click()
    elif mode.lower() == "lmvm" or mode.lower() == "lm":
        wait()
        pyautogui.moveTo(TEXTBAR[6], TEXTBAR[7])
        wait()
        pyautogui.click()
    else:
        wait()
        pyautogui.moveTo(TEXTBAR[0], TEXTBAR[1])
        wait()
        pyautogui.click()
    wait()

def writeEnter(thing):
    wait()
    pyautogui.write(thing)
    wait()
    pyautogui.press("enter")
    wait()

def goToMarry():
    wait()
    pyautogui.hotkey("ctrl", "k")
    wait()
    pyautogui.write("psycho")
    wait()
    pyautogui.press("enter")
    wait()

def altTab():
    wait()
    pyautogui.hotkey("alt", "tab")
    wait()

def daily():
    altTab()
    goToMarry()
    focusChatbar()
    writeEnter("$daily")
    writeEnter("$rolls")
    wait()
    altTab()

def nav():
    altTab()
    goToMarry()

while True:
    entered = input("Command: ")
    enteredList = entered.split()
    if entered == "quit" or entered == "exit":
        exit()
    elif entered == "b" or entered == "start":
        if mode != "lmvm" and mode != "lm":
            altTab()
        else:
            print("5 seconds to switch to Discord")
            time.sleep(5)
        goToMarry()
        focusChatbar()
        for x in range(1, 15):
            pyautogui.write("$w")
            pyautogui.press("enter")
            time.sleep(1.5)
        pyautogui.write("$tu")
        pyautogui.press("enter")
    elif entered == "daily" or entered == "rolls" or entered == "dr":
        daily()

    elif entered == "d" or entered == "dk":
        if mode != "lm" and mode != "lmvm":
            pyautogui.hotkey("alt", "tab")
        else:
            print("5 seconds to switch to channel")
            time.sleep(5)
        goToMarry()
        focusChatbar()
        pyautogui.write("$dk")
        pyautogui.press("enter")
        pyautogui.hotkey("alt", "tab")
    elif entered == "tu" or entered == "t":
        if mode != "lm" and mode != "lmvm":
            pyautogui.hotkey("alt", "tab")
        else:
            print("5 seconds to switch to Discord")
            time.sleep(5)
        goToMarry()
        focusChatbar()
        pyautogui.write("$tu")
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.hotkey("alt", "tab")
    elif entered == "nav":
        altTab()
        goToMarry()

    elif entered == "at":
        altTab()

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

