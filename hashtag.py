import os
quitKeywords = ["exit", "quit", "ex", "eit", "eixt"]
os.system("clear")
import pyclip
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
MD_TITLE = Markdown("# Hashtag")
def defaultDisplay():
    os.system("clear")
    console.print(MD_TITLE)
	
def logic(entered, enteredList):
    if entered in quitKeywords:
        exit()
    else:
        newList = []
        for x in range(0, len(enteredList)):
            newList.append("#{}".format(enteredList[x]))
        newString = ""
        for x in range(0, len(newList)):
            if x != len(newList)-1:
                newString += "{} ".format(newList[x])
            else:
                newString += "{}".format(newList[x])
        console.print("[bold green]Result:[/] {}".format(newString))
        systemMode = input("Are you on WSL?: ")
        if systemMode == "y":
            dtools.wslCopy(newString)
        else:
            pyclip.copy(newString)
        print("Result has been copied to clipboard.")

while True:
    defaultDisplay()
    entered = input("> ")
    enteredList = entered.split()
    logic(entered, enteredList)
    stop = input("Hit ENTER to continue ")
