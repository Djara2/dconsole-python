import time
import pyautogui
import pyperclip
import os
import dmath
import matplotlib.pyplot as plt
from rich.console import Console

externalProgramsList = ["genblankapp", "markdownwriter", "mudaeGui", "dtools", "latexBuilder", "bintodec", "dectobin", "mudae", "bt", "richbuilder", "htmlbuilder", "w3mh", "changelog", "discount", "search", "calculator", "tip", "help"]

knownCommandsList = ["wc", "wordcount", "vim", "rb", "commands", "speedtest", "binToDec", "decToBin", "h", "mudae", "binomial theorem", "bt", "richbuilder", "htmlBuilder", "programs", "translate" "programs", "len", "discount", "help", "exit", "quit", "history", "hre", "new", "numbers", "v", "discount", "system", "os", "search", "calculator", "tip", "w3m"]

console = Console()

def clear():
    os.system("clear")

def generateClickableLink(link, altText):
    linkString = "\x1b]8;;https://{}/\a{}\x1b]8;;\a".format(link, altText)
    return(linkString)

def reverseList(thing):
    newList = []
    x = len(thing)-1
    while x != -1:
        newList.append(thing[x])
        x-=1
    return(newList)

def reverseString(thing):
    newString = ""
    x = len(thing)-1
    while x != -1:
        newString += thing[x]
        x-=1
    return(newString)

def addToFront(new, thing):
    buildString = new
    buildString += thing
    return(buildString)

def whereIs(thing, somethingElse):
    # function to find a thing in an object
    found = False
    indexOfThing = -1
    for x in range(0, len(somethingElse)):
            if thing == somethingElse[x]:
                found = True
                indexOfThing = x
                break
    return(indexOfThing)

def count(thing, inObject):
    instances = 0
    if thing in inObject:
        for x in range(0, len(inObject)):
            if thing == inObject[x]:
                instances+=1
    return(instances)

def getUniqueWords(workingList):
    # remove punctuation symbols from every listing so that "characters" and "characters." do not appear as 2 unique words.
    for x in range(0, len(workingList)):
        workingList[x] = removePunctuations(workingList[x])

    uniqueWords = []
    for x in range(0, len(workingList)):
        if not workingList[x] in uniqueWords:
            uniqueWords.append(workingList[x])
    return(uniqueWords)

def wordCount(thing):
    thingList = thing.split()
    return(len(thingList))

def generateListOfListsByOccurence(workingList):
    uniqueWords = getUniqueWords(workingList)
    buildList = []
    for x in range(0, len(uniqueWords)):
        buildList.append([uniqueWords[x], count(uniqueWords[x], workingList)])
    return(buildList)

def getTerminalSize():
    terminalRows, terminalColumns = os.popen('stty size', 'r').read().split()
    return(terminalRows, terminalColumns)

def getStartingLetters(workingList):
    letters = []
    for x in range(0, len(workingList)):
        if not workingList[x][0] in letters:
            letters.append(workingList[x][0])
    letters.sort()
    return(letters)

def lenLongestItem(workingList):
    lenCurrentLongest = 0
    for x in range(0, len(workingList)):
        if len(workingList[x]) > lenCurrentLongest:
            lenCurrentLongest = len(workingList[x])
    return(lenCurrentLongest)

def longestItem(workingList):
    lengthLookingFor = lenLongestItem(workingList)
    longestItem = ""
    for x in range(0, len(workingList)):
        if len(workingList[x]) == lengthLookingFor:
            longestItem = workingList[x]
            break
    return(longestItem)

def indexesWhereatLetterChanges(workingList):
    returnList = []
    for x in range(0, len(workingList)):
        if x != 0:
            if workingList[x][0] != workingList[x-1][0]:
                returnList.append(x)
        else:
            next
    return(returnList)

def allThingsThatStartWith(startsWith, workingList):
    buildList = []
    for x in range(0, len(workingList)):
        if workingList[x][0] == startsWith:
            buildList.append(workingList[x])
    return(buildList)

def generateListOfListsByLetter(workingList):
    lettersOfWorkingList = getStartingLetters(workingList)
    listOfLists = []
    for x in range(0, len(lettersOfWorkingList)):
        listOfLists.append(allThingsThatStartWith(lettersOfWorkingList[x], workingList))
    return(listOfLists)

def iteratePrintList(workingList, mode):
    for x in range(0, len(workingList)):
        if mode == "none":
            print(workingList[x])
        elif mode == "num" or mode == "numbers" or mode == "nums":
            if x < 10:
                str_x = "0{}".format(x)
            else:
                str_x = str(x)
            print("{}. {}".format(str_x, workingList[x]))
        elif mode == "num1":
            if x+1 < 10:
                str_x = "0{}".format(x+1)
            else:
                str_x = str(x+1)
            print("{}. {}".format(str_x, workingList[x]))
        elif mode == "alphabet":
            #print("{}:\n{}\n".format(workingList[x][0][0].upper(), workingList[x]))
            console.print("[bold cyan]{}:[/]".format(workingList[x][0][0].upper()))
            print("{}\n".format(workingList[x]))

def detectExternalProgramAlias(entered):
    # pass in the variable "entered" in dconsole. Set it equal to the return of this function. The function will return the "official" name if an alias is detected. Otherwise it will return what was passed in.
    aliases = ["md", "markdown", "calc", "latexbuilder", "latex", "mg", "mudaeg"]
    if entered in aliases:
        if entered == "calc":
            return("calculator")
        elif entered == "latexbuilder" or entered == "latex":
            return("latexBuilder")
        elif entered == "md" or entered == "markdown":
            return("markdownwriter")
    else:
        return(entered)

def handleSpecialChars(workingList, specialChars):
    for x in range(0, len(workingList)):
        if workingList[x] in specialChars:
            if workingList[x] == "vec":
                workingList[x] = "\\vec{"
                workingList[x+1] += "}"
            elif workingList[x] == "delta" or workingList[x] == "dd":
                workingList[x] = "\\Delta "
            elif workingList[x] == "alpha" or workingList[x] == "aa":
                workingList[x] = "\\alpha "
            elif workingList[x] == "omega" or workingList[x] == "oo":
                workingList[x] = "\\omega "
            elif workingList[x] == "right" or workingList[x] == "rr":
                workingList[x] == "\\Rightarrow "
            elif workingList[x] == "left" or workingList[x] == "ll":
                workingList[x] = "\\Leftarrow "
            
            elif workingList[x] == "in" or workingList[x] == "member" or workingList[x] == "mem":
                workingList[x] = "\\in"
            
            elif workingList[x] == "neq" or workingList[x] == "notequal" or workingList[x] == "!=":
                workingList[x] = "\\neq"
            
            elif workingList[x] == "notin" or workingList[x] == "notmem" or workingList[x] == "notmember":
                workingList[x] = "\\notin"
            
            elif workingList[x] == "porm" or workingList[x] == "plusorminus" or workingList[x] == "pm" or workingList[x] == "+-":
                workingList[x] = "\\pm"

            
            elif workingList[x] == "notlessthan" or workingList[x] == "notless" or workingList[x] == "nless" or workingList[x] == "!<":
                workingList[x] = "\\nless"

            elif workingList[x] == "!>" or workingList[x] == "notgreaterthan" or workingList[x] == "notgreater" or workingList[x] == "ngreater":
                workingList[x] == "\\ngtr"

            elif workingList[x] == "!>=":
                workingList[x] = "\\ngeq"

            elif workingList[x] == "!<=":
                workingList[x] = "\\nleq"

            elif workingList[x] == "<=" or workingList[x] == "leq" or workingList[x] == "lessthanorqualto" or workingList[x] == "lessequal" or workingList[x] == "lessthanequal" or workingList[x] == "lessequalto":
                workingList[x] = "\\leq"

            elif workingList[x] == ">=" or workingList[x] == "geq" or workingList[x] == "greaterorequal" or workingList[x] == "greaterthanorrequalto" or workingList[x] == "greaterthanequalto" or workingList[x] == "greaterequal":
                workingList[x] = "\\geq"
            
            elif workingList[x] == "abt" or workingList[x] == "approx" or workingList[x] == "about":
                 workingList[x] = "\\approx"
            
            elif workingList[x] == "subset" or workingList[x] == "sub":
                workingList[x] = "\\subset"
            
            elif workingList[x] == "notsubset" or workingList[x] == "nsubset" or workingList[x] == "notsub" or workingList[x] == "nsub" or workingList[x] == "!sub":
                workingList[x] = "\\not\\subset"
            
            elif workingList[x] == "real":
                workingList[x] = "\\R"
            
            elif workingList[x] == "ints":
                workingList[x] = "\\Z"
            
            elif workingList[x] == "natural":
                workingList[x] = "\\N"
            
            else:
                pass
        else:
            next
    return(workingList)

def getTerminalSize():
    terminalRows, terminalColumns = os.popen('stty size', 'r').read().split()
    return(terminalRows, terminalColumns)

def betterPrint(what, mode):
    rows, columns = getTerminalSize()
    allWords = what.split()
    buildString = ""
    buildLine = ""
    for x in range(0, len(allWords)):
        if mode[0] == "t" and len(buildLine) == 0:
            buildLine += "\t"*int(mode[1])
        if len(buildLine+" {}".format(allWords[x])) < int(columns):
            buildLine += " {}".format(allWords[x])
        else:
            buildString += "{}\n".format(buildLine)
            buildLine = ""
    console.print(buildString)

def removeThing(what, fromWhat):
    # removes all occurrences of a thing from a list
    replacementList = []
    for x in range(0, len(fromWhat)):
        if what != fromWhat[x]:
            replacementList.append(fromWhat[x])
    return(replacementList)

def removeChar(what, fromWhat):
    #removes all occurrences of a thing from a string and returns the new string
    replacementString = ""
    for x in range(0, len(fromWhat)):
        if what != fromWhat[x]:
            replacementString += fromWhat[x]
    return(replacementString)

def removePunctuations(fromWhat):
    replacementString = ""
    punctuations = [".", ",", "\"", ";", ":", "!", "?", "*", "/"]
    for x in range(0, len(fromWhat)):
        if not fromWhat[x] in  punctuations:
            replacementString += fromWhat[x]
    return(replacementString)

def plotLaTex(thing):
    plt.plot()
    plt.text(0.0, 0.0,'$%s$'%thing)
    plt.show()

def engageTextbar(): #for mudae
    pyautogui.moveTo(730, 1023)
    time.sleep(0.3)
    pyautogui.click()

def handleExpression(thing):
    thingList = thing.split()
    # PEMDAS 

def errorMessage(text):
    console.print("[bold red]Error:[/] {}".format(text))

def imperialConvert(amt, unit, destination):
    result = -1
    scalar = -1
    dividing = True
    errorText = "Unexpected conversion destination"
    inList = ["in", "inch", "inches"]
    ftList = ["ft", "feet"]
    ydList = ["yd", "yards", "yds", "yard"]
    miList = ["mi", "miles", "mile"]
    if unit == "inches" or unit == "inch" or unit == "in":
        if destination == "feet" or destination == "ft":
            scalar = 12
        elif destination == "yards" or destination == "yard" or destination == "yd" or destination == "yds":
            scalar = 36
        elif destination == "miles" or destination == "mile" or destination == "mi":
            scalar = 63360
        else:
            console.print("[bold red]Error:[/]Unexpected conversion destination.")
    
    elif unit == "ft" or unit == "feet":
        if destination == "in" or destination == "inches" or destination == "inch":
            scalar = 12
            dividing = False
        elif destination == "yd" or destination == "yds" or destination == "yards" or destination == "yard":
            scalar = 3
        elif destination == "mi" or destination == "miles" or destination == "mile":
            scalar = 5280
        else:
            errorMessage("Unexpected conversion destination")

    elif unit == "yd" or unit == "yards" or unit == "yds" or unit == "yard":
        if destination == "in" or destination == "inches" or destination == "inches":
            scalar = 36
            dividing = False
        elif destination == "ft" or destination == "feet":
            scalar = 3
            dividing = False
        elif destination == "mi" or destination == "miles" or destination == "mile":
            scalar = 1760
        else:
            errorMessage(errorText)
    
    elif unit == "mi" or unit == "miles" or unit == "mile":
        dividing = False
        if destination in inList:
            scalar = 63360
        elif destination in ftList:
            scalar = 5280
        elif destination in ydList:
            scalar = 1760
        else:
            errorMessage(errorText)
    
    elif unit == "teaspoons":
        if destination == "tablespoons":
            scalar = 3
        elif destination == "fluid ounces":
            scalar = 6
        elif destination == "cups":
            scalar = 48
        elif destination == "pints":
            scalar = 96
        elif destination == "quarts":
            scalar = 192
        elif destination == "gallons":
            scalar = 768
    
    elif unit == "tablespoons":
        if destination == "teaspoons":
            scalar = 3
            dividing = False
        elif destination == "fluid ounces":
            scalar = 2                                                     
        elif destination == "cups":                                        
            scalar = 16
        elif destination == "pints":
            scalar = 32
        elif destination == "quarts":
            scalar = 64
        elif destination == "gallons":
            scalar = 256
    
    elif unit == "fluid ounces":
        if destination == "teaspoons":
            scalar = 6
            dividing = False
        elif destination == "tablespoons":
            scalar = 2
            dividing = False
        elif destination == "cups":                                        
            scalar = 8
        elif destination == "pints":
            scalar = 16
        elif destination == "quarts":
            scalar = 32
        elif destination == "gallons":
            scalar = 128
    
    elif unit == "cups":
        if destination == "teaspoons":
            scalar = 48
            dividing = False
        elif destination == "tablespoons":
            scalar = 16
            dividing = False
        elif destination == "fluid ounces":
            scalar = 8   
            dividing = False
        elif destination == "pints":                                    
            scalar = 2
        elif destination == "quarts":
            scalar = 4
        elif destination == "gallons":
            scalar = 16
    
    elif unit == "pints":
        if destination == "teaspoons":
            scalar = 96
            dividing = False
        elif destination == "tablespoons":
            scalar = 32
            dividing = False
        elif destination == "fluid ounces":
            scalar = 16
            dividing = False
        elif destination == "cups":                                        
            scalar = 2
            dividing = False
        elif destination == "quarts":
            scalar = 2
        elif destination == "gallons":
            scalar = 8
    
    elif unit == "quarts":
        if destination == "teaspoons":
            scalar = 192
            dividing = False
        elif destination == "tablespooons":
            scalar = 64
            dividing = False
        elif destination == "fluid ounces":
            scalar = 32
            dividing = False
        elif destination == "cups":                                        
            scalar = 4
            dividing = False
        elif destination == "pints":
            scalar = 2
            dividing = False
        elif destination == "gallons":
            scalar = 4
    
    elif unit == "gallons":
        if destination == "teaspoons":
            scalar = 768
            dividing = False
        elif destination == "tablespooons":
            scalar = 256
            dividing = False
        elif destination == "fluid ounces":
            scalar = 128
            dividing = False
        elif destination == "cups":                                        
            scalar = 16
            dividing = False
        elif destination == "pints":
            scalar = 8
            dividing = False
        elif destination == "quarts":
            scalar = 4
            dividing = False

    else:
        errorMessage("Either the unit parameter or the destination parameter was wrong. It is possible both were not entered correctly.")
    if dividing == True:
        result = amt/scalar
    else:
        result = amt*scalar
    return(result)

def metricConvert(amt, unit, destination):
    result = -1
    scalar = -1
    dividing = True
    errorText = "Unexpected conversion destination"
    if unit == "picometers":
        if destination == "nanometers":
            scalar = 1000
        elif destination == "micrometers":
            scalar = pow(10, 6)
        elif destination == "millimeters":
            scalar = pow(10, 9)
        elif destination == "centimeters":
            scalar = pow(10, 10)
        elif destination == "decimeters":
            scalar = pow(10, 11)
        elif destination == "meters":
            scalar = pow(10, 12)
        elif destination == "dekameters":
            scalar = pow(10, 13)
        elif destination == "hectometers":
            scalar = pow(10, 14)
        elif destination == "kilometers":
            scalar = pow(10, 15)
        elif destination == "megameters":
            scalar = pow(10, 18)
        elif destination == "gigameters":
            scalar = pow(10, 21)
        elif destination == "terameters":
            scalar = pow(10, 24)
        else:
            console.print("[bold red]Error:[/]Unexpected conversion destination.")
    
    elif unit == "nanometers":
        if destination == "picometers":
            scalar = 1000
            dividing = False
        elif destination == "micrometers":
            scalar = 1000
        elif destination == "millimeters":
            scalar = 1000000
        elif destination == "centimeters":
            scalar = 10000000
        elif destination == "decimeters":
            scalar = 100000000
        elif destination == "meters":
            scalar = pow(10, 9)
        elif destination == "dekameters":
            scalar = pow(10, 10)
        elif destination == "hectometers":
            scalar = pow(10, 11)
        elif destination == "kilometers":
            scalar = pow(10, 12)
        elif destination == "megameters":
            scalar = pow(10, 15)
        elif destination == "gigameters":
            scalar = pow(10, 18)
        elif destination == "terameters":
            scalar = pow(10, 21)
        else:
            console.print("[bold red]Error:[/]Unexpected conversion destination.")
    
    elif unit == "micrometers":
        if destination == "picometers":
            scalar = pow(10, 6)
            dividing = False
        elif destination == "nanometers":
            scalar = 1000
            dividing = False
        elif destination == "millimeters":
            scalar = 1000
        elif destination == "centimeters":
            scalar = 10000
        elif destination == "decimeters":
            scalar = 100000
        elif destination == "meters":
            scalar = 1000000
        elif destination == "dekameters":
            scalar = 10000000
        elif destination == "hectometers":
            scalar = 100000000
        elif destination == "kilometers":
            scalar = pow(10, 9)
        elif destination == "megameters":
            scalar = pow(10, 12)
        elif destination == "gigameters":
            scalar = pow(10, 15)
        elif destination == "terameters":
            scalar = pow(10, 18)
        else:
            console.print("[bold red]Error:[/]Unexpected conversion destination.")

    if unit == "millimeters":
        if destination == "picometers":
            scalar = pow(10, 9)
            dividing = False
        elif destination == "nanometers":
            scalar = 1000000
            dividing = False
        elif destination == "micrometers":
            scalar = 1000
            dividing = False
        elif destination == "centimeters":
            scalar = 10
        elif destination == "decimeters":
            scalar = 100
        elif destination == "meters":
            scalar = 1000
        elif destination == "dekameters":
            scalar = 10000
        elif destination == "hectometers":
            scalar = 100000
        elif destination == "kilometers":
            scalar = pow(10, 6)
        elif destination == "megameters":
            scalar = pow(10, 9)
        elif destination == "gigameters":
            scalar = pow(10, 12)
        elif destination == "terameters":
            scalar = pow(10, 15)
        else:
            console.print("[bold red]Error:[/]Unexpected conversion destination.")
    else:
        errorMessage("Either the unit parameter or the destination parameter was wrong. It is possible both were not entered correctly.")
    if dividing == True:
        result = amt/scalar
    else:
        result = amt*scalar
    return(result)
