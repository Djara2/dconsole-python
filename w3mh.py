from figlet import *
import os
from colors import *
os.system("clear")
figlet("w3m Manual")
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
