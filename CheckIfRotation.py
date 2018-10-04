def isRotation(inputStr, toCheck):
    temp = inputStr + inputStr
    if toCheck in temp:
        return True
    else:
        return False

if __name__ == '__main__':
    # inputStr = "ABCD"
    # toCheck = "CDAB"

    inputStr = "ABCD"
    toCheck = "ACBD"

    print isRotation(inputStr, toCheck)
