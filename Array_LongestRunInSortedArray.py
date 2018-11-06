def makeListComprehensible(input):
    output = []
    i = 0
    while i < len(input):
        if input[i+1] == input[i]+1:
            start = input[i]
            while i+1 < len(input) and input[i+1] == input[i]+1:
                i += 1
            output.append(str(start) + "-" + str(input[i]))
            i += 1
        else:
            output.append(str(input[i]))
            i += 1

    return output


if __name__ == '__main__':
    input = [1,2,3,5,8,12,13,14,15]
    print makeListComprehensible(input)
