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
	
def logic(entered, enteredList):
	pass

while True:
	defaultDisplay()
	entered = input("% ")
	entered = entered.lower()
	enteredList = entered.split()
	

