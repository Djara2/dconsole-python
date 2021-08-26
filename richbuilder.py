from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
import keyboard
import os
import pyclip
os.system("clear")
console = Console()
MD_TITLE = Markdown("# Rich (Python Library) Builder")
console.print(MD_TITLE)
entered = ""
work = ""
columns = 0
title = ""
headers = []
while(True):
    entered = input("> ")
    entered = entered.lower()
    if entered == "quit" or entered == "exit":
        quit()
    elif entered == "table":
        entered = input("What is the name of this table? ")
        title = entered
        work+="{} = Table(title=\"{}\")\n".format(entered, entered)
        entered = input("How many columns should there be?: ")
        columns = int(entered)
        for x in range(0, columns):
            entered = input("Label for column (header) {}?: ".format(x+1))
            headers.append(entered)
            work+="{}.add_column(\"{}\")\n".format(title, entered)
        building = True
        while(building):
            entered = input("Add a new row?: ")
            if entered == "n" or entered == "no":
                building = False
            elif entered == "yes" or entered == "y":
                for x in range(0, columns):
                    entered = input("Content for column {} ({}) in new row?: ".format(x+1, headers[x]))
                    if x == 0:
                        work+="{}.add_row(\"{}\", ".format(title, entered)
                    elif x != 0 and x != columns-1:
                        work+="\"{}\", ".format(entered)
                    else:
                        work+="\"{}\")\n".format(entered)
            else:
                print("I did not recognize your input. Please enter yes, y, no, or n.")
        print()
        print(work)
        pyclip.copy(work)
        stop = input("Hit ENTER to continue ")


