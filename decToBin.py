import os
import time # used for debug
from colors import GREEN, CLEAR, CYAN
os.system("clear")
terminalRows, terminalColumns = os.popen('stty size', 'r').read().split() 
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
quitKeywords = ["quit", "exit", "eixt", "eit", "ex"]
MD_TITLE = Markdown("# Decimal to Binary Converter")
def defaultDisplay():
	os.system("clear")
	console.print(MD_TITLE)
	
def maxPowerOfTwo(num):
	power = -1
	while pow(2, power+1) <= num:
		power+=1
	return(power)

def debug(t, text):
	print(text)
	for x in range(0, len(t)):
		time.sleep(0.01)
		print(t[x])

def decToBin(num):
	table = []
	while int(num/2) != 0:
		table.append([num, str(int(num/2))[0],  num%2])
		num = int(num/2)
	table.append([1, 0, 1])
	# invert table order so that you can read remainders from bottom to top:
	index = len(table)-1
	# debug(table, "Table")
	invertedTable = []
	while index != -1:
		invertedTable.append(table[index])
		index-=1
	# debug(invertedTable, "Inverted Table")
	bitString = ""
	for x in range(0, len(invertedTable)):
		bitString+=str(invertedTable[x][2])
	return(bitString)

def logic(decimals, mode, arguments):
	startTime = time.time()
	if mode == "regular":
		bitStrings = []
		for x in range(0, len(decimals)):
			bitStrings.append(decToBin(decimals[x]))
		outputTable = Table(title="Conversion")
		outputTable.add_column("In")
		outputTable.add_column("Out")
		for x in range(0, len(decimals)):
			outputTable.add_row(str(decimals[x]),bitStrings[x])
		console.print(outputTable)
	elif mode == "range":
		iteratorValue = int(arguments[2])
		lower = int(arguments[0])
		upper = int(arguments[1])
		bitStrings = []
		for x in range(lower, upper+1, iteratorValue):
			decimals.append(x)
		for x in range(0, len(decimals)):
			bitStrings.append(decToBin(decimals[x]))
			amtToPrint = float(terminalColumns) * (x/(len(decimals)-1))
			amtToPrint = int(amtToPrint)
			#print(amtToPrint)
			buildingText = ""
			buildingText+="{}{}{}".format(GREEN, "|"*amtToPrint, CLEAR)
			buildingText += "\nConverted: {}{}{} out of {}{}{}".format(CYAN, x, CLEAR, CYAN, len(decimals)-1, CLEAR)
			print(buildingText)
			os.system("clear")
		prevText = "Converted: {}{}{} out of {}{}{}".format(CYAN, len(decimals)-1, CLEAR, CYAN, len(decimals)-1, CLEAR)
		console.print("Building table...")
		outputTable = Table(title="Conversion")
		os.system("clear")
		prevText+="\nBuilding table: created!"
		console.print(prevText)
		console.print("Columns: {}{}{} out of {}{}{}".format(CYAN, "0", CLEAR, CYAN, "2", CLEAR))
		outputTable.add_column("In")
		outputTable.add_column("Out")
		os.system("clear")
		prevText+="\n{}{}".format(" "*len("Building table: "), "Columns: {}2{} out of {}2{}".format(CYAN, CLEAR, CYAN, CLEAR))
		console.print(prevText)
		for x in range(0, len(decimals)):
			amtToPrint = float(terminalColumns) * (x/(len(decimals)-1))
			amtToPrint = int(amtToPrint)
			#print(amtToPrint)
			buildingText = ""
			buildingText += "{}{}{}".format(GREEN, "|"*amtToPrint, CLEAR)
			buildingText += "\n{}".format(prevText)
			outputTable.add_row(str(decimals[x]),bitStrings[x])
			buildingText+="\n{}Added rows: {}{}{} out of {}{}{}".format(" "*len("Building table: "), CYAN, x, CLEAR, CYAN, len(decimals)-1, CLEAR)
			print(buildingText)
			os.system("clear")
		console.print("Printing table...\n")
		console.print(outputTable)
		elapsedTime = time.time() - startTime
		console.print("[Generated in {} seconds]\n".format(elapsedTime))

while True:
	defaultDisplay()
	#print("Terminal columns: {}".format(terminalColumns))
	decimals = []
	exceptionRaised = False
	entered = input("Enter a decimal value: ")
	print()
	if " " in entered:
		enteredList = entered.split()
	else:
		enteredList = []
		enteredList.append(entered)
	# convert values
	if len(enteredList) == 1:
		try:
			decimals.append(int(enteredList[0])) 
		except:
			if not "range" in entered and not entered in quitKeywords:
				console.print("[bold red]Error:[/] you can only enter integer values")
				exceptionRaised = True
	else:
		try:
			for x in range(0, len(enteredList)):
				decimals.append(int(enteredList[x]))
		except:
			if not "range" in entered and not entered in quitKeywords:
				console.print("[bold red]Error:[/] you can only enter ienteger values")
				exceptionRaised = True
	if exceptionRaised == False and not entered in quitKeywords:
		if not "range" in entered:
			logic(decimals, "regular", 0)
		else:
			lower = int(enteredList[1])
			upper = int(enteredList[2])
			step = int(enteredList[3])
			arguments = [lower, upper, step]
			logic([], "range", arguments)
	else:
            if entered in quitKeywords:
                quit()
	stop = input("Press ENTER to continue ")
