import os
import tkinter
import pyautogui
entities = ["Matrix", "Vec", "Reg"]
root = Tk()
assignedToAVariable = IntVar()
shaveDollarSigns = IntVar()
root.title("LaTex Builder GUI")
entityTypeLabel = Label(root, text="Entity Type")
entityOptions = Listbox(root)
for x in range(0, len(entities)):
    entityOptions.insert(x+1, entities[x])
variableCheckBox = Checkbutton(root, text="Assign to a variable",
        variable = assignedToAVariable,
        onvalue = 1,
        offvalue = 0
        height = 2,
        width = 10)
dollarSignsCheckbox = Checkbutton(root, text="Shave off $s",
        variable = shaveDollarSigns,
        onvalue = 1,
        offvalue = 0,
        height = 2,
        width = 10)
goButton = Button(root, text="Generate")
