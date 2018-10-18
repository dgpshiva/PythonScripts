def moveAllOnesToEnd(input):
    count = 0
    for i in range(0, len(input)):
        if input[i] != 1:
            input[count] = input[i]
            count += 1

    while count < len(input):
        input[count] = 1
        count += 1


if __name__ == '__main__':
    input = [1, 2, 1, 3, 4, 1, 5, 1]
    moveAllOnesToEnd(input)

    for i in range(0, len(input)):
        print str(input[i]) + " ",




