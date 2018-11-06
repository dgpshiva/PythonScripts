def returnLongesRun(input):
    numbersSet = set(input)

    maxCount = 0
    for number in numbersSet:
        currentNumber = number
        if number-1 not in numbersSet:
            while number+1 in numbersSet:
                number += 1
            maxCount = max(maxCount,  (number+1) - currentNumber)

    return maxCount


if __name__ == '__main__':
    input = [1, 9, 3, 10, 4, 20, 2]
    #input = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    print returnLongesRun(input)
