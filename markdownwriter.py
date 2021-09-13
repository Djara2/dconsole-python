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
    PARAMETERS = ["-b", "-r", "-l", "-wsl", "-w"]
    tempLen = len(PARAMETERS)
    for x in range(0, tempLen):
        PARAMETERS.append("-{}".format(PARAMETERS[x][1:len(PARAMETERS)-1].upper())) 
    buildString = ""
    if entered in quitKeywords:
        exit()
    elif entered == "add color" or enteredList[0] == "color" or enteredList[0] == "ac":
        if not len(enteredList) > 1:
            color = input("Which color?: ")
        else:
            color = enteredList[1]
        if (enteredList[0] == "ac" and len(enteredList) > 2) or (enteredList[0] == "color" and len(enteredList) > 2):
            text = ""
            for x in range(2, len(enteredList)):
                if enteredList[x] != "-l" and enteredList[x] != "-wsl" and enteredList[x] != "-b" and enteredList[x] != "-r":
                    text += "{}".format(enteredList[x])
                    if x != len(enteredList)-1:
                        text += " "
        else:
            text = input("Text to be stylized: ")
        if color == "green" or color == "g":
            color = "#8eb398"
        elif color == "red" or color == "r":
            color = "#cd3333"
        elif color == "y":
            color = "yellow"
        elif color == "c":
            color = "cyan"
        elif color == "o" or color == "orange":
            color = "#ff7f24"
        elif color == "op" or color == "peach":
            color = "#ff7f50"
        if text[len(text)-1] == " ":
            text = text[0:len(text)-1]
        buildString = "<span style = \"color: {}\">{}</span>".format(color, text)
        if not "-b" in entered:
            if not "-r" in entered:
                makeBold = input("Make bold?: ")
            else:
                makeBold = "n"
        else:
            makeBold = "y"
        if makeBold == "y":
            buildString = dtools.addToFront("**", buildString)
            buildString += "**"
        console.print("\n[bold green]Result:[/] {}".format(buildString))
        if not "-wsl" in entered and not "-w" in entered:
            if not "-l" in entered:
                wsl = input("Are you on WSL?: ")
            else:
                wsl = "n"
        else:
            wsl = "y"
        if wsl == "n":
            pyclip.copy(buildString)
        else:
            dtools.wslCopy(buildString)
        console.print("\nResult has been copied to clipboard!")
    
    elif enteredList[0].lower() == "notice" or enteredList[0].lower() == "note":
        buildString = "**<span style=\"background-color: yellow; color: black\">{}:</span> ".format(enteredList[0])
        if len(enteredList) < 2:
            buildString += input("{}: ")
        else:
            for x in range(1, len(enteredList)):
                buildString += "{}".format(enteredList[x])
                if x != len(enteredList)-1:
                    buildString += " "
        if not "-wsl" in entered and not "-w" in entered:
            if not "-l" in entered:
                wsl = input("Are you on WSL?: ")
            else:
                wsl = "n"
        else:
            wsl = "y"
        if wsl != "y":
            pyclip.copy(buildString)
        else:
            dtools.wslCopy(buildString)

    elif entered == "citation":
        buildString = "**<span style=\"color: yellow\">Citation:</span>** "
        if not "-wsl" in entered:
            if not "-l" in entered:
                wsl = input("Are you on WSL?: ")
            else:
                wsl = "n"
        else:
            wsl = "y"
        if wsl != "y":
            pyclip.copy(buildString)
        else:
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
    elif enteredList[0] == "highlight" or enteredList[0] == "hl":
        if len(enteredList) == 1:
            color = input("Which color?: ")
        else:
            color = enteredList[1]
        if color == "green" or color == "g":
            color = "#7e9f87"
        elif color == "red" or color == "r":
            color = "#cd3333" 
        elif color == "y":
            color = "yellow"
        elif color == "c":
            color = "cyan"
        elif color == "o":
            color = "#ff7f24"
        elif color == "op" or color == "peach":
            color = "#ff7f50"
        if len(enteredList) < 2:
            text = input("Text to be stylized?: ")
        else:
            text = ""
            for x in range(2, len(enteredList)):
                if enteredList[x] != "-l" and enteredList[x] != "-wsl" and enteredList[x] != "-r" and enteredList[x] != "-b":
                    text += "{}".format(enteredList[x])
                    if x != len(enteredList)-1:
                        text += " "
        if color != "yellow":
            buildString = "<span style=\"background-color: {}\">{}</span>".format(color, text)
        else:
            buildString = "<span style=\"background-color: yellow; color: black\">{}</span>".format(text)
        if not "-b" in entered:
            if not "-r" in entered:
                makeBold = input("Make bold?: ")
            else:
                makeBold = "n"
        else:
            makeBold = "y"
        if makeBold == "y":
            buildString = dtools.addToFront("**", buildString)
            buildString += "**"
        console.print("\n[bold green]Result:[/] {}".format(buildString))
        if not "-wsl" in entered:
            if not "-l" in entered:
                wsl = input("Are you on WSL?: ")
            else:
                wsl = "n"
        else:
            wsl = "y"
        if wsl == "n":
            pyclip.copy(buildString)
        else:
            dtools.wslCopy(buildString)
        console.print("\nResult has been copied to clipboard!")
    elif entered == "help":
        dtools.clear()
        console.print(Markdown("# Options\n* ***Add color:*** wraps text in HTML span tag so that you can have markdown with color.\n\t* Aliases: color, ac\n\n* ***Table:*** see htmlBuilder\n\n* **Highlight:** highlights the text you give it in a particular color that you specify.\n\t* Aliases: hl\n\n* **Citation:** copies the text \"citation:\" with bold weight and yellow color.\n\n* **Note:** copies \"Note:\" to the clipboard with bold weight and yellow color. If you give text after the command keyword then that will be inserted as well."))
    else:
        dtools.errorMessage("Invalid option")
while True:
    defaultDisplay()
    entered = input("> ")
    enteredList = entered.split()
    logic(entered, enteredList)
    stop = input("\nHit ENTER to continue ")
