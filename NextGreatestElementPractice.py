def nextGreatestElement(input):
    s = []
    output = []

    for i in range(len(input) - 1, -1, -1):
        element = input[i]

        while len(s) != 0 and s[len(s) - 1] < element:
            s.pop()

        if len(s) == 0:
            output.append(-1)
        else:
            output.append(s[len(s) - 1])

        s.append(element)

    for i in range(0, len(input)):
        print str(input[i]) + " -- " + str(output[len(output) - 1 - i])
        print "\n"


if __name__ == '__main__':
    # input = [11, 13, 21, 3]
    # input = [11, 12, 10, 9, 15]
    # input = [11, 10, 9, 8, 7]
    input = [7, 8, 9, 10, 11]
    nextGreatestElement(input)
