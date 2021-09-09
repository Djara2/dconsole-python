from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
import os
import pyclip
import dtools
console = Console()
MD_TITLE = Markdown("# HTML Builder")
QUIT_KEYWORDS = ["exit", "quit", "eit", "eixt", "qiut"]
while(True):
    os.system("clear")
    console.print(MD_TITLE)
    print()
    print("Version 1")
    print("Enter \"HELP\" for the manual.")
    print()
    entered = input("> ")
    entered = entered.lower()
    if entered in QUIT_KEYWORDS:
        quit()
    elif(entered == "table"):
        workingTable = "<table>\n\t<thead>\n\t\t<tr>\n\t\t\t<th colspan=\""
        rows = 0
        columns = 0
        title = ""
        operation = ""
        headers = []
        operation = input("How many columns should be in this table?: ")
        rows = int(operation)
        workingTable+="{}\">".format(rows)
        operation = input("What is the title of this table?: ")
        workingTable+="{}</th>\n\t\t</tr>\n\t</thead>\n\t<tbody>\n\t\t<tr>\n\t\t\t<td>".format(operation)
        for x in range(0, rows):
            operation = input("Column {} (header {}) label?: ".format(x+1, x+1))
            headers.append(operation)
            if x != rows-1:
                workingTable+="<strong>{}</td>\n\t\t\t<td>".format(operation)
            else:
                workingTable+="<strong>{}</td>\n\t\t</tr>".format(operation)
        building = True
        while(building):
            operation = input("Add another row?: ")
            if operation == "yes" or  operation == "y":
                workingTable+="\n\t\t<tr>\n\t\t\t<td>"
                for x in range(0, len(headers)):
                    operation = input("Content for column {} in new row? (header for this column = {}): ".format(x+1, headers[x]))
                    if x != len(headers)-1:
                        workingTable+="{}</td>\n\t\t\t<td>".format(operation)
                    else:
                        workingTable+="{}</td>\n\t\t</tr>".format(operation)

            elif operation == "no" or operation == "n":
                building = False
            else:
                print("I didn't recognize you. Please enter \"yes\" or \"no\"")
        workingTable+="\n\t</tbody>\n</table>"
        print(workingTable)
        wsl = input("Are you on WSL?: ")
        if wsl != "y":
            pyclip.copy(workingTable)
        else:
            dtools.wslCopy(workingTable)
        stop = input("Hit ENTER to continue")
        quit()








