import os
quitKeywords = ["exit", "quit", "ex", "eit", "eixt"]
os.system("clear")
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
MD_TITLE = Markdown("# Markdown Editor")

def defaultDisplay():
    os.system("clear")
    console.print(MD_TITLE)
	

def logic(entered, enteredList):
    if entered in quitKeywords:
        exit()

while True:
    defaultDisplay()
    entered = input("")
    enteredList = entered.split()
    logic(entered, enteredList)
    stop = input("Hit ENTER to continue ")
