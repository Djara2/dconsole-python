import os
quitKeywords = ["exit", "quit", "ex", "eit", "eixt"]
os.system("clear")
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
CONTENTS = Markdown("# Manual\n## What is dconsole?\n\n* **Dconsole** is a program I made to help me to work related to school, note-taking, and playing Mudae in me and my friends' Discord server. With that, dconsole can be used for math, markdown, writing LaTex, writing HTML, and so on.\n\n## What Can I Do?\n\n* Entering **\"programs\"** in the command line in dconsole will print out all the external programs dconsole is related to. dconsole is actually just an interface for accessing all these apps a little easier.\n\n* Entering **\"commands\"** will show all the commands you can do from within dconsole without launching into a different .py file.\n\n## External Programs\n\n* **bintodec** - Short for \"binary to decimal;\" it converts a bit string into its decimal number system equivalent.\n\n* **bt** - Short for \"binomial theorem;\" it does the binomial theorem.\n\n* **calculator** - More than a regular calculator app, it is supposed to emulate the functionality of the TI-84. That's what I use for my school work, but if I don't have batteries, forgot where I left it and don't want to get up, or don't want to get out of the flow of just having my hands on the keyboard and entering stuff in, then it's nice to have something that can basically do all the same stuff.\n\n* **dectobin** - Short for \"decimal to binary;\" it converts a decimal number to a bit string.\n\n* **discount** - Tool for figuring discount differences and final balances.\n\n* **dtools** - The brains of dconsole and other mini programs that can be opened using dconsole is dtools, which is just a library of functions. \n\n* **genblankapp** - Used to create a boiler plate program in the model of how most of the external apps are written. Fully automated. \n\n* **htmlbuilder** - Used to write HTML faster. I use this a lot to write tables in HTML.\n\n* **latexbuilder** - Used to write LaTex a little faster.\n\n* **markdownwriter** - Used to write markdown a little faster. I use it a lot to add span tags and generic design stuff.\n* **mudae** - Semi-automatically plays the Mudae game in Discord for me. Only works with my Discord server unless you modify the code.\n\n* **richbuilder** - Used to write in the syntax of the Rich library (Python) a little faster.\n\n* **search** - A search tool. Searches multiple search engines. \n\n* **tip** - A tool for calculating tips.\n\n* **w3m** - Opens the w3m browser.")
def defaultDisplay():
    os.system("clear")
    console.print(CONTENTS)

def logic(entered, enteredList):
    if entered in quitKeywords:
        exit()

while True:
    defaultDisplay()
    entered = input("\n> ")
    enteredList = entered.split()
    logic(entered, enteredList)
    stop = input("Hit ENTER to continue ")
