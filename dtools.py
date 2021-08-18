import time
import pyautogui
import pyperclip
import os
import dmath
import matplotlib.pyplot as plt
from rich.console import Console

externalProgramsList = ["mudaeGui", "dtools", "latexBuilder", "binToDec", "decToBin", "mudae", "bt", "richbuilder", "htmlBuilder", "w3mh", "changelog", "discount", "search", "calculator", "tip", "help"]

knownCommandsList = ["wc", "wordcount", "vim", "rb", "commands", "speedtest", "binToDec", "decToBin", "h", "mudae", "binomial theorem", "bt", "richbuilder", "htmlBuilder", "programs", "translate" "programs", "len", "discount", "help", "exit", "quit", "history", "hre", "new", "numbers", "v", "discount", "system", "os", "search", "calculator", "tip", "w3m"]

console = Console()

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
    aliases = ["calc", "latexbuilder", "latex", "mg", "mudaeg"]
    if entered in aliases:
        if entered == "calc":
            return("calculator")
        elif entered == "latexbuilder" or entered == "latex":
            return("latexBuilder")
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

