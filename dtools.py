import dmath
import re
from rich.console import Console
externalProgramsList = ["dtools", "latexBuilder", "binToDec", "decToBin", "mudae", "bt", "richbuilder", "htmlBuilder", "w3mh", "changelog", "discount", "search", "calculator", "tip", "help"]

knownCommandsList = ["vim", "rb", "commands", "speedtest", "binToDec", "decToBin", "h", "mudae", "binomial theorem", "bt", "richbuilder", "htmlBuilder", "programs", "translate" "programs", "len", "discount", "help", "exit", "quit", "history", "hre", "new", "numbers", "v", "discount", "system", "os", "search", "calculator", "tip", "w3m"]

console = Console()

def generateClickableLink(link, altText):
    linkString = "\x1b]8;;https://{}/\a{}\x1b]8;;\a".format(link, altText)
    return(linkString)

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
    uniqueWords = []
    for x in range(0, len(workingList)):
        if not workingList[x] in uniqueWords:
            uniqueWords.append(workingList[x])
    return(uniqueWords)

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

def purgeFromString(thing, string):
    if thing == " ":
        thing = "\s+"
    return(re.sub(thing, "", string))

def detectExternalProgramAlias(entered):
    # pass in the variable "entered" in dconsole. Set it equal to the return of this function. The function will return the "official" name if an alias is detected. Otherwise it will return what was passed in.
    aliases = ["calc", "latexbuilder", "latex"]
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
                workingList[x] = "\\vec{"+workingList[x+1]+"}"
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
            else:
                pass
        else:
            next
    return(workingList)
