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

def sum(arg, lower, upper):
    coefficient = 1
    indexOfVar = 0
    if function == "x":
        if "x" or "k" or "n" in arg: #if the sum has a variable in it
            for x in range(0, len(arg)):
                if arg[x] == "x" or arg[x] == "k" or arg[x] == "n":
                    indexOfVar = x
                    break
            coefficient = arg[0:indexOfVar]
            coefficient = int(coefficient)
        else:
            # this is the case wherein it is the sum of just a constant
            coefficent = int(arg)
        # NOW COEFFICIENT IS KNOWN
    else:
        coefficient = 1
        skippedSum = 0
        for z in range(lowerBound, upperBound+1):
            skippedSum+= z
    # find the power of the variable
    if "^" in arg:
        indexOfCaret = 0
        for x in range(indexOfVar, len(arg)):
            if arg[x] == "^":
                indexOfCaret = x
                break
        power = arg[indexOfCaret+1:len(arg)]
        power = int(power)
    else: #case - there is no power ( power of 1 )
        if "x" or "k" or "n" in arg:
            power = 1
        else:
            power = -1 # fix so that summation of just a constant value will work
    # NOW POWER IS KNOWN
    result = 0
    num = 0
    den = 0
    # sum algorithm
    if power == -1:
        for x in range(lower, upper+1):
            result += coefficient
    if power == 1:
        if lower == 1:
            result = upper * (upper+1)
            result = result/2
            result = result * coefficient
        else:
            return(-1) # do later
    elif power == 2:
        if lower == 1:
            den = 6
            num = upper * (upper+1) * ((2*upper)+1)
            result = num/den
            result *= coefficient
        else:
            return(-1)
    elif power == 3:
        if lower == 1:
            den = 4
            upper_squared = pow(upper, 2)
            upper_plus_one_squared = pow(upper+1, 2)
            num = upper_squared * upper_plus_one_squared
            result = num/den
            result *= coefficient
        else:
            return(-1)
    elif power == 4:
        if lower == 1:
            den = 30
            three_times_var_squared = 3 * pow(upper, 2)
            # do later 
            result = -1
        else:
            return(-1)
    elif power == 5:
        # do later
        return(-1)
    else:
        # power too large for summation shortcut
        return(-1)
    if skippedSum != 0:
        result = skippedSum
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
            functionList = function
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

