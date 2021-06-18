import os
import math
from colors import *
os.system("clear")
history = []
inputHistory = []
outputHistory = []
knowncmd = ["quit", "exit", "add", "sub", "mult", "div", "sqrt", "pow", "mod", "history"]
def figlet(text):
    os.system("figlet {}".format(text))

def logic(enteredList):
    global knowncmd, history
    if not enteredList[0] in knowncmd:
        print("{}Error:{} {} is not a valid command.".format(RED, CLEAR, enteredList[0]))
        outputHistory.append("Error (command invalid)")
        stop = input("Hit ENTER to continue ")
    elif enteredList[0] == "add":
        num1 = float(enteredList[1])
        num2 = float(enteredList[2])
        result = num1 + num2
        outputHistory.append(result)
        print(PINK)
        print("{} + {} = {}".format(num1, num2, result))
        print(CLEAR)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    elif enteredList[0] == "quit" or enteredList[0] == "exit":
        exit()
    elif enteredList[0] == "sub":
        num1 = float(enteredList[1])
        num2 = float(enteredList[2])
        result = num1 - num2
        outputHistory.append(result)
        print(PINK)
        print("{} - {} = {}".format(num1, num2, result))
        print(CLEAR)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    elif enteredList[0] == "mult":
        num1 = float(enteredList[1])
        num2 = float(enteredList[2])
        result = num1 * num2
        outputHistory.append(result)
        print(PINK)
        print("{} * {} = {}".format(num1, num2, result))
        print(CLEAR)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    elif enteredList[0] == "div":
        num1 = float(enteredList[1])
        num2 = float(enteredList[2])
        if num2 != 0:
            result = num1/num2
            outputHistory.append(result)
            print(PINK)
            print("{} / {} = {}".format(num1, num2, result))
            print(CLEAR)
            stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
        else:
            print()
            outputHistory.append("Error (cannot divide by zero)")
            print("{}Error:{} cannot divide by 0.".format(RED, CLEAR))
            stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    elif enteredList[0] == "sqrt":
        num1 = float(enteredList[1])
        result = math.sqrt(num1)
        outputHistory.append(result)
        print(PINK)
        print("sqrt({}) = {}".format(num1, result))
        print(CLEAR)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    elif enteredList[0] == "pow":
        num1 = float(enteredList[1])
        if enteredList[2] != "f":
            power = float(enteredList[2])
        else:
            power = float(enteredList[3])
            power = power/float(enteredList[4])
        result = pow(num1, power)
        outputHistory.append(result)
        print(PINK)
        print("{}^{} = {}".format(num1, power, result))
        print(CLEAR)
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))
    elif enteredList[0] == "history":
        os.system("clear")
        figlet("History")
        outputHistory.append("~")
        print()
        for x in range(0, len(history)):
            print("{}. {} [Output: {}]".format(x+1, history[x], outputHistory[x]))
        print()
        stop = input("Hit {}ENTER{} to continue ".format(GREEN, CLEAR))






while(True):
    os.system("clear")
    figlet("Calculator")
    print()
    print("{}add:{} add     {}sub:{}  subtract     {}mult:{} multiply".format(GREEN, CLEAR, GREEN, CLEAR, GREEN, CLEAR))
    print("{}div:{} divide  {}sqrt:{} square root  {}pow: {} power".format(GREEN, CLEAR, GREEN, CLEAR, GREEN, CLEAR))
    print()
    entered = input("> {}".format(CYAN))
    print(CLEAR)
    entered = entered.lower()
    enteredList = entered.split()
    history.append(entered)
    logic(enteredList)

