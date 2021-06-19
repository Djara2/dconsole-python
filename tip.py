from colors import *
import os
from rich.console import Console
from rich.markdown import Markdown
os.system("clear")
console = Console()
MD_TITLE = Markdown("# Tips Calculator")
def figlet(text):
    os.system("figlet {}".format(text))

def clear():
    os.system("clear")

while(True):
    clear()
    console.print(MD_TITLE)
    entered = input("Original charge? $")
    if entered != "quit" and entered != "exit":
        entered = float(entered)
    else:
        quit()
    print("")
    specials = [5, 10, 15, 20]
    for x in range(1, 21):
        tip = (x/100)*entered
        if not x in specials:
            print("{}{}% tip for ${}: {}${}{} | Total: {}${}".format(CLEAR, x, entered, GREEN, tip, CLEAR, GREEN, entered+tip))
        else:
            print()
            print("{}{}% tip for ${}: {}${}{} | Total: {}${}".format(YELLOW, x, entered, GREEN, tip, YELLOW, GREEN, entered+tip))
            print()
    print(CLEAR)
    stop = input("Hit ENTER to continue")
    


