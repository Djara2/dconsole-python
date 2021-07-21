from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
import os
CONSOLE = Console()
MD_TITLE = Markdown("# Binomial Theorem Calculator")
CONSTANT = 0
POWER = 0
entered = ""
enteredList = []
def factorial(n):
    if n > 1:
        return(n*factorial(n-1))
    else:
        return(1)

def choose(n, r):
    num = factorial(n)
    r_factorial = factorial(r)
    n_sub_r = n-r
    n_sub_r_factorial = factorial(n_sub_r)
    den = r_factorial * n_sub_r_factorial
    result = num/den
    return(result)
    
while True:
    CONSOLE.print(MD_TITLE)
    CONSOLE.print("Binomial Theorem takes the form [green](x+a)^b[/]")
    CONSOLE.print("Where [green italic]a[/] is a constant")
    CONSTANT = input("Constant value?: ")
    if CONSTANT != "quit" or CONSTANT != "exit":
        CONSTANT = int(CONSTANT)
    else:
            exit()
    POWER = input("Exponent?: ")
    POWER = int(POWER)
    build_string = ""
    for x in range(0, POWER+1):
        comb = choose(POWER, x)
        if((POWER-x)==1):
            current_x = "x"
        elif((POWER-x)==0):
            current_x = ""
        else:
            current_x = "x^"+str(POWER-x)
        current_constant = pow(CONSTANT, x)
        coefficient_of_x = comb*current_constant
        if x != POWER:
            build_string += "{}{} + ".format(coefficient_of_x, current_x)
        else:
            build_string += "{}{}".format(coefficient_of_x, current_x)
    CONSOLE.print(build_string)
    stop = input("Hit ENTER to continue ")
    os.system("clear")

