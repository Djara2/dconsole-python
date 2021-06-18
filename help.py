import os
from colors import *
stoptext = "Hit ENTER to continue "
def figlet(text):
    os.system("figlet {}".format(text))
os.system("clear")
figlet("Manual")
print()
print("{}GENERAL{}".format(CYAN, CLEAR))
print()
print("\t{}HISTORY:{} will show you all the things you entered over the course of this session. You can copy items from your history using the HRE command followed by the index number of the entry in the history list.".format(PINK, CLEAR))
figlet("======")
print("{}EXTERNAL PROGRAMS{}".format(CYAN, CLEAR))
print()
print("\t{}DISCOUNT:{} entering discount will open the discount.py file. It takes the argument syntax [value] [percentage of value] and prints out simple information about the arguments provided.".format(PINK, CLEAR))
print()
print("\t{}CALCULATOR:{} opens a calculator program.".format(PINK, CLEAR))
print()
print("\t{}TIP:{} utility for finding out various tip percentages based on an input".format(PINK, CLEAR))
print()
quit()
