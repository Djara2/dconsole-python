from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
console = Console()
MD_TITLE = Markdown("# w3m Manual")
import os
from colors import *
os.system("clear")
console.print(MD_TITLE)
print()
print("{}q{}: quit (with confirmation)".format(GREEN, CLEAR))
print()
print("{}Q{}: quit ({}NO{} confirmation)".format(GREEN, CLEAR, RED, CLEAR))
print()
print("{}B{}: go back one page".format(GREEN, CLEAR))
print()
print("{}H{}: show hot keys".format(GREEN, CLEAR))
print()
quit()
