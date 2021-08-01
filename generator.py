import os
quitKeywords = ["exit", "quit", "ex", "eit", "eixt"]
os.system("clear")
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
MD_TITLE = Markdown("# Generator")

def defaultDisplay():
    os.system("clear")
    console.print(MD_TITLE)

def logic(entered, enteredList):
    buildString = ""
    if entered in quitKeywords:
        exit()
    elif enteredList[0] == "list":
        if len(enteredList) == 1:
            pass #walk user through
        elif len(enteredList) == 2:
            boundary = int(enteredList[1])
            for x in range(1, boundary+1):
                buildString += "{}. \n".format(x)
            print("Output: \n{}".format(buildString))
            paste = input("\nCopy result? [y/n] ")
            if paste == "y":
                pyperclip.copy(buildString)
                print("\nCopied!\n")
            else:
                print("\n\n")
        elif len(enteredList) > 2:
            boundary = int(enteredList[1])
            args = []
            showZeros = False
            greatestLen = len(str(boundary))
            for x in range(1, len(enteredList)):
                args.append(enteredList[x])
            if "-0" in args:
                showZeros = True
            singleString = ""
            for x in range(1, boundary+1):
                if showZeros:
                    if len(str(x)) != greatestLen:
                        zerosToShow = greatestLen-len(str(x))
                        zeros = "0"*zerosToShow
                        singleString = "{}{}. \n".format(zeros, x)
                buildString += singleString
            print("Output: \n{}\n".format(buildString))
            paste = input("\nCopy result? [y/n] ")
            if paste == "y":
                pyperclip.copy(buildString)
                print("\nCopied!\n")
            else:
                print("\n\n")

while True:
    defaultDisplay()
    entered = input("% ")
    if " " in entered:
        enteredList = entered.split()
    else:
        enteredList = [entered]
    logic(entered, enteredList)
    stop = input("Press ENTER to continue ")

