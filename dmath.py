import math
def perfectSquaresInRange(args):
    # lists off the numbers within a range that are perfect squares.
    # Expects a list of length 3 for its argument, however, if it has less then:
        # length 1: The lower boundary is assumed to be 0 and the only argument is taken as the upper boundary with a step of 1.
        # length 2: the lower boundary is the first argument and the upper boundary is the second argument
        # length 3: normal function, 1st is lower, 2nd is upper, and 3rd is step.
        lower = 0
        upper = 0
        step = 1
        if len(args) == 1:
            lower = int(args[0])
        elif len(args) == 2:
            lower = int(args[0])
            upper = int(args[1])
        else:
            lower = int(args[0])
            upper = int(args[1])
            step = int(args[2])
        squaresFound = []
        for x in range(lower, upper+1, step):
            currentOutput = math.sqrt(x)
            indexOfPeriod = -1
            for y in range(0, len(str(currentOutput))):
                if str(currentOutput)[y] == ".":
                    indexOfPeriod = y
                    break
            decimals = str(currentOutput)[indexOfPeriod+1:len(str(currentOutput))]
            if len(decimals) == 1 and decimals[0] == "0":
                squaresFound.append(x)
            else:
                next
        return(squaresFound)

def squareRootsInRange(args):
    lower = 0
    upper = 0
    step = 1
    if len(args) == 1:
        upper = int(args[0])
    elif len(args) == 2:
        lower = int(args[0])
        upper = int(args[1])
    else:
        lower = int(args[0])
        upper = int(args[1])
        step = int(args[2])
    results = []
    numbersVisited = []
    for x in range(lower, upper+1, step):
        numbersVisited.append(x) # need this for when the user actually wants a step other than 1
        results.append(math.sqrt(x))
    return(numbersVisited, results)

def divides(divisor, dividend):
    if dividend%divisor == 0:
        return(True)
    else:
        return(False)
