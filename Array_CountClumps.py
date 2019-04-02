def countClumps(input):
    count = 0
    for i in range(len(input) - 1):
        if (input[i] == input[i+1]) and (i==0 or input[i] != input[i-1]):
            count += 1

    return count

if __name__ == '__main__':
    print countClumps([1, 2, 2, 3, 4, 4])   # Expectd output: 2
    print countClumps([1, 1, 2, 1, 1])  # Expectd output: 2
    print countClumps([1, 1, 1, 1, 1])  # Expectd output: 1
    print countClumps([1, 2, 2, 2, 3])  # Expectd output: 1
    print countClumps([2, 2, 2, 3])  # Expectd output: 1
    print countClumps([2, 3, 3])  # Expectd output: 1
    print countClumps([2, 3])  # Expectd output: 0
    print countClumps([2])  # Expectd output: 0


