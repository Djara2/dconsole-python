from colors import *
from figlet import *
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()
MD_TITLE = Markdown("# Changelog")
os.system("clear")
console.print(MD_TITLE)
print("{}VERSION 1.3{}".format(CYAN, CLEAR))
print("- {}Calculator{} visuals improved".format(GREEN, CLEAR))
print("- {}Calculator{} can now do fractional powers using the syntax \"pow num1 f frac_numerator frac_denominator\"".format(GREEN, CLEAR))
print("- Added {}changelog{}".format(GREEN, CLEAR))
print("- Added {}figlet.py{} file, which makes it easier to write external programs by just importing it".format(GREEN, CLEAR))
print()
stop = input("Hit ENTER to continue ")
quit()
