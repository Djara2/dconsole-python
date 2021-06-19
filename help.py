import os
from colors import *
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
MD_TITLE = Markdown("# Manual")
stoptext = "Hit ENTER to continue "
def figlet(text):
    os.system("figlet {}".format(text))
os.system("clear")
console.print(MD_TITLE)
print()
general = Table(title="General")
general.add_column("Command")
general.add_column("Description")
general.add_row("[green]History[/]", "Shows you all the things you entered over the course of this session. You can copy items from your history using the HRE command followed by the index number of the entry in the history list.")
externalPrograms = Table(title="External Programs")
externalPrograms.add_column("Program")
externalPrograms.add_column("Description")
externalPrograms.add_row("[green]Discount[/]", "entering discount will open the discount.py file. It takes the argument syntax [value] [percentage of value] and prints out simple information about the arguments provided.")
externalPrograms.add_row("[green]Calculator[/]", "opens a calculator program.")
externalPrograms.add_row("[green]Tip[/]", "utility for finding out various tip percentages based on an input")
externalPrograms.add_row("[green]Search[/]", "Search is a program that can search multiple websites, such as bing, bing images, google, google images, jisho.org, wikipedia, amazon, etc. It will not work on mobile devices running Termux.")
externalPrograms.add_row("[green]Changelog[/]", "Changelog will show what has been changed over the updates. It will just reflect information from the github repository.")
externalPrograms.add_row("[green]w3mh[/]", "Displays a very brief list of commands for the w3mbrowser which can be accessed from dconsole using the command w3m. If you entered \"w3m e [web address]\" then it will load the exact address after the e - the \"e\" stands for exact - otherwise, it will perform a bing search for whatever follows w3m in the input field.")
console.print(general)
print()
console.print(externalPrograms)
quit()
