import pyautogui
from tkinter import *
import tkinter.font as font
import pyperclip
import os
import time
buttonbg = "#474747"
root = Tk()
standardFont = font.Font(family="Ubuntu", size=16)
root.configure(bg = "#333333")
def switchToDiscord():
    pyautogui.hotkey("win", "5")

def engageTextbar():
    pyautogui.moveTo(730, 1023)
    time.sleep(1)
    pyautogui.click()

def switchToMarryChannel():
    time.sleep(1)
    pyautogui.hotkey("ctrl", "k")
    time.sleep(1)
    pyautogui.write("psycho")
    pyautogui.press("enter")

def dk():
    switchToDiscord()
    time.sleep(1)
    switchToMarryChannel()
    time.sleep(1)
    engageTextbar()
    time.sleep(1)
    pyautogui.write("$dk")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("alt", "tab")

def roll():
    switchToDiscord()
    switchToMarryChannel()
    time.sleep(0.2)
    engageTextbar()
    for x in range(0, 14):
        pyautogui.write("$w")
        pyautogui.press("enter")
        time.sleep(1.2)

def tu():
    switchToDiscord()
    switchToMarryChannel()
    time.sleep(1)
    engageTextbar()
    pyautogui.write("$tu")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.hotkey("alt", "tab")

def stopProgram():
    pyautogui.hotkey("win", "6")
    exit()
root.title("Mudae GUI")
root.geometry("400x600")
tuButton = Button(root, text="$tu", width=200, bg = buttonbg, activebackground = "#dd4814", fg="white", activeforeground="white", command = tu)
quitButton = Button(root, text="quit", width = 200, activebackground = "#800000", activeforeground="white", bg="#5e2750", fg="white", command = stopProgram)
dkButton = Button(root, text="$dk", width=200, bg = buttonbg, fg="white", activebackground="#dd4814", command = dk)
rollsButton = Button(root, text="$w", width=200, bg = buttonbg, fg="white", activebackground = "#dd4814", command = roll)
dkButton['font'] = standardFont
rollsButton['font'] = standardFont
quitButton['font'] = standardFont
tuButton['font'] = standardFont
dkButton.pack()
tuButton.pack()
rollsButton.pack()
quitButton.pack()
root.mainloop()
