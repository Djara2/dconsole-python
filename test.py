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
