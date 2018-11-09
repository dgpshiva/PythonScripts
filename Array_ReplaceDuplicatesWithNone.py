def removeDuplicates(input):
    currentValue = input[len(input)-1]
    toSwapPos = None

    for i in range(len(input)-2, -1, -1):
        if input[i] == currentValue:
            if (i == 0 or input[i-1] != input[i]) and toSwapPos is not None:
                while toSwapPos < len(input) and input[toSwapPos] is not None:
                    input[i+1] = input[toSwapPos]
                    input[toSwapPos] = None
                    toSwapPos += 1
                    i += 1
            else:
                input[i+1] = None
        else:
            toSwapPos = i+1
            currentValue = input[i]



if __name__ == '__main__':
    # input = [1, 1, 1, 2]
    # input = [1, 1, 1, 2, 2]
    # input = [0, 1, 1, 1, 2, 2, 5, 6]
    input = [-1, 0, 1, 1, 1, 2, 2, 5, 6]

    removeDuplicates(input)

    print input
