import os
quitKeywords = ["exit", "quit", "ex", "eit", "eixt"]
os.system("clear")
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
import pyclip
import dtools
console = Console()
MD_TITLE = Markdown("# Markdown Writer")
def defaultDisplay():
    os.system("clear")
    console.print(MD_TITLE)
    console.print("Type [bold green]help[/] for options\n")
def result_statement(text):
    console.print("\n[bold green]Result:[/] {}".format(text))
    console.print("\n\"{}\" has been copied to the clipboard!\n".format(text))
def logic(entered, enteredList):
    buildString = ""
    if entered in quitKeywords:
        exit()
    elif entered == "add color" or entered == "color" or entered == "ac":
        color = input("Which color?: ")
        text = input("Text to be stylized: ")
        if color == "green":
            color = "#8eb398"
        if color == "red":
            color = "#cd3333"
        buildString = "<span style = \"color: {}\">{}</span>".format(color, text)
        makeBold = input("Make bold?: ")
        if makeBold == "y":
            buildString = dtools.addToFront("**", buildString)
            buildString += "**"
        console.print("\n[bold green]Result:[/] {}".format(buildString))
        wsl = input("Are you on WSL?: ")
        if wsl == "n":
            pyclip.copy(buildString)
        else:
            dtools.wslCopy(buildString)
        console.print("\nResult has been copied to clipboard!")
    
    elif entered == "notice" or entered == "note":
        buildString = "**<span style=\"background-color: yellow; color: black\">{}:</span> ".format(entered)
        buildString += input("{}: ")
        wsl = input("Are you on WSL?: ")
        if wsl != "y":
            pyclip.copy(buildString)
        else:
            dtools.wslCopy(buildString)

    elif entered == "citation":
        buildString = "**<span style=\"color: yellow\">Citation:</span>** "
        if len(enteredList) == 1:
            wsl = input("Are you on WSL?: ")
            if wsl != "y":
                pyclip.copy(buildString)
            else:
                dtools.wslCopy(buildString)
        else:
            if enteredList[1] == "wsl":
                dtools.wslCopy(buildString)
        result_statement(buildString)
    elif entered == "table of contents" or entered == "toc" or entered == "contents":
        buildString = "${toc}"
        if "wsl" in enteredList:
            dtools.wslCopy(buildString)
        else:
            wsl = input("Are you on WSL?: ")
            if wsl != "y":
                pyclip.copy(buildString)
            else:
                dtools.wslCopy(buildString)
        result_statement(buildString)
    elif entered == "highlight":
        color = input("Which color?: ")
        if color == "green":
            color = "#7e9f87"
        elif color == "red":
            color = "#cd3333" 
        text = input("Text to be stylized?: ")
        if color != "yellow":
            buildString = "<span style=\"background-color: {}\">{}</span>".format(color, text)
        else:
            buildString = "<span style=\"background-color: yellow; color: black\">{}</span>".format(text)
        makeBold = input("Make bold?: ")
        if makeBold == "y":
            buildString = dtools.addToFront("**", buildString)
            buildString += "**"
        console.print("\n[bold green]Result:[/] {}".format(buildString))
        wsl = input("Are you on WSL?: ")
        if wsl == "n":
            pyclip.copy(buildString)
        else:
            dtools.wslCopy(buildString)
        console.print("\nResult has been copied to clipboard!")
    elif entered == "help":
        dtools.clear()
        console.print(Markdown("# Options\n* ***Add color:*** wraps text in HTML span tag so that you can have markdown with color.\n* ***Table:*** see htmlBuilder"))
    else:
        dtools.errorMessage("Invalid option")
while True:
    defaultDisplay()
    entered = input("> ")
    enteredList = entered.split()
    logic(entered, enteredList)
    stop = input("\nHit ENTER to continue ")
