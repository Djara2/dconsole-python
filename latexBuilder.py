import os
import dtools
import pyperclip
quitKeywords = ["exit", "quit", "ex", "eit", "eixt"]
os.system("clear")
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
MD_TITLE = Markdown("# LaTex Auto Generator")

def defaultDisplay():
    os.system("clear")
    console.print(MD_TITLE)
	

def logic(entered, enteredList):
    latexEntities = ["sqrt", "frac"]
    specialChars = ["<=", "=>", "!<", "!>", "!<=", "!=>", "notmem", "notmember", "notequal", "neq", "notin", "notlessthan", "notless", "nless", "leq", "geq", "notgreater" , "notgreaterthan", "about", "approx", "abt", "plusorminus", "porm", "pm", "subset", "sub", "natural", "real", "ints", "dd", "oo", "aa", "rr", "ll" "delta", "rightarrow", "leftarrow", "alpha", "omega", "vec", "member", "in", "mem", "!=", "nsubset", "notsubset", "nsub", "notsub", "!sub", ]
    buildString = ""
    matrixType = "bmatrix"
    if entered in quitKeywords:
        exit()

    elif entered == "reg" or entered == "general":
        console.print("[bold cyan]Special characters like \\ will be added automatically. You can just type \"delta\" for example as opposed to \"\\delta\".")
        expression = input("Type your expression: ")
        expressionList = expression.split()
        expressionList = dtools.handleSpecialChars(expressionList, specialChars)
        buildString = "$"
        for x in range(0, len(expressionList)):
            buildString += "{} ".format(expressionList[x])
        buildString += "$"
        usePyperclip = input("Does your system work with Pyperclip?: ")
        if usePyperclip == "y":
            pyperclip.copy(buildString)
        print()
        printOutput = input("Print result to console?: ")
        if printOutput == "y":
            print()
            console.print("[bold yellow]RESULT:[/][bold cyan] {}[/]".format(buildString))
        print()


    elif entered == "frac":
        numerator = []
        denominator = []
        buildingNumerator = "y"
        buildingDenominator = "y"
        count = 1
        buildString = "$\\frac{"
        print()
        console.print("! [bold cyan]You can add a bunch of items in a single input line, [/][bold italic yellow]however, if you are trying to add a LaTex entity (i.e. a fraction), then hit RETURN and do it on a new input line.[/]")
        print()
        dtools.betterPrint("[bold red]! An exception to this is simple entities like theta and omega, which can be entered without starting a new input line or escape characters.[/]", "t1")
        print()
        while buildingNumerator == "y":
            item = input("What do you want to add?: ")
            if item != "done":
                usingEntity = False
                for x in range(0, len(latexEntities)):
                    if latexEntities[x] in item:
                        usingEntity = True
                        entityFound = latexEntities[x]
                        break
                if usingEntity == False:
                    if " " in item:
                        itemList = item.split()
                    else:
                        itemList = [item]
                    itemList = dtools.handleSpecialChars(itemList, specialChars)
                else:
                    if entityFound == "frac":
                        print()
                        console.print("[bold cyan]Use formatting [italic yellow]numerator_contents -- denominator_contents[/] on the next input line. You cannot add another fraction from here without using LaTex formatting. You do not have to use LaTex for simple entities, though.[/]")
                        print()
                        secondaryFrac = input("> ")
                        secondaryFracList = secondaryFrac.split()
                        secondaryFracList = dtools.handleSpecialChars(secondaryFracList, specialChars)
                        endNumeratorPoint = dtools.whereIs("--", secondaryFracList)
                        fracString = "\\frac{"
                        for x in range(0, endNumeratorPoint):
                            fracString += secondaryFracList[x]
                        fracString += "}{"
                        for x in range(endNumeratorPoint+1, len(secondaryFracList)):
                            fracString += secondaryFracList[x]
                        fracString+="}"
                        itemList = [fracString]
                numerator.append(itemList)
            else:
                buildingNumerator = "n"
        print()
        console.print("[bold cyan]Now working on denominator[/]")
        print()
        while buildingDenominator == "y":
            item = input("What do you want to add?: ")
            if item != "done":
                usingEntity = False
                for x in range(0, len(latexEntities)):
                    if latexEntities[x] in item:
                        usingEntity = True
                        entityFound = latexEntities[x]
                        break
                if usingEntity == False:
                    if " " in item:
                        itemList = item.split()
                    else:
                        itemList = [item]
                    itemList = dtools.handleSpecialChars(itemList, specialChars)
                else:
                    if entityFound == "frac":
                        print()
                        console.print("[bold cyan]Use formatting [italic yellow]numerator_contents -- denominator_contents[/] on the next input line. You cannot add another fraction from here without using LaTex formatting. You do not have to use LaTex for simple entities, though.[/]")
                        print()
                        secondaryFrac = input("> ")
                        secondaryFracList = secondaryFrac.split()
                        secondaryFracList = dtools.handleSpecialChars(secondaryFracList, specialChars)
                        endNumeratorPoint = dtools.whereIs("--", secondaryFracList)
                        fracString = "\\frac{"
                        for x in range(0, endNumeratorPoint):
                            fracString += secondaryFracList[x]
                        fracString += "}{"
                        for x in range(endNumeratorPoint+1, len(secondaryFracList)):
                            fracString += secondaryFracList[x]
                        fracString+="}"
                        itemList = [fracString]
                        print()
                denominator.append(itemList)
            else:
                buildingDenominator = "n"
        print()
        for x in range(0, len(numerator)):
            for y in range(0, len(numerator[x])):
                buildString += numerator[x][y]
                buildString += " "
        buildString += "}{"
        for x in range(0, len(denominator)):
            for y in range(0, len(denominator[x])):
                buildString += denominator[x][y]
                buildString += " "
        buildString += "}$"
        usePyperclip = input("Does your system work with Pyperclip?: ")
        if usePyperclip == "y":
            pyperclip.copy(buildString)
        print()
        printOutput = input("Print result to console?: ")
        if printOutput == "y":
            print()
            console.print("[bold yellow]RESULT:[/][bold cyan] {}[/]".format(buildString))
        print()




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
