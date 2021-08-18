import dtools
myList = ["dog", "bagel", "david", "bob", "apple", "alice", "youtube", "erin"]
lettersOfMyList = dtools.getStartingLetters(myList)
listOfLists = []
for x in range(0, len(lettersOfMyList)):
    listOfLists.append(dtools.allThingsThatStartWith(lettersOfMyList[x], myList))
print(listOfLists)
list2 = dtools.generateListOfListsByLetter(myList)
dtools.iteratePrintList(list2, "num")
print()
dtools.iteratePrintList(list2, "alphabet")
string = "Python has many built-in methods that perform operations on strings. One of the operations is to change the case of letters. We'll see different ways to change the case of the letters in a string, and go through many examples in each section, and finally go through some of the applications."
string.lower()
stringList = string.split(" ")
stringList.sort()
wordCount = dtools.generateListOfListsByOccurence(stringList)
dtools.iteratePrintList(wordCount, "num")
testString = "This is a simple string with spaces that I want to see if it can properly print it takes up 2 lines so it should do it well"
dtools.betterPrint(testString, "t2")
removeTest = ["dog", "john", "youtube", "linux", "google", "microsoft"]
print("list before removal: {}".format(removeTest))
removeTest = dtools.removeThing("youtube", removeTest)
print("list after removal: {}".format(removeTest))
wordWithPeriod = "characters."
print("String before removing period: {}".format(wordWithPeriod))
wordWithoutPeriod = dtools.removeChar(".", wordWithPeriod)
print("String after removing period: {}".format(wordWithoutPeriod))
dtools.plotLaTex("\\frac{\omega}{2}")
string1 = "1234"
list3 = [1, 2, 3, 4]
print(string1)
print(dtools.reverseString(string1))
print(list3)
print(dtools.reverseList(list3))
