def checkIfValid(input):
    parenthesisDict = {}
    parenthesisDict['{'] = '}'
    parenthesisDict['('] = ')'
    parenthesisDict['['] = ']'

    s = []

    for i in input:
        if i in parenthesisDict:
            s.append(i)
        elif i in parenthesisDict.values():
            if parenthesisDict[s.pop()] != i:
                return False

    return True

if __name__ == '__main__':
    input = "{([]({()}))}"
    print checkIfValid(input)



