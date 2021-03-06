import os
import math
import time
import dmath
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
import pyclip
from colors import *
import dtools
modeList = ["Trigonometry Units"]
trigUnits = "degree"
trigStatuses = ["degree", "radian"]
tableMode = 1
os.system("clear")
# 2nd mode table
Options2 = Table(title="Options (2nd)")
Options2.add_column("Special")
Options2.add_column("Trigonometry")
Options2.add_column("Operators")
Options2.add_column("Geometry")
Options2.add_row("programs", "[bold cyan]arcsin[/]", "[bold cyan]sum[/]", "area")
Options2.add_row("mode", "[bold cyan]arcos[/]", "sub", "surfacearea")
Options2.add_row("func", "[bold cyan]arctan[/]", "mult", "volume")
Options2.add_row("[bold cyan]1st[/]", "", "div", "")
Options2.add_row("", "", "pow", "")
Options2.add_row("", "", "sqrt", "")

# programs table
Programs = Table(title="Programs")
Programs.add_column("discount")
Programs.add_column("tip")
Programs.add_column("bt (binomial theorem)")

# new table layout test
Options = Table(title="Options")
Options.add_column("Special")
Options.add_column("Trigonometry")
Options.add_column("Operators")
Options.add_column("Geometry")
Options.add_row("programs", "sin", "add", "area")
Options.add_row("mode", "cos", "sub", "surfacearea")
Options.add_row("func", "tan", "mult", "volume")
Options.add_row("2nd", "", "div", "")
Options.add_row("expression", "", "pow", "")
Options.add_row("convert units", "", "sqrt", "")
# end 
#
Functions = Table(title="Functions")
Functions.add_column("Ranges")
Functions.add_column("Other")
Functions.add_row("range", "choose")
Functions.add_row("srir (squareRootsInRange)", "bt (binomial theorem)")
Functions.add_row("psir (perfectSquaresInRange)", "factorial")
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
knowncmd = ["copy", "convert", "sin", "arcsin", "cos", "tan", "arccos", "arctan", "sec", "csc", "simplifyfrac", "expression", "mode", "range", "func", "functions", "2nd", "1st", "programs", "srir", "squareRootsInRange", "psir", "perfectsquaresinrange", "sum", "choose", "factorial", "area", "volume", "surfacearea", "quit", "exit", "add", "sub", "mult", "div", "sqrt", "pow", "mod", "history"]


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
    #There are a few possibilities
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

def generateListInTableString(thing):
    buildString = ""
    for x in range(0, len(thing)):
        if x != len(thing)-1:
            buildString+="{}. {}\n".format(x+1, thing[x])
        else:
            buildString+="{}. {}".format(x+1, thing[x])
    return(buildString)

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
    global modeList, trigStatuses, trigUnits, tableMode, entered, knowncmd, history, twoDimensionalShapes, threeDimensionalShapes
    
    if not enteredList[0] in knowncmd:
        print("{}Error:{} {} is not a valid command.".format(RED, CLEAR, enteredList[0]))
        outputHistory.append("Error (command invalid)")
    
    elif enteredList[0] in externalPrograms:
        os.system("python3 {}.py".format(enteredList[0]))
        outputHistory.append("opened {}".format(enteredList[0]))
        update_historyTable()
    
    elif enteredList[0] == "copy":
        mode = input("Are you on WSL?: ")
        #try:
        index = int(enteredList[1])
        copy = str(outputHistory[index-1])
        if mode != "y":
            pyclip.copy(copy)
        else:
            dtools.wslCopy(copy)
        console.print("[bold green]Copied:[/] {}".format(outputHistory[int(enteredList[1])-1]))
        #except:
            #dtools.errorMessage("Please provide an index of the output history listing to copy.")
    elif enteredList[0] == "simplifyfrac":
        if len(enteredList) != 1:
            n, d = dmath.simplifyFraction(float(enteredList[1]), float(enteredList[2]))
        else:
            n = input("Numerator: ")
            d = input("Denominator: ")
            n, d = dmath.simplifyFraction(n, d)
        console.print("[bold green]Simplified fraction:[/] {}/{}".format(n, d))

    elif enteredList[0] == "expression":
        console.print("[bold yellow]Expression formatting rules are explained in help page.[/]")
        expression = input("Enter the expression: ")

    elif enteredList[0] == "convert" and enteredList[1] == "units":
        teaspoons = ["teaspoons", "teaspoon", "tsp", "tsps"]
        tablespoons = ["tablespoons", "tablespoon", "tbsp", "tbsps"]
        floz = ["fluid ounces", "fluid ounce", "floz", "flozs", "fl oz", "fl ozs"]
        cups = ["cups", "cup"]
        pints = ["pints", "pts", "pt", "pint"]
        quarts = ["quarts", "qt", "qts", "quart"]
        gallons = ["gallons", "gallon", "gal", "gals"]
        
        console.print("\n[bold yellow]Please pick a measurement system:[/]\n\n1. Imperial\n2. Metric\n3. Imperial to Metric\n4. Metric to Imperial\n")
        system = input("Measurement system: ")
        
        if system == "1" or system == "imperial" or system == "Imperial":
            console.print("\n[bold yellow]Please pick type of measurement:[/]\n\n1. Distance\n2. Volume\n3. Temperature\n")
            measurementType = input("Measurement type: ")
            if measurementType == "1":
                measurementType = "distance"
            elif measurementType == "2":
                measurementType = "volume"
            elif measurementType == "3":
                measurementType = "temperature"
            
            if measurementType == "distance":
                console.print("\n[bold yellow]Please pick original units:[/]\n1. inches\n2. feet\n3. yards\n 4. miles")
                original = input("Original units: ")
                if original == "1":
                    original = "inches"
                elif original == "2":
                    original = "feet"
                elif original == "3":
                    original = "yards"
                elif original == "4":
                    original = "miles"
                console.print("\n[bold yellow]Please pick destination units:[/]\n1. inches\n2. feet\n3. yards\n 4. miles")
                destination = input("Destination units: ")
                if destination == "1":
                    destination = "inches"
                elif destination == "2":
                    destination = "feet"
                elif destination == "3":
                    destination = "yards"
                elif destination == "4":
                    destination = "miles"
                amt = input("Amount of {}: ".format(original))
                amt = float(amt)
            
            elif measurementType == "temperature":
                original = "fahrenheit"
                console.print("[bold yellow]What destination units?[/]\n\n1. Celsius\n2. Kelvin\n\n")
                destination = input("Which one?: ")
                if destination == "1":
                    destination = "celsius"
                elif destination == "2":
                    destination = "kelvin"
                else:
                    destination = destination.lower()
                amt = input("Amount of degrees {}?: ".format(original))
                amt = float(amt)
            elif measurementType == "volume":
                console.print("\n[bold yellow]Please pick original units:[/]\n1. teaspoon (tsp)\n2. tablespoon (tbsp)\n3. fluid ounce (fl oz or oz)\n 4. cups\n5. pints (pt)\n6. quarts (qt)\n7. gallons (gal)\n")
                original = input("Original units: ")
                if original == "1" or original in teaspoons:
                    original = "teaspoons"
                elif original == "2" or original in tablespoons:
                    original = "tablespoons"
                elif original == "3" or original in floz: 
                    original = "fluid ounces"
                elif original == "4" or original == "cups" or original == "cup":
                    original = "cups"
                elif original == "5" or original in pints:
                    original = "pints"
                elif original == "6" or original in quarts:
                    original = "quarts"
                elif original == "7" or original in gallons:
                    original = "gallons"
                console.print("\n[bold yellow]Please pick destination units:[/]\n1. teaspoons (tsp)\n2. tablespoons (tbsp)\n3. fluid ounces (fl oz)\n 4. cups\n5. pints\n6. quarts\n7. gallons")
                destination = input("Destination units: ")
                if destination == "1" or destination in teaspoons:
                    destination = "teaspoons"
                elif destination == "2" or destination in tablespoons:
                    destination = "tablespoons"
                elif destination == "3" or destination in floz:
                    destination = "fluid ounces"
                elif destination == "4" or destination in cups:
                    destination = "cups"
                elif destination == "5" or destination in pints:
                    destination = "pints"
                elif destination == "6" or destination in quarts:
                    destination = "quarts"
                elif destination == "7" or destination in gallons:
                    destination = "gallons"
                amt = input("\nAmount of {}: ".format(original))
                amt = float(amt)

            if measurementType != "temperature":
                result = dtools.imperialConvert(amt, original, destination)
            else:
                result = dtools.tempConvert(amt, original, destination)
        
        elif system == "2" or system.lower() == "metric":
            console.print("\n[bold yellow]Please pick type of measurement:[/]\n\n1. Distance\n2. Volume\n")
            measurementType = input("Measurement type: ")
            if measurementType == "1":
                measurementType = "distance"
            elif measurementType == "2":
                measurementType = "volume"
            if measurementType == "distance":
                console.print("\n[bold yellow]Please pick original units:[/]\n1. picometers\n2. nanometers\n3. micrometers\n 4. millimeters\n5. centimeters\n6. decimeters\n7. meters\n8. dekameters\n9. hectometers\n10. kilometers\n11. megameters\n12. gigameters\n13. terameters")
                original = input("Original units: ")
                if original == "1" or original == "picometers":
                    original = "picometers"
                elif original == "2" or original == "nanometers":
                    original = "nanometers"
                elif original == "3" or original == "micrometers":
                    original = "micrometers"
                elif original == "4" or original == "millimeters":
                    original = "millimeters"
                elif original == "5" or original == "centimeters" or original == "cm" or original == "centi":
                    original = "centimeters"
                elif original == "6" or original == "decimeters" or original == "decimeter" or original == "deci":
                    original = "decimeters"
                elif original == "7" or original == "meters" or original == "meter" or original == "m":
                    original = "meters"
                elif original == "8" or original == "dekameters" or original == "deka" or original == "dekameter":
                    original = "dekameters"
                elif original == "9" or original == "hectometers" or original == "hecto" or original == "hectometer":
                    original = "hectometers"
                elif original == "10" or original == "kilometers" or original == "km" or original == "kilo" or original == "kilometer":
                    original = "kilometers"
                elif original == "11" or original == "megameters" or original == "mega" or original == "megameter":
                    original == "megameters"
                elif original == "12" or original == "gigameters" or original == "giga" or original == "gigameter":
                    original == "gigameters"
                elif original == "13" or original == "tera" or original == "terameters" or original == "terameter":
                    original == "terameters"

                elif original == "13" or original == "tera" or original == "terameters" or original == "terameter":
                    original == "terameters"

                console.print("\n[bold yellow]Please pick destination units:[/]\n1. inches\n2. feet\n3. yards\n 4. miles")
                destination = input("Destination units: ")
                if destination == "1" or destination == "picometers":
                    destination = "picometers"
                elif destination == "2" or destination == "nanometers":
                    destination = "nanometers"
                elif destination == "3" or destination == "micrometers":
                    destination = "micrometers"
                elif destination == "4" or destination == "millimeters":
                    destination = "millimeters"
                elif destination == "5" or destination == "centimeters" or destination == "cm" or destination == "centi":
                    destination = "centimeters"
                elif destination == "6" or destination == "decimeters" or destination == "decimeter" or destination == "deci":
                    destination = "decimeters"
                elif destination == "7" or destination == "meters" or destination == "meter" or destination == "m":
                    destination = "meters"
                elif destination == "8" or destination == "dekameters" or destination == "deka" or destination == "dekameter":
                    destination = "dekameters"
                elif destination == "9" or destination == "hectometers" or destination == "hecto" or destination == "hectometer":
                    destination = "hectometers"
                elif destination == "10" or destination == "kilometers" or destination == "km" or destination == "kilo" or destination == "kilometer":
                    destination = "kilometers"
                elif destination == "11" or destination == "megameters" or destination == "mega" or destination == "megameter":
                    destination == "megameters"
                elif destination == "12" or destination == "gigameters" or destination == "giga" or destination == "gigameter":
                    destination == "gigameters"
                elif destination == "13" or destination == "tera" or destination == "terameters" or destination == "terameter":
                    destination == "terameters"

                elif destination == "13" or destination == "tera" or destination == "terameters" or destination == "terameter":
                    destination == "terameters"
                amt = input("Amount of {}: ".format(original))
                amt = float(amt)
            result = dtools.metricConvert(amt, original, destination)



        console.print("\n[bold green]Result:[/] {} {}\n".format(result, destination))
        
    
    elif enteredList[0] == "programs":
        console.print(Programs)
        outputHistory.append("displayed programs list")
        update_historyTable()

    elif enteredList[0] == "sin" or enteredList[0] == "cos" or enteredList[0] == "tan":
        if len(enteredList) == 1:
            if enteredList[0] == "sin":
                enteredList.append(input("sin of: "))
                history[len(history)-1] = "sin {}".format(enteredList[1])
            elif enteredList[0] == "cos":
                enteredList.append(input("cos of: "))
                history[len(history)-1] = "cos {}".format(enteredList[1])
            elif enteredList[0] == "tan":
                enteredList.append(input("tan of: "))
                history[len(history)-1] = "tan {}".format(enteredList[1])
        enteredList[1] = float(enteredList[1])
        if trigUnits == "degree":
            original = enteredList[1]
            enteredList[1] = math.radians(enteredList[1])
        if enteredList[0] == "sin":
            result = math.sin(enteredList[1])
        elif enteredList[0] == "cos":
            result = math.cos(enteredList[1])
        elif enteredList[0] == "tan":
            result = math.tan(enteredList[1])
        outputHistory.append(str(result))
        update_historyTable()
        if trigUnits == "degree":
            if enteredList[0] == "sin":
                console.print("Result: sin({} {}) = {}".format(original, trigUnits, result))
            elif enteredList[0] == "cos":
                console.print("Result: cos({} {}) = {}".format(original, trigUnits, result))
            elif enteredList[0] == "tan":
                console.print("Result: tan({} {}) = {}".format(original, trigUnits, result))
        else:
            if enteredList[0] == "sin":
                console.print("Result: sin({} {}) = {}".format(enteredList[1], trigUnits, result))
            elif enteredList[0] == "cos":
                console.print("Result: cos({} {}) = {}".format(enteredList[1], trigUnits, result))
            elif enteredList[0] == "tan":
                console.print("Result: tan({} {}) = {}".format(enteredList[1], trigUnits, result))
    elif enteredList[0] == "arcsin":
        if len(enteredList) == 1:
            enteredList.append(input("arcsin of: "))
            history[len(history)-1] = "arcsin {}".format(enteredList[1])
        enteredList[1] = float(enteredList[1])
        if trigUnits == "degree":
            original = enteredList[1]
            enteredList[1] = math.radians(enteredList[1])
        result = pow(math.sin(enteredList[1]), -1)
        outputHistory.append(str(result))
        update_historyTable()
        if trigUnits == "degree":
            console.print("Result: arcsin({} {}) = {}".format(original, trigUnits, result))
        else:
            console.print("Result: arcsin({} {}) = {}".format(enteredList[1], trigUnits, result))
    
    elif enteredList[0] == "mode":
        trigStatusesString = generateListInTableString(trigStatuses)
        tempTable = Table(title = "Settings")
        tempTable.add_column("Index")
        tempTable.add_column("Option")
        tempTable.add_column("Current Status")
        tempTable.add_column("Other Statuses")
        for x in range(0, len(modeList)):
            tempTable.add_row(str(x+1), modeList[x], trigUnits, trigStatusesString)
        console.print(tempTable)
        selection = input("Option to change (index)? ")
        if selection != "exit" and selection != "quit" and selection != "":
            selection = int(selection)
            subSelection = input("Set to which status index? ")
            subSelection = int(subSelection)
            if selection == 1:
                trigUnits = trigStatuses[subSelection-1]
            print()
            console.print("[bold green]Change set[/]")
        else:
            console.print("[bold green]Settings will not be changed")



    
    elif enteredList[0] == "2nd":
        tableMode = 2
        outputHistory.append("switched options table to 2nd mode")
        update_historyTable()
    
    elif enteredList[0] == "1st":
        tableMode = 1
        outputHistory.append("switched options table to 1st mode")
        update_historyTable()

    elif enteredList[0] == "functions" or enteredList[0] == "func":
        console.print(Functions)

    elif enteredList[0] == "range":
        functions = []
        lowerBound = "a"
        upperBound = "a"
        repeat = True
        while repeat:
            coefficient = input("Coefficient of variable? ")
            power = input("Power of variable? ")
            constant = input("Constant? ")
            if lowerBound == "a":
                lowerBound = input("Lower bound?: ")
                upperBound = input("Upper bound?: ")
            try:
                coefficient = float(coefficient)
                power = float(power)
                constant = float(constant)
                lowerBound = int(lowerBound)
                upperBound = int(upperBound)
                functions.append([coefficient, power, constant])
                repeat = input("Continue? ")
                if repeat == "y":
                    repeat = True
                else:
                    repeat = False
            except:
                console.print("[bold red]Error:[/] entries must be float or integer")
                outputHistory.append("Error on range entry")
                update_historyTable()
        titleString = "Function Range"
        tempTable = Table(title=titleString)
        tempTable.add_column("x")
        for x in range(0, len(functions)):
            tempTable.add_column("{}x^{}+{}".format(functions[x][0], functions[x][1], functions[x][2]))
        if len(functions) == 1:
            for x in range(lowerBound, upperBound+1):
                result = pow(x, power)
                result *= coefficient
                result += constant
                tempTable.add_row("x={}".format(x), str(result))
        elif len(functions) == 2:
            for x in range(lowerBound, upperBound+1):
                f1result = pow(x, functions[0][1])
                f1result *= functions[0][0]
                f1result += functions[0][2]
                f2result = pow(x, functions[1][1])
                f2result *= functions[1][0]
                f2result += functions[1][2]
                tempTable.add_row(str(x), str(f1result), str(f2result))
        elif len(functions) == 3:
            for x in range(lowerBound, upperBound+1):
                f1result = pow(x, functions[0][1])
                f1result *= functions[0][0]
                f1result += functions[0][2]
                f2result = pow(x, functions[1][1])
                f2result *= functions[1][0]
                f2result += functions[1][2]
                f3result = pow(x, functions[2][1])
                f3result *= functions[2][0]
                f3result += functions[2][2]
                tempTable.add_row(str(x), str(f1result), str(f2result), str(f3result))
        elif len(functions) == 4:
            for x in range(lowerBound, upperBound+1):
                f1result = pow(x, functions[0][1])
                f1result *= functions[0][0]
                f1result += functions[0][2]
                f2result = pow(x, functions[1][1])
                f2result *= functions[1][0]
                f2result += functions[1][2]
                f3result = pow(x, functions[2][1])
                f3result *= functions[2][0]
                f3result += functions[2][2]
                f4result = pow(x, functions[3][1])
                f4result *= functions[3][0]
                f4result += functions[3][2]
                tempTable.add_row(str(x), str(f1result), str(f2result), str(f3result), str(f4result))


        console.print(tempTable)
        if len(functions) == 1:
            outputHistory.append("range table for function {}x^{}+{}".format(coefficient, power, constant))
        else:
            outputHistory.append("range table for {} functions".format(len(functions)))
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

    elif enteredList[0] == "squareRootsInRange" or enteredList[0] == "srir":
        start = time.time()
        parameter = []
        for x in range(1, len(enteredList)):
            parameter.append(enteredList[x])
        numbersVisited, result = dmath.squareRootsInRange(parameter)
        squareRootsTable = Table(title="Square Roots in Range")
        squareRootsTable.add_column("Number")
        squareRootsTable.add_column("Square Root")
        for x in range(0, len(result)):
            squareRootsTable.add_row(str(numbersVisited[x]), str(result[x]))
        console.print(squareRootsTable)
        timeTaken = time.time() - start
        console.print("Generated in {} seconds.".format(timeTaken))
        stop = input("Hit ENTER to continue ")
    elif enteredList[0] == "perfectsquaresinrange" or enteredList[0] == "psir":
        start = time.time()
        parameter = []
        for x in range(1, len(enteredList)):
            parameter.append(enteredList[x])
        result = dmath.perfectSquaresInRange(parameter)
        console.print("Found {} squares in the given range.".format(len(result)))
        squaresInRangeTable = Table(title="Squares in Range")
        squaresInRangeTable.add_column("Square")
        squaresInRangeTable.add_column("Square Root")

        for y in range(0, len(result)):
            squaresInRangeTable.add_row(str(result[y]), str(math.sqrt(result[y])))
        console.print(squaresInRangeTable)
        timeTaken = time.time() - start
        print("Generated in {} seconds.".format(timeTaken))
        stop = input("\nHit ENTER to continue ")

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
    stop = input("Hit ENTER to continue ")

        
#MAIN FUNCTION
while(True):
    os.system("clear")
    console.print(MD_TITLE)
    print()
    if tableMode == 1:
        console.print(Options, historyTable)
    else:
        console.print(Options2, historyTable)
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

