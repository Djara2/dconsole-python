import pyautogui
import os
from tkinter import *
import time
root = Tk()
import tkinter.font as font
root.configure(bg = "#333333")
standardFont = font.Font(family="Ubuntu", size=16)
buttonbg = "#474747"
activebg =  "#dd4814"
listLabel = Label(root, text="Recorded Coordinates")
listbox = Listbox(root)
def run():
    x = 1
    while True:
        x, y = pyautogui.position()
        listbox.insert(x, "x, y: {}, {}".format(x, y))
        x+=1
        time.sleep(0.3)
def quit():
    exit()

startButton = Button(root, bg = buttonbg, fg = "white", activebackground = activebg, activeforeground = "white", text = "start", command = run)
startButton['font'] = standardFont
quitButton = Button(root, bg = "red", fg = "white", activebackground = activebg, activeforeground = "white", text = "quit", command = quit)
quitButton ['font'] = standardFont
root.geometry("400x600")
root.title("Mouse GUI")
listLabel.grid(row=0, column = 0)
listbox.grid(row=0, column=1)
startButton.grid(row=1, column=0, columnspan=2)
quitButton.grid(row=2, column=0, columnspan=2)
root.mainloop()

