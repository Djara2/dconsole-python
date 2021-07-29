import os
os.system("clear")
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
MD_TITLE = Markdown("# Binary to Decimal Converter")

def defaultDisplay():
	os.system("clear")
	console.print(MD_TITLE)

def binToDec(bitString):
	# invert bitString
	index = len(bitString)-1
	invertedString = ""
	while index != -1:
		invertedString += bitString[index]
		index-=1
	# now you have the string inverted
	sumValue = 0
	for x in range(0, len(invertedString)):
		if invertedString[x] == "1":
			sumValue += pow(2, x)
	return(sumValue)
	
def logic(entered, enteredList):
	if entered == "quit" or entered == "exit":
		quit()
	returns = []
	if len(enteredList) != 1:
		for x in range(0, len(enteredList)):
			returns.append(binToDec(enteredList[x]))
	else:
		returns.append(binToDec(entered))
	table = Table(title="Conversion")
	table.add_column("Binary")
	table.add_column("Decimal")
	for x in range(0, len(returns)):
		table.add_row(str(enteredList[x]), str(returns[x]))
	console.print(table)
	stop = input("Press ENTER to continue ")
	
while True:
	defaultDisplay()
	entered = input("% ")
	entered = entered.lower()
	enteredList = entered.split()
	logic(entered, enteredList)
	

