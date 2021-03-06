import os
import sys
import time
if len(sys.argv) == 1:
    import pyautogui
else:
    if sys.argv[1] == "mobile":
        input("Pyautogui will not be imported ")
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
TITLE = "# dconsole"
mdTITLE = Markdown(TITLE)
from dnum import *
from colors import *
from dbin import *
import dtools
import pyclip
header = "version 1 . 88"
header2 = "last updated: 09/10/2021" # TIME STAMP
os.system("clear")
console = Console() #from rich library
stoptext = "Hit ENTER to continue "
knowncmd = dtools.knownCommandsList
externalPrograms = dtools.externalProgramsList
externalPrograms.sort()
history = []
numbers = []
binaries = []
new = dnum(1, 1, 1)

def defaultDisplay():
    global console, mdTITLE
    os.system("clear")
    console.print(mdTITLE)
    print(header)
    print(header2+"\n")
    console.print("Type [bold green]\"help\"[/] for options\n")

def logic(enteredList):
    global knowncmd, history, numbers, binaries, stoptext, new, header, externalPrograms, entered
    print()
    
    if enteredList[0].lower() in externalPrograms:
        cmd = "python3 {}.py".format(enteredList[0])
        try:
            os.system(cmd)
        except:
            dtools.errorMessage("no such program.")
        print()
        stop = input(stoptext)
    
    if not enteredList[0] in knowncmd and not enteredList[0] in externalPrograms:
        print("Command unrecognized. Type \"help\" for commands")
        stop = input("Hit ENTER to continue ")
        defaultDisplay()
    
    if enteredList[0] == "quit" or enteredList[0] == "exit":
        exit()

    elif entered == "help":
        os.system("python3 neohelp.py")
    elif enteredList[0] == "wordcount" or enteredList[0] == "wc":
        thing = input("String to count: ")
        count = dtools.wordCount(thing)
        console.print("[bold green]Word count:[/] {} [{} unique words]".format(count, len(dtools.getUniqueWords(thing.split()))))
        reprint = input("Show word numbers? ")
        if reprint == "y":
            thingList = thing.split()
            for x in range(0, len(thingList)):
                thingList[x] = "({}){}".format(x+1, thingList[x])
            buildString = ""
            for x in range(0, len(thingList)):
                if x != len(thingList)-1:
                    buildString += "{} ".format(thingList[x])
                else:
                    buildString += thingList[x]
            console.print("[bold green]With word numbers:[/] {}".format(buildString))
        stop = input(stoptext)
    
    elif enteredList[0] == "speedtest":
        os.system("./speedtest.sh")
        stop = input(stoptext)
    
    elif enteredList[0] == "commands":
        listOfLists = dtools.generateListOfListsByLetter(knowncmd)
        dtools.iteratePrintList(listOfLists, "alphabet")
        stop = input(stoptext)
    
    elif enteredList[0] == "w3m":
        if enteredList[1] == "e":
            # parameter for exact link
            os.system("w3m {}".format(enteredList[2]))
        else:
            buildString = "w3m https://www.bing.com/search?q="
            for x in range(1, len(enteredList)):
                buildString+="{}+".format(enteredList[x])
            os.system("w3m {}".format(buildString))
        stop = input(stoptext)
    
    elif enteredList[0] == "vim":
        if len(enteredList) == 1:
            console.print("[bold cyan]Frequently used:[/] 7. dtools")
            dtools.iteratePrintList(externalPrograms, "num1")
            console.print("[bold cyan]Enter \"none\" or leave blank to rollback[/]")
            argument = input("Edit which file?: ")
            if argument == "none" or argument == "":
                print("Exiting selection process.")
            else:
                os.system("vim {}.py".format(externalPrograms[int(argument)-1]))
        else:
            argument = enteredList[1]
            os.system("vim {}.py".format(externalPrograms[int(argument)-1]))
        stop = input(stoptext)
    
    elif enteredList[0] == "programs":
        dtools.iteratePrintList(externalPrograms, "num1")
        stop = input("\n"+stoptext)
    
    elif enteredList[0] == "len":
        print()
        print("The length of \"{}\" is {} characters".format(entered[4:], len(entered[4:])))
        print()
        stop = input(stoptext)

    elif enteredList[0] == "history" or enteredList[0] == "h":
        os.system("clear")
        MD_HISTORY_TITLE = Markdown("# History")
        console.print(MD_HISTORY_TITLE)
        for x in range(0, len(history)):
            print("{}. {}".format(x+1, history[x]))
        print()
        console.print("Use command [green]\"hre #\"[/] to enter an item from history as input")
        print()
        stop = input("Hit ENTER to continue ")

    elif enteredList[0] == "hre":
        index = int(enteredList[1])
        itemToCopy = history[index-1]
        pyclip.copy(itemToCopy)
        print("\"{}\" has been copied to the clipboard. Paste from clipboard or type \"v\" on the input line to automatically paste.".format(itemToCopy))
        stop = input("Hit ENTER to continue ")
    
    elif enteredList[0] == "new":
        if enteredList[1] == "num":
            if len(enteredList) != 3:
                coefficient = float(enteredList[2])
                value = float(enteredList[3])
                exponent = float(enteredList[4])
                if coefficient == value:
                    coefficient = 1
                    exponent += 1
                evaluated = pow(value, exponent)
                if coefficient != 1:
                    evaluated = evaluated * coefficient
                print("Resultant value is {}".format(evaluated))
                new.coefficient = coefficient
                new.value = value
                new.exponent = exponent
                numbers.append(new)
                stop = input(stoptext)
            else:
                print("Created number: {}".format(float(enteredList[2])))
                stop = input(stoptext)
        elif enteredList[1] == "bin":
            pass

    elif enteredList[0] == "numbers":
        os.system("clear")
        figlet("Numbers")
        for x in range(0, len(numbers)):
            bits = numbers[x].evaluate()
            bits = int(bits)
            binary = bin(bits)
            print("{}. {}*{}^{} (#: {}) (b: {})".format(x+1, numbers[x].coefficient, numbers[x].value, numbers[x].exponent, numbers[x].evaluate(), binary))
        print()
        stop = input(stoptext)

    elif enteredList[0] == "v":
        copied = pyclip.paste()
        copiedList = copied.split()
        print("Entered previously copied command: {}".format(copied))
        logic(copiedList)

    elif enteredList[0] == "os" or enteredList[0] == "system":
        if(enteredList[0] == "os"):
            print(GREEN)
            os.system(entered[3:])
            print(CLEAR)
            stop = input(stoptext)
        else:
            print(GREEN)
            os.system(entered[7:])
            print(CLEAR)
            stop = input(stoptext)
    
        

while(True):
    defaultDisplay()
    entered = input("> ")
    if not entered in externalPrograms:
        entered = entered.lower()
    entered = dtools.detectExternalProgramAlias(entered)
    if " " in entered:
        enteredList = entered.split()
    else:
        enteredList = [entered]
    history.append(entered)
    logic(enteredList)
    







    
