import math

x = 0
def checkIfPerfectSquare(input):
    sr = math.sqrt(input)
    return (sr - math.floor(sr) == 0)

def checkIfPerfectSquaresExists(input):
    return True if math.floor(math.sqrt(input)) > 0 else False

def resultOfMove(move):
    global x

    if not checkIfPerfectSquare(move):
        return "Invalid move"

    x = x - move
    if x < 0:
        return "Invalid move"

    if x == 0:
        return "Winner"

    if checkIfPerfectSquaresExists(x):
        return "Continue"
    else:
        return "Winner"


if __name__ == '__main__':
    x = 47

    print resultOfMove(25)
    print resultOfMove(16)
    print resultOfMove(4)
    print resultOfMove(1)
    print resultOfMove(1)
