def countClumps(input):
    count = 0
    for i in range(len(input) - 1):
        if (input[i] == input[i+1]) and (i==0 or input[i] != input[i-1]):
            count += 1

    return count

if __name__ == '__main__':
    # input = [1, 2, 2, 3, 4, 4]
    # input = [1, 1, 2, 1, 1]
    input = [1, 1, 1, 1, 1]
    print countClumps(input)
