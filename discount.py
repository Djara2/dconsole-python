import os
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown
from colors import *
console = Console()
MD_TITLE = Markdown("# Discount Calculator")
stoptext = "Hit ENTER to continue "
while(True):
    os.system("clear")
    console.print(MD_TITLE)
    print("Enter \"help\" for help")
    entered = input("% {}".format(CYAN))
    entered = entered.lower()
    enteredList = entered.split()
    print("{}".format(CLEAR), end='')
    if enteredList[0] == "help":
        os.system("clear")
        os.system("figlet Manual")
        print()
        print("The command line takes the syntax [Value] [Percentage of value]")
        stop = input(stoptext)
    elif enteredList[0] == "exit" or enteredList[0] == "quit":
        exit()
    else:
        value = float(enteredList[0])
        percent = float(enteredList[1])
        percent = percent/100
        discount = value * percent
        discountedCost = value - discount
        print()
        print("{}% of {} is {}".format(percent*100, value, discount))
        print("If something costs ${} and is discounted {}% the final cost would be ${}".format(value, percent*100, discountedCost))
        stop = input(stoptext)
