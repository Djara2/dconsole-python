import os
import math
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from colors import *
os.system("clear")
Functions = Table(title="Functions")
Functions.add_column("Normal")
Functions.add_column("Special")
Functions.add_row("add", "area")
Functions.add_row("sub", "surfacearea")
Functions.add_row("mult", "volume")
Functions.add_row("div", "discount")
Functions.add_row("sqrt", "tip")
Functions.add_row("pow", "-")
################
historyTable = Table(title="History")
historyTable.add_column("Index")
historyTable.add_column("User Input")
historyTable.add_column("Output")
################
MD_TITLE = Markdown("# Calculator")
MD_TITLE_HISTORY = Markdown("# History")
history = []
twoDimensionalShapes = ["square", "rectangle", "circle", "triangle"]
threeDimensionalShapes = ["sphere", "cylinder", "cube", "cuboid", "pyramid"]
console = Console()
inputHistory = []
outputHistory = []
externalPrograms = ["discount", "tip"]
knowncmd = ["area", "volume", "surfacearea", "quit", "exit", "add", "sub", "mult", "div", "sqrt", "pow", "mod", "history"]

for x in range(0, len(externalPrograms)):
    knowncmd.append(externalPrograms[x])

def figlet(text):
    os.system("figlet {}".format(text))

def endof(userlist):
    end = len(userlist)-1
    return(end)

def update_historyTable():
    global history, outputHistory, historyTable
    index = len(history)
    index = str(index)
    h_annex = history[len(history)-1]
    o_annex = outputHistory[len(outputHistory)-1]
    h_annex = str(h_annex)
    o_annex = str(o_annex)
    historyTable.add_row(index, h_annex, o_annex)

def logic(enteredList):
    global entered, knowncmd, history, twoDimensionalShapes, threeDimensionalShapes
    
    if not enteredList[0] in knowncmd:
        print("{}Error:{} {} is not a valid command.".format(RED, CLEAR, enteredList[0]))
        outputHistory.append("Error (command invalid)")
        stop = input("Hit ENTER to continue ")
    
    elif enteredList[0] in externalPrograms:
        os.system("python3 {}.py".format(enteredList[0]))
    
    elif enteredList[0] == "add":
        result = float(enteredList[1])
        print(PINK)
        for x in range(2, len(enteredList)):
            result += float(enteredList[x])
        print("The sum of ", end = "")
        for x in range(2, len(enteredList)):
            if x != len(enteredList)-1:
                print("{} + ".format(enteredList[x]), end = "")
            else:
                print("{} is {}".format(enteredList[x], result))
        outputHistory.append(result)
        print(CLEAR)
        index = len(history)
        index = str(index)
        h_annex = history[len(history)-1]
        o_annex = outputHistory[len(outputHistory)-1]
        h_annex = str(h_annex)
        o_annex = str(o_annex)
        historyTable.add_row(index, h_annex, o_annex)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    
    elif enteredList[0] == "quit" or enteredList[0] == "exit":
        exit()
    
    elif enteredList[0] == "sub":
        result = float(enteredList[1])
        for x in range(2, len(enteredList)):
            result -= float(enteredList[x])
        outputHistory.append(result)
        print(PINK)
        print("The difference of ", end = "")
        for x in range(1, len(enteredList)):
            if x != len(enteredList)-1:
                print("{} - ".format(enteredList[x]), end = "")
            else:
                print("{} is {}".format(enteredList[x], result))
        print(CLEAR)
        index = len(history)
        index = str(index)
        h_annex = history[len(history)-1]
        o_annex = outputHistory[len(outputHistory)-1]
        h_annex = str(h_annex)
        o_annex = str(o_annex)
        historyTable.add_row(index, h_annex, o_annex)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    
    elif enteredList[0] == "mult":
        result = 1
        for x in range(1, len(enteredList)):
            result *= float(enteredList[x])
        outputHistory.append(result)
        print(PINK)
        print("The product of ", end = "")
        for x in range(1, len(enteredList)):
            if x != len(enteredList)-1:
                print("{} * ".format(enteredList[x]), end = "")
            else:
                print("{} is {}".format(enteredList[x], result))
        print(CLEAR)
        index = len(history)
        index = str(index)
        h_annex = history[len(history)-1]
        o_annex = outputHistory[len(outputHistory)-1]
        h_annex = str(h_annex)
        o_annex = str(o_annex)
        historyTable.add_row(index, h_annex, o_annex)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    
    elif enteredList[0] == "div":
        result = float(enteredList[1])
        for x in range(2, len(enteredList)):
            if float(enteredList[x]) != 0:
                result/=float(enteredList[x])
            else:
                print()
                outputHistory.append("Error (cannot divide by zero)")
                print("{}Error:{} cannot divide by 0.".format(RED, CLEAR))
                update_historyTable()
                stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
            outputHistory.append(result)
            print(PINK)
            print("The quotient of ", end = "")
            for x in range(1, len(enteredList)):
                if x != len(enteredList)-1:
                    print("{} / ".format(enteredList[x]), end = "")
                else:
                    print("{} is {}".format(enteredList[x], result))
            print(CLEAR)
            update_historyTable()
            stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    
    elif enteredList[0] == "sqrt":
        num1 = float(enteredList[1])
        result = math.sqrt(num1)
        outputHistory.append(result)
        print(PINK)
        print("sqrt({}) = {}".format(num1, result))
        print(CLEAR)
        update_historyTable()
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    
    elif enteredList[0] == "pow":
        num1 = float(enteredList[1])
        if enteredList[2] != "f":
            power = float(enteredList[2])
        else:
            power = float(enteredList[3])
            power = power/float(enteredList[4])
        result = pow(num1, power)
        outputHistory.append(result)
        print(PINK)
        update_historyTable()
        print("{}^{} = {}".format(num1, power, result))
        print(CLEAR)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    
    elif enteredList[0] == "history":
        os.system("clear")
        console.print(MD_TITLE_HISTORY)
        outputHistory.append("~")
        update_historyTable()
        print()
        for x in range(0, len(history)):
            print("{}. {} [Output: {}]".format(x+1, history[x], outputHistory[x]))
        print()
        console.print(historyTable)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    
    elif enteredList[0] == "area":
        shape = ""
        area = 0
        if len(enteredList) == 1:
            shape = input("Shape?: ")
            if shape in twoDimensionalShapes:
                enteredList.append(shape)
            else:
                enteredList.append("-")
                while not shape in twoDimensionalShapes:
                    console.print("[red]\"{}\" is not a valid shape.[/]".format(enteredList[1]))
                    enteredList[1] = input("Shape?: ")
        else:
            if not enteredList[1] in twoDimensionalShapes:
                while not enteredList[1] in twoDimensionalShapes:
                    console.print("[red]\"{}\" is not a valid shape.[/]".format(enteredList[1]))
                    enteredList[1] = input("Shape?: ")
        if enteredList[1] == "circle":
            history[len(history)-1] = "area circle"
            radius = input("What is the radius of the circle?: ")
            if radius == "diameter" or radius == "d":
                radius = input("What is the diameter?: ")
                radius = float(radius)
                radius = radius/2
            else:
                radius = float(radius)
                history[len(history)-1] = "area circle r={}".format(radius)
                area = math.pi * math.pow(radius, 2)
                print()
                print("The area is {}".format(area))
                outputHistory.append(area)
                update_historyTable()
                print()
                stop = input("Hit ENTER to continue ")
        elif enteredList[1] == "square":
            history[len(history)-1] = "area square"
            dimension = input("What is the dimension of the square?: ")
            dimension = float(dimension)
            area = dimension * dimension
            history[len(history)-1] = "area square dimension = {}".format(dimension)
            outputHistory.append(area)
            print("\nThe area is {} units^2".format(area))
            update_historyTable()
            print()
            stop = input("Hit ENTER to continue ")
        elif enteredList[1] == "rectangle":
            history[endof(history)] = "area rectangle"
            base = input("What is the base of the rectangle?: ")
            height = input("What is the height of the rectangle?: ")
            base = float(base)
            height = float(height)
            area = base * height
            history[endof(history)] = "area rectange b={} h={}".format(base, height)
            outputHistory.append(area)
            update_historyTable()
            print("\nThe area is {} units^2".format(area))
            print()
            stop = input("Hit ENTER to continue ")
        elif enteredList[1] == "triangle":
            history[endof(history)] = "area triangle"
            base = input("What is the base of the triangle?: ")
            height = input("What is the height of the triangle?: ")
            base = float(base)
            height = float(height)
            area = 0.5 * base * height
            history[endof(history)] = "area triangle b={} h={}".format(base, height)
            outputHistory.append(area)
            update_historyTable()
            print("\nThe area is {} units^2".format(area))
            print()
            stop = input("Hit ENTER to continue ")

        
#MAIN FUNCTION
while(True):
    os.system("clear")
    console.print(MD_TITLE)
    print()
    console.print(Functions)
    print()
    #print("{}add:{} add     {}sub:{}  subtract     {}mult:{} multiply".format(GREEN, CLEAR, GREEN, CLEAR, GREEN, CLEAR))
    #print("{}div:{} divide  {}sqrt:{} square root  {}pow: {} power".format(GREEN, CLEAR, GREEN, CLEAR, GREEN, CLEAR))
    #print()
    entered = input("> {}".format(CYAN))
    print(CLEAR)
    entered = entered.lower()
    enteredList = entered.split()
    history.append(entered)
    logic(enteredList)

