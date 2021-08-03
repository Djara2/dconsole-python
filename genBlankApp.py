import pyautogui
import time
import pyperclip
import os
header = input("What is the header title of this program?: ")
progName = input("What should the name of this file be?: ")
buildString = "import os\nquitKeywords = [\"exit\", \"quit\", \"ex\", \"eit\", \"eixt\"]\nos.system(\"clear\")\nfrom rich.console import Console\nfrom rich.markdown import Markdown\nfrom rich.table import Table\nconsole = Console()\nMD_TITLE = Markdown(\"# {}\")\ndef defaultDisplay():\n\tos.system(\"clear\")\n\tconsole.print(MD_TITLE)\n\t\n\ndef logic(entered, enteredList):\n\tif entered in quitKeywords:\n\t\texit()\n\nwhile True:\n\tpass".format(header)
copy = input("Does your system work with pyperclip? ")
if copy == "y":
    pyperclip.copy(buildString)
else:
    print("Copy this text in case pyautogui fails to work correctly")
    print("\n{}\n".format(buildString))
gui = input("Does your system work with pyautogui? ")
if gui == "y" or gui == "yes":
    time.sleep(1)
    pyautogui.hotkey("ctrl", "alt", "t")
    time.sleep(2)
    pyautogui.write("cd dconsole-python")
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.write(("vim {}.py".format(progName)))
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("i")
    time.sleep(0.5)
    if copy == "y" or copy == "yes":
        pyautogui.hotkey("ctrl", "shift", "v")
    else:
        pyautogui.write(buildString)
    time.sleep(0.5)
    pyautogui.press("esc")
    time.sleep(0.5)
    pyautogui.write(":wq")
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.hotkey("alt", "f4")
    print("{}.py created and written to".format(progName))
stop = input("Hit ENTER to proceed and terminate this program.")
