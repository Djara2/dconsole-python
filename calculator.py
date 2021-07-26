import os
import numpy as np
import matplotlib.pyplot as plt
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
externalPrograms = ["discount", "tip", "bt"]
knowncmd = ["sum", "choose", "factorial", "area", "volume", "surfacearea", "quit", "exit", "add", "sub", "mult", "div", "sqrt", "pow", "mod", "history"]

for x in range(0, len(externalPrograms)):
    knowncmd.append(externalPrograms[x])

def figlet(text):
    os.system("figlet {}".format(text))

def endof(userlist):
    end = len(userlist)-1
    return(end)

def factorial(x):
    if x > 1:
        return(x*factorial(x-1))
    else:
        return(1)
def integral(arg, lower, upper):
    pass
def derivative(arg):
    pass
def sum(arg, lower, upper):
    #first figure out how it is that the user has entered their function.
    #as you know, the terminal will accept something like 4x^2+13x^3 which will then be split up into a list with the delimiter being "+". 
    #There are a few possibilities:
        # x
        # x^2
        # 4x
        # 4x^2
        # we do not have to worry about when these are larger than this because they would be split up
    # CASE: X
    coefficient = 1
    power = 1
    indexOfCaret = -1
    indexOfVar = -1
    endIndexOfCoefficient = -1
    result = 0
    powerAsString = ""
    mode = "default"
    if len(arg) == 1:
        mode = "justVar"
    # CASE: x^2 (x^y)
    elif arg[0] == "x":
        indexOfCaret = 1
        power = float(arg[indexOfCaret+1:len(arg)]) # : goes from start to end (uninclusive of end)
    # CASE: 4x
    elif arg[0] != "x" and not "^" in arg:
        # figure out where x is so that you know where the coefficient ends
        for x in range(0, len(arg)):
            if arg[x] == "x":
                indexOfVar = x
                break
        coefficient = float(arg[0:indexOfVar])
    elif arg[0] != "x" and "^" in arg:
        # figure out where x is so that you know where the coefficient ends
        for x in range(0, len(arg)):
            if arg[x] == "x":
                indexOfVar = x
                break
        coefficient = float(arg[0:indexOfVar])

        # do the same thing we just did for the coefficient but now for the power
        for x in range(indexOfVar+2, len(arg)):
            powerAsString += arg[x]
        power = float(powerAsString)
    # select a shortcut algorithm
    if mode == "default":
        if power == 1:
            # use shortcut (n(n+1))/2
            numerator = upper * (upper+1)
            denominator = 2
            
        elif power == 2:
            numerator = upper * (upper+1) * ((2*upper)+1)
            denominator = 6

        elif power == 3:
            numerator = pow(upper, 2) * pow(upper+1, 2)
            denominator = 4

        elif power == 4:
            numerator = upper * (upper+1) * ((2*upper)+1) * ( (3*pow(upper, 2)) +(3*upper) -1 )
            denominator = 30

        elif power == 5:
            numerator = (2*pow(upper, 6)) + (6*pow(upper, 5)) + (5*pow(upper, 4)) - pow(upper, 2)
            denominator = 12
        else:
            result = -1 #power too high
        if result != -1:
            result = numerator/denominator
    else:
        if mode == "justVar":
            for x in range(lower, upper+1):
                result+=x
    result *= coefficient
    return(result)


def generateSumTable(fList, rList):
    sumTable = Table(title="Summation")
    sumTable.add_column("Function")
    sumTable.add_column("Result", style="green")
    for x in range(0, len(fList)):
        sumTable.add_row(str(fList[x]), str(rList[x]))
    return(sumTable)

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
        outputHistory.append("opened {}".format(enteredList[0]))
        update_historyTable()
    
    elif enteredList[0] == "choose":
        if(len(enteredList) != 1):
            n = enteredList[1]
            n = int(n)
            r = enteredList[2]
            r = int(r)
            num = factorial(n)
            r_factorial = factorial(r)
            n_sub_r = n - r
            n_sub_r_factorial = factorial(n_sub_r)
            den = r_factorial * n_sub_r_factorial
            result = num/den
            outputHistory.append(result)
            update_historyTable()
            print("Result: {}".format(result))
        else:
            console.print("[bold red]Error:[/] you did not provide parameters. Try format \"choose n r\"")
        stop = input("Hit ENTER to continue ")


    elif enteredList[0] == "factorial":
        result = factorial(int(enteredList[1]))
        print("Result: {}".format(result))
        outputHistory.append(result)
        update_historyTable()
        stop = input("Hit ENTER to continue ")

    elif enteredList[0] == "sum":
        print()
        console.print("[bold yellow]NOTICE:[/] your variable must be x when entering the function.")
        print()
        lowerBound = input("Lower bound (will break if not 1 for now): ")
        upperBound = input("Upper bound: ")
        lowerBound = int(lowerBound)
        upperBound = int(upperBound)
        function = input("Function: ")
        history[len(history)-1]="sum {} from {} to {}".format(function, lowerBound, upperBound)
        if "+" in function:
            functionList = function.split("+")
        else:
            functionList = []
            functionList.append(function)
        returnList = []
        totalSum = 0
        if function != functionList:
            for x in range(0, len(functionList)):
                returnList.append(sum(functionList[x], lowerBound, upperBound))
            for y in range(0, len(functionList)):
                # print("Return for {}: {}".format(functionList[y], returnList[y]))
                totalSum+=returnList[y]
            print()
            console.print(generateSumTable(functionList, returnList))
            print("\nSum of {}: {}".format(function, totalSum))
        else:
            for x in range(lowerBound, upperBound+1):
                totalSum += int(function)
            print("Sum of {} from {} to {}: {}".format(function, lowerBound, upperBound, totalSum))
        outputHistory.append(totalSum)
        update_historyTable()
        stop = input("Hit ENTER to continue ")

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
    console.print(Functions, historyTable)
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

