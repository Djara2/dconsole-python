import os
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
TITLE = "# dconsole"
mdTITLE = Markdown(TITLE)
from dnum import *
from colors import *
from dbin import *
import dtools
import pyperclip
header = "version 1 . 82"
header2 = "last updated: 08/03/2021" # TIME STAMP
os.system("clear")
console = Console() #from rich library
stoptext = "Hit ENTER to continue "
knowncmd = dtools.knownCommandsList
externalPrograms = dtools.externalProgramsList
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
    print("Type \"help\" for options\n")

def logic(enteredList):
    global knowncmd, history, numbers, binaries, stoptext, new, header, externalPrograms, entered
    print()
    if enteredList[0] in externalPrograms:
        cmd = "python3 {}.py".format(enteredList[0])
        os.system(cmd)
        print()
        stop = input(stoptext)
    if not enteredList[0] in knowncmd and not enteredList[0] in externalPrograms:
        print("Command unrecognized. Type \"help\" for commands")
        stop = input("Hit ENTER to continue ")
        defaultDisplay()
    if enteredList[0] == "quit" or enteredList[0] == "exit":
        exit()
    elif enteredList[0] == "speedtest":
        os.system("./speedtest.sh")
        stop = input(stoptext)
    elif enteredList[0] == "commands":
        alphabetizedList = knowncmd.sort()
        for x in range(0, len(knowncmd)):
            print("{}. {}".format(x, known[x]))
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
    elif enteredList[0] == "programs":
        for x in range(0, len(externalPrograms)):
            print("{}. {}".format(x+1, externalPrograms[x]))
        stop = input("\n"+stoptext)
    elif enteredList[0] == "len":
        print()
        print("The length of \"{}\" is {} characters".format(entered[4:], len(entered[4:])))
        print()
        stop = input(stoptext)
    elif enteredList[0] == "translate":
        src1 = enteredList[1]
        dest1 = enteredList[2]
        start = (len(src1)-1)+(len(dest1)-1)+1
        content = entered[start:]
        translator.translate(content, src=src1, dest=dest1)
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
        pyperclip.copy(itemToCopy)
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
        copied = pyperclip.paste()
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
    if entered == "calc":
        entered = "calculator"
    enteredList = entered.split()
    history.append(entered)
    logic(enteredList)
    







    
