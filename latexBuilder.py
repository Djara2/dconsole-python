import os
import dtools
import pyperclip
quitKeywords = ["exit", "quit", "ex", "eit", "eixt"]
os.system("clear")
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
MD_TITLE = Markdown("# Latex Builder")

def defaultDisplay():
    os.system("clear")
    console.print(MD_TITLE)
	

def logic(entered, enteredList):
    buildString = ""
    matrixType = "bmatrix"
    if entered in quitKeywords:
        exit()
    elif entered == "matrix":
        brackets = input("Should this matrix have brackets?: ")
        if brackets != "y":
            matrixType = "matrix"
        variableName = "!NONE"
        variable = input("Should this matrix be assigned to a variable? ")
        if variable == "y":
            variableName = input("What is the name of the variable?: ")
            if "vec" in variableName:
                variableNameList = variableName.split()
                variableName = "\\vec{"
                variableName += "{}".format(variableNameList[1])
                variableName += "}"
        continueBuild = "y"
        rows = [] #each list within this will be a row. Index 0 is row 1. Index 1 is row 2.. etc.
            # likewise, each index in the list within the bigger list corresponds to a column. 
        count = 1
        console.print("[bold cyan]Separate column contents with a space![/]")
        console.print("[bold cyan]Enter \"done\" for row contents when finished[/]")
        while continueBuild == "y":
            preliminaryString = ""
            buildRow = []
            preliminaryString = input("Enter row contents (row {}): ".format(count))
            if not preliminaryString == "done":
                if " " in preliminaryString:
                    rows.append(preliminaryString.split())
                else:
                    singleItemList = [preliminaryString]
                    rows.append(singleItemList)
                count+=1
                rows.append(buildRow)
            else:
                continueBuild = "n"
        # DEBUG START!
        print("Primitive rows")
        dtools.iteratePrintList(rows, "num")
        # DEBUG END!
        if variable == "y":
            buildString += "${}=\\begin".format(variableName)
            buildString += "{"
        else:
            buildString += "$\\begin{"
        buildString += matrixType
        buildString += "}"
        for x in range(0, len(rows)):
            for y in range(0, len(rows[x])):
                if y != (len(rows[x])-1):
                    buildString += "{} & ".format(rows[x][y])
                else:
                    buildString += "{}".format(rows[x][y])
                    buildString += "\\\\"
        buildString += "\\end{"
        buildString += matrixType
        buildString += "}$"
        useClipboard = input("Does your system work with pyperclip?: ")
        if useClipboard == "y":
            pyperclip.copy(buildString)
        printBuild = input("Print result to console?: ")
        if printBuild == "y":
            print(buildString)

while True:
    defaultDisplay()
    entered = input("What kind of LaTex entity are you trying to build? ")
    enteredList = []
    logic(entered, enteredList)
    stop = input("Hit ENTER to continue ")
